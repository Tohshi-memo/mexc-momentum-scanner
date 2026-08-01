from __future__ import annotations

import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from core.stats import StatsManager, TradeRecord
from core.tracker import OUTCOME_SL_HIT, OUTCOME_TP_HIT


def _record(index: int, outcome: str, pnl_pct: float) -> TradeRecord:
    return TradeRecord(
        symbol=f"TEST{index}/USDT:USDT",
        detected_at=f"2026-07-31T{index:02d}:00:00+00:00",
        closed_at=f"2026-07-31T{index:02d}:30:00+00:00",
        outcome=outcome,
        entry_price=100.0,
        exit_price=100.0 - pnl_pct,
        sl_price=104.0,
        tp_price=92.0,
        pnl_pct=pnl_pct,
        hours_held=0.5,
        conviction="MEDIUM",
        catalyst_type="NONE",
        detection_rsi=70.0,
        detection_1h_change=6.0,
        live_tier="A",
        live_direction="short",
        live_entry_style="MARKET",
    )


class CircuitBreakerStateTests(unittest.TestCase):
    def _manager(self, outcomes: list[tuple[str, float]]) -> StatsManager:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        manager = StatsManager(root / "stats.json", root / "meta.json")
        manager._records = [
            _record(index, outcome, pnl)
            for index, (outcome, pnl) in enumerate(outcomes)
        ]
        return manager

    def _state(self, outcomes: list[tuple[str, float]]):
        manager = self._manager(outcomes)
        with patch.dict(
            os.environ,
            {"CIRCUIT_BREAKER_LOOKBACK_HOURS": "0"},
            clear=False,
        ):
            return manager.circuit_breaker_state(
                window=10,
                warning_loss_threshold=5,
                loss_threshold=7,
                cost_pct=0.51,
                severe_net_loss_pct=-8.0,
            )

    def test_five_losses_with_positive_net_pnl_warns_but_does_not_stop(self) -> None:
        state = self._state(
            [(OUTCOME_SL_HIT, -4.0)] * 5
            + [(OUTCOME_TP_HIT, 8.0)] * 5
        )

        self.assertFalse(state.active)
        self.assertTrue(state.warning)
        self.assertEqual(state.level, "warning")
        self.assertAlmostEqual(state.net_pnl_pct, 14.9)

    def test_seven_losses_and_negative_net_pnl_stops(self) -> None:
        state = self._state(
            [(OUTCOME_SL_HIT, -4.0)] * 7
            + [(OUTCOME_TP_HIT, 8.0)] * 3
        )

        self.assertTrue(state.active)
        self.assertEqual(state.level, "blocked")
        self.assertAlmostEqual(state.net_pnl_pct, -9.1)

    def test_severe_net_loss_stops_even_below_hard_loss_count(self) -> None:
        state = self._state(
            [(OUTCOME_SL_HIT, -4.0)] * 6
            + [(OUTCOME_TP_HIT, 1.0)] * 4
        )

        self.assertTrue(state.active)
        self.assertLessEqual(state.net_pnl_pct, -8.0)

    def test_severe_net_loss_stops_after_minimum_sample_size(self) -> None:
        state = self._state(
            [(OUTCOME_SL_HIT, -4.0)] * 4
            + [(OUTCOME_TP_HIT, 2.0)]
        )

        self.assertEqual(state.sample_size, 5)
        self.assertTrue(state.active)
        self.assertLessEqual(state.net_pnl_pct, -8.0)

    def test_positive_net_pnl_prevents_count_only_hard_stop(self) -> None:
        state = self._state(
            [(OUTCOME_SL_HIT, -1.0)] * 7
            + [(OUTCOME_TP_HIT, 8.0)] * 3
        )

        self.assertFalse(state.active)
        self.assertTrue(state.warning)

    def test_incomplete_window_is_warmup(self) -> None:
        state = self._state([(OUTCOME_SL_HIT, -4.0)] * 4)

        self.assertFalse(state.active)
        self.assertFalse(state.warning)
        self.assertEqual(state.level, "warmup")


if __name__ == "__main__":
    unittest.main()
