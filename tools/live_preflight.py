"""Read-only preflight for the protected MEXC live workflow.

This command never creates, changes, or cancels an order.  It verifies that the
runtime, credentials, account mode, and ccxt endpoints required by LiveExecutor
are available before ``main.py`` is allowed to evaluate a signal.
"""
from __future__ import annotations

import math
import os
import sys
from pathlib import Path
from typing import Any

import ccxt

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from utils.mexc_client import MEXCClient


MIN_CCXT_VERSION = (4, 5, 69)
REQUIRED_EXCHANGE_METHODS = (
    "create_order",
    "fetch_order",
    "fetch_orders",
    "fetch_open_orders",
    "fetch_ticker",
    "fetch_order_book",
    "fetch_positions",
    "fetch_position_mode",
    "set_leverage",
    "contractPrivateGetOrderExternalSymbolExternalOid",
    "contractPrivateGetOrderListHistoryOrders",
    "contractPrivateGetStoporderOpenOrders",
    "contractPrivatePostStoporderPlace",
)


def _version_tuple(raw: str) -> tuple[int, int, int]:
    try:
        parts = tuple(int(part) for part in raw.split(".")[:3])
    except ValueError as exc:
        raise RuntimeError(f"Unparseable ccxt version: {raw!r}") from exc
    if len(parts) != 3:
        raise RuntimeError(f"Unparseable ccxt version: {raw!r}")
    return parts


def _finite_nonnegative_float(value: Any, *, field: str) -> float:
    """Parse an API number and reject ambiguity before safety comparisons."""
    if value is None or isinstance(value, bool):
        raise RuntimeError(f"{field} must be a finite non-negative number")
    try:
        parsed = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise RuntimeError(
            f"{field} must be a finite non-negative number"
        ) from exc
    if not math.isfinite(parsed) or parsed < 0:
        raise RuntimeError(f"{field} must be a finite non-negative number")
    return parsed


def _usdt_balance(balance: Any) -> tuple[float, float]:
    """Return validated futures USDT balances or fail closed."""
    if not isinstance(balance, dict):
        raise RuntimeError("Authenticated balance must be an object")
    usdt = balance.get("USDT")
    if not isinstance(usdt, dict):
        raise RuntimeError("Authenticated balance has no USDT object")
    free = _finite_nonnegative_float(
        usdt.get("free"),
        field="USDT free balance",
    )
    total = _finite_nonnegative_float(
        usdt.get("total"),
        field="USDT total balance",
    )
    return free, total


def _validate_position_mode(
    position_mode: Any,
    expected_mode: str,
) -> bool:
    """Validate config and require ccxt's hedged field to be exactly bool."""
    normalized = expected_mode.strip().lower()
    if normalized not in {"hedged", "one_way"}:
        raise RuntimeError("LIVE_POSITION_MODE must be 'hedged' or 'one_way'")
    if not isinstance(position_mode, dict):
        raise RuntimeError("MEXC fetch_position_mode returned invalid data")

    actual_hedged = position_mode.get("hedged")
    if type(actual_hedged) is not bool:
        raise RuntimeError(
            "MEXC position mode 'hedged' must be a strict bool"
        )

    expected_hedged = normalized == "hedged"
    if actual_hedged != expected_hedged:
        raise RuntimeError(
            f"MEXC position mode mismatch: expected hedged={expected_hedged}, "
            f"actual={actual_hedged}. Change it in MEXC before live execution."
        )
    return actual_hedged


def _count_open_positions(positions: Any) -> int:
    """Count positive contracts after validating every returned position."""
    if not isinstance(positions, list):
        raise RuntimeError("MEXC fetch_positions returned invalid data")

    open_count = 0
    for index, position in enumerate(positions):
        if not isinstance(position, dict):
            raise RuntimeError(
                f"MEXC position[{index}] must be an object"
            )
        contracts = _finite_nonnegative_float(
            position.get("contracts"),
            field=f"MEXC position[{index}] contracts",
        )
        if contracts > 0:
            open_count += 1
    return open_count


def run_preflight() -> None:
    if not os.getenv("MEXC_API_KEY") or not os.getenv("MEXC_SECRET_KEY"):
        raise RuntimeError("MEXC_API_KEY and MEXC_SECRET_KEY are required")

    installed = _version_tuple(ccxt.__version__)
    if installed < MIN_CCXT_VERSION:
        minimum = ".".join(str(part) for part in MIN_CCXT_VERSION)
        raise RuntimeError(
            f"ccxt {ccxt.__version__} is too old; require >= {minimum}"
        )

    client = MEXCClient()
    exchange = client.exchange
    exchange.load_markets()

    missing = [
        name for name in REQUIRED_EXCHANGE_METHODS
        if not callable(getattr(exchange, name, None))
    ]
    if missing:
        raise RuntimeError(
            "Installed ccxt is missing required MEXC methods: "
            + ", ".join(missing)
        )

    balance = client.fetch_balance()
    free_usdt, total_usdt = _usdt_balance(balance)
    minimum_balance = _finite_nonnegative_float(
        os.getenv("LIVE_MIN_BALANCE_USDT", "5.0"),
        field="LIVE_MIN_BALANCE_USDT",
    )
    if free_usdt < minimum_balance or total_usdt <= 0:
        raise RuntimeError(
            f"Insufficient futures USDT balance: free={free_usdt:.2f}, "
            f"total={total_usdt:.2f}, minimum={minimum_balance:.2f}"
        )

    position_mode = exchange.fetch_position_mode()
    expected_mode = os.getenv("LIVE_POSITION_MODE", "hedged").strip().lower()
    _validate_position_mode(position_mode, expected_mode)

    positions = exchange.fetch_positions()
    open_position_count = _count_open_positions(positions)
    try:
        maximum = int(os.getenv("LIVE_MAX_OPEN_POSITIONS", "1"))
    except ValueError as exc:
        raise RuntimeError(
            "LIVE_MAX_OPEN_POSITIONS must be a positive integer"
        ) from exc
    if maximum <= 0:
        raise RuntimeError(
            "LIVE_MAX_OPEN_POSITIONS must be a positive integer"
        )
    if open_position_count >= maximum:
        raise RuntimeError(
            f"Open-position cap already reached: {open_position_count}/{maximum}"
        )

    print(
        "MEXC live preflight OK "
        f"| ccxt={ccxt.__version__} "
        f"| free_usdt={free_usdt:.2f} "
        f"| total_usdt={total_usdt:.2f} "
        f"| position_mode={expected_mode} "
        f"| open_positions={open_position_count}"
    )


def main() -> int:
    try:
        run_preflight()
    except Exception as exc:
        print(f"MEXC live preflight FAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
