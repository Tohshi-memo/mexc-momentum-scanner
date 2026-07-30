"""Read-only MEXC live API monitor with transition-only Telegram alerts."""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
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
) -> int:
    """Return 0 healthy, 1 API unhealthy, or 2 notification/setup failure."""
    previous = _load_state(state_file)
    previous_status = str(previous.get("status") or "unknown")
    checked_at = datetime.now(timezone.utc).isoformat()

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
        _write_state(
            state_file,
            {
                "status": status,
                "changed_at": checked_at,
                "detail": detail,
            },
        )

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
