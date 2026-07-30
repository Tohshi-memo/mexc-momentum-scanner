from __future__ import annotations

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

from core.causal_adaptive_portfolio import CausalAdaptivePortfolio
from core.safe_adaptive_portfolio import SafeAdaptivePortfolio


def _trade(
    symbol: str,
    detected: datetime,
    *,
    closed: datetime | None = None,
    relative_strength: float = 5.0,
    market_pnl: float = 1.0,
    long_pnl: float = -1.0,
) -> dict:
    variants = [
        {
            "strategy": "MARKET",
            "entry_price": 100.0,
            "sl_price": 104.0,
            "filled": True,
            "outcome": "EXPIRED",
            "pnl_pct": market_pnl,
        },
        {
            "strategy": "MARKET_LONG",
            "entry_price": 100.0,
            "sl_price": 96.0,
            "filled": True,
            "outcome": "EXPIRED",
            "pnl_pct": long_pnl,
        },
    ]
    return {
        "symbol": symbol,
        "detected_at": detected.isoformat(),
        "outcome_at": closed.isoformat() if closed else None,
        "market_regime": "STAGNANT",
        "filters": {"relative_strength": relative_strength},
        "entry_variants": variants,
        "pnl_pct": market_pnl if closed else None,
        "outcome": "EXPIRED" if closed else None,
    }


class CausalHistoryTest(unittest.TestCase):
    def test_history_excludes_results_closed_after_signal(self) -> None:
        signal_time = datetime(2026, 1, 2, tzinfo=timezone.utc)
        known = _trade(
            "KNOWN/USDT:USDT",
            signal_time - timedelta(hours=10),
            closed=signal_time - timedelta(hours=1),
        )
        unknown = _trade(
            "UNKNOWN/USDT:USDT",
            signal_time - timedelta(hours=9),
            closed=signal_time + timedelta(hours=1),
        )

        history = SafeAdaptivePortfolio._history_available_at(
            [known, unknown],
            signal_time,
        )

        self.assertEqual([row["symbol"] for row in history], ["KNOWN/USDT:USDT"])

    def test_selector_uses_cost_adjusted_positive_log_growth(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            portfolio = CausalAdaptivePortfolio(
                file_path=Path(directory) / "portfolio.json",
                experiment_path=Path(directory) / "experiments.json",
            )
            start = datetime(2026, 1, 1, tzinfo=timezone.utc)
            history = [
                _trade(
                    f"T{i}/USDT:USDT",
                    start + timedelta(hours=i),
                    closed=start + timedelta(hours=i, minutes=30),
                    market_pnl=1.0,
                    long_pnl=-1.0,
                )
                for i in range(100)
            ]

            decision = portfolio._select_strategy(history)

            self.assertEqual(decision["strategy"], "MARKET")
            self.assertEqual(decision["reason"], "selected_by_causal_log_growth")


class ForwardRegistrationTest(unittest.TestCase):
    def test_only_top_two_active_signals_are_registered(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            experiment_path = Path(directory) / "experiments.json"
            portfolio_path = Path(directory) / "portfolio.json"
            portfolio = CausalAdaptivePortfolio(portfolio_path, experiment_path)
            # Keep all three samples in the same minute-based signal batch.
            # A wall-clock second near :59 otherwise makes this test flaky.
            detected = (datetime.now(timezone.utc) + timedelta(minutes=1)).replace(
                second=10,
                microsecond=0,
            )
            active = [
                _trade("LOW/USDT:USDT", detected, relative_strength=5.0),
                _trade("HIGH/USDT:USDT", detected + timedelta(seconds=1), relative_strength=9.0),
                _trade("MID/USDT:USDT", detected + timedelta(seconds=2), relative_strength=7.0),
            ]
            experiment_path.write_text(
                json.dumps({"active": active, "closed": []}),
                encoding="utf-8",
            )
            decision = {
                "strategy": "MARKET",
                "direction": "short",
                "reason": "selected_by_causal_log_growth",
                "causal_score": 0.001,
                "robust_score": 0.001,
            }

            with (
                patch(
                    "core.causal_adaptive_portfolio._load_closed_records",
                    return_value=[],
                ),
                patch.object(portfolio, "_select_strategy", return_value=decision),
            ):
                result = portfolio.update()

            state = portfolio.state
            registered_symbols = {
                signal["symbol"] for signal in state["signals"].values()
            }
            self.assertEqual(result["registered"], 2)
            self.assertEqual(registered_symbols, {"HIGH/USDT:USDT", "MID/USDT:USDT"})
            self.assertEqual(state["balance"], 100.0)
            self.assertEqual(state["summary"]["trade_count"], 0)

    def test_registered_strategy_is_frozen_until_settlement(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            experiment_path = Path(directory) / "experiments.json"
            portfolio = CausalAdaptivePortfolio(
                Path(directory) / "portfolio.json",
                experiment_path,
            )
            detected = datetime.now(timezone.utc) + timedelta(minutes=1)
            active = _trade("FIXED/USDT:USDT", detected, relative_strength=9.0)
            experiment_path.write_text(
                json.dumps({"active": [active], "closed": []}),
                encoding="utf-8",
            )
            short_decision = {
                "strategy": "MARKET",
                "direction": "short",
                "reason": "selected_by_causal_log_growth",
                "causal_score": 0.001,
                "robust_score": 0.001,
            }
            with (
                patch(
                    "core.causal_adaptive_portfolio._load_closed_records",
                    return_value=[],
                ),
                patch.object(portfolio, "_select_strategy", return_value=short_decision),
            ):
                portfolio.update()

            closed = _trade(
                "FIXED/USDT:USDT",
                detected,
                closed=detected + timedelta(hours=1),
                market_pnl=8.0,
                long_pnl=-4.0,
            )
            experiment_path.write_text(
                json.dumps({"active": [], "closed": [closed]}),
                encoding="utf-8",
            )
            later_long_decision = {
                "strategy": "MARKET_LONG",
                "direction": "long",
                "reason": "selected_by_causal_log_growth",
                "causal_score": 0.002,
                "robust_score": 0.002,
            }
            with (
                patch(
                    "core.causal_adaptive_portfolio._load_closed_records",
                    return_value=[closed],
                ),
                patch.object(
                    portfolio,
                    "_select_strategy",
                    return_value=later_long_decision,
                ),
            ):
                result = portfolio.update()

            self.assertEqual(result["settled"], 1)
            self.assertEqual(portfolio.state["trades"][0]["strategy"], "MARKET")
            self.assertGreater(portfolio.state["balance"], 100.0)

    def test_pre_start_closed_data_is_not_backfilled(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            experiment_path = Path(directory) / "experiments.json"
            portfolio = CausalAdaptivePortfolio(
                Path(directory) / "portfolio.json",
                experiment_path,
            )
            old = _trade(
                "OLD/USDT:USDT",
                datetime.now(timezone.utc) - timedelta(days=2),
                closed=datetime.now(timezone.utc) - timedelta(days=1),
            )
            experiment_path.write_text(
                json.dumps({"active": [], "closed": [old]}),
                encoding="utf-8",
            )

            with patch(
                "core.causal_adaptive_portfolio._load_closed_records",
                return_value=[old],
            ):
                portfolio.update()

            self.assertEqual(portfolio.state["balance"], 100.0)
            self.assertEqual(portfolio.state["summary"]["trade_count"], 0)


if __name__ == "__main__":
    unittest.main()
