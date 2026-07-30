from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.executor import TradeProposal
from core.live_execution_ledger import append_confirmed_live_execution


def _proposal() -> TradeProposal:
    return TradeProposal(
        symbol="AAA/USDT:USDT",
        direction="short",
        entry_price=100.0,
        stop_loss=104.0,
        take_profit=92.0,
        sl_pct=4.0,
        tp_pct=8.0,
        rsi_at_entry=72.0,
        bb_upper_at_entry=99.0,
        volume_24h_usdt=2_000_000.0,
        change_1h_pct=6.0,
        risk_pct_of_account=0.1,
        idempotency_key=(
            "mexc-primary|AAA/USDT:USDT|short|MARKET|"
            "2026-07-29T06:00:00+00:00"
        ),
    )


def _execution() -> dict:
    return {
        "status": "ok",
        "order_id": "123",
        "external_oid": "mt-e-123",
        "symbol": "AAA/USDT:USDT",
        "filled_amount": 2.0,
        "average_fill_price": 100.1,
        "actual_notional_usdt": 200.2,
        "actual_risk_usdt": 0.78,
        "risk_pct_of_account": 0.1,
        "sl_price": 104.0,
        "tp_price": 92.0,
        "leverage": 2,
        "margin_mode": "isolated",
        "position_mode": "hedged",
        "fill_verified": True,
        "protection_verified": True,
        "raw": {"secretish": "not persisted"},
    }


class LiveExecutionLedgerTest(unittest.TestCase):
    def test_appends_validated_fill_without_raw_response(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ledger.jsonl"
            with patch.dict(
                "os.environ",
                {
                    "LIVE_EXECUTION_LEDGER_FILE": str(path),
                    "LIVE_ACCOUNT_ID": "mexc-primary",
                    "LIVE_POLICY_VERSION": "live-v1",
                },
                clear=False,
            ):
                record = append_confirmed_live_execution(
                    _proposal(),
                    _execution(),
                )

            stored = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(stored, record)
            self.assertEqual(
                stored["signal_candle_at"],
                "2026-07-29T06:00:00+00:00",
            )
            self.assertNotIn("raw", stored)

    def test_rejects_unverified_or_inconsistent_execution(self) -> None:
        invalid = _execution()
        invalid["protection_verified"] = False
        with self.assertRaises(RuntimeError):
            append_confirmed_live_execution(_proposal(), invalid)

        invalid = _execution()
        invalid["average_fill_price"] = 105.0
        with self.assertRaises(RuntimeError):
            append_confirmed_live_execution(_proposal(), invalid)


if __name__ == "__main__":
    unittest.main()
