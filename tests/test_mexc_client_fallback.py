from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import ccxt

from core.market_context import MarketContextRecorder
from utils.mexc_client import MEXCClient


class MEXCClientFallbackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = MEXCClient()

    def test_contract_markets_are_converted_to_ccxt_symbols(self) -> None:
        rows = [
            {
                "symbol": "BTC_USDT",
                "baseCoin": "BTC",
                "quoteCoin": "USDT",
                "state": 0,
                "apiAllowed": True,
                "contractSize": 0.0001,
            }
        ]
        with (
            patch.object(self.client, "_call_with_retry", side_effect=RuntimeError("ccxt down")),
            patch.object(self.client, "_direct_get", return_value=rows),
        ):
            self.assertEqual(
                self.client.fetch_swap_usdt_symbols(),
                ["BTC/USDT:USDT"],
            )

    def test_ticker_fallback_preserves_scanner_fields(self) -> None:
        rows = [
            {
                "symbol": "BTC_USDT",
                "lastPrice": "100",
                "riseFallRate": "0.0125",
                "amount24": "2500000",
                "volume24": "25000",
                "bid1": "99.9",
                "ask1": "100.1",
            }
        ]
        with (
            patch.object(self.client, "_call_with_retry", side_effect=RuntimeError("ccxt down")),
            patch.object(self.client, "_direct_get", return_value=rows),
        ):
            ticker = self.client.fetch_tickers(["BTC/USDT:USDT"])["BTC/USDT:USDT"]

        self.assertEqual(ticker["last"], 100.0)
        self.assertEqual(ticker["percentage"], 1.25)
        self.assertEqual(ticker["quoteVolume"], 2_500_000.0)

    def test_kline_fallback_converts_column_arrays_to_ohlcv(self) -> None:
        data = {
            "time": [100, 200],
            "open": [10, 11],
            "high": [12, 13],
            "low": [9, 10],
            "close": [11, 12],
            "vol": [1000, 1100],
        }
        with (
            patch.object(self.client, "_call_with_retry", side_effect=RuntimeError("ccxt down")),
            patch.object(self.client, "_direct_get", return_value=data) as direct_get,
        ):
            candles = self.client.fetch_ohlcv("BTC/USDT:USDT", "1h", 2)

        self.assertEqual(candles[0], [100000, 10.0, 12.0, 9.0, 11.0, 1000.0])
        direct_get.assert_called_once_with(
            "/kline/BTC_USDT",
            {"interval": "Min60", "limit": 2},
        )

    def test_mutating_create_order_is_never_retried(self) -> None:
        create_order = MagicMock(side_effect=ccxt.NetworkError("timeout"))
        self.client._exchange = SimpleNamespace(
            create_order=create_order,
            rateLimit=0,
        )

        with self.assertRaises(ccxt.NetworkError):
            self.client.create_order(
                "BTC/USDT:USDT",
                "market",
                "sell",
                1.0,
                params={"externalOid": "test-idempotency-key"},
            )

        create_order.assert_called_once()

    def test_funding_rate_uses_direct_official_fallback(self) -> None:
        with (
            patch.object(
                self.client,
                "_call_with_retry",
                side_effect=RuntimeError("ccxt unavailable"),
            ),
            patch.object(
                self.client,
                "_direct_get",
                return_value={"fundingRate": "0.00018"},
            ) as direct_get,
        ):
            rate = self.client.fetch_funding_rate("BTC/USDT:USDT")

        self.assertAlmostEqual(rate or 0.0, 0.018)
        direct_get.assert_called_once_with("/funding_rate/BTC_USDT")


class MarketContextValidationTest(unittest.TestCase):
    def test_invalid_btc_context_is_not_saved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "market_context.json"
            recorder = MarketContextRecorder(output)
            recorder.record(
                cycle=1,
                btc_status=SimpleNamespace(
                    symbol="BTC/USDT:USDT",
                    price=0.0,
                    change_1h_pct=0.0,
                    regime="STAGNANT",
                    is_signal_active=False,
                ),
                scan_context={"available": False},
                analysis_results=[],
            )
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
