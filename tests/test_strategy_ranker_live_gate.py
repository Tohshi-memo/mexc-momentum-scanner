from __future__ import annotations

import os
import unittest
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from unittest.mock import patch

from core.strategy_ranker import StrategyRanker


LIVE_GATE_ENV = {
    "LIVE_GATE_WINDOWS": "20,50,100,200",
    "LIVE_GATE_FEE_PCT": "0.16",
    "LIVE_GATE_SLIPPAGE_PCT": "0.10",
    "LIVE_GATE_FUNDING_PCT": "0.05",
    "LIVE_GATE_MIN_NET_EV_PCT": "0.20",
    "LIVE_GATE_MIN_FILLED": "20",
    "LIVE_GATE_MIN_FILL_RATE": "0.80",
    "LIVE_GATE_MAX_DATA_AGE_HOURS": "24",
    "LIVE_GATE_MIN_DISTINCT_DAYS": "30",
    "LIVE_GATE_MIN_CI_PCT": "0.0",
}


def _trade(
    pnl: float | None = 1.0,
    *,
    strategy: str = "MARKET",
    filled: bool = True,
    include_variant: bool = True,
    outcome_at: str | None = None,
    detected_at: str | None = None,
    eligible: bool = True,
) -> SimpleNamespace:
    variants = []
    if include_variant:
        variants.append(
            SimpleNamespace(
                strategy=strategy,
                filled=filled,
                pnl_pct=pnl,
            )
        )
    return SimpleNamespace(
        entry_variants=variants,
        outcome_at=outcome_at or datetime.now(timezone.utc).isoformat(),
        detected_at=detected_at,
        eligible=eligible,
    )


def _ranker(
    closed: list[SimpleNamespace],
    *,
    predicate=None,
) -> StrategyRanker:
    tracker = SimpleNamespace(_closed=closed)
    return StrategyRanker(tracker, live_trade_predicate=predicate)


def _history(
    count: int,
    pnl: float = 1.0,
    *,
    distinct_days: int = 40,
    latest_at: datetime | None = None,
) -> list[SimpleNamespace]:
    """古い順に並び、指定日数へ分散したclosed履歴を作る。"""
    latest = latest_at or datetime.now(timezone.utc)
    day_span = max(0, min(distinct_days, count) - 1)
    denominator = max(1, count - 1)
    return [
        _trade(
            pnl,
            outcome_at=(
                latest
                - timedelta(
                    days=((count - 1 - index) * day_span // denominator)
                )
            ).isoformat(),
        )
        for index in range(count)
    ]


class StrategyRankerLiveGateTest(unittest.TestCase):
    def test_passes_only_when_all_default_windows_have_positive_net_ev(self) -> None:
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(_history(200)).evaluate_live_gate()

        self.assertTrue(decision.passed)
        self.assertAlmostEqual(decision.total_cost_pct, 0.31)
        self.assertEqual([item.window for item in decision.windows], [20, 50, 100, 200])
        self.assertGreaterEqual(decision.distinct_days, 30)
        self.assertGreater(decision.lower95_pct or 0.0, 0.0)
        for item in decision.windows:
            self.assertTrue(item.passed)
            self.assertAlmostEqual(item.gross_ev or 0.0, 1.0)
            self.assertAlmostEqual(item.net_ev or 0.0, 0.69)

    def test_costs_are_deducted_per_filled_trade_before_ev_gate(self) -> None:
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(_history(200, 0.40)).evaluate_live_gate()

        self.assertFalse(decision.passed)
        for item in decision.windows:
            self.assertAlmostEqual(item.gross_ev or 0.0, 0.40)
            self.assertAlmostEqual(item.net_ev or 0.0, 0.09)
            self.assertFalse(item.passed)

    def test_rejects_when_long_window_disagrees_with_recent_windows(self) -> None:
        closed = _history(200)
        for trade in closed[:100]:
            trade.entry_variants[0].pnl_pct = -1.0

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        by_window = {item.window: item for item in decision.windows}
        self.assertTrue(by_window[20].passed)
        self.assertTrue(by_window[50].passed)
        self.assertTrue(by_window[100].passed)
        self.assertFalse(by_window[200].passed)
        self.assertFalse(decision.passed)

    def test_insufficient_history_fails_closed(self) -> None:
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(_history(199)).evaluate_live_gate()

        self.assertFalse(decision.passed)
        longest = decision.windows[-1]
        self.assertEqual(longest.window, 200)
        self.assertIsNone(longest.net_ev)
        self.assertIn("history 199 < required 200", longest.reasons)

    def test_missing_strategy_variant_fails_closed_without_partial_ev(self) -> None:
        closed = _history(200)
        closed[-1] = _trade(include_variant=False)

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        self.assertFalse(decision.passed)
        for item in decision.windows:
            self.assertEqual(item.missing, 1)
            self.assertIsNone(item.net_ev)
            self.assertFalse(item.passed)

    def test_missing_or_nonfinite_pnl_fails_closed(self) -> None:
        for invalid_pnl in (None, float("nan"), float("inf")):
            with self.subTest(pnl=invalid_pnl):
                closed = _history(200)
                closed[-1] = _trade(invalid_pnl)
                with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
                    decision = _ranker(closed).evaluate_live_gate()

                self.assertFalse(decision.passed)
                self.assertGreater(decision.windows[0].invalid, 0)
                self.assertIsNone(decision.windows[0].net_ev)

    def test_minimum_fill_rate_is_enforced_in_every_window(self) -> None:
        closed = _history(200)
        for index in range(5):
            closed[-(index + 1)] = _trade(1.0, filled=False)

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        recent = decision.windows[0]
        self.assertEqual(recent.window, 20)
        self.assertEqual(recent.filled, 15)
        self.assertEqual(recent.required_filled, 20)
        self.assertFalse(recent.passed)
        self.assertFalse(decision.passed)

    def test_environment_can_tighten_costs_windows_and_thresholds(self) -> None:
        env = {
            **LIVE_GATE_ENV,
            "LIVE_GATE_WINDOWS": "10,30",
            "LIVE_GATE_FEE_PCT": "0.20",
            "LIVE_GATE_SLIPPAGE_PCT": "0.20",
            "LIVE_GATE_FUNDING_PCT": "0.10",
            "LIVE_GATE_MIN_NET_EV_PCT": "0.40",
            "LIVE_GATE_MIN_FILLED": "10",
            "LIVE_GATE_MIN_FILL_RATE": "1.0",
        }
        with patch.dict(os.environ, env, clear=False):
            decision = _ranker(
                _history(30, distinct_days=30)
            ).evaluate_live_gate()

        self.assertTrue(decision.passed)
        self.assertEqual([item.window for item in decision.windows], [10, 30])
        self.assertAlmostEqual(decision.total_cost_pct, 0.50)
        self.assertAlmostEqual(decision.windows[0].net_ev or 0.0, 0.50)

    def test_existing_compute_and_top_remain_gross_ev_compatible(self) -> None:
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            ranker = _ranker([_trade(0.40) for _ in range(20)])
            stat = ranker.top(allow={"MARKET"})

        self.assertIsNotNone(stat)
        assert stat is not None
        self.assertEqual(stat.strategy, "MARKET")
        self.assertEqual(stat.filled, 20)
        self.assertAlmostEqual(stat.effective_ev, 0.40)

    def test_invalid_live_gate_configuration_stops_initialization(self) -> None:
        env = {**LIVE_GATE_ENV, "LIVE_GATE_WINDOWS": "20,bad,100"}
        with patch.dict(os.environ, env, clear=False):
            with self.assertRaisesRegex(ValueError, "LIVE_GATE_WINDOWS"):
                _ranker(_history(200))

    def test_stale_latest_trade_fails_closed(self) -> None:
        stale = (
            datetime.now(timezone.utc) - timedelta(hours=25)
        )
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(_history(200, latest_at=stale)).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertIsNotNone(decision.data_age_hours)
        self.assertGreater(decision.data_age_hours or 0.0, 24.0)
        self.assertTrue(any("freshness:" in reason for reason in decision.reasons))

    def test_detected_at_is_used_when_outcome_at_is_missing(self) -> None:
        closed = _history(200)
        for trade in closed:
            trade.detected_at = trade.outcome_at
            trade.outcome_at = None
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        self.assertTrue(decision.passed)
        self.assertEqual(decision.latest_data_at, closed[-1].detected_at)

    def test_future_latest_trade_fails_closed(self) -> None:
        future = (
            datetime.now(timezone.utc) + timedelta(minutes=1)
        ).isoformat()
        closed = _history(200)
        closed[-1].outcome_at = future
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertLess(decision.data_age_hours or 0.0, 0.0)
        self.assertTrue(any("future" in reason for reason in decision.reasons))

    def test_unparseable_latest_trade_timestamp_fails_closed(self) -> None:
        closed = _history(200)
        closed[-1].outcome_at = "not-a-timestamp"
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertIsNone(decision.data_age_hours)
        self.assertTrue(any("unparseable" in reason for reason in decision.reasons))

    def test_live_predicate_filters_population_before_windows(self) -> None:
        eligible = _history(200)
        ineligible = _history(50, -10.0, distinct_days=10)
        for trade in ineligible:
            trade.eligible = False
        closed = eligible + ineligible

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(
                closed,
                predicate=lambda trade: trade.eligible,
            ).evaluate_live_gate()

        self.assertTrue(decision.passed)
        self.assertEqual(decision.source_total, 250)
        self.assertEqual(decision.eligible_total, 200)
        self.assertTrue(all(item.net_ev == 0.69 for item in decision.windows))

    def test_live_predicate_filtered_sample_shortage_fails_closed(self) -> None:
        closed = _history(250)
        for index, trade in enumerate(closed):
            trade.eligible = index < 199

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(
                closed,
                predicate=lambda trade: trade.eligible,
            ).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertEqual(decision.eligible_total, 199)
        self.assertIn(
            "history 199 < required 200",
            decision.windows[-1].reasons,
        )

    def test_live_predicate_exception_fails_closed(self) -> None:
        def broken_predicate(_trade):
            raise RuntimeError("predicate unavailable")

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(
                _history(200),
                predicate=broken_predicate,
            ).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertEqual(decision.windows, ())
        self.assertTrue(any("predicate failed" in reason for reason in decision.reasons))

    def test_compute_remains_unfiltered_when_live_predicate_is_present(self) -> None:
        closed = _history(20, 1.0)
        closed[-1].entry_variants[0].pnl_pct = 21.0
        closed[-1].eligible = False

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            stat = _ranker(
                closed,
                predicate=lambda trade: trade.eligible,
            ).top(allow={"MARKET"})

        self.assertIsNotNone(stat)
        assert stat is not None
        self.assertAlmostEqual(stat.avg_pnl, 2.0)

    def test_daily_cluster_requires_minimum_distinct_days(self) -> None:
        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(
                _history(200, distinct_days=10)
            ).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertEqual(decision.distinct_days, 10)
        self.assertTrue(all(item.passed for item in decision.windows))
        self.assertTrue(
            any("distinct days" in reason for reason in decision.reasons)
        )

    def test_daily_lower95_must_exceed_configured_floor(self) -> None:
        now = datetime.now(timezone.utc)
        closed: list[SimpleNamespace] = []
        for day_offset in range(39, -1, -1):
            # 39日間は net +1%、最古の1日だけ net -20%。
            gross_pnl = -19.69 if day_offset == 39 else 1.31
            for _ in range(5):
                closed.append(
                    _trade(
                        gross_pnl,
                        outcome_at=(
                            now - timedelta(days=day_offset)
                        ).isoformat(),
                    )
                )

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        self.assertTrue(all(item.passed for item in decision.windows))
        self.assertEqual(decision.distinct_days, 40)
        self.assertGreater(decision.daily_mean_net_pnl or 0.0, 0.20)
        self.assertLess(decision.lower95_pct or 0.0, 0.0)
        self.assertFalse(decision.passed)

    def test_invalid_older_cluster_timestamp_fails_closed(self) -> None:
        closed = _history(200)
        closed[0].outcome_at = "invalid-older-timestamp"

        with patch.dict(os.environ, LIVE_GATE_ENV, clear=False):
            decision = _ranker(closed).evaluate_live_gate()

        self.assertFalse(decision.passed)
        self.assertIsNotNone(decision.data_age_hours)
        self.assertTrue(all(item.passed for item in decision.windows))
        self.assertTrue(
            any("daily cluster:" in reason for reason in decision.reasons)
        )


if __name__ == "__main__":
    unittest.main()
