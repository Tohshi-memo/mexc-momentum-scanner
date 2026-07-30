"""Read-only MEXC live API monitor with transition-only Telegram alerts."""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.live_preflight import (
    _count_open_positions,
    _usdt_balance,
    _validate_position_mode,
)
from utils.mexc_client import MEXCClient
from utils.notifier import Notifier


DEFAULT_STATE_FILE = Path("data/mexc_api_health.json")
EXPIRY_ALERT_THRESHOLDS_DAYS = (5, 1, 0)
JST = timezone(timedelta(hours=9), name="JST")


def _load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return value if isinstance(value, dict) else {}


def _write_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def _sanitize_error(error: Exception) -> str:
    message = f"{type(error).__name__}: {error}"
    for name in (
        "MEXC_API_KEY",
        "MEXC_SECRET_KEY",
        "TELEGRAM_BOT_TOKEN",
        "TELEGRAM_CHAT_ID",
    ):
        value = os.getenv(name, "")
        if value:
            message = message.replace(value, "***")
    return message[:800]


def _parse_expiry(value: str) -> datetime:
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as error:
        raise ValueError(
            "MEXC_LIVE_API_EXPIRES_AT must be an ISO-8601 datetime"
        ) from error
    if parsed.tzinfo is None:
        raise ValueError(
            "MEXC_LIVE_API_EXPIRES_AT must include a timezone"
        )
    return parsed.astimezone(timezone.utc)


def _expiry_notification(
    *,
    expires_at: datetime,
    now: datetime,
    notified_thresholds: set[int],
) -> tuple[int | None, set[int]]:
    remaining_days = (
        expires_at - now
    ).total_seconds() / (24 * 60 * 60)
    reached = {
        threshold
        for threshold in EXPIRY_ALERT_THRESHOLDS_DAYS
        if remaining_days <= threshold
    }
    pending = reached - notified_thresholds
    if not pending:
        return None, notified_thresholds
    return min(pending), notified_thresholds | reached


def _run_url() -> str:
    server = os.getenv("GITHUB_SERVER_URL", "").rstrip("/")
    repository = os.getenv("GITHUB_REPOSITORY", "").strip("/")
    run_id = os.getenv("GITHUB_RUN_ID", "").strip()
    if server and repository and run_id:
        return f"{server}/{repository}/actions/runs/{run_id}"
    return ""


def check_live_api(
    client_factory: Callable[[], MEXCClient] = MEXCClient,
) -> dict[str, Any]:
    """Exercise authenticated read endpoints without placing an order."""
    if not os.getenv("MEXC_API_KEY") or not os.getenv("MEXC_SECRET_KEY"):
        raise RuntimeError("MEXC live API credentials are missing")

    client = client_factory()
    exchange = client.exchange
    exchange.load_markets()

    balance = client.fetch_balance()
    free_usdt, total_usdt = _usdt_balance(balance)

    expected_mode = os.getenv(
        "LIVE_POSITION_MODE",
        "hedged",
    ).strip().lower()
    position_mode = exchange.fetch_position_mode()
    _validate_position_mode(position_mode, expected_mode)

    positions = exchange.fetch_positions()
    open_positions = _count_open_positions(positions)
    return {
        "free_usdt": free_usdt,
        "total_usdt": total_usdt,
        "position_mode": expected_mode,
        "open_positions": open_positions,
    }


def run_monitor(
    *,
    state_file: Path,
    notifier: Notifier,
    client_factory: Callable[[], MEXCClient] = MEXCClient,
    now: datetime | None = None,
) -> int:
    """Return 0 healthy, 1 API unhealthy, or 2 notification/setup failure."""
    previous = _load_state(state_file)
    previous_status = str(previous.get("status") or "unknown")
    checked_at_datetime = now or datetime.now(timezone.utc)
    if checked_at_datetime.tzinfo is None:
        raise ValueError("now must include a timezone")
    checked_at_datetime = checked_at_datetime.astimezone(timezone.utc)
    checked_at = checked_at_datetime.isoformat()

    expiry_value = os.getenv(
        "MEXC_LIVE_API_EXPIRES_AT",
        "",
    ).strip()
    try:
        expires_at = _parse_expiry(expiry_value) if expiry_value else None
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2

    next_state = dict(previous)
    state_changed = False

    result: dict[str, Any] | None = None
    try:
        result = check_live_api(client_factory)
        status = "healthy"
        detail = (
            "認証・残高・ポジションモード・ポジション取得に成功"
        )
    except Exception as error:
        status = "unhealthy"
        detail = _sanitize_error(error)

    transition = status != previous_status
    if transition:
        if not notifier.telegram_enabled:
            print(
                "Telegram credentials are missing; health transition "
                "was not acknowledged.",
                file=sys.stderr,
            )
            return 2
        run_url = _run_url()
        notification_detail = detail
        if run_url:
            notification_detail += f"\nRun: {run_url}"
        sent = notifier.notify_api_health(
            healthy=(status == "healthy"),
            detail=notification_detail,
            free_usdt=(
                float(result["free_usdt"])
                if result is not None
                else None
            ),
            open_positions=(
                int(result["open_positions"])
                if result is not None
                else None
            ),
            initial=(previous_status == "unknown"),
        )
        if not sent:
            print(
                "Telegram health notification failed; state was not advanced.",
                file=sys.stderr,
            )
            return 2
        next_state.update(
            status=status,
            changed_at=checked_at,
            detail=detail,
        )
        state_changed = True

    if expires_at is None:
        if "expiry" in next_state:
            del next_state["expiry"]
            state_changed = True
    else:
        canonical_expiry = expires_at.isoformat()
        previous_expiry = previous.get("expiry")
        if not isinstance(previous_expiry, dict):
            previous_expiry = {}
        same_expiry = (
            previous_expiry.get("expires_at") == canonical_expiry
        )
        raw_notified = (
            previous_expiry.get("notified_threshold_days", [])
            if same_expiry
            else []
        )
        notified_thresholds = {
            int(value)
            for value in raw_notified
            if isinstance(value, int)
        }
        threshold, advanced_thresholds = _expiry_notification(
            expires_at=expires_at,
            now=checked_at_datetime,
            notified_thresholds=notified_thresholds,
        )
        expiry_state = {
            "expires_at": canonical_expiry,
            "notified_threshold_days": sorted(advanced_thresholds),
        }
        if threshold is not None:
            sent = notifier.notify_api_expiry(
                expires_at_jst=expires_at.astimezone(JST).strftime(
                    "%Y-%m-%d %H:%M JST"
                ),
                threshold_days=threshold,
            )
            if not sent:
                if state_changed:
                    _write_state(state_file, next_state)
                print(
                    "Telegram expiry notification failed; expiry state "
                    "was not advanced.",
                    file=sys.stderr,
                )
                return 2
        if previous_expiry != expiry_state:
            next_state["expiry"] = expiry_state
            state_changed = True

    if state_changed:
        _write_state(state_file, next_state)

    if status == "healthy":
        assert result is not None
        print(
            "MEXC live API health OK "
            f"| free_usdt={float(result['free_usdt']):.2f} "
            f"| total_usdt={float(result['total_usdt']):.2f} "
            f"| position_mode={result['position_mode']} "
            f"| open_positions={int(result['open_positions'])}"
        )
        return 0

    print(f"MEXC live API health FAILED: {detail}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--state-file",
        type=Path,
        default=DEFAULT_STATE_FILE,
    )
    args = parser.parse_args()
    return run_monitor(
        state_file=args.state_file,
        notifier=Notifier(),
    )


if __name__ == "__main__":
    raise SystemExit(main())
