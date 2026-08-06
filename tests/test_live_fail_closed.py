from __future__ import annotations

import unittest
from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from unittest.mock import patch

from core.fundamental import FundamentalAnalyzer
from core.live_filter import LiveTradeFilter


def _analysis_result(**overrides):
    values = {
        "rsi": 70.0,
        "rsi_4h": 60.0,
        "relative_strength_pct": 6.0,
        "atr_pct": 9.0,
        "consecutive_green_1h": 2,
        "consecutive_green_4h": 1,
        "bb_width_pct": 10.0,
        "ma20_deviation_pct": 3.0,
        "upper_wick_ratio_1h": 0.9,
        "volume_trend": "RISING",
        "funding_rate": 0.01,
        "obv_divergence": "NONE",
        "daily_direction": "GREEN",
        "signal_candle_at": (
            datetime.now(timezone.utc) - timedelta(hours=1)
        ).isoformat(),
    }
    values.update(overrides)
    return SimpleNamespace(**values)


class FundamentalAvailabilityTest(unittest.TestCase):
    def test_all_source_failures_are_unknown_not_high_conviction(self) -> None:
        analyzer = FundamentalAnalyzer()
        analyzer._sources_attempted = 7
        analyzer._sources_succeeded = 0

        result = analyzer._evaluate(
            "TEST/USDT:USDT",
            "TEST",
            [],
        )

        self.assertEqual(result.news_count, -1)
        self.assertEqual(result.catalyst_type, "UNKNOWN")
        self.assertEqual(result.short_conviction, "UNKNOWN")
        self.assertEqual(result.sources_succeeded, 0)

    def test_no_articles_is_high_only_when_a_source_succeeded(self) -> None:
        analyzer = FundamentalAnalyzer()
        analyzer._sources_attempted = 7
        analyzer._sources_succeeded = 2

        result = analyzer._evaluate(
            "TEST/USDT:USDT",
            "TEST",
            [],
        )

        self.assertEqual(result.news_count, 0)
        self.assertEqual(result.short_conviction, "HIGH")
        self.assertEqual(result.sources_succeeded, 2)


class LiveFilterFailClosedTest(unittest.TestCase):
    def setUp(self) -> None:
        self.env = patch.dict(
            "os.environ",
            {
                "LIVE_REQUIRE_COMPLETE_TECHNICAL_DATA": "true",
                "LIVE_REQUIRE_FUNDING_DATA": "true",
                "LIVE_REQUIRE_FUND_NON_AVOID": "true",
                "LIVE_ALLOWED_FUNDAMENTAL_CONVICTIONS": "HIGH,MEDIUM",
                "LIVE_BLOCK_UPPER_WICK": "false",
                "LIVE_POLICY_VERSION": "",
                "LIVE_REQUIRE_POLICY_VERSION": "false",
                "LIVE_DATA_DRIVEN_MARKET_SHORT_V2": "false",
            },
            clear=False,
        )
        self.env.start()
        self.addCleanup(self.env.stop)
        self.live_filter = LiveTradeFilter()

    def test_nonfinite_or_inverted_configuration_stops_initialization(self) -> None:
        for overrides in (
            {"LIVE_RSI_4H_MAX": "nan"},
            {"BLOCK_ATR_LO": "9", "BLOCK_ATR_HI": "7"},
            {"LIVE_ALLOWED_FUNDAMENTAL_CONVICTIONS": ""},
        ):
            with self.subTest(overrides=overrides):
                with patch.dict("os.environ", overrides, clear=False):
                    with self.assertRaises(ValueError):
                        LiveTradeFilter()

    def test_missing_funding_is_rejected(self) -> None:
        decision = self.live_filter.evaluate(
            _analysis_result(funding_rate=None),
            fundamental_conviction="HIGH",
        )
        self.assertFalse(decision.passed)
        self.assertTrue(
            any("funding_rate n/a" in reason for reason in decision.reasons)
        )

    def test_nonfinite_inputs_are_rejected(self) -> None:
        for field, value in (
            ("rsi", float("nan")),
            ("rsi_4h", float("inf")),
            ("relative_strength_pct", float("-inf")),
            ("funding_rate", float("nan")),
        ):
            with self.subTest(field=field):
                decision = self.live_filter.evaluate(
                    _analysis_result(**{field: value}),
                    fundamental_conviction="HIGH",
                )
                self.assertFalse(decision.passed)

    def test_signal_candle_must_be_present_fresh_and_timezone_aware(self) -> None:
        cases = (
            None,
            "2026-07-29T12:00:00",
            (datetime.now(timezone.utc) - timedelta(hours=4)).isoformat(),
            (datetime.now(timezone.utc) + timedelta(minutes=1)).isoformat(),
        )
        for timestamp in cases:
            with self.subTest(timestamp=timestamp):
                decision = self.live_filter.evaluate(
                    _analysis_result(signal_candle_at=timestamp),
                    fundamental_conviction="HIGH",
                )
                self.assertFalse(decision.passed)

    def test_unknown_fundamental_is_rejected(self) -> None:
        decision = self.live_filter.evaluate(
            _analysis_result(),
            fundamental_conviction="UNKNOWN",
        )
        self.assertFalse(decision.passed)
        self.assertTrue(
            any("fundamental=UNKNOWN" in reason for reason in decision.reasons)
        )

    def test_missing_block_indicator_is_rejected(self) -> None:
        decision = self.live_filter.evaluate(
            _analysis_result(bb_width_pct=None),
            fundamental_conviction="HIGH",
        )
        self.assertFalse(decision.passed)
        self.assertTrue(
            any("BB width" in reason for reason in decision.reasons)
        )

    def test_stale_upper_wick_block_is_disabled_by_default(self) -> None:
        decision = self.live_filter.evaluate(
            _analysis_result(upper_wick_ratio_1h=0.95),
            fundamental_conviction="HIGH",
        )
        self.assertTrue(decision.passed)

    def test_historical_population_uses_same_fail_closed_filters(self) -> None:
        historical = SimpleNamespace(
            confirmed_strict=True,
            short_conviction="HIGH",
            spread_pct=0.02,
            filters=SimpleNamespace(
                rsi=70.0,
                rsi_4h=60.0,
                relative_strength=6.0,
                atr_pct=9.0,
                consecutive_green_1h=2,
                bb_width_pct=10.0,
                ma20_deviation_pct=3.0,
                upper_wick_ratio_1h=0.9,
                volume_trend="RISING",
                funding_rate=0.01,
            ),
        )
        self.assertTrue(self.live_filter.historical_trade_passes(historical))

        historical.short_conviction = "UNKNOWN"
        self.assertFalse(self.live_filter.historical_trade_passes(historical))
        historical.short_conviction = "HIGH"
        historical.spread_pct = 0.11
        self.assertFalse(self.live_filter.historical_trade_passes(historical))

    def test_historical_population_resets_when_policy_version_changes(self) -> None:
        with patch.dict(
            "os.environ",
            {"LIVE_POLICY_VERSION": "new-policy"},
            clear=False,
        ):
            live_filter = LiveTradeFilter()
            historical = SimpleNamespace(
                policy_version="old-policy",
                policy_fingerprint=live_filter._policy_fingerprint,
                confirmed_strict=True,
                short_conviction="HIGH",
                spread_pct=0.02,
                filters=SimpleNamespace(
                    rsi=70.0,
                    rsi_4h=60.0,
                    relative_strength=6.0,
                    atr_pct=9.0,
                    consecutive_green_1h=2,
                    bb_width_pct=10.0,
                    ma20_deviation_pct=3.0,
                    upper_wick_ratio_1h=0.9,
                    volume_trend="RISING",
                    funding_rate=0.01,
                ),
            )
            self.assertFalse(
                live_filter.historical_trade_passes(historical)
            )
            historical.policy_version = "new-policy"
            self.assertTrue(
                live_filter.historical_trade_passes(historical)
            )
            historical.policy_fingerprint = "different"
            self.assertFalse(
                live_filter.historical_trade_passes(historical)
            )


class DataDrivenMarketShortFilterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.env = patch.dict(
            "os.environ",
            {
                "LIVE_DATA_DRIVEN_MARKET_SHORT_V2": "true",
                "LIVE_MIN_FUNDING_RATE_PCT": "-0.05",
                "LIVE_ALLOWED_FUNDAMENTAL_CONVICTIONS": (
                    "HIGH,MEDIUM,UNKNOWN"
                ),
            },
            clear=False,
        )
        self.env.start()
        self.addCleanup(self.env.stop)
        self.live_filter = LiveTradeFilter()

    def test_accepts_reproduced_setup_with_unknown_fundamental(self) -> None:
        decision = self.live_filter.evaluate(
            _analysis_result(
                daily_direction="RED",
                consecutive_green_1h=3,
                funding_rate=0.01,
            ),
            fundamental_conviction="UNKNOWN",
        )

        self.assertTrue(decision.passed)
        self.assertEqual("S", decision.tier)
        self.assertEqual(
            "market_short_daily_red_green_3_4_v2",
            decision.strategy_id,
        )

    def test_rejects_setup_miss_avoid_and_unsafe_funding(self) -> None:
        cases = (
            (
                _analysis_result(
                    daily_direction="GREEN", consecutive_green_1h=3
                ),
                "UNKNOWN",
            ),
            (
                _analysis_result(
                    daily_direction="RED", consecutive_green_1h=2
                ),
                "UNKNOWN",
            ),
            (
                _analysis_result(
                    daily_direction="RED",
                    consecutive_green_1h=3,
                    funding_rate=-0.051,
                ),
                "UNKNOWN",
            ),
            (
                _analysis_result(
                    daily_direction="RED", consecutive_green_1h=3
                ),
                "AVOID",
            ),
        )
        for result, conviction in cases:
            with self.subTest(conviction=conviction, result=result):
                self.assertFalse(
                    self.live_filter.evaluate(
                        result,
                        fundamental_conviction=conviction,
                    ).passed
                )

    def test_historical_predicate_matches_the_same_setup(self) -> None:
        historical = SimpleNamespace(
            short_conviction="UNKNOWN",
            filters=SimpleNamespace(
                daily_direction="RED",
                consecutive_green_1h=4,
                funding_rate=0.01,
            ),
        )
        self.assertTrue(self.live_filter.historical_trade_passes(historical))
        historical.filters.consecutive_green_1h = 5
        self.assertFalse(self.live_filter.historical_trade_passes(historical))


if __name__ == "__main__":
    unittest.main()
