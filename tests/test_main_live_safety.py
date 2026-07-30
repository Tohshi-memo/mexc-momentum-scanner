from __future__ import annotations

import os
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import main
from core.live_strategy import (
    DIR_SHORT,
    ENTRY_MARKET,
    EntryLeg,
    LiveTradePlan,
)


def _result(
    symbol: str = "AAA/USDT:USDT",
    *,
    signal_candle_at: str | None = "2026-07-29T06:00:00+00:00",
) -> SimpleNamespace:
    return SimpleNamespace(
        symbol=symbol,
        price=100.0,
        rsi=72.0,
        bb_upper=99.0,
        change_1h_pct=6.5,
        volume_24h_usdt=2_000_000.0,
        relative_strength_pct=6.0,
        is_confirmed_signal=True,
        signal_candle_at=signal_candle_at,
    )


def _plan(symbol: str = "AAA/USDT:USDT") -> LiveTradePlan:
    return LiveTradePlan(
        symbol=symbol,
        direction=DIR_SHORT,
        entry_style=ENTRY_MARKET,
        legs=[EntryLeg(kind="MARKET", price=100.0, weight=1.0)],
        stop_loss=104.0,
        take_profit=92.0,
        sl_pct=4.0,
        tp_pct=8.0,
        risk_pct_of_account=0.37,
        position_usdt=9.25,
        tier="S",
    )


class ProposalSafetyBoundaryTest(unittest.TestCase):
    def test_proposal_carries_risk_and_restart_stable_intent_key(self) -> None:
        result = _result()
        plan = _plan()

        with patch.dict(
            os.environ,
            {"LIVE_ACCOUNT_ID": " account-7 "},
            clear=False,
        ):
            first = main._proposal_from_live_plan(result, None, plan)
            second = main._proposal_from_live_plan(result, None, plan)

        self.assertIsNotNone(first)
        self.assertIsNotNone(second)
        assert first is not None
        assert second is not None
        self.assertEqual(first.risk_pct_of_account, 0.37)
        self.assertEqual(
            first.idempotency_key,
            (
                "account-7|AAA/USDT:USDT|short|MARKET|"
                "2026-07-29T06:00:00+00:00"
            ),
        )
        self.assertEqual(first.idempotency_key, second.idempotency_key)

    def test_missing_account_or_signal_candle_yields_no_intent_key(self) -> None:
        with self.subTest(missing="account"):
            with patch.dict(
                os.environ,
                {"LIVE_ACCOUNT_ID": ""},
                clear=False,
            ):
                proposal = main._proposal_from_live_plan(
                    _result(),
                    None,
                    _plan(),
                )
            self.assertIsNotNone(proposal)
            assert proposal is not None
            self.assertIsNone(proposal.idempotency_key)

        with self.subTest(missing="signal_candle"):
            with patch.dict(
                os.environ,
                {"LIVE_ACCOUNT_ID": "account-7"},
                clear=False,
            ):
                proposal = main._proposal_from_live_plan(
                    _result(signal_candle_at=None),
                    None,
                    _plan(),
                )
            self.assertIsNotNone(proposal)
            assert proposal is not None
            self.assertIsNone(proposal.idempotency_key)


class RunOnceLiveAbortTest(unittest.TestCase):
    def _dependencies(
        self,
        executor: Mock,
        *,
        first_signal_candle: str | None = "2026-07-29T06:00:00+00:00",
        tracker_add_side_effect=None,
    ) -> dict:
        btc_status = SimpleNamespace(
            price=65_000.0,
            change_1h_pct=0.1,
            is_bearish=False,
            is_stagnant=True,
            is_signal_active=True,
            regime="STAGNANT",
        )
        results = [
            _result(
                "AAA/USDT:USDT",
                signal_candle_at=first_signal_candle,
            ),
            _result(
                "BBB/USDT:USDT",
                signal_candle_at="2026-07-29T07:00:00+00:00",
            ),
        ]

        scanner = SimpleNamespace(
            _client=object(),
            last_scan_context={},
            run_scan=Mock(return_value=(btc_status, [object(), object()])),
        )
        analyzer = Mock()
        analyzer.analyze_candidates.return_value = results

        stats = Mock()
        stats.summary.return_value = SimpleNamespace(recent_losses=0)
        stats.circuit_breaker_active.return_value = False
        stats.had_sl_within.return_value = False

        tracker = Mock()
        tracker.update_prices.return_value = []
        tracker.active_symbols.return_value = []
        tracker.clean_expired.return_value = []
        tracker.add_if_new.return_value = True
        if tracker_add_side_effect is not None:
            tracker.add_if_new.side_effect = tracker_add_side_effect

        fundamental = SimpleNamespace(
            short_conviction="MEDIUM",
            catalyst_type="NONE",
            news_count=0,
        )
        fundamental_analyzer = Mock()
        fundamental_analyzer.analyze.return_value = fundamental

        live_decision = SimpleNamespace(
            passed=True,
            tier="S",
            boosters=[],
            score=0.0,
            summary=lambda: "PASS",
        )
        live_filter = Mock()
        live_filter.evaluate.return_value = live_decision

        live_strategy = Mock()
        live_strategy.build.side_effect = (
            lambda result, *_args, **_kwargs: _plan(result.symbol)
        )

        experiment_tracker = Mock()
        live_portfolio = Mock()
        live_portfolio.balance = 100.0

        return {
            "cycle": 1,
            "scanner": scanner,
            "analyzer": analyzer,
            "fundamental_analyzer": fundamental_analyzer,
            "builder": Mock(),
            "executor": executor,
            "tracker": tracker,
            "stats": stats,
            "notifier": Mock(),
            "experiment_tracker": experiment_tracker,
            "live_portfolio": live_portfolio,
            "live_filter": live_filter,
            "live_strategy": live_strategy,
            "market_context": Mock(),
            "experiment_max_per_cycle": 0,
            "max_live_orders_per_run": 2,
            "dry_run": False,
            "cooldown_hours": 48,
            "cb_window": 10,
            "cb_loss_threshold": 5,
        }

    @staticmethod
    def _run_silently(dependencies: dict, *, account_id: str = "account-7"):
        display_names = (
            "print_header",
            "print_stats_panel",
            "print_btc_status",
            "print_scan_result",
            "print_analysis_result",
            "print_confirmed_signal",
        )
        display_patches = {
            name: Mock()
            for name in display_names
        }
        with (
            patch.dict(
                os.environ,
                {"LIVE_ACCOUNT_ID": account_id},
                clear=False,
            ),
            patch.multiple(main, **display_patches),
            patch.object(main.console, "print"),
            patch.object(
                main,
                "append_confirmed_live_execution",
                return_value={},
            ),
            patch.object(main, "try_record", return_value=None),
        ):
            return main.run_once(**dependencies)

    def test_execute_exception_aborts_run_before_second_candidate(self) -> None:
        executor = Mock()
        executor.execute.side_effect = RuntimeError("transport interrupted")
        dependencies = self._dependencies(executor)

        with self.assertRaises(main.LiveExecutionSafetyError):
            self._run_silently(dependencies)

        self.assertEqual(executor.execute.call_count, 1)

    def test_non_dict_execute_result_aborts_before_second_candidate(self) -> None:
        executor = Mock()
        executor.execute.return_value = None
        dependencies = self._dependencies(executor)

        with self.assertRaises(main.LiveExecutionSafetyError):
            self._run_silently(dependencies)

        self.assertEqual(executor.execute.call_count, 1)

    def test_error_execute_status_aborts_before_second_candidate(self) -> None:
        executor = Mock()
        executor.execute.return_value = {
            "status": "error",
            "reason": "protection verification failed",
            "emergency_close": {
                "status": "ok",
                "order_id": "close-1",
            },
        }
        dependencies = self._dependencies(executor)

        with self.assertRaises(main.LiveExecutionSafetyError):
            self._run_silently(dependencies)

        self.assertEqual(executor.execute.call_count, 1)
        dependencies[
            "notifier"
        ].notify_live_execution_error.assert_called_once()

    def test_confirmed_live_fill_sends_one_telegram_notification(self) -> None:
        executor = Mock()
        executor.execute.return_value = {
            "status": "ok",
            "order_id": "order-1",
            "amount": 0.01,
            "filled_amount": 0.01,
            "average_fill_price": 100.0,
            "notional_usdt": 1.0,
            "actual_notional_usdt": 1.0,
            "risk_usdt": 0.04,
            "actual_risk_usdt": 0.04,
            "sl_price": 104.0,
            "tp_price": 92.0,
            "leverage": 2.0,
            "protection_verified": True,
        }
        dependencies = self._dependencies(executor)
        dependencies["max_live_orders_per_run"] = 1

        self._run_silently(dependencies)

        self.assertEqual(executor.execute.call_count, 1)
        dependencies[
            "notifier"
        ].notify_live_trade_opened.assert_called_once()

    def test_post_ok_processing_error_aborts_before_second_candidate(self) -> None:
        executor = Mock()
        executor.execute.return_value = {
            "status": "ok",
            "order_id": "order-1",
            "average_fill_price": 100.0,
            "sl_price": 104.0,
            "tp_price": 92.0,
        }
        dependencies = self._dependencies(
            executor,
            tracker_add_side_effect=RuntimeError("tracking write failed"),
        )

        with self.assertRaises(main.LiveExecutionSafetyError):
            self._run_silently(dependencies)

        self.assertEqual(executor.execute.call_count, 1)

    def test_missing_intent_key_aborts_without_calling_execute(self) -> None:
        cases = (
            ("account", "", "2026-07-29T06:00:00+00:00"),
            ("signal_candle", "account-7", None),
        )
        for missing, account_id, signal_candle in cases:
            with self.subTest(missing=missing):
                executor = Mock()
                dependencies = self._dependencies(
                    executor,
                    first_signal_candle=signal_candle,
                )

                with self.assertRaises(main.LiveExecutionSafetyError):
                    self._run_silently(
                        dependencies,
                        account_id=account_id,
                    )

                executor.execute.assert_not_called()

    def test_rejected_live_candidate_still_records_shadow_fundamental(self) -> None:
        executor = Mock()
        dependencies = self._dependencies(executor)
        dependencies["live_filter"].evaluate.return_value = SimpleNamespace(
            passed=False,
            tier="REJECT",
            boosters=[],
            score=0.0,
            summary=lambda: "REJECT",
        )

        self._run_silently(dependencies)

        self.assertEqual(
            2,
            dependencies["experiment_tracker"].update_fundamental.call_count,
        )
        executor.execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
