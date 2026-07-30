"""Incrementally dual-write MEXC research/audit events to Sakura.

The source JSON files remain in place during migration.  This tool never
uploads those cumulative files.  It derives immutable events, advances a
small cursor only after a successful batch, and relies on repo+event_id
uniqueness for crash-safe retries.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.live_policy import (  # noqa: E402
    _POLICY_ENV_DEFAULTS,
    live_policy_fingerprint,
)
from core.trading_data_events import (  # noqa: E402
    DATASET_EXECUTIONS,
    DATASET_OUTCOMES,
    DATASET_POLICIES,
    DATASET_SIGNALS,
    EVENT_SCHEMA_VERSION,
    json_value,
    make_event,
    normalize_timestamp,
    shadow_signal_event_id,
    signal_data_quality,
    signal_identity,
    utc_now_iso,
)


logger = logging.getLogger(__name__)

DEFAULT_EXPERIMENT_FILE = PROJECT_ROOT / "data" / "experiments.json"
DEFAULT_ARCHIVE_DIR = PROJECT_ROOT / "data" / "archive"
DEFAULT_LEDGER_FILE = PROJECT_ROOT / "logs" / "live-executions.jsonl"
DEFAULT_OUTBOX_FILE = PROJECT_ROOT / "logs" / "trading-data-events.jsonl"
DEFAULT_STATE_FILE = PROJECT_ROOT / "data" / "trading_data_sync_state.json"


def runtime_path(name: str, default: Path) -> Path:
    configured = Path(os.getenv(name, str(default)))
    return configured if configured.is_absolute() else PROJECT_ROOT / configured


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, 1):
            stripped = raw.strip()
            if not stripped:
                continue
            try:
                item = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise RuntimeError(
                    f"invalid JSONL at {path}:{line_number}"
                ) from exc
            if not isinstance(item, dict):
                raise RuntimeError(
                    f"JSONL item must be an object at {path}:{line_number}"
                )
            records.append(item)
    return records


def load_experiment_records(
    experiment_file: Path = DEFAULT_EXPERIMENT_FILE,
    archive_dir: Path = DEFAULT_ARCHIVE_DIR,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if experiment_file.exists():
        payload = _read_json(experiment_file)
        if not isinstance(payload, dict):
            raise RuntimeError(f"{experiment_file} must contain an object")
        for section in ("active", "closed"):
            values = payload.get(section, [])
            if not isinstance(values, list):
                raise RuntimeError(
                    f"{experiment_file}:{section} must contain a list"
                )
            records.extend(item for item in values if isinstance(item, dict))

    if archive_dir.exists():
        for path in sorted(archive_dir.glob("experiments_*.json.gz")):
            try:
                with gzip.open(path, "rt", encoding="utf-8") as handle:
                    payload = json.load(handle)
            except Exception as exc:
                raise RuntimeError(f"failed to read archive {path}") from exc
            values = payload.get("closed", []) if isinstance(payload, dict) else []
            if not isinstance(values, list):
                raise RuntimeError(f"{path}:closed must contain a list")
            records.extend(item for item in values if isinstance(item, dict))

    # Rotation/retry can temporarily leave the same record hot and archived.
    # Deduplicate locally before sending; the server enforces the same identity.
    unique: dict[str, dict[str, Any]] = {}
    for record in records:
        unique[shadow_signal_event_id(record)] = record
    return list(unique.values())


def _canonical_features(record: Mapping[str, Any]) -> dict[str, Any]:
    filters = record.get("filters")
    return json_value(dict(filters) if isinstance(filters, dict) else {})


def build_shadow_signal_event(record: Mapping[str, Any]) -> dict[str, Any]:
    detected_at = normalize_timestamp(record.get("detected_at"))
    signal_candle_at = str(record.get("signal_candle_at") or "").strip()
    policy_fingerprint = str(record.get("policy_fingerprint") or "")
    identity = signal_identity(
        symbol=record.get("symbol"),
        signal_candle_at=signal_candle_at,
        detected_at=detected_at,
        policy_fingerprint=policy_fingerprint,
    )
    features = _canonical_features(record)
    event = make_event(
        event_type="mexc.shadow_signal",
        dataset=DATASET_SIGNALS,
        event_time=signal_candle_at or detected_at,
        available_at=detected_at,
        identity=identity,
        policy_fingerprint=policy_fingerprint or None,
        tags=[
            "strict-pass"
            if bool(record.get("confirmed_strict"))
            else "strict-reject",
            str(record.get("market_regime") or "UNKNOWN").lower(),
        ],
        payload={
            "symbol": record.get("symbol"),
            "signal_candle_at": signal_candle_at or None,
            "detected_at": detected_at,
            "policy_version": record.get("policy_version", "unversioned"),
            "policy_fingerprint": policy_fingerprint,
            "market_regime": record.get("market_regime", "UNKNOWN"),
            "confirmed_strict": bool(record.get("confirmed_strict")),
            "strict_reject_reasons": list(
                record.get("strict_reject_reasons") or []
            ),
            "features": features,
            "data_quality": signal_data_quality(
                features=features,
                signal_candle_at=signal_candle_at,
                ask_price=record.get("ask_price"),
                bid_price=record.get("bid_price"),
            ),
            "entry_plan": {
                "entry_price": record.get("entry_price"),
                "sl_price": record.get("sl_price"),
                "tp_price": record.get("tp_price"),
                "sl_pct": record.get("sl_pct"),
                "tp_pct": record.get("tp_pct"),
                "ask_price": record.get("ask_price"),
                "bid_price": record.get("bid_price"),
                "spread_pct": record.get("spread_pct"),
            },
        },
    )
    # Keep the direct outbox and historical extractor on exactly one identity.
    if event["event_id"] != shadow_signal_event_id(record):
        raise RuntimeError("shadow signal identity mismatch")
    return event


def build_outcome_event(record: Mapping[str, Any]) -> dict[str, Any] | None:
    outcome = str(record.get("outcome") or "")
    outcome_at = str(record.get("outcome_at") or "").strip()
    if not outcome_at or outcome in {"", "ACTIVE"}:
        return None
    available_at = normalize_timestamp(outcome_at)
    signal_id = shadow_signal_event_id(record)
    policy_fingerprint = str(record.get("policy_fingerprint") or "")
    identity = {
        "signal_event_id": signal_id,
        "label_available_at": available_at,
        "outcome": outcome,
        "label_schema": "shadow-ohlcv-1m-v1",
    }
    return make_event(
        event_type="mexc.outcome",
        dataset=DATASET_OUTCOMES,
        event_time=available_at,
        available_at=available_at,
        identity=identity,
        strategy_id="mexc:shadow:variants",
        policy_fingerprint=policy_fingerprint or None,
        tags=["shadow", outcome.lower()],
        payload={
            "signal_event_id": signal_id,
            "symbol": record.get("symbol"),
            "detected_at": record.get("detected_at"),
            "label_available_at": available_at,
            "outcome": outcome,
            "outcome_price": record.get("outcome_price"),
            "entry_price": record.get("entry_price"),
            "pnl_pct": record.get("pnl_pct"),
            "hours_held": record.get("hours_held"),
            "max_favorable_pct": record.get("max_favorable_pct"),
            "max_adverse_pct": record.get("max_adverse_pct"),
            "last_price": record.get("last_price"),
            "entry_variants": record.get("entry_variants") or [],
            "fundamental": {
                "catalyst_type": record.get("catalyst_type", "UNKNOWN"),
                "short_conviction": record.get(
                    "short_conviction", "UNKNOWN"
                ),
                "news_count": record.get("news_count", -1),
            },
            "policy_version": record.get("policy_version", "unversioned"),
            "policy_fingerprint": policy_fingerprint,
            "data_quality": {
                "fundamental_available": (
                    str(record.get("short_conviction") or "UNKNOWN")
                    != "UNKNOWN"
                    and isinstance(record.get("news_count"), int)
                    and int(record.get("news_count")) >= 0
                ),
                "variant_count": len(record.get("entry_variants") or []),
                "outcome_price_available": record.get("outcome_price")
                is not None,
                "mfe_mae_available": (
                    record.get("max_favorable_pct") is not None
                    and record.get("max_adverse_pct") is not None
                ),
            },
            "label_method": {
                "timeframe": "1m",
                "window_candles": 6,
                "same_candle_tie_break": "SL_FIRST",
                "available_at_is_observation_time": True,
            },
        },
    )


def build_policy_events(
    records: Iterable[Mapping[str, Any]],
    *,
    current_policy_version: str | None = None,
    current_policy_fingerprint: str | None = None,
    current_effective_at: str | None = None,
    current_policy_config: Mapping[str, str] | None = None,
) -> list[dict[str, Any]]:
    first_seen: dict[tuple[str, str], str] = {}
    for record in records:
        fingerprint = str(record.get("policy_fingerprint") or "").strip()
        if not fingerprint:
            continue
        version = str(record.get("policy_version") or "unversioned")
        detected_at = normalize_timestamp(record.get("detected_at"))
        key = (version, fingerprint)
        if key not in first_seen or detected_at < first_seen[key]:
            first_seen[key] = detected_at

    if current_policy_fingerprint:
        version = current_policy_version or "unversioned"
        effective = normalize_timestamp(
            current_effective_at or utc_now_iso()
        )
        # The current policy declaration is authoritative.  A later archive
        # scan may discover older signals, but must never mutate an already
        # published append-only policy event.
        first_seen[(version, current_policy_fingerprint)] = effective

    events: list[dict[str, Any]] = []
    for (version, fingerprint), effective_at in first_seen.items():
        events.append(
            make_event(
                event_type="mexc.policy",
                dataset=DATASET_POLICIES,
                event_time=effective_at,
                available_at=effective_at,
                identity={
                    "policy_version": version,
                    "policy_fingerprint": fingerprint,
                },
                policy_fingerprint=fingerprint,
                tags=["policy"],
                payload={
                    "policy_version": version,
                    "policy_fingerprint": fingerprint,
                    "effective_at": effective_at,
                    "legacy_unversioned": version == "unversioned",
                    "configuration": (
                        dict(current_policy_config or {})
                        if (
                            version == current_policy_version
                            and fingerprint == current_policy_fingerprint
                        )
                        else None
                    ),
                },
            )
        )
    return events


def build_execution_event(record: Mapping[str, Any]) -> dict[str, Any]:
    recorded_at = normalize_timestamp(record.get("recorded_at"))
    policy_fingerprint = str(record.get("policy_fingerprint") or "")
    direction = str(record.get("direction") or "")
    entry_style = str(record.get("entry_style") or "")
    return make_event(
        event_type="mexc.execution",
        dataset=DATASET_EXECUTIONS,
        event_time=recorded_at,
        available_at=recorded_at,
        identity={
            "account_id": record.get("account_id"),
            "external_oid": record.get("external_oid"),
            "order_id": record.get("order_id"),
        },
        strategy_id=(
            f"mexc:{direction}:{entry_style}"
            if direction and entry_style
            else None
        ),
        policy_fingerprint=policy_fingerprint or None,
        tags=["live", "verified-fill", "protected"],
        payload=dict(record),
    )


def _load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": 1, "streams": {}}
    state = _read_json(path)
    if not isinstance(state, dict):
        raise RuntimeError(f"{path} must contain an object")
    state.setdefault("schema_version", 1)
    state.setdefault("streams", {})
    return state


def _save_state(path: Path, state: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _cursor(event: Mapping[str, Any]) -> tuple[str, str]:
    return (
        normalize_timestamp(event.get("available_at")),
        str(event.get("event_id") or ""),
    )


def _saved_cursor(
    state: Mapping[str, Any],
    stream: str,
) -> tuple[str, str] | None:
    streams = state.get("streams")
    raw = streams.get(stream) if isinstance(streams, dict) else None
    if not isinstance(raw, dict):
        return None
    if str(raw.get("schema_version") or "") != EVENT_SCHEMA_VERSION:
        return None
    available_at = raw.get("available_at")
    event_id = raw.get("event_id")
    if not available_at or not event_id:
        return None
    return (normalize_timestamp(available_at), str(event_id))


def _batch_id(stream: str, events: list[Mapping[str, Any]]) -> str:
    digest = hashlib.sha256()
    digest.update(stream.encode("utf-8"))
    for event in events:
        digest.update(b"\n")
        digest.update(str(event["event_id"]).encode("utf-8"))
    return f"mexc-sync-{digest.hexdigest()[:40]}"


def sync_stream(
    client: Any,
    *,
    stream: str,
    events: Iterable[dict[str, Any]],
    state: dict[str, Any],
    state_path: Path,
    batch_size: int,
) -> int:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    high_water = _saved_cursor(state, stream)
    pending = sorted(
        (
            event
            for event in events
            if high_water is None or _cursor(event) > high_water
        ),
        key=_cursor,
    )
    sent = 0
    for offset in range(0, len(pending), batch_size):
        batch = pending[offset : offset + batch_size]
        client.ingest_events(
            batch,
            schema_version=EVENT_SCHEMA_VERSION,
            idempotency_key=_batch_id(stream, batch),
        )
        last = batch[-1]
        state["streams"][stream] = {
            "schema_version": EVENT_SCHEMA_VERSION,
            "available_at": last["available_at"],
            "event_id": last["event_id"],
        }
        state["updated_at"] = utc_now_iso()
        _save_state(state_path, state)
        sent += len(batch)
    return sent


def sync_outbox(
    client: Any,
    *,
    outbox_path: Path,
    batch_size: int,
) -> int:
    events = _read_jsonl(outbox_path)
    if not events:
        return 0
    sent = 0
    remaining = list(events)
    while remaining:
        batch = remaining[:batch_size]
        client.ingest_events(
            batch,
            schema_version=EVENT_SCHEMA_VERSION,
            idempotency_key=_batch_id("runtime-outbox", batch),
        )
        sent += len(batch)
        remaining = remaining[len(batch) :]

        # Remove only the acknowledged prefix.  A timeout/error leaves the
        # current and later events intact for artifact recovery or local retry.
        outbox_path.parent.mkdir(parents=True, exist_ok=True)
        temporary = outbox_path.with_suffix(outbox_path.suffix + ".tmp")
        encoded = "".join(
            json.dumps(
                event,
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n"
            for event in remaining
        )
        temporary.write_text(encoded, encoding="utf-8")
        temporary.replace(outbox_path)
    return sent


def sync_all(
    client: Any,
    *,
    runtime_only: bool = False,
    experiment_file: Path = DEFAULT_EXPERIMENT_FILE,
    archive_dir: Path = DEFAULT_ARCHIVE_DIR,
    ledger_file: Path = DEFAULT_LEDGER_FILE,
    outbox_file: Path = DEFAULT_OUTBOX_FILE,
    state_file: Path = DEFAULT_STATE_FILE,
    batch_size: int = 100,
) -> dict[str, int]:
    counts = {"outbox": 0, "signals": 0, "outcomes": 0, "policies": 0, "executions": 0}
    counts["outbox"] = sync_outbox(
        client,
        outbox_path=outbox_file,
        batch_size=batch_size,
    )

    state = _load_state(state_file)
    ledger_records = _read_jsonl(ledger_file)
    counts["executions"] = sync_stream(
        client,
        stream="mexc.execution",
        events=(build_execution_event(record) for record in ledger_records),
        state=state,
        state_path=state_file,
        batch_size=batch_size,
    )
    if runtime_only:
        return counts

    records = load_experiment_records(experiment_file, archive_dir)
    signal_events = [build_shadow_signal_event(record) for record in records]
    outcome_events = [
        event
        for record in records
        if (event := build_outcome_event(record)) is not None
    ]
    current_version = (
        os.getenv("LIVE_POLICY_VERSION", "unversioned").strip()
        or "unversioned"
    )
    current_fingerprint = live_policy_fingerprint()
    effective_at = (
        os.getenv("LIVE_POLICY_EFFECTIVE_AT", "").strip()
        or min(
            (
                normalize_timestamp(record.get("detected_at"))
                for record in records
                if record.get("policy_fingerprint") == current_fingerprint
            ),
            default=utc_now_iso(),
        )
    )
    policy_events = build_policy_events(
        records,
        current_policy_version=current_version,
        current_policy_fingerprint=current_fingerprint,
        current_effective_at=effective_at,
        current_policy_config={
            name: os.getenv(name, default).strip()
            for name, default in _POLICY_ENV_DEFAULTS.items()
        },
    )

    for stream, events, key in (
        ("mexc.shadow_signal", signal_events, "signals"),
        ("mexc.outcome", outcome_events, "outcomes"),
        ("mexc.policy", policy_events, "policies"),
    ):
        counts[key] = sync_stream(
            client,
            stream=stream,
            events=events,
            state=state,
            state_path=state_file,
            batch_size=batch_size,
        )
    return counts


def _storage_configuration() -> tuple[bool, list[str]]:
    base_url = os.getenv("TD_BASE_URL", "").strip()
    repo = os.getenv("TD_REPO", "").strip()
    secret = os.getenv("TD_HMAC_SECRET", "").strip()
    secret_file = os.getenv("TD_HMAC_SECRET_FILE", "").strip()
    # The gateway URL and repo are intentionally non-secret workflow config.
    # Until the HMAC secret is provisioned, syncing remains an explicit no-op.
    if not secret and not secret_file:
        return False, ["TD_HMAC_SECRET"]
    missing = []
    if not base_url:
        missing.append("TD_BASE_URL")
    if not repo:
        missing.append("TD_REPO")
    if missing:
        raise RuntimeError(
            "partial trading-data configuration; missing " + ", ".join(missing)
        )
    return True, []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--runtime-only",
        action="store_true",
        help="send only runner-local decision/execution events",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=int(os.getenv("TD_BATCH_SIZE", "100")),
    )
    args = parser.parse_args(argv)

    try:
        from dotenv import load_dotenv

        load_dotenv(PROJECT_ROOT / ".env")
    except ImportError:
        pass

    configured, _ = _storage_configuration()
    if not configured:
        print(
            "Trading-data sync disabled: TD_HMAC_SECRET "
            "(or TD_HMAC_SECRET_FILE) is unset."
        )
        return 0

    from utils.trading_data_client import TradingDataClient

    client = TradingDataClient.from_env(timeout=30)
    client.health()
    counts = sync_all(
        client,
        runtime_only=args.runtime_only,
        ledger_file=runtime_path("LIVE_EXECUTION_LEDGER_FILE", DEFAULT_LEDGER_FILE),
        outbox_file=runtime_path("TD_OUTBOX_FILE", DEFAULT_OUTBOX_FILE),
        state_file=runtime_path("TD_SYNC_STATE_FILE", DEFAULT_STATE_FILE),
        batch_size=args.batch_size,
    )
    print(
        "Trading-data sync complete: "
        + ", ".join(f"{name}={count}" for name, count in counts.items())
    )
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    raise SystemExit(main())
