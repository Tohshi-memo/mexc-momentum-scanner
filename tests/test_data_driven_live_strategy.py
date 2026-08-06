from __future__ import annotations

from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from core.live_filter import (
    DATA_DRIVEN_MARKET_SHORT_ID,
    LiveFilterDecision,
    TIER_S,
)
from core.live_strategy import DIR_SHORT, ENTRY_MARKET, LiveStrategyBuilder


class DataDrivenLiveStrategyTest(unittest.TestCase):
    def test_bypasses_legacy_ranker_and_builds_market_short(self) -> None:
        proposal_builder = Mock()
        proposal_builder.build.return_value = SimpleNamespace(
            sl_pct=4.0,
            tp_pct=8.0,
        )
        decision = LiveFilterDecision(
            passed=True,
            tier=TIER_S,
            boosters=["daily_RED", "1h_green=3"],
            strategy_id=DATA_DRIVEN_MARKET_SHORT_ID,
        )
        result = SimpleNamespace(symbol="TEST/USDT:USDT", price=100.0)

        with patch.dict(
            "os.environ",
            {
                "LIVE_USE_RANKER": "true",
                "LIVE_BASE_RISK_PCT": "0.10",
                "LIVE_MAX_RISK_PCT": "0.10",
            },
            clear=False,
        ):
            plan = LiveStrategyBuilder(
                proposal_builder=proposal_builder,
                ranker=None,
            ).build(
                result,
                decision,
                account_balance_usdt=25.0,
            )

        self.assertEqual(DIR_SHORT, plan.direction)
        self.assertEqual(ENTRY_MARKET, plan.entry_style)
        self.assertEqual(1, len(plan.legs))
        self.assertEqual("MARKET", plan.legs[0].kind)
        self.assertEqual(1.0, plan.legs[0].weight)
        self.assertEqual(104.0, plan.stop_loss)
        self.assertEqual(92.0, plan.take_profit)
        self.assertEqual(0.10, plan.risk_pct_of_account)


if __name__ == "__main__":
    unittest.main()
