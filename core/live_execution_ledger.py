"""Append-only runner-local audit records for confirmed live entries.

The exchange remains the source of truth.  This ledger gives operators a
non-secret snapshot of the exact fill/protection result returned by
``LiveExecutor`` before any display, notification, or shadow tracking runs.
The workflow uploads it as an artifact; it is not a substitute for exchange
reconciliation or an external transactional risk store.
"""
from __future__ import annotations

import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from core.executor import TradeProposal
from core.live_policy import live_policy_fingerprint


DEFAULT_LEDGER_FILE = Path("logs/live-executions.jsonl")


def append_confirmed_live_execution(
    proposal: TradeProposal,
    execution: dict[str, Any],
) -> dict[str, Any]:
    """Validate and synchronously append one confirmed live entry record."""
    if execution.get("status") != "ok":
        raise RuntimeError("only status=ok executions may enter the live ledger")
    if execution.get("fill_verified") is not True:
        raise RuntimeError("live ledger requires a verified fill")
    if execution.get("protection_verified") is not True:
        raise RuntimeError("live ledger requires verified exchange protection")
    account_id = os.getenv("LIVE_ACCOUNT_ID", "").strip()
    policy_version = os.getenv("LIVE_POLICY_VERSION", "").strip()
    if not account_id or not policy_version or not proposal.idempotency_key:
        raise RuntimeError(
            "live ledger requires account, policy and idempotency identity"
        )

    required_text = {
        "order_id": execution.get("order_id"),
        "external_oid": execution.get("external_oid"),
        "symbol": execution.get("symbol"),
    }
    for field, value in required_text.items():
        if not isinstance(value, str) or not value.strip():
            raise RuntimeError(f"live ledger requires {field}")

    numeric_fields = {
        "filled_amount": execution.get("filled_amount"),
        "average_fill_price": execution.get("average_fill_price"),
        "actual_notional_usdt": execution.get("actual_notional_usdt"),
        "actual_risk_usdt": execution.get("actual_risk_usdt"),
        "risk_pct_of_account": execution.get("risk_pct_of_account"),
        "sl_price": execution.get("sl_price"),
        "tp_price": execution.get("tp_price"),
    }
    parsed_numbers: dict[str, float] = {}
    for field, value in numeric_fields.items():
        if value is None or isinstance(value, bool):
            raise RuntimeError(f"live ledger requires finite {field}")
        try:
            number = float(value)
        except (TypeError, ValueError, OverflowError) as exc:
            raise RuntimeError(f"live ledger requires finite {field}") from exc
        if not math.isfinite(number) or number <= 0:
            raise RuntimeError(f"live ledger requires positive finite {field}")
        parsed_numbers[field] = number

    fill_price = parsed_numbers["average_fill_price"]
    if not (
        parsed_numbers["sl_price"]
        > fill_price
        > parsed_numbers["tp_price"]
    ):
        raise RuntimeError("live ledger rejected inconsistent SHORT protection")

    record: dict[str, Any] = {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "account_id": account_id,
        "policy_version": policy_version,
        "policy_fingerprint": live_policy_fingerprint(),
        "signal_candle_at": (
            proposal.idempotency_key.rsplit("|", 1)[-1]
            if proposal.idempotency_key and "|" in proposal.idempotency_key
            else None
        ),
        "idempotency_key": proposal.idempotency_key,
        "direction": proposal.direction,
        "entry_style": "MARKET",
        **required_text,
        **parsed_numbers,
        "margin_mode": execution.get("margin_mode"),
        "position_mode": execution.get("position_mode"),
        "leverage": execution.get("leverage"),
        "recovered_after_error": bool(
            execution.get("recovered_after_error")
        ),
        "reused_existing_order": bool(
            execution.get("reused_existing_order")
        ),
    }

    # Avoid storing credentials or the raw exchange response.
    target = Path(
        os.getenv("LIVE_EXECUTION_LEDGER_FILE", str(DEFAULT_LEDGER_FILE))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(
        record,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    with target.open("a", encoding="utf-8") as handle:
        handle.write(encoded + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    return record
