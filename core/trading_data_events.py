"""Canonical, append-only trading data events for Sakura dual-write.

This module deliberately does not perform network I/O.  The scanner writes
small runner-local JSONL events first; ``tools/sync_trading_data.py`` sends
them after the trading cycle.  A storage outage therefore cannot alter a
market decision, and Git never receives another copy of a cumulative JSON
dataset.
"""
from __future__ import annotations

import hashlib
import json
import logging
import math
import os
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


logger = logging.getLogger(__name__)

DEFAULT_OUTBOX_FILE = Path("logs/trading-data-events.jsonl")
SOURCE_ID = "mexc-futures"
EVENT_SCHEMA_VERSION = "1"

DATASET_SIGNALS = "mexc_signals"
DATASET_DECISIONS = "mexc_decisions"
DATASET_OUTCOMES = "mexc_outcomes"
DATASET_POLICIES = "mexc_policies"
DATASET_EXECUTIONS = "mexc_executions"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_timestamp(value: object, *, fallback: str | None = None) -> str:
    """Return a timezone-aware ISO timestamp or a supplied safe fallback."""
    raw = str(value or "").strip()
    if raw:
        normalized = f"{raw[:-1]}+00:00" if raw.endswith(("Z", "z")) else raw
        try:
            parsed = datetime.fromisoformat(normalized)
        except ValueError:
            parsed = None
        if parsed is not None and parsed.tzinfo is not None:
            return parsed.astimezone(timezone.utc).isoformat()
    if fallback is not None:
        return normalize_timestamp(fallback)
    raise ValueError(f"timestamp must be timezone-aware ISO 8601: {value!r}")


def json_value(value: Any) -> Any:
    """Convert dataclasses and numeric scalar types to strict JSON values."""
    if is_dataclass(value):
        return json_value(asdict(value))
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, Mapping):
        return {str(key): json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [json_value(item) for item in value]

    # numpy/pandas scalars expose item(), but importing either library here
    # would make the audit path unnecessarily fragile.
    item_method = getattr(value, "item", None)
    if callable(item_method):
        try:
            return json_value(item_method())
        except (TypeError, ValueError, OverflowError):
            pass
    return str(value)


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        json_value(value),
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def stable_event_id(event_type: str, identity: Any) -> str:
    digest = hashlib.sha256(
        _canonical_bytes(
            {
                "event_schema_version": EVENT_SCHEMA_VERSION,
                "identity": identity,
            }
        )
    ).hexdigest()
    suffix = event_type.rsplit(".", 1)[-1].replace("_", "-")
    return f"mexc-{suffix}-{digest[:40]}"


def signal_identity(
    *,
    symbol: object,
    signal_candle_at: object,
    detected_at: object,
    policy_fingerprint: object,
) -> dict[str, str]:
    signal_time = str(signal_candle_at or "").strip() or str(detected_at or "").strip()
    return {
        "symbol": str(symbol or "").upper(),
        "signal_time": signal_time,
        "detected_at": str(detected_at or "").strip(),
        "policy_fingerprint": str(policy_fingerprint or "legacy-unversioned"),
    }


def signal_group_id(
    *,
    symbol: object,
    signal_candle_at: object,
    policy_fingerprint: object,
) -> str:
    """Logical candle/policy group used to de-cluster repeated scan runs."""
    return stable_event_id(
        "mexc.signal_group",
        {
            "symbol": str(symbol or "").upper(),
            "signal_candle_at": str(signal_candle_at or "").strip(),
            "policy_fingerprint": str(
                policy_fingerprint or "legacy-unversioned"
            ),
        },
    )


def shadow_signal_event_id(record: Mapping[str, Any]) -> str:
    return stable_event_id(
        "mexc.shadow_signal",
        signal_identity(
            symbol=record.get("symbol"),
            signal_candle_at=record.get("signal_candle_at"),
            detected_at=record.get("detected_at"),
            policy_fingerprint=record.get("policy_fingerprint"),
        ),
    )


def signal_data_quality(
    *,
    features: Mapping[str, Any],
    signal_candle_at: object,
    ask_price: object,
    bid_price: object,
) -> dict[str, Any]:
    missing = sorted(
        str(name)
        for name, value in features.items()
        if value is None or value == ""
    )
    return {
        "missing_features": missing,
        "signal_candle_available": bool(
            str(signal_candle_at or "").strip()
        ),
        "order_book_available": ask_price is not None and bid_price is not None,
    }


def make_event(
    *,
    event_type: str,
    dataset: str,
    event_time: object,
    available_at: object,
    payload: Mapping[str, Any],
    identity: Any,
    strategy_id: str | None = None,
    policy_fingerprint: str | None = None,
    tags: list[str] | None = None,
) -> dict[str, Any]:
    available = normalize_timestamp(available_at)
    observed = normalize_timestamp(event_time, fallback=available)
    event: dict[str, Any] = {
        "event_id": stable_event_id(event_type, identity),
        "event_type": event_type,
        "dataset": dataset,
        "source_id": SOURCE_ID,
        "event_time": observed,
        "available_at": available,
        "payload": json_value(payload),
    }
    if strategy_id:
        event["strategy_id"] = strategy_id
    if policy_fingerprint:
        event["policy_fingerprint"] = policy_fingerprint
    if tags:
        event["tags"] = sorted({str(tag) for tag in tags if str(tag)})
    # Validate now so the live runner never leaves a malformed outbox line.
    _canonical_bytes(event)
    return event


def append_outbox_event(
    event: Mapping[str, Any],
    *,
    outbox_path: Path | None = None,
) -> None:
    target = outbox_path or Path(
        os.getenv("TD_OUTBOX_FILE", str(DEFAULT_OUTBOX_FILE))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = _canonical_bytes(event).decode("utf-8")
    with target.open("a", encoding="utf-8") as handle:
        handle.write(encoded + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def _canonical_features(
    result: Any,
    *,
    btc_change_1h: float | None,
) -> dict[str, Any]:
    price = getattr(result, "price", None)
    bb_upper = getattr(result, "bb_upper", None)
    price_vs_bb = None
    try:
        if price is not None and bb_upper is not None and float(bb_upper) > 0:
            price_vs_bb = float(price) / float(bb_upper)
    except (TypeError, ValueError, OverflowError):
        price_vs_bb = None
    return json_value(
        {
            "change_1h": getattr(result, "change_1h_pct", None),
            "relative_strength": getattr(result, "relative_strength_pct", None),
            "btc_change_1h": btc_change_1h,
            "rsi": getattr(result, "rsi", None),
            "rsi_4h": getattr(result, "rsi_4h", None),
            "rsi_15m": getattr(result, "rsi_15m", None),
            "bb_upper": bb_upper,
            "price_vs_bb": price_vs_bb,
            "bb_width_pct": getattr(result, "bb_width_pct", None),
            "volume_ratio": getattr(result, "volume_trend_ratio", None),
            "volume_trend": getattr(result, "volume_trend", None),
            "atr_pct": getattr(result, "atr_pct", None),
            "funding_rate": getattr(result, "funding_rate", None),
            "obv_divergence": getattr(result, "obv_divergence", None),
            "open_interest_usd": getattr(result, "open_interest_usd", None),
            "oi_change_pct": getattr(result, "oi_change_pct", None),
            "long_short_ratio": getattr(result, "long_short_ratio", None),
            "upper_wick_ratio_1h": getattr(
                result, "upper_wick_ratio_1h", None
            ),
            "consecutive_green_1h": getattr(
                result, "consecutive_green_1h", None
            ),
            "consecutive_green_4h": getattr(
                result, "consecutive_green_4h", None
            ),
            "ma20_deviation_pct": getattr(
                result, "ma20_deviation_pct", None
            ),
            "candle_body_ratio": getattr(result, "candle_body_ratio", None),
            "daily_direction": getattr(result, "daily_direction", None),
        }
    )


def record_analysis_event(
    result: Any,
    *,
    regime: str,
    proposal: Any,
    policy_version: str,
    policy_fingerprint: str,
    btc_change_1h: float | None = None,
    ask_price: float | None = None,
    bid_price: float | None = None,
    recorded_at: str | None = None,
) -> dict[str, Any]:
    """Record one candidate, including candidates rejected by STRICT."""
    available_at = normalize_timestamp(recorded_at or utc_now_iso())
    signal_candle_at = str(
        getattr(result, "signal_candle_at", "") or ""
    ).strip()
    observed_at = normalize_timestamp(signal_candle_at, fallback=available_at)
    spread_pct = None
    if ask_price and bid_price and ask_price > 0 and bid_price > 0:
        midpoint = (ask_price + bid_price) / 2
        spread_pct = (ask_price - bid_price) / midpoint * 100
    identity = signal_identity(
        symbol=getattr(result, "symbol", ""),
        signal_candle_at=signal_candle_at,
        detected_at=available_at,
        policy_fingerprint=policy_fingerprint,
    )
    features = _canonical_features(
        result,
        btc_change_1h=btc_change_1h,
    )
    event = make_event(
        event_type="mexc.shadow_signal",
        dataset=DATASET_SIGNALS,
        event_time=observed_at,
        available_at=available_at,
        identity=identity,
        policy_fingerprint=policy_fingerprint or None,
        tags=[
            "strict-pass"
            if bool(getattr(result, "is_confirmed_signal", False))
            else "strict-reject",
            str(regime or "UNKNOWN").lower(),
        ],
        payload={
            "symbol": getattr(result, "symbol", ""),
            "signal_candle_at": signal_candle_at or None,
            "detected_at": available_at,
            "policy_version": policy_version or "unversioned",
            "policy_fingerprint": policy_fingerprint,
            "market_regime": regime,
            "confirmed_strict": bool(
                getattr(result, "is_confirmed_signal", False)
            ),
            "strict_reject_reasons": list(
                getattr(result, "reject_reasons", []) or []
            ),
            "features": features,
            "data_quality": signal_data_quality(
                features=features,
                signal_candle_at=signal_candle_at,
                ask_price=ask_price,
                bid_price=bid_price,
            ),
            "entry_plan": {
                "entry_price": getattr(proposal, "entry_price", None),
                "sl_price": getattr(proposal, "stop_loss", None),
                "tp_price": getattr(proposal, "take_profit", None),
                "sl_pct": getattr(proposal, "sl_pct", None),
                "tp_pct": getattr(proposal, "tp_pct", None),
                "ask_price": ask_price,
                "bid_price": bid_price,
                "spread_pct": spread_pct,
            },
        },
    )
    append_outbox_event(event)
    return event


def _filter_payload(decision: Any | None) -> dict[str, Any] | None:
    if decision is None:
        return None
    return json_value(
        {
            "passed": getattr(decision, "passed", None),
            "tier": getattr(decision, "tier", None),
            "reasons": list(getattr(decision, "reasons", []) or []),
            "block_reasons": list(
                getattr(decision, "block_reasons", []) or []
            ),
            "boosters": list(getattr(decision, "boosters", []) or []),
            "score": getattr(decision, "score", None),
            "strategy_id": getattr(decision, "strategy_id", None),
        }
    )


def _plan_payload(plan: Any | None) -> dict[str, Any] | None:
    if plan is None:
        return None
    return json_value(
        {
            "direction": getattr(plan, "direction", None),
            "entry_style": getattr(plan, "entry_style", None),
            "legs": getattr(plan, "legs", None),
            "stop_loss": getattr(plan, "stop_loss", None),
            "take_profit": getattr(plan, "take_profit", None),
            "sl_pct": getattr(plan, "sl_pct", None),
            "tp_pct": getattr(plan, "tp_pct", None),
            "risk_pct_of_account": getattr(
                plan, "risk_pct_of_account", None
            ),
            "position_usdt": getattr(plan, "position_usdt", None),
            "tier": getattr(plan, "tier", None),
            "reasons": list(getattr(plan, "reasons", []) or []),
        }
    )


def record_live_decision_event(
    result: Any,
    *,
    accepted: bool,
    stage: str,
    reasons: list[str],
    policy_version: str,
    policy_fingerprint: str,
    dry_run: bool,
    filter_decision: Any | None = None,
    plan: Any | None = None,
    fundamental: Any | None = None,
    context: Mapping[str, Any] | None = None,
    decided_at: str | None = None,
) -> dict[str, Any]:
    """Append one idempotent live approval/rejection event."""
    available_at = normalize_timestamp(decided_at or utc_now_iso())
    signal_candle_at = str(
        getattr(result, "signal_candle_at", "") or ""
    ).strip()
    event_type = "mexc.live_decision" if accepted else "mexc.live_reject"
    mode = "dry_run" if dry_run else "live"
    identity = {
        **signal_identity(
            symbol=getattr(result, "symbol", ""),
            signal_candle_at=signal_candle_at,
            detected_at=available_at,
            policy_fingerprint=policy_fingerprint,
        ),
        "mode": mode,
        "stage": stage,
        "decision_at": available_at,
    }
    direction = str(getattr(plan, "direction", "") or "")
    entry_style = str(getattr(plan, "entry_style", "") or "")
    strategy_id = (
        f"mexc:{direction}:{entry_style}"
        if direction and entry_style
        else None
    )
    event = make_event(
        event_type=event_type,
        dataset=DATASET_DECISIONS,
        event_time=signal_candle_at or available_at,
        available_at=available_at,
        identity=identity,
        strategy_id=strategy_id,
        policy_fingerprint=policy_fingerprint or None,
        tags=[mode, stage, "accepted" if accepted else "rejected"],
        payload={
            "symbol": getattr(result, "symbol", ""),
            "signal_group_id": signal_group_id(
                symbol=getattr(result, "symbol", ""),
                signal_candle_at=signal_candle_at,
                policy_fingerprint=policy_fingerprint,
            ),
            "signal_candle_at": signal_candle_at or None,
            "decision_at": available_at,
            "mode": mode,
            "stage": stage,
            "accepted": accepted,
            "reasons": list(reasons),
            "policy_version": policy_version or "unversioned",
            "policy_fingerprint": policy_fingerprint,
            "filter": _filter_payload(filter_decision),
            "plan": _plan_payload(plan),
            "fundamental": json_value(fundamental),
            "context": json_value(dict(context or {})),
        },
    )
    append_outbox_event(event)
    return event


def record_guard_state_event(
    *,
    guard_key: str,
    active: bool,
    level: str,
    reasons: list[str],
    metrics: Mapping[str, Any],
    policy_version: str,
    policy_fingerprint: str,
    dry_run: bool,
    decided_at: str | None = None,
) -> dict[str, Any]:
    """Record the current safety-guard state for the independent live runner.

    This is emitted once per scanner cycle.  The live runner uses the newest
    explicit state instead of inferring current status from an old rejected
    candidate, which prevents stale circuit-breaker alerts and stale entries.
    """
    available_at = normalize_timestamp(decided_at or utc_now_iso())
    mode = "dry_run" if dry_run else "live"
    event = make_event(
        event_type="mexc.guard_state",
        dataset=DATASET_DECISIONS,
        event_time=available_at,
        available_at=available_at,
        identity={
            "guard_key": guard_key,
            "observed_at": available_at,
            "active": active,
            "policy_fingerprint": policy_fingerprint,
        },
        policy_fingerprint=policy_fingerprint or None,
        tags=[mode, "guard", level, "active" if active else "inactive"],
        payload={
            "stage": f"{guard_key}_state",
            "guard_key": guard_key,
            "active": active,
            "level": level,
            "reasons": list(reasons),
            "metrics": json_value(dict(metrics)),
            "policy_version": policy_version or "unversioned",
            "policy_fingerprint": policy_fingerprint,
            "mode": mode,
            "decision_at": available_at,
        },
    )
    append_outbox_event(event)
    return event


def try_record(func: Any, *args: Any, **kwargs: Any) -> dict[str, Any] | None:
    """Best-effort telemetry wrapper; storage must not change trade selection."""
    try:
        return func(*args, **kwargs)
    except Exception as exc:
        logger.warning("Trading-data event capture failed: %s", exc)
        return None
