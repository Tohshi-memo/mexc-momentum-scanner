from __future__ import annotations

import time
import unittest
from unittest.mock import patch

from core.executor import LiveExecutor, TradeProposal


SYMBOL = "BTC/USDT:USDT"


class FakeExchange:
    def __init__(
        self,
        *,
        create_timeout: bool = False,
        protection_enabled: bool = True,
        leverage_error: Exception | None = None,
        fill_average: float = 99.99,
    ) -> None:
        self.create_timeout = create_timeout
        self.protection_enabled = protection_enabled
        self.leverage_error = leverage_error
        self.fill_average = fill_average
        self.create_calls: list[dict] = []
        self.leverage_calls: list[dict] = []
        self.position_open = False
        self.stored_order: dict | None = None
        self.recent_orders: list[dict] = []
        self.daily_orders: list[dict] = []

    def market(self, symbol: str) -> dict:
        self._assert_symbol(symbol)
        return {
            "id": "BTC_USDT",
            "symbol": SYMBOL,
            "contract": True,
            "swap": True,
            "settle": "USDT",
            "active": True,
            "info": {"apiAllowed": True},
            "contractSize": 1.0,
            "limits": {
                "amount": {"min": 0.001},
                "cost": {"min": 1.0},
            },
        }

    def amount_to_precision(self, symbol: str, amount: float) -> str:
        self._assert_symbol(symbol)
        return f"{amount:.8f}"

    def price_to_precision(self, symbol: str, price: float) -> str:
        self._assert_symbol(symbol)
        return f"{price:.8f}"

    def fetch_positions(self) -> list[dict]:
        if not self.position_open:
            return []
        return [
            {
                "id": "position-1",
                "symbol": SYMBOL,
                "side": "short",
                "contracts": 0.25,
                "entryPrice": 99.99,
                "info": {
                    "positionId": "position-1",
                    "positionType": 2,
                    "holdVol": "0.25",
                    "openAvgPrice": "99.99",
                },
            }
        ]

    def fetch_open_orders(self, symbol: str | None = None, *args) -> list[dict]:
        if symbol is not None:
            self._assert_symbol(symbol)
        return []

    def fetch_orders(
        self,
        symbol: str,
        since: int | None = None,
        limit: int | None = None,
    ) -> list[dict]:
        self._assert_symbol(symbol)
        return list(self.recent_orders)

    def fetch_ticker(self, symbol: str) -> dict:
        self._assert_symbol(symbol)
        now = int(time.time() * 1000)
        return {
            "symbol": SYMBOL,
            "timestamp": now,
            "last": 100.0,
            "bid": 99.99,
            "ask": 100.01,
        }

    def fetch_order_book(self, symbol: str, limit: int) -> dict:
        self._assert_symbol(symbol)
        return {
            "symbol": SYMBOL,
            "timestamp": int(time.time() * 1000),
            "bids": [[99.99, 10.0], [99.98, 10.0]],
            "asks": [[100.01, 10.0], [100.02, 10.0]],
        }

    def set_leverage(
        self,
        leverage: int,
        symbol: str,
        params: dict,
    ) -> dict:
        self._assert_symbol(symbol)
        self.leverage_calls.append(
            {"leverage": leverage, "symbol": symbol, "params": dict(params)}
        )
        if self.leverage_error is not None:
            raise self.leverage_error
        return {"success": True, "code": 0}

    def create_order(
        self,
        symbol: str,
        order_type: str,
        side: str,
        amount: float,
        price: float | None,
        params: dict,
    ) -> dict:
        self._assert_symbol(symbol)
        call = {
            "symbol": symbol,
            "type": order_type,
            "side": side,
            "amount": amount,
            "price": price,
            "params": dict(params),
        }
        self.create_calls.append(call)

        if side == "sell":
            self.position_open = True
            self.stored_order = {
                "id": "entry-1",
                "symbol": SYMBOL,
                "side": "sell",
                "status": "closed",
                "filled": amount,
                "average": self.fill_average,
                "clientOrderId": params["externalOid"],
                "info": {
                    "orderId": "entry-1",
                    "externalOid": params["externalOid"],
                    "state": 3,
                    "dealVol": str(amount),
                    "dealAvgPrice": str(self.fill_average),
                },
            }
            if self.create_timeout:
                raise TimeoutError("simulated ambiguous timeout")
            return self.stored_order

        if side == "buy" and params.get("reduceOnly") is True:
            self.position_open = False
            return {
                "id": "close-1",
                "symbol": SYMBOL,
                "side": "buy",
                "status": "closed",
                "filled": amount,
                "average": 99.98,
                "clientOrderId": params["externalOid"],
                "info": {"state": 3, "dealVol": str(amount)},
            }
        raise AssertionError(f"unexpected order call: {call}")

    def contractPrivateGetOrderExternalSymbolExternalOid(
        self,
        params: dict,
    ) -> dict:
        if params["symbol"] != "BTC_USDT":
            raise AssertionError(params)
        external_oid = params["external_oid"]
        if (
            self.stored_order is not None
            and self.stored_order["clientOrderId"] == external_oid
        ):
            return {"success": True, "code": 0, "data": self.stored_order}
        return {"success": True, "code": 0, "data": None}

    def contractPrivateGetOrderListHistoryOrders(self, params: dict) -> dict:
        return {
            "success": True,
            "code": 0,
            "data": {
                "totalCount": len(self.daily_orders),
                "resultList": list(self.daily_orders),
            },
        }

    def fetch_order(self, order_id: str, symbol: str) -> dict:
        self._assert_symbol(symbol)
        if self.stored_order is None or self.stored_order["id"] != order_id:
            raise AssertionError(f"unknown order: {order_id}")
        return self.stored_order

    def contractPrivateGetStoporderListOrders(self, params: dict) -> dict:
        if "symbol" in params and params["symbol"] != "BTC_USDT":
            raise AssertionError(params)
        records: list[dict] = []
        if self.position_open and self.protection_enabled:
            records.append(
                {
                    "symbol": "BTC_USDT",
                    "orderId": "entry-1",
                    "positionId": "position-1",
                    "state": 1,
                    "isFinished": 0,
                    "stopLossPrice": "102",
                    "takeProfitPrice": "96",
                    "stopLossVol": "0.25",
                    "takeProfitVol": "0.25",
                }
            )
        return {
            "success": True,
            "code": 0,
            "data": {"resultList": records},
        }

    @staticmethod
    def _assert_symbol(symbol: str) -> None:
        if symbol != SYMBOL:
            raise AssertionError(symbol)


class FakeClient:
    def __init__(self, exchange: FakeExchange) -> None:
        self.exchange = exchange
        self.wrapper_create_calls = 0

    def fetch_balance(self) -> dict:
        return {"USDT": {"free": 100.0, "total": 100.0}}

    def create_order(self, **kwargs) -> dict:
        self.wrapper_create_calls += 1
        raise AssertionError("retrying MEXCClient.create_order must be bypassed")


def proposal(**overrides) -> TradeProposal:
    values = {
        "symbol": SYMBOL,
        "direction": "short",
        "entry_price": 100.0,
        "stop_loss": 102.0,
        "take_profit": 96.0,
        "sl_pct": 2.0,
        "tp_pct": 4.0,
        "rsi_at_entry": 80.0,
        "bb_upper_at_entry": 99.0,
        "volume_24h_usdt": 1_000_000.0,
        "change_1h_pct": 5.0,
        "created_at": "2026-07-29T00:00:00+00:00",
        "risk_pct_of_account": 0.5,
        "idempotency_key": "acct|BTC|short|momentum|2026-07-29T00:00Z",
    }
    values.update(overrides)
    return TradeProposal(**values)


class LiveExecutorSafetyTests(unittest.TestCase):
    ENV = {
        "LIVE_BASE_RISK_PCT": "0.5",
        "LIVE_MAX_RISK_PCT": "1.5",
        "LIVE_MAX_LEVERAGE": "3",
        "LIVE_MIN_BALANCE_USDT": "5",
        "LIVE_MAX_OPEN_POSITIONS": "3",
        "LIVE_MARGIN_MODE": "isolated",
        "LIVE_OPEN_TYPE": "1",
        "LIVE_POSITION_MODE": "hedged",
        "LIVE_ORDER_VERIFY_ATTEMPTS": "1",
        "LIVE_ORDER_VERIFY_DELAY_SECONDS": "0",
        "LIVE_SYMBOL_REENTRY_COOLDOWN_HOURS": "48",
        "LIVE_MAX_NEW_ENTRIES_PER_UTC_DAY": "1",
        "LIVE_MARKET_DATA_MAX_AGE_SECONDS": "10",
        "LIVE_MAX_ENTRY_DRIFT_PCT": "0.5",
        "LIVE_MAX_SPREAD_PCT": "0.1",
        "LIVE_MAX_SLIPPAGE_PCT": "0.1",
        "LIVE_MIN_DEPTH_MULTIPLE": "1",
        "LIVE_MAX_ACTUAL_RISK_MULTIPLIER": "1.05",
    }

    def make_executor(
        self,
        exchange: FakeExchange,
    ) -> tuple[LiveExecutor, FakeClient]:
        client = FakeClient(exchange)
        with patch.dict("os.environ", self.ENV, clear=False):
            executor = LiveExecutor(client)  # type: ignore[arg-type]
        return executor, client

    def test_success_is_single_submit_and_fully_verified(self) -> None:
        exchange = FakeExchange()
        executor, client = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("ok", result["status"])
        self.assertTrue(result["fill_verified"])
        self.assertTrue(result["protection_verified"])
        self.assertTrue(result["post_fill_risk_verified"])
        self.assertAlmostEqual(24.9975, result["actual_notional_usdt"])
        self.assertEqual(1, len(exchange.create_calls))
        self.assertEqual(0, client.wrapper_create_calls)
        params = exchange.create_calls[0]["params"]
        self.assertEqual(32, len(params["externalOid"]))
        self.assertTrue(params["externalOid"].startswith("mt-e-"))
        self.assertEqual("isolated", params["marginMode"])
        self.assertEqual(1, params["openType"])
        self.assertEqual(3, params["leverage"])
        self.assertTrue(params["hedged"])
        self.assertEqual(1, params["positionMode"])
        self.assertEqual(1, exchange.leverage_calls[0]["params"]["openType"])

    def test_ambiguous_create_timeout_reconciles_without_retry(self) -> None:
        exchange = FakeExchange(create_timeout=True)
        executor, client = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("ok", result["status"])
        self.assertTrue(result["recovered_after_error"])
        self.assertEqual(1, len(exchange.create_calls))
        self.assertEqual(0, client.wrapper_create_calls)

    def test_missing_protection_triggers_one_reduce_only_close(self) -> None:
        exchange = FakeExchange(protection_enabled=False)
        executor, client = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertTrue(result["fill_verified"])
        self.assertFalse(result["protection_verified"])
        self.assertEqual("ok", result["emergency_close"]["status"])
        self.assertEqual(2, len(exchange.create_calls))
        close_call = exchange.create_calls[1]
        self.assertEqual("buy", close_call["side"])
        self.assertIs(True, close_call["params"]["reduceOnly"])
        self.assertTrue(close_call["params"]["externalOid"].startswith("mt-c-"))
        self.assertEqual(0, client.wrapper_create_calls)

    def test_leverage_failure_is_fail_closed_without_order(self) -> None:
        exchange = FakeExchange(leverage_error=RuntimeError("leverage denied"))
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertIn("set_leverage", result["reason"])
        self.assertEqual([], exchange.create_calls)

        unknown_exchange = FakeExchange()
        unknown_exchange.set_leverage = lambda leverage, symbol, params: None
        unknown_executor, _ = self.make_executor(unknown_exchange)

        unknown_result = unknown_executor.execute(proposal())

        self.assertEqual("error", unknown_result["status"])
        self.assertIn("set_leverage", unknown_result["reason"])
        self.assertEqual([], unknown_exchange.create_calls)

    def test_existing_external_oid_is_reconciled_without_mutation(self) -> None:
        exchange = FakeExchange()
        executor, _ = self.make_executor(exchange)
        expected_oid = executor._entry_external_oid(  # noqa: SLF001
            proposal(),
            amount=0.25,
            sl_price=102.0,
            tp_price=96.0,
        )
        exchange.position_open = True
        exchange.stored_order = {
            "id": "entry-1",
            "symbol": SYMBOL,
            "side": "sell",
            "status": "closed",
            "filled": 0.25,
            "average": 99.99,
            "clientOrderId": expected_oid,
            "info": {
                "orderId": "entry-1",
                "externalOid": expected_oid,
                "state": 3,
                "dealVol": "0.25",
                "dealAvgPrice": "99.99",
            },
        }

        result = executor.execute(proposal())

        self.assertEqual("ok", result["status"])
        self.assertTrue(result["reused_existing_order"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_invalid_plan_risk_and_missing_idempotency_fail_closed(self) -> None:
        exchange = FakeExchange()
        executor, _ = self.make_executor(exchange)

        too_large = executor.execute(proposal(risk_pct_of_account=2.0))
        missing_key = executor.execute(proposal(idempotency_key=""))

        self.assertEqual("error", too_large["status"])
        self.assertIn("risk_pct_of_account", too_large["reason"])
        self.assertEqual("error", missing_key["status"])
        self.assertIn("idempotency_key", missing_key["reason"])
        self.assertEqual([], exchange.create_calls)

    def test_recent_mt_entry_blocks_symbol_reentry(self) -> None:
        exchange = FakeExchange()
        exchange.recent_orders = [
            {
                "id": "prior-entry",
                "symbol": SYMBOL,
                "side": "sell",
                "status": "closed",
                "filled": 0.2,
                "timestamp": int(time.time() * 1000),
                "clientOrderId": "mt-e-" + "a" * 27,
                "info": {"reduceOnly": False},
            }
        ]
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("skipped_reentry_cooldown", result["status"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_filled_mt_entry_today_blocks_daily_entry_cap(self) -> None:
        exchange = FakeExchange()
        exchange.daily_orders = [
            {
                "orderId": "daily-entry",
                "externalOid": "mt-e-" + "b" * 27,
                "state": 3,
                "dealVol": "0.1",
                "createTime": int(time.time() * 1000),
                "symbol": "ETH_USDT",
            }
        ]
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("skipped_daily_entry_cap", result["status"])
        self.assertEqual(1, result["filled_entries_today"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_stale_or_shallow_market_data_blocks_before_mutation(self) -> None:
        stale_exchange = FakeExchange()
        stale_exchange.fetch_ticker = lambda symbol: {
            "symbol": symbol,
            "timestamp": int(time.time() * 1000) - 20_000,
            "last": 100.0,
            "bid": 99.99,
            "ask": 100.01,
        }
        stale_executor, _ = self.make_executor(stale_exchange)

        stale_result = stale_executor.execute(proposal())

        self.assertEqual("error", stale_result["status"])
        self.assertIn("market_execution_guard", stale_result["reason"])
        self.assertEqual([], stale_exchange.create_calls)
        self.assertEqual([], stale_exchange.leverage_calls)

        shallow_exchange = FakeExchange()
        shallow_exchange.fetch_order_book = lambda symbol, limit: {
            "symbol": symbol,
            "timestamp": int(time.time() * 1000),
            "bids": [[99.99, 0.1], [99.98, 0.1]],
            "asks": [[100.01, 1.0], [100.02, 1.0]],
        }
        shallow_executor, _ = self.make_executor(shallow_exchange)

        shallow_result = shallow_executor.execute(proposal())

        self.assertEqual("error", shallow_result["status"])
        self.assertIn("insufficient bid depth", shallow_result["reason"])
        self.assertEqual([], shallow_exchange.create_calls)
        self.assertEqual([], shallow_exchange.leverage_calls)

    def test_post_fill_risk_excess_triggers_reduce_only_close(self) -> None:
        exchange = FakeExchange(fill_average=98.0)
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertIn("post_fill_risk", result["reason"])
        self.assertFalse(result["post_fill_risk_verified"])
        self.assertEqual("ok", result["emergency_close"]["status"])
        self.assertEqual(2, len(exchange.create_calls))
        self.assertIs(True, exchange.create_calls[1]["params"]["reduceOnly"])

    def test_nonfinite_exchange_values_fail_closed(self) -> None:
        balance_exchange = FakeExchange()
        balance_executor, balance_client = self.make_executor(balance_exchange)
        balance_client.fetch_balance = lambda: {
            "USDT": {"free": float("nan"), "total": 100.0}
        }

        balance_result = balance_executor.execute(proposal())

        self.assertEqual("error", balance_result["status"])
        self.assertEqual([], balance_exchange.create_calls)

        position_exchange = FakeExchange()
        position_exchange.fetch_positions = lambda: [
            {"symbol": SYMBOL, "contracts": float("inf")}
        ]
        position_executor, _ = self.make_executor(position_exchange)

        position_result = position_executor.execute(proposal())

        self.assertEqual("error", position_result["status"])
        self.assertIn("fetch_positions", position_result["reason"])
        self.assertEqual([], position_exchange.create_calls)

    def test_unknown_open_entry_order_blocks_new_order(self) -> None:
        exchange = FakeExchange()
        exchange.fetch_open_orders = lambda symbol, *args: [
            {
                "id": "unknown-entry",
                "symbol": symbol,
                "side": "sell",
                "status": "open",
                "reduceOnly": False,
            }
        ]
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertIn("account_order_audit", result["reason"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_account_wide_orphan_stop_blocks_new_order(self) -> None:
        exchange = FakeExchange()

        def orphan_stop(params: dict) -> dict:
            records = (
                [
                    {
                        "symbol": "ETH_USDT",
                        "positionId": "missing-position",
                        "orderId": "orphan-stop",
                        "state": 1,
                        "stopLossPrice": "200",
                        "vol": "1",
                    }
                ]
                if "symbol" not in params
                else []
            )
            return {
                "success": True,
                "code": 0,
                "data": {"resultList": records},
            }

        exchange.contractPrivateGetStoporderListOrders = orphan_stop
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertIn("account_order_audit", result["reason"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_unmatched_existing_position_is_an_error_not_a_skip(self) -> None:
        exchange = FakeExchange()
        exchange.position_open = True
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertIn("unknown_existing_position", result["reason"])
        self.assertTrue(result["protection_verified"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_malformed_idempotency_lookup_blocks_before_order(self) -> None:
        exchange = FakeExchange()
        exchange.contractPrivateGetOrderExternalSymbolExternalOid = (
            lambda params: {"success": True, "code": 0, "data": "unknown"}
        )
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertIn("external_oid_preflight", result["reason"])
        self.assertEqual([], exchange.create_calls)
        self.assertEqual([], exchange.leverage_calls)

    def test_protection_without_symbol_and_position_binding_is_rejected(self) -> None:
        exchange = FakeExchange()

        def unbound_stops(params: dict) -> dict:
            records = []
            if exchange.position_open:
                records = [
                    {
                        "state": 1,
                        "isFinished": 0,
                        "stopLossPrice": "102",
                        "takeProfitPrice": "96",
                        "stopLossVol": "0.25",
                        "takeProfitVol": "0.25",
                    }
                ]
            return {
                "success": True,
                "code": 0,
                "data": {"resultList": records},
            }

        exchange.contractPrivateGetStoporderListOrders = unbound_stops
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertFalse(result["protection_verified"])
        self.assertEqual("ok", result["emergency_close"]["status"])
        self.assertEqual(2, len(exchange.create_calls))

    def test_protection_without_confirmed_volume_is_rejected(self) -> None:
        exchange = FakeExchange()

        def volume_unknown_stops(params: dict) -> dict:
            records = []
            if exchange.position_open:
                records = [
                    {
                        "symbol": "BTC_USDT",
                        "orderId": "entry-1",
                        "positionId": "position-1",
                        "state": 1,
                        "isFinished": 0,
                        "stopLossPrice": "102",
                        "takeProfitPrice": "96",
                    }
                ]
            return {
                "success": True,
                "code": 0,
                "data": {"resultList": records},
            }

        exchange.contractPrivateGetStoporderListOrders = volume_unknown_stops
        executor, _ = self.make_executor(exchange)

        result = executor.execute(proposal())

        self.assertEqual("error", result["status"])
        self.assertFalse(result["protection_verified"])
        self.assertEqual("ok", result["emergency_close"]["status"])


if __name__ == "__main__":
    unittest.main()
