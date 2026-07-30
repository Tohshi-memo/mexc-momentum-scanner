"""
core/executor.py
注文実行管理 - DRY RUN (Mock) モードと将来の Live モードの共通インターフェース

設計方針:
    - BaseExecutor: 注文インターフェースの抽象基底クラス
    - DryRunExecutor: ログ出力のみ（現在のデフォルト）
    - LiveExecutor: 実際の API 注文（Trade権限取得後に有効化）
    - ExecutorFactory: DRY_RUN 環境変数に基づいて適切な実装を返す
"""
from __future__ import annotations

import hashlib
import logging
import math
import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

import ccxt

from core.analyzer import AnalysisResult
from core.fundamental import FundamentalResult
from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Trade Proposal データクラス
# ---------------------------------------------------------------------------

@dataclass
class TradeProposal:
    """擬似（または実際の）トレード提案を表すデータクラス。

    エントリー根拠、損切りライン、利確目標を一元管理する。
    将来の Live 実行時はこの構造を変えずにインターフェースのみ差し替える。
    """

    symbol: str
    direction: str          # "short" (擬似ショート)
    entry_price: float      # エントリー参考価格
    stop_loss: float        # 損切りライン (SL)
    take_profit: float      # 利確目標 (TP)
    sl_pct: float           # SL 幅 (%)
    tp_pct: float           # TP 幅 (%)
    rsi_at_entry: float | None
    bb_upper_at_entry: float | None
    volume_24h_usdt: float
    change_1h_pct: float
    fundamental: FundamentalResult | None = None  # ファンダ考察結果
    created_at: str = ""    # ISO 8601 タイムスタンプ

    risk_pct_of_account: float | None = None
    idempotency_key: str | None = None

    def __post_init__(self) -> None:
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Abstract Base Class
# ---------------------------------------------------------------------------

class BaseExecutor(ABC):
    """注文実行の共通インターフェース。

    DryRunExecutor と LiveExecutor はこのクラスを継承し、
    execute() メソッドを実装する。
    main.py や scanner ループは BaseExecutor 型として扱うため、
    実装を切り替えても呼び出し側のコードは変更不要。
    """

    @abstractmethod
    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """トレード提案を実行する（またはモック出力する）。

        Args:
            proposal: TradeProposal オブジェクト
        Returns:
            実行結果の辞書。DRY RUN 時はモック結果、Live 時は取引所レスポンス。
        """
        ...

    @staticmethod
    def _response_failed(response: Any) -> bool:
        if not isinstance(response, dict):
            return False
        if response.get("success") is False:
            return True
        code = response.get("code")
        return code not in (None, 0, 200, "0", "200")

    @classmethod
    def _response_confirmed_success(cls, response: Any) -> bool:
        if not isinstance(response, dict) or cls._response_failed(response):
            return False
        success = response.get("success")
        code = response.get("code")
        if isinstance(code, bool):
            return False
        return success is True or code in (0, 200, "0", "200")

    @staticmethod
    def _derived_external_oid(seed: str, *, kind: str = "x") -> str:
        digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
        kind_marker = (kind or "x")[0].lower()
        return f"mt-{kind_marker}-{digest[:27]}"

    def _entry_external_oid(
        self,
        proposal: TradeProposal,
        *,
        amount: float,
        sl_price: float,
        tp_price: float,
    ) -> str:
        stable_intent = (
            str(proposal.idempotency_key).strip()
            if proposal.idempotency_key is not None
            else ""
        )
        if stable_intent:
            seed = "|".join(
                ("entry", proposal.symbol, proposal.direction, stable_intent)
            )
        else:
            seed = "|".join(
                (
                    "entry",
                    proposal.symbol,
                    proposal.direction,
                    proposal.created_at,
                    format(amount, ".16g"),
                    format(sl_price, ".16g"),
                    format(tp_price, ".16g"),
                )
            )
        return self._derived_external_oid(seed, kind="e")

    def _create_order_once(
        self,
        *,
        symbol: str,
        order_type: str,
        side: str,
        amount: float,
        price: float | None,
        params: dict[str, Any],
    ) -> dict[str, Any]:
        """Submit one mutating request exactly once.

        In particular, this deliberately bypasses MEXCClient.create_order:
        transport timeouts are reconciled through read-only APIs instead of
        risking a duplicate order.
        """
        response = self._client.exchange.create_order(
            symbol,
            order_type,
            side,
            amount,
            price,
            params,
        )
        if self._response_failed(response):
            raise RuntimeError(f"exchange rejected order: {response}")
        if not isinstance(response, dict):
            raise RuntimeError(f"unexpected create_order response: {response!r}")
        return response

    @staticmethod
    def _is_ambiguous_error(error: Exception) -> bool:
        if isinstance(
            error,
            (ccxt.NetworkError, TimeoutError, ConnectionError),
        ):
            return True
        message = str(error).lower()
        return any(
            marker in message
            for marker in ("timeout", "timed out", "network", "connection reset")
        )

    @staticmethod
    def _unwrap_data(response: Any) -> Any:
        value = response
        for _ in range(3):
            if not isinstance(value, dict) or "data" not in value:
                break
            value = value.get("data")
        return value

    @staticmethod
    def _order_id(order: Any) -> str | None:
        if not isinstance(order, dict):
            return None
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        data = order.get("data") if isinstance(order.get("data"), dict) else {}
        value = (
            order.get("id")
            or order.get("orderId")
            or info.get("orderId")
            or info.get("id")
            or data.get("orderId")
            or data.get("id")
        )
        return str(value) if value not in (None, "") else None

    @staticmethod
    def _order_external_oid(order: Any) -> str | None:
        if not isinstance(order, dict):
            return None
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        value = (
            order.get("clientOrderId")
            or order.get("externalOid")
            or order.get("external_oid")
            or info.get("externalOid")
            or info.get("external_oid")
        )
        return str(value) if value not in (None, "") else None

    @staticmethod
    def _order_timestamp_ms(order: Any) -> int | None:
        if not isinstance(order, dict):
            return None
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        value = (
            order.get("timestamp")
            or order.get("createTime")
            or info.get("createTime")
            or info.get("createdAt")
        )
        try:
            timestamp = int(float(value))
        except (TypeError, ValueError):
            return None
        if timestamp and timestamp < 10_000_000_000:
            timestamp *= 1000
        return timestamp

    @staticmethod
    def _is_order_not_found(error: Exception) -> bool:
        if isinstance(error, ccxt.OrderNotFound):
            return True
        message = str(error).lower()
        return any(
            marker in message
            for marker in (
                "order not found",
                "order does not exist",
                "order not exist",
                "no order exists",
                "no order found",
            )
        )

    def _fetch_recent_orders(
        self,
        symbol: str,
        *,
        hours: float,
    ) -> list[dict[str, Any]] | None:
        method = getattr(self._client.exchange, "fetch_orders", None)
        if not callable(method):
            return None
        since_ms = int(time.time() * 1000 - max(hours, 0.0) * 3_600_000)
        response = method(symbol, since_ms, 100)
        if self._response_failed(response):
            raise RuntimeError(f"fetch_orders rejected: {response}")
        data = self._unwrap_data(response)
        if not isinstance(data, list):
            raise RuntimeError(f"unexpected fetch_orders response: {response!r}")
        if not all(isinstance(item, dict) for item in data):
            raise RuntimeError("fetch_orders list contains a non-object item")
        if len(data) >= 100:
            raise RuntimeError(
                "fetch_orders history reached the page limit; cooldown audit "
                "would be incomplete"
            )
        return list(data)

    def _recent_entry_in_cooldown(
        self,
        symbol: str,
        *,
        current_external_oid: str,
    ) -> dict[str, Any] | None:
        if self._symbol_reentry_cooldown_hours <= 0:
            return None
        recent_orders = self._fetch_recent_orders(
            symbol,
            hours=self._symbol_reentry_cooldown_hours,
        )
        if recent_orders is None:
            raise RuntimeError(
                "fetch_orders unavailable while symbol re-entry cooldown is "
                "enabled"
            )

        cutoff_ms = int(
            time.time() * 1000
            - self._symbol_reentry_cooldown_hours * 3_600_000
        )
        for candidate in recent_orders:
            external_oid = self._order_external_oid(candidate)
            if (
                external_oid is None
                or external_oid == current_external_oid
                or not external_oid.startswith("mt-e-")
            ):
                continue
            if not self._symbol_matches(candidate.get("symbol"), symbol):
                continue
            timestamp = self._order_timestamp_ms(candidate)
            if timestamp is not None and timestamp < cutoff_ms:
                continue
            info = (
                candidate.get("info")
                if isinstance(candidate.get("info"), dict)
                else {}
            )
            side = str(candidate.get("side") or info.get("side") or "").lower()
            if side and side not in {"sell", "short"}:
                continue
            reduce_only = candidate.get(
                "reduceOnly",
                info.get("reduceOnly"),
            )
            if str(reduce_only).lower() in {"1", "true"}:
                continue
            status = str(candidate.get("status") or "").lower()
            if status in {"canceled", "cancelled", "rejected", "expired"} and (
                self._order_filled_amount(candidate) <= 0
            ):
                continue
            return candidate
        return None

    def _filled_mt_entries_today(self) -> list[dict[str, Any]]:
        exchange = self._client.exchange
        method = None
        for name in (
            "contractPrivateGetOrderListHistoryOrders",
            "contract_private_get_order_list_history_orders",
        ):
            candidate = getattr(exchange, name, None)
            if callable(candidate):
                method = candidate
                break
        if method is None:
            raise RuntimeError("exchange exposes no account order-history API")

        now = datetime.now(timezone.utc)
        utc_start = datetime(
            now.year,
            now.month,
            now.day,
            tzinfo=timezone.utc,
        )
        start_ms = int(utc_start.timestamp() * 1000)
        response = method(
            {
                "start_time": start_ms,
                "end_time": int(now.timestamp() * 1000),
                "page_num": 1,
                "page_size": 100,
            }
        )
        if self._response_failed(response):
            raise RuntimeError(f"daily order history rejected: {response}")
        data = self._unwrap_data(response)
        if isinstance(data, dict):
            total_value = data.get("totalCount", data.get("total"))
            if total_value is not None:
                try:
                    total_count = int(total_value)
                except (TypeError, ValueError):
                    raise RuntimeError("daily order history total is malformed")
                if total_count > 100:
                    raise RuntimeError(
                        "daily order history exceeds one audited page"
                    )
        orders = self._list_from_response(response)
        if len(orders) >= 100:
            raise RuntimeError(
                "daily order history reached the page limit; audit incomplete"
            )

        entries_by_intent: dict[str, dict[str, Any]] = {}
        for order in orders:
            external_oid = self._order_external_oid(order)
            if external_oid is None or not external_oid.startswith("mt-e-"):
                continue
            timestamp = self._order_timestamp_ms(order)
            if timestamp is not None and timestamp < start_ms:
                continue
            if self._order_is_reduce_only(order):
                continue
            info = order.get("info") if isinstance(order.get("info"), dict) else {}
            raw_state = order.get("state", info.get("state"))
            if self._order_filled_amount(order) <= 0 and str(raw_state) != "3":
                continue
            entries_by_intent[external_oid] = order
        return list(entries_by_intent.values())

    def _market_id(self, symbol: str) -> str:
        try:
            market_id = self._client.exchange.market(symbol).get("id")
            if market_id:
                return str(market_id)
        except Exception:
            pass
        return symbol.split(":", 1)[0].replace("/", "_")

    @staticmethod
    def _symbol_key(symbol: Any) -> str:
        return (
            str(symbol or "")
            .upper()
            .replace("/", "")
            .replace("_", "")
            .replace("-", "")
            .split(":", 1)[0]
        )

    def _symbol_matches(self, actual: Any, expected: str) -> bool:
        if actual in (None, ""):
            return False
        actual_key = self._symbol_key(actual)
        return actual_key in {
            self._symbol_key(expected),
            self._symbol_key(self._market_id(expected)),
        }

    def _fetch_order_by_external_oid(
        self,
        symbol: str,
        external_oid: str,
    ) -> dict[str, Any] | None:
        exchange = self._client.exchange
        method = None
        for name in (
            "fetch_order_by_external_oid",
            "contractPrivateGetOrderExternalSymbolExternalOid",
            "contract_private_get_order_external_symbol_external_oid",
        ):
            candidate = getattr(exchange, name, None)
            if callable(candidate):
                method = candidate
                break
        if method is None:
            recent_orders = self._fetch_recent_orders(
                symbol,
                hours=max(self._symbol_reentry_cooldown_hours, 48.0),
            )
            if recent_orders is None:
                raise RuntimeError(
                    "exchange exposes neither externalOid lookup nor fetch_orders"
                )
            return next(
                (
                    order
                    for order in recent_orders
                    if self._order_external_oid(order) == external_oid
                ),
                None,
            )

        params = {
            "symbol": self._market_id(symbol),
            "external_oid": external_oid,
        }
        try:
            response = method(params)
        except Exception as error:
            if self._is_order_not_found(error):
                return None
            raise
        if response is None:
            raise RuntimeError("externalOid lookup returned no response envelope")
        if self._response_failed(response):
            message = str(response).lower()
            if any(
                marker in message
                for marker in (
                    "not found",
                    "not exist",
                    "does not exist",
                    "no order exists",
                    "no order found",
                )
            ):
                return None
            raise RuntimeError(f"externalOid lookup rejected: {response}")
        data = self._unwrap_data(response)
        if isinstance(data, list):
            if not all(isinstance(item, dict) for item in data):
                raise RuntimeError(
                    "externalOid lookup list contains a non-object item"
                )
            matches = [
                item
                for item in data
                if self._order_external_oid(item) == external_oid
            ]
            if len(matches) == 1:
                return matches[0]
            if not data:
                return None
            raise RuntimeError(
                "externalOid lookup returned no unique matching order"
            )
        if data is None:
            return None
        if not isinstance(data, dict):
            raise RuntimeError("externalOid lookup returned malformed data")
        returned_external_oid = self._order_external_oid(data)
        if (
            returned_external_oid is not None
            and returned_external_oid != external_oid
        ):
            raise RuntimeError("externalOid lookup returned a different order")
        return data

    def _fetch_order_details(
        self,
        order_id: str,
        symbol: str,
    ) -> dict[str, Any] | None:
        method = getattr(self._client.exchange, "fetch_order", None)
        if not callable(method):
            return None
        response = method(order_id, symbol)
        if self._response_failed(response):
            raise RuntimeError(f"fetch_order rejected: {response}")
        data = self._unwrap_data(response)
        if not isinstance(data, dict):
            raise RuntimeError("fetch_order returned malformed data")
        returned_order_id = self._order_id(data)
        if returned_order_id is not None and returned_order_id != str(order_id):
            raise RuntimeError("fetch_order returned a different order")
        return data

    def _fetch_positions_once(self) -> list[dict[str, Any]]:
        response = self._client.exchange.fetch_positions()
        if self._response_failed(response):
            raise RuntimeError(f"fetch_positions rejected: {response}")
        data = self._unwrap_data(response)
        if not isinstance(data, list):
            raise RuntimeError(f"unexpected positions response: {response!r}")
        if not all(isinstance(item, dict) for item in data):
            raise RuntimeError("positions list contains a non-object item")
        positions = list(data)
        for position in positions:
            contracts = self._raw_position_contracts(position)
            if not math.isfinite(contracts) or contracts < 0:
                raise RuntimeError(
                    f"invalid position contracts in response: {contracts!r}"
                )
        return positions

    def _find_short_position(
        self,
        positions: list[dict[str, Any]],
        symbol: str,
    ) -> dict[str, Any] | None:
        for position in positions:
            if not self._symbol_matches(position.get("symbol"), symbol):
                continue
            if self._position_contracts(position) <= 0:
                continue
            info = (
                position.get("info")
                if isinstance(position.get("info"), dict)
                else {}
            )
            side = str(
                position.get("side")
                or info.get("side")
                or info.get("positionSide")
                or ""
            ).lower()
            position_type = position.get("positionType", info.get("positionType"))
            if side and side not in {"short", "sell"}:
                continue
            if position_type not in (None, "") and str(position_type) != "2":
                continue
            if side not in {"short", "sell"} and str(position_type) != "2":
                continue
            return position
        return None

    @staticmethod
    def _raw_position_contracts(position: Any) -> float:
        if not isinstance(position, dict):
            return 0.0
        info = (
            position.get("info")
            if isinstance(position.get("info"), dict)
            else {}
        )
        value: Any = None
        found = False
        for container, key in (
            (position, "contracts"),
            (position, "amount"),
            (info, "holdVol"),
            (info, "vol"),
        ):
            if key in container and container.get(key) is not None:
                value = container.get(key)
                found = True
                break
        if not found:
            return math.nan
        if isinstance(value, bool):
            return math.nan
        try:
            return float(value)
        except (TypeError, ValueError):
            return math.nan

    @staticmethod
    def _position_contracts(position: Any) -> float:
        contracts = BaseExecutor._raw_position_contracts(position)
        return contracts if math.isfinite(contracts) and contracts > 0 else 0.0

    @staticmethod
    def _position_id(position: Any) -> str | None:
        if not isinstance(position, dict):
            return None
        info = (
            position.get("info")
            if isinstance(position.get("info"), dict)
            else {}
        )
        value = (
            position.get("id")
            or position.get("positionId")
            or info.get("positionId")
            or info.get("id")
        )
        return str(value) if value not in (None, "") else None

    @staticmethod
    def _order_filled_amount(order: Any) -> float:
        if not isinstance(order, dict):
            return 0.0
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        value = (
            order.get("filled")
            or order.get("dealVol")
            or info.get("dealVol")
            or info.get("filled")
            or 0
        )
        try:
            return abs(float(value))
        except (TypeError, ValueError):
            return 0.0

    @staticmethod
    def _order_average(order: Any) -> float | None:
        if not isinstance(order, dict):
            return None
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        value = (
            order.get("average")
            or order.get("dealAvgPrice")
            or info.get("dealAvgPrice")
            or info.get("openAvgPrice")
        )
        try:
            average = float(value)
        except (TypeError, ValueError):
            return None
        return average if average > 0 else None

    @staticmethod
    def _position_entry_price(position: Any) -> float | None:
        if not isinstance(position, dict):
            return None
        info = (
            position.get("info")
            if isinstance(position.get("info"), dict)
            else {}
        )
        value = (
            position.get("entryPrice")
            or position.get("average")
            or info.get("openAvgPrice")
            or info.get("entryPrice")
        )
        try:
            entry_price = float(value)
        except (TypeError, ValueError):
            return None
        if not math.isfinite(entry_price) or entry_price <= 0:
            return None
        return entry_price

    def _validate_post_fill_risk(
        self,
        verification: dict[str, Any],
        *,
        contract_size: float,
        expected_risk_usdt: float,
        sl_price: float,
        tp_price: float,
    ) -> dict[str, Any]:
        order = verification.get("order")
        position = verification.get("position")
        fill_price = self._order_average(order) or self._position_entry_price(position)
        filled_amount = max(
            self._order_filled_amount(order),
            self._position_contracts(position),
        )
        values = (
            fill_price,
            filled_amount,
            contract_size,
            expected_risk_usdt,
            sl_price,
            tp_price,
        )
        if (
            fill_price is None
            or not all(
                math.isfinite(float(value))
                for value in values
                if value is not None
            )
            or filled_amount <= 0
            or contract_size <= 0
            or expected_risk_usdt <= 0
        ):
            raise RuntimeError("fill price/amount unavailable or non-finite")
        if not (sl_price > fill_price > tp_price):
            raise RuntimeError(
                "post-fill SHORT protection direction invalid "
                f"(SL={sl_price}, fill={fill_price}, TP={tp_price})"
            )
        actual_risk_usdt = (
            filled_amount * contract_size * (sl_price - fill_price)
        )
        actual_notional_usdt = filled_amount * contract_size * fill_price
        allowed_risk_usdt = (
            expected_risk_usdt * self._max_actual_risk_multiplier
        )
        if (
            not math.isfinite(actual_risk_usdt)
            or not math.isfinite(actual_notional_usdt)
            or actual_risk_usdt <= 0
            or actual_notional_usdt <= 0
            or actual_risk_usdt > allowed_risk_usdt
        ):
            raise RuntimeError(
                f"actual risk ${actual_risk_usdt:.8g} exceeds allowed "
                f"${allowed_risk_usdt:.8g}"
            )
        return {
            "average_fill_price": fill_price,
            "actual_notional_usdt": actual_notional_usdt,
            "actual_risk_usdt": actual_risk_usdt,
            "actual_sl_pct": (sl_price - fill_price) / fill_price * 100,
            "actual_tp_pct": (fill_price - tp_price) / fill_price * 100,
        }

    def _order_is_filled(self, order: Any, requested_amount: float) -> bool:
        if not isinstance(order, dict):
            return False
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        status = str(order.get("status") or "").lower()
        raw_state = order.get("state", info.get("state"))
        filled = self._order_filled_amount(order)
        full_amount = (
            requested_amount > 0 and filled >= requested_amount * 0.999
        )
        return full_amount or status == "filled" or str(raw_state) == "3"

    @staticmethod
    def _list_from_response(response: Any) -> list[dict[str, Any]]:
        data = LiveExecutor._unwrap_data(response)
        if isinstance(data, list):
            if not all(isinstance(item, dict) for item in data):
                raise RuntimeError("order list contains a non-object item")
            return list(data)
        if not isinstance(data, dict):
            raise RuntimeError("order-list payload is neither a list nor an object")
        for key in ("resultList", "list", "orders", "rows"):
            value = data.get(key)
            if isinstance(value, list):
                if not all(isinstance(item, dict) for item in value):
                    raise RuntimeError(
                        f"order list '{key}' contains a non-object item"
                    )
                return list(value)
            if key in data:
                raise RuntimeError(f"order list '{key}' is not a list")
        raise RuntimeError("unknown order-list response schema")

    def _fetch_active_stop_orders(
        self,
        symbol: str | None,
    ) -> list[dict[str, Any]]:
        exchange = self._client.exchange
        symbol_params = (
            {"symbol": self._market_id(symbol)}
            if symbol is not None
            else {}
        )
        candidates = (
            (
                "contractPrivateGetStoporderOpenOrders",
                dict(symbol_params),
            ),
            (
                "contract_private_get_stoporder_open_orders",
                dict(symbol_params),
            ),
            (
                "contractPrivateGetStoporderListOrders",
                {
                    **symbol_params,
                    "is_finished": 0,
                    "page_num": 1,
                    "page_size": 100,
                },
            ),
            (
                "contract_private_get_stoporder_list_orders",
                {
                    **symbol_params,
                    "is_finished": 0,
                    "page_num": 1,
                    "page_size": 100,
                },
            ),
        )
        errors: list[str] = []
        attempted = False
        for name, params in candidates:
            method = getattr(exchange, name, None)
            if not callable(method):
                continue
            attempted = True
            try:
                response = method(params)
                if self._response_failed(response):
                    errors.append(f"{name}: rejected response")
                    continue
                return self._list_from_response(response)
            except Exception as error:
                errors.append(f"{name}: {error}")
        if not attempted:
            raise RuntimeError("exchange exposes no stop-order query API")
        raise RuntimeError("; ".join(errors) or "stop-order query failed")

    def _fetch_open_orders_once(
        self,
        symbol: str | None,
    ) -> list[dict[str, Any]]:
        method = getattr(self._client.exchange, "fetch_open_orders", None)
        if not callable(method):
            raise RuntimeError("exchange exposes no fetch_open_orders API")
        response = (
            method(None, None, None, {"type": "swap"})
            if symbol is None
            else method(symbol)
        )
        if self._response_failed(response):
            raise RuntimeError(f"fetch_open_orders rejected: {response}")
        data = self._unwrap_data(response)
        if not isinstance(data, list):
            raise RuntimeError(
                f"unexpected fetch_open_orders response: {response!r}"
            )
        if not all(isinstance(item, dict) for item in data):
            raise RuntimeError("open-orders list contains a non-object item")
        return list(data)

    @staticmethod
    def _order_is_reduce_only(order: dict[str, Any]) -> bool:
        info = order.get("info") if isinstance(order.get("info"), dict) else {}
        value = order.get("reduceOnly", info.get("reduceOnly"))
        return str(value).lower() in {"1", "true"}

    @staticmethod
    def _record_position_id(record: dict[str, Any]) -> str | None:
        info = record.get("info") if isinstance(record.get("info"), dict) else {}
        value = record.get("positionId") or info.get("positionId")
        return str(value) if value not in (None, "", 0, "0") else None

    def _audit_account_orders(
        self,
        positions: list[dict[str, Any]],
    ) -> None:
        position_ids = {
            position_id
            for position_id in (
                self._position_id(position) for position in positions
            )
            if position_id is not None
        }

        open_orders = self._fetch_open_orders_once(None)
        for order in open_orders:
            if not self._order_is_reduce_only(order):
                raise RuntimeError(
                    "account has an unknown pending entry "
                    f"(order_id={self._order_id(order)})"
                )
            order_symbol = order.get("symbol")
            matching_positions = [
                position
                for position in positions
                if self._symbol_matches(
                    position.get("symbol"),
                    str(order_symbol or ""),
                )
            ]
            record_position_id = self._record_position_id(order)
            if not matching_positions or (
                record_position_id is not None
                and record_position_id not in position_ids
            ):
                raise RuntimeError(
                    "account has an orphan reduce-only open order "
                    f"(order_id={self._order_id(order)})"
                )

        stop_orders = self._fetch_active_stop_orders(None)
        for stop_order in stop_orders:
            stop_position_id = self._record_position_id(stop_order)
            if stop_position_id is None or stop_position_id not in position_ids:
                raise RuntimeError(
                    "account has an orphan/unbound stop order "
                    f"(order_id={self._order_id(stop_order)})"
                )
            matching_position = next(
                (
                    position
                    for position in positions
                    if self._position_id(position) == stop_position_id
                ),
                None,
            )
            info = (
                stop_order.get("info")
                if isinstance(stop_order.get("info"), dict)
                else {}
            )
            if matching_position is None or not self._symbol_matches(
                stop_order.get("symbol") or info.get("symbol"),
                str(matching_position.get("symbol") or ""),
            ):
                raise RuntimeError(
                    "stop order symbol/position binding is inconsistent"
                )

    def _audit_empty_symbol_state(self, symbol: str) -> None:
        open_orders = self._fetch_open_orders_once(symbol)
        entry_orders = [
            order
            for order in open_orders
            if not self._order_is_reduce_only(order)
        ]
        if entry_orders:
            raise RuntimeError(
                "unknown open entry order exists "
                f"(order_id={self._order_id(entry_orders[0])})"
            )
        if open_orders:
            raise RuntimeError(
                "orphan reduce-only open order exists without a position "
                f"(order_id={self._order_id(open_orders[0])})"
            )
        stop_orders = self._fetch_active_stop_orders(symbol)
        if stop_orders:
            raise RuntimeError(
                "orphan reduce-only/stop order exists without a position"
            )

    def _existing_position_has_protection(
        self,
        position: dict[str, Any],
    ) -> bool:
        symbol = str(position.get("symbol") or "")
        if not symbol:
            return False
        position_id = self._position_id(position)
        if position_id is None:
            return False
        amount = self._position_contracts(position)
        sl_volume = 0.0
        tp_volume = 0.0
        for stop_order in self._fetch_active_stop_orders(symbol):
            info = (
                stop_order.get("info")
                if isinstance(stop_order.get("info"), dict)
                else {}
            )
            if not self._symbol_matches(
                stop_order.get("symbol") or info.get("symbol"),
                symbol,
            ):
                continue
            record_position_id = (
                stop_order.get("positionId") or info.get("positionId")
            )
            if (
                record_position_id in (None, "", 0, "0")
                or str(record_position_id) != position_id
            ):
                continue
            generic_volume = self._positive_float(
                stop_order.get("vol")
                or info.get("vol")
                or stop_order.get("amount")
                or info.get("amount")
            )
            stop_loss_price = self._positive_float(
                stop_order.get("stopLossPrice") or info.get("stopLossPrice")
            )
            take_profit_price = self._positive_float(
                stop_order.get("takeProfitPrice") or info.get("takeProfitPrice")
            )
            if stop_loss_price is not None:
                confirmed_sl_volume = (
                    self._positive_float(
                        stop_order.get("stopLossVol")
                        or info.get("stopLossVol")
                    )
                    or generic_volume
                )
                if confirmed_sl_volume is not None:
                    sl_volume += confirmed_sl_volume
            if take_profit_price is not None:
                confirmed_tp_volume = (
                    self._positive_float(
                        stop_order.get("takeProfitVol")
                        or info.get("takeProfitVol")
                    )
                    or generic_volume
                )
                if confirmed_tp_volume is not None:
                    tp_volume += confirmed_tp_volume
        threshold = amount * 0.999
        return sl_volume >= threshold and tp_volume >= threshold

    def _audit_existing_position_protection(
        self,
        positions: list[dict[str, Any]],
    ) -> None:
        for position in positions:
            if not self._existing_position_has_protection(position):
                raise RuntimeError(
                    "existing position has no confirmed full SL/TP protection "
                    f"({position.get('symbol')})"
                )

    @staticmethod
    def _payload_timestamp_ms(payload: dict[str, Any]) -> int | None:
        info = payload.get("info") if isinstance(payload.get("info"), dict) else {}
        value = (
            payload.get("timestamp")
            or payload.get("time")
            or info.get("timestamp")
            or info.get("time")
        )
        try:
            timestamp = int(float(value))
        except (TypeError, ValueError):
            return None
        if timestamp and timestamp < 10_000_000_000:
            timestamp *= 1000
        return timestamp

    def _validate_market_execution(
        self,
        symbol: str,
        *,
        proposal_entry_price: float,
        requested_amount: float,
    ) -> dict[str, Any]:
        ticker = self._client.exchange.fetch_ticker(symbol)
        order_book = self._client.exchange.fetch_order_book(symbol, 50)
        if not isinstance(ticker, dict) or not isinstance(order_book, dict):
            raise RuntimeError("ticker/orderbook returned an invalid payload")

        now_ms = int(time.time() * 1000)
        for label, payload in (("ticker", ticker), ("orderbook", order_book)):
            timestamp = self._payload_timestamp_ms(payload)
            if timestamp is None:
                raise RuntimeError(f"{label} timestamp is missing")
            age_ms = now_ms - timestamp
            if age_ms < -5_000 or age_ms > self._market_data_max_age_seconds * 1000:
                raise RuntimeError(
                    f"{label} is stale or future-dated (age_ms={age_ms})"
                )

        ticker_prices = [
            ticker.get(key)
            for key in ("last", "bid", "ask")
            if ticker.get(key) is not None
        ]
        if not ticker_prices:
            raise RuntimeError("ticker has no price")
        for value in ticker_prices:
            if isinstance(value, bool):
                raise RuntimeError("ticker contains a boolean price")
            price = float(value)
            if not math.isfinite(price) or price <= 0:
                raise RuntimeError("ticker contains a non-finite/non-positive price")

        bids = order_book.get("bids")
        asks = order_book.get("asks")
        if not isinstance(bids, list) or not bids or not isinstance(asks, list) or not asks:
            raise RuntimeError("orderbook has no executable bid/ask")

        def parse_level(level: Any, label: str) -> tuple[float, float]:
            if not isinstance(level, (list, tuple)) or len(level) < 2:
                raise RuntimeError(f"invalid {label} level")
            if isinstance(level[0], bool) or isinstance(level[1], bool):
                raise RuntimeError(f"boolean {label} level")
            price = float(level[0])
            quantity = float(level[1])
            if (
                not math.isfinite(price)
                or not math.isfinite(quantity)
                or price <= 0
                or quantity <= 0
            ):
                raise RuntimeError(f"non-finite/non-positive {label} level")
            return price, quantity

        parsed_bids = [parse_level(level, "bid") for level in bids]
        parsed_asks = [parse_level(level, "ask") for level in asks]
        if any(
            parsed_bids[index][0] > parsed_bids[index - 1][0]
            for index in range(1, len(parsed_bids))
        ):
            raise RuntimeError("bid levels are not monotonically descending")
        if any(
            parsed_asks[index][0] < parsed_asks[index - 1][0]
            for index in range(1, len(parsed_asks))
        ):
            raise RuntimeError("ask levels are not monotonically ascending")

        best_bid, _ = parsed_bids[0]
        best_ask, _ = parsed_asks[0]
        if best_ask < best_bid:
            raise RuntimeError("crossed orderbook")
        if any(price >= best_ask for price, _ in parsed_bids[1:]) or any(
            price <= best_bid for price, _ in parsed_asks[1:]
        ):
            raise RuntimeError("crossed orderbook depth")
        midpoint = (best_bid + best_ask) / 2
        spread_pct = (best_ask - best_bid) / midpoint * 100
        drift_pct = abs(best_bid - proposal_entry_price) / proposal_entry_price * 100
        if not math.isfinite(spread_pct) or spread_pct > self._max_spread_pct:
            raise RuntimeError(
                f"spread {spread_pct:.6g}% exceeds {self._max_spread_pct:.6g}%"
            )
        if not math.isfinite(drift_pct) or drift_pct > self._max_entry_drift_pct:
            raise RuntimeError(
                f"entry drift {drift_pct:.6g}% exceeds "
                f"{self._max_entry_drift_pct:.6g}%"
            )

        # MEXC contract depth `vol` and CCXT create_order `amount` are both
        # contract counts; contractSize is applied later for USDT risk.
        required_depth = requested_amount * self._min_depth_multiple
        total_depth = 0.0
        remaining = requested_amount
        filled_value = 0.0
        for price, quantity in parsed_bids:
            total_depth += quantity
            if remaining > 0:
                take = min(quantity, remaining)
                filled_value += take * price
                remaining -= take
        if total_depth < required_depth or remaining > requested_amount * 1e-9:
            raise RuntimeError(
                f"insufficient bid depth {total_depth:.8g} "
                f"for required {required_depth:.8g}"
            )
        estimated_vwap = filled_value / requested_amount
        slippage_pct = (best_bid - estimated_vwap) / best_bid * 100
        if (
            not math.isfinite(slippage_pct)
            or slippage_pct < 0
            or slippage_pct > self._max_slippage_pct
        ):
            raise RuntimeError(
                f"estimated slippage {slippage_pct:.6g}% exceeds "
                f"{self._max_slippage_pct:.6g}%"
            )
        return {
            "best_bid": best_bid,
            "best_ask": best_ask,
            "spread_pct": spread_pct,
            "entry_drift_pct": drift_pct,
            "estimated_vwap": estimated_vwap,
            "estimated_slippage_pct": slippage_pct,
            "bid_depth": total_depth,
        }

    @staticmethod
    def _price_matches(actual: Any, expected: float) -> bool:
        if isinstance(actual, bool):
            return False
        try:
            actual_float = float(actual)
        except (TypeError, ValueError):
            return False
        if not math.isfinite(actual_float):
            return False
        tolerance = max(1e-12, abs(expected) * 1e-7)
        return abs(actual_float - expected) <= tolerance

    @staticmethod
    def _positive_float(value: Any) -> float | None:
        if isinstance(value, bool):
            return None
        try:
            number = float(value)
        except (TypeError, ValueError):
            return None
        return number if math.isfinite(number) and number > 0 else None

    def _protection_verified(
        self,
        stop_orders: list[dict[str, Any]],
        *,
        symbol: str,
        order_id: str | None,
        position_id: str | None,
        position_amount: float,
        sl_price: float,
        tp_price: float,
    ) -> bool:
        sl_covered = False
        tp_covered = False
        for stop_order in stop_orders:
            info = (
                stop_order.get("info")
                if isinstance(stop_order.get("info"), dict)
                else {}
            )
            if not self._symbol_matches(
                stop_order.get("symbol") or info.get("symbol"),
                symbol,
            ):
                continue
            is_finished = stop_order.get(
                "isFinished",
                info.get("isFinished"),
            )
            if str(is_finished).lower() in {"1", "true"}:
                continue
            state = stop_order.get("state", info.get("state"))
            if state not in (None, "", 1, "1", "open", "active"):
                continue

            record_order_id = (
                stop_order.get("orderId")
                or info.get("orderId")
                or stop_order.get("parentOrderId")
                or info.get("parentOrderId")
            )
            record_position_id = (
                stop_order.get("positionId")
                or info.get("positionId")
            )
            id_fields_present = record_order_id not in (None, "", 0, "0") or (
                record_position_id not in (None, "", 0, "0")
            )
            id_matches = (
                order_id is not None and str(record_order_id) == order_id
            ) or (
                position_id is not None and str(record_position_id) == position_id
            )
            if not id_fields_present or not id_matches:
                continue

            generic_volume = (
                stop_order.get("vol")
                or info.get("vol")
                or stop_order.get("amount")
                or info.get("amount")
            )
            sl_volume = (
                stop_order.get("stopLossVol")
                or info.get("stopLossVol")
                or generic_volume
            )
            tp_volume = (
                stop_order.get("takeProfitVol")
                or info.get("takeProfitVol")
                or generic_volume
            )
            sl_volume_float = self._positive_float(sl_volume)
            tp_volume_float = self._positive_float(tp_volume)
            volume_threshold = position_amount * 0.999

            record_sl = (
                stop_order.get("stopLossPrice")
                or info.get("stopLossPrice")
                or stop_order.get("stopPrice")
                or info.get("stopPrice")
            )
            record_tp = (
                stop_order.get("takeProfitPrice")
                or info.get("takeProfitPrice")
            )
            if (
                self._price_matches(record_sl, sl_price)
                and sl_volume_float is not None
                and sl_volume_float >= volume_threshold
            ):
                sl_covered = True
            if (
                self._price_matches(record_tp, tp_price)
                and tp_volume_float is not None
                and tp_volume_float >= volume_threshold
            ):
                tp_covered = True
        return sl_covered and tp_covered

    def _verify_entry_and_protection(
        self,
        *,
        symbol: str,
        external_oid: str,
        requested_amount: float,
        sl_price: float,
        tp_price: float,
        initial_order: dict[str, Any] | None,
        allow_position_only: bool,
    ) -> dict[str, Any]:
        order = initial_order
        position: dict[str, Any] | None = None
        fill_verified = False
        protection_verified = False
        last_error: Exception | None = None

        for attempt in range(self._verify_attempts):
            try:
                external_order = self._fetch_order_by_external_oid(
                    symbol,
                    external_oid,
                )
                if external_order is not None:
                    order = external_order
            except Exception as error:
                last_error = error

            order_id = self._order_id(order)
            if order_id is not None:
                try:
                    detailed_order = self._fetch_order_details(order_id, symbol)
                    if detailed_order is not None:
                        order = detailed_order
                except Exception as error:
                    last_error = error

            try:
                position = self._find_short_position(
                    self._fetch_positions_once(),
                    symbol,
                )
            except Exception as error:
                last_error = error

            position_amount = self._position_contracts(position)
            fill_verified = self._order_is_filled(
                order,
                requested_amount,
            ) or (
                allow_position_only
                and position_amount >= requested_amount * 0.999
            )

            if fill_verified and position is not None:
                try:
                    stop_orders = self._fetch_active_stop_orders(symbol)
                    protection_verified = self._protection_verified(
                        stop_orders,
                        symbol=symbol,
                        order_id=self._order_id(order),
                        position_id=self._position_id(position),
                        position_amount=position_amount,
                        sl_price=sl_price,
                        tp_price=tp_price,
                    )
                except Exception as error:
                    last_error = error
                    protection_verified = False

            if fill_verified and protection_verified:
                filled_amount = max(
                    self._order_filled_amount(order),
                    position_amount,
                )
                return {
                    "ok": True,
                    "order": order,
                    "position": position,
                    "filled_amount": filled_amount,
                    "average_fill_price": self._order_average(order),
                    "fill_verified": True,
                    "protection_verified": True,
                }

            if (
                attempt + 1 < self._verify_attempts
                and self._verify_delay_seconds > 0
            ):
                time.sleep(self._verify_delay_seconds)

        reason_parts = []
        if not fill_verified:
            reason_parts.append("fill not confirmed")
        if fill_verified and not protection_verified:
            reason_parts.append("SL/TP protection not confirmed")
        if last_error is not None:
            reason_parts.append(f"last reconciliation error: {last_error}")
        return {
            "ok": False,
            "reason": "; ".join(reason_parts) or "entry state not confirmed",
            "order": order,
            "position": position,
            "fill_verified": fill_verified,
            "protection_verified": protection_verified,
        }

    def _emergency_close(
        self,
        symbol: str,
        amount: float,
        *,
        parent_external_oid: str,
    ) -> dict[str, Any]:
        close_oid = self._derived_external_oid(
            f"{parent_external_oid}|emergency-close",
            kind="c",
        )
        close_order: dict[str, Any] | None = None
        create_error: Exception | None = None
        try:
            precise_amount = float(
                self._client.exchange.amount_to_precision(symbol, amount)
            )
            close_order = self._create_order_once(
                symbol=symbol,
                order_type="market",
                side="buy",
                amount=precise_amount,
                price=None,
                params={
                    "externalOid": close_oid,
                    "reduceOnly": True,
                    "openType": self._open_type,
                    "marginMode": self._margin_mode,
                    "leverage": int(self._max_leverage),
                    "hedged": self._hedged,
                    "positionMode": 1 if self._hedged else 2,
                },
            )
        except Exception as error:
            create_error = error
            logger.critical(
                "[LIVE] emergency reduce-only close result unknown "
                "%s external_oid=%s: %s",
                symbol,
                close_oid,
                error,
            )

        remaining_position: dict[str, Any] | None = None
        last_error: Exception | None = None
        for attempt in range(self._verify_attempts):
            try:
                remaining_position = self._find_short_position(
                    self._fetch_positions_once(),
                    symbol,
                )
                if self._position_contracts(remaining_position) <= 0:
                    return {
                        "status": "ok",
                        "order_id": self._order_id(close_order),
                        "external_oid": close_oid,
                        "position_closed": True,
                        "recovered_after_error": create_error is not None,
                        "raw": close_order,
                    }
            except Exception as error:
                last_error = error
            if (
                attempt + 1 < self._verify_attempts
                and self._verify_delay_seconds > 0
            ):
                time.sleep(self._verify_delay_seconds)

        reason = (
            f"close_order: {create_error}"
            if create_error is not None
            else "position remains open after emergency close"
        )
        if last_error is not None:
            reason += f"; last reconciliation error: {last_error}"
        return {
            "status": "error",
            "reason": reason,
            "order_id": self._order_id(close_order),
            "external_oid": close_oid,
            "position_closed": False,
            "remaining_contracts": self._position_contracts(remaining_position),
            "raw": close_order,
        }

    @abstractmethod
    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """ポジションをクローズする（将来実装）。

        Args:
            symbol: クローズ対象シンボル
            amount: クローズ数量
        Returns:
            実行結果の辞書
        """
        ...


# ---------------------------------------------------------------------------
# Dry Run Executor (現在のデフォルト)
# ---------------------------------------------------------------------------

class DryRunExecutor(BaseExecutor):
    """トレード提案を構造化ログとして出力するモック実装。

    実際の API 注文は一切発行しない。
    将来 LiveExecutor に切り替える際は ExecutorFactory の分岐を変更するだけ。
    """

    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """擬似トレード提案をログ出力し、モック結果を返す。

        出力形式:
            [DRY RUN] ========================================
            Symbol     : XXX/USDT:USDT
            Direction  : SHORT (擬似ショート)
            Entry Ref  : $0.0001234
            Stop Loss  : $0.0001258 (+2.00%) ← 上方向（ショートのSLは上）
            Take Profit: $0.0001185 (-4.00%) ← 下方向（ショートのTPは下）
            RSI        : 82.4 (OVERBOUGHT)
            BB Upper   : $0.0001230 (BREAK)
            1h Change  : +7.85%
            Volume 24h : $5,234,567 USDT
            Timestamp  : 2025-01-01T00:00:00+00:00
        """
        # AVOID 判定の場合は出力してスキップ
        if (
            proposal.fundamental is not None
            and proposal.fundamental.short_conviction == "AVOID"
        ):
            logger.warning(
                "[DRY RUN] SKIPPED (AVOID) %s — Fundamental: %s",
                proposal.symbol,
                proposal.fundamental.reason,
            )
            return {"status": "skipped_avoid", "symbol": proposal.symbol}

        logger.info("=" * 60)
        logger.info("[DRY RUN] Trade Proposal Generated")
        logger.info("  Symbol      : %s", proposal.symbol)
        logger.info("  Direction   : %s (擬似ショート)", proposal.direction.upper())
        logger.info("  Entry Ref   : $%.8g", proposal.entry_price)
        logger.info(
            "  Stop Loss   : $%.8g (+%.2f%%) ← ショートSLは上方向",
            proposal.stop_loss,
            proposal.sl_pct,
        )
        logger.info(
            "  Take Profit : $%.8g (-%.2f%%) ← ショートTPは下方向",
            proposal.take_profit,
            proposal.tp_pct,
        )
        logger.info(
            "  RSI         : %s",
            f"{proposal.rsi_at_entry:.1f} (OVERBOUGHT)"
            if proposal.rsi_at_entry is not None
            else "N/A",
        )
        logger.info(
            "  BB Upper    : %s",
            f"${proposal.bb_upper_at_entry:.8g} (BREAK)"
            if proposal.bb_upper_at_entry is not None
            else "N/A",
        )
        logger.info("  1h Change   : +%.2f%%", proposal.change_1h_pct)
        logger.info("  Volume 24h  : $%s USDT", f"{proposal.volume_24h_usdt:,.0f}")
        # ファンダ考察サマリー
        if proposal.fundamental is not None and proposal.fundamental.news_count >= 0:
            logger.info(
                "  Fundamental : catalyst=%s conviction=%s news=%d件",
                proposal.fundamental.catalyst_type,
                proposal.fundamental.short_conviction,
                proposal.fundamental.news_count,
            )
            logger.info("  Fund Reason : %s", proposal.fundamental.reason)
        logger.info("  Timestamp   : %s", proposal.created_at)
        logger.info("=" * 60)

        return {
            "status": "dry_run",
            "symbol": proposal.symbol,
            "direction": proposal.direction,
            "entry_price": proposal.entry_price,
            "stop_loss": proposal.stop_loss,
            "take_profit": proposal.take_profit,
            "timestamp": proposal.created_at,
        }

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """擬似クローズをログ出力する。"""
        logger.info("[DRY RUN] Close position | symbol=%s amount=%.6f", symbol, amount)
        return {"status": "dry_run_close", "symbol": symbol, "amount": amount}


# ---------------------------------------------------------------------------
# Live Executor (本番実装)
# ---------------------------------------------------------------------------

class LiveExecutor(BaseExecutor):
    """MEXC USDT-M 先物への実発注を行う本番実装。

    安全設計:
        - 必ず SL/TP を注文と同時に attach (約定後に別注文ではない)
        - AVOID シグナルは発注しない
        - 残高 < LIVE_MIN_BALANCE_USDT なら発注しない
        - 既存ポジションがあるシンボルは重複エントリー禁止
        - 計算後の数量 / 名目額が取引所の最小値を下回ったらスキップ
        - LIVE_MAX_OPEN_POSITIONS を超える同時保有は禁止
        - エラー時はリトライせずログ + 状態を返す (上位で stats / tracker に
          反映しないこと)

    ポジションサイズ:
        risk_usdt   = balance × LIVE_BASE_RISK_PCT%   (≤ LIVE_MAX_RISK_PCT)
        notional    = risk_usdt / (sl_pct / 100)
        notional   ≤ balance × LIVE_MAX_LEVERAGE
        amount      = notional / (entry_price × contract_size)
    """

    def __init__(self, client: MEXCClient) -> None:
        self._client = client
        # ポジションサイジング
        self._base_risk_pct: float = float(os.getenv("LIVE_BASE_RISK_PCT", "0.5"))
        self._max_risk_pct:  float = float(os.getenv("LIVE_MAX_RISK_PCT",  "1.5"))
        self._max_leverage:  float = float(os.getenv("LIVE_MAX_LEVERAGE",  "3.0"))
        # 安全装置
        self._min_balance_usdt:    float = float(os.getenv("LIVE_MIN_BALANCE_USDT", "5.0"))
        self._max_open_positions:  int   = int(os.getenv("LIVE_MAX_OPEN_POSITIONS", "3"))
        self._margin_mode: str = os.getenv("LIVE_MARGIN_MODE", "isolated").strip().lower()
        self._position_mode: str = os.getenv("LIVE_POSITION_MODE", "hedged").strip().lower()
        default_open_type = {"isolated": 1, "cross": 2}.get(self._margin_mode)
        configured_open_type = os.getenv("LIVE_OPEN_TYPE")
        try:
            self._open_type: int | None = (
                int(configured_open_type)
                if configured_open_type is not None
                else default_open_type
            )
        except ValueError:
            self._open_type = None
        self._hedged: bool = self._position_mode == "hedged"
        self._mode_config_error: str | None = None
        if self._margin_mode not in {"isolated", "cross"}:
            self._mode_config_error = "LIVE_MARGIN_MODE must be 'isolated' or 'cross'"
        elif self._position_mode not in {"hedged", "oneway"}:
            self._mode_config_error = "LIVE_POSITION_MODE must be 'hedged' or 'oneway'"
        elif self._open_type not in {1, 2}:
            self._mode_config_error = "LIVE_OPEN_TYPE must be 1 or 2"
        elif self._open_type != default_open_type:
            self._mode_config_error = (
                "LIVE_OPEN_TYPE conflicts with LIVE_MARGIN_MODE "
                f"({self._margin_mode} requires {default_open_type})"
            )
        # Mutating calls are never retried. Only read-only reconciliation is
        # polled because a timed-out order request may already have committed.
        self._verify_attempts: int = max(
            1, int(os.getenv("LIVE_ORDER_VERIFY_ATTEMPTS", "5"))
        )
        self._verify_delay_seconds: float = max(
            0.0, float(os.getenv("LIVE_ORDER_VERIFY_DELAY_SECONDS", "1.0"))
        )
        self._symbol_reentry_cooldown_hours: float = float(
            os.getenv("LIVE_SYMBOL_REENTRY_COOLDOWN_HOURS", "48")
        )
        self._max_new_entries_per_utc_day: int = int(
            os.getenv("LIVE_MAX_NEW_ENTRIES_PER_UTC_DAY", "1")
        )
        self._market_data_max_age_seconds: float = float(
            os.getenv("LIVE_MARKET_DATA_MAX_AGE_SECONDS", "10")
        )
        self._max_entry_drift_pct: float = float(
            os.getenv("LIVE_MAX_ENTRY_DRIFT_PCT", "0.5")
        )
        self._max_spread_pct: float = float(
            os.getenv("LIVE_MAX_SPREAD_PCT", "0.10")
        )
        self._max_slippage_pct: float = float(
            os.getenv("LIVE_MAX_SLIPPAGE_PCT", "0.10")
        )
        self._min_depth_multiple: float = float(
            os.getenv("LIVE_MIN_DEPTH_MULTIPLE", "1.0")
        )
        self._max_actual_risk_multiplier: float = float(
            os.getenv("LIVE_MAX_ACTUAL_RISK_MULTIPLIER", "1.05")
        )
        market_guard_values = (
            self._market_data_max_age_seconds,
            self._max_entry_drift_pct,
            self._max_spread_pct,
            self._max_slippage_pct,
            self._min_depth_multiple,
            self._max_actual_risk_multiplier,
        )
        if self._mode_config_error is None and (
            not all(math.isfinite(value) for value in market_guard_values)
            or self._market_data_max_age_seconds <= 0
            or self._max_entry_drift_pct < 0
            or self._max_spread_pct < 0
            or self._max_slippage_pct < 0
            or self._min_depth_multiple < 1
            or self._max_actual_risk_multiplier < 1
        ):
            self._mode_config_error = "invalid LIVE market execution guard config"
        risk_guard_values = (
            self._base_risk_pct,
            self._max_risk_pct,
            self._max_leverage,
            self._min_balance_usdt,
            self._symbol_reentry_cooldown_hours,
        )
        if self._mode_config_error is None and (
            not all(math.isfinite(value) for value in risk_guard_values)
            or self._base_risk_pct <= 0
            or self._max_risk_pct <= 0
            or self._max_leverage <= 0
            or self._min_balance_usdt < 0
            or self._symbol_reentry_cooldown_hours < 0
            or self._max_new_entries_per_utc_day < 1
        ):
            self._mode_config_error = "invalid LIVE risk guard config"

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """SHORT エントリーを 1 件発注する (SL/TP 同時 attach)。

        失敗時は status="error" を返す。上位 (main.py) はこれを見て
        tracker / stats に登録しないようにすること。
        """
        # ── ガード 1: AVOID ──────────────────────────────────────────
        if (
            proposal.fundamental is not None
            and proposal.fundamental.short_conviction == "AVOID"
        ):
            logger.warning(
                "[LIVE] SKIP %s — fundamental AVOID (%s)",
                proposal.symbol, proposal.fundamental.reason,
            )
            return {"status": "skipped_avoid", "symbol": proposal.symbol}

        # ── ガード 2: 残高 ────────────────────────────────────────────
        if (
            not isinstance(proposal.idempotency_key, str)
            or not proposal.idempotency_key.strip()
        ):
            return {
                "status": "error",
                "reason": "idempotency_key is required for live execution",
                "symbol": proposal.symbol,
            }

        try:
            balance = self._client.fetch_balance()
        except Exception as e:
            logger.error("[LIVE] fetch_balance failed: %s", e)
            return {"status": "error", "reason": f"fetch_balance: {e}"}

        if not isinstance(balance, dict):
            return {"status": "error", "reason": "invalid balance response"}
        usdt_info  = balance.get("USDT", {}) or {}
        if not isinstance(usdt_info, dict):
            return {"status": "error", "reason": "invalid USDT balance response"}
        free_raw = usdt_info.get("free")
        total_raw = usdt_info.get("total")
        if (
            free_raw is None
            or total_raw is None
            or isinstance(free_raw, bool)
            or isinstance(total_raw, bool)
        ):
            return {"status": "error", "reason": "invalid USDT balance response"}
        try:
            free_usdt = float(free_raw)
            total_usdt = float(total_raw)
        except (TypeError, ValueError):
            return {"status": "error", "reason": "invalid USDT balance response"}
        if (
            not math.isfinite(free_usdt)
            or not math.isfinite(total_usdt)
            or free_usdt < 0
            or total_usdt <= 0
            or free_usdt > total_usdt * 1.000001
        ):
            return {
                "status": "error",
                "reason": "non-finite or inconsistent USDT balance",
                "free_usdt": free_usdt,
                "total_usdt": total_usdt,
            }

        if free_usdt < self._min_balance_usdt:
            logger.warning(
                "[LIVE] SKIP %s — free $%.2f < min $%.2f",
                proposal.symbol, free_usdt, self._min_balance_usdt,
            )
            return {
                "status": "skipped_low_balance",
                "symbol": proposal.symbol,
                "free_usdt": free_usdt,
            }

        # ── ガード 3: 既存ポジション + 同時保有数 ────────────────────
        try:
            all_positions = self._fetch_positions_once()
        except Exception as e:
            logger.error("[LIVE] fetch_positions failed: %s", e)
            return {"status": "error", "reason": f"fetch_positions: {e}"}

        open_positions = [
            p for p in all_positions
            if self._position_contracts(p) > 0
        ]
        existing_symbol_position = next(
            (
                position
                for position in open_positions
                if self._symbol_matches(position.get("symbol"), proposal.symbol)
            ),
            None,
        )
        other_positions = [
            position
            for position in open_positions
            if position is not existing_symbol_position
        ]

        try:
            self._audit_existing_position_protection(other_positions)
        except Exception as error:
            logger.error(
                "[LIVE] existing-position protection audit failed closed: %s",
                error,
            )
            return {
                "status": "error",
                "reason": f"existing_position_audit: {error}",
                "symbol": proposal.symbol,
            }

        max_positions_reached = len(open_positions) >= self._max_open_positions

        # ── ガード 4: SL/TP 健全性 ──────────────────────────────────
        proposal_prices = (
            proposal.entry_price,
            proposal.stop_loss,
            proposal.take_profit,
            proposal.sl_pct,
            proposal.tp_pct,
        )
        if any(
            isinstance(value, bool) or not isinstance(value, (int, float))
            for value in proposal_prices
        ) or not all(math.isfinite(float(value)) for value in proposal_prices):
            return {"status": "error", "reason": "non-finite proposal price/risk"}
        if proposal.direction.lower() != "short":
            return {"status": "error", "reason": "LiveExecutor supports SHORT only"}
        if (
            proposal.entry_price <= 0
            or proposal.stop_loss <= 0
            or proposal.take_profit <= 0
        ):
            return {"status": "error", "reason": "proposal prices must be positive"}
        if proposal.sl_pct <= 0 or proposal.tp_pct <= 0:
            return {"status": "error", "reason": "sl_pct or tp_pct <= 0"}
        if proposal.stop_loss <= proposal.entry_price:
            # SHORT: SL は entry より上であるべき
            return {"status": "error", "reason": "SHORT SL must be above entry"}
        if proposal.take_profit >= proposal.entry_price:
            # SHORT: TP は entry より下であるべき
            return {"status": "error", "reason": "SHORT TP must be below entry"}

        # ── ポジションサイズ ─────────────────────────────────────────
        if self._mode_config_error is not None:
            logger.error("[LIVE] invalid execution mode config: %s", self._mode_config_error)
            return {
                "status": "error",
                "reason": f"execution_mode_config: {self._mode_config_error}",
                "symbol": proposal.symbol,
            }

        requested_risk_pct = proposal.risk_pct_of_account
        if isinstance(requested_risk_pct, bool):
            return {
                "status": "error",
                "reason": "risk_pct_of_account must be numeric",
                "symbol": proposal.symbol,
            }
        try:
            risk_pct = (
                min(self._base_risk_pct, self._max_risk_pct)
                if requested_risk_pct is None
                else float(requested_risk_pct)
            )
        except (TypeError, ValueError):
            return {
                "status": "error",
                "reason": "risk_pct_of_account must be numeric",
                "symbol": proposal.symbol,
            }
        if (
            not math.isfinite(risk_pct)
            or risk_pct <= 0
            or risk_pct > self._max_risk_pct
        ):
            logger.error(
                "[LIVE] invalid risk for %s: %.8g (max %.8g)",
                proposal.symbol,
                risk_pct,
                self._max_risk_pct,
            )
            return {
                "status": "error",
                "reason": (
                    "risk_pct_of_account must satisfy "
                    f"0 < risk <= {self._max_risk_pct}"
                ),
                "symbol": proposal.symbol,
                "risk_pct_of_account": risk_pct,
            }
        risk_usdt = total_usdt * risk_pct / 100
        notional  = risk_usdt / (proposal.sl_pct / 100)
        notional  = min(notional, total_usdt * self._max_leverage)

        try:
            market = self._client.exchange.market(proposal.symbol)
        except Exception as e:
            return {"status": "error", "reason": f"market_meta: {e}"}
        if not isinstance(market, dict):
            return {"status": "error", "reason": "market_meta: invalid response"}
        market_info = (
            market.get("info") if isinstance(market.get("info"), dict) else {}
        )
        api_allowed = market_info.get("apiAllowed")
        api_explicitly_disabled = api_allowed is False or str(api_allowed).lower() in {
            "0",
            "false",
        }
        if market.get("active") is False or api_explicitly_disabled:
            return {
                "status": "error",
                "reason": "market is inactive or API trading is disabled",
            }
        if market.get("swap") is not True:
            return {"status": "error", "reason": "market is not a swap contract"}
        if str(market.get("settle") or "").upper() != "USDT":
            return {"status": "error", "reason": "market is not USDT-settled"}

        contract_size_raw = market.get("contractSize")
        if contract_size_raw is None or isinstance(contract_size_raw, bool):
            return {"status": "error", "reason": "invalid contractSize"}
        try:
            contract_size = float(contract_size_raw)
        except (TypeError, ValueError):
            return {"status": "error", "reason": "invalid contractSize"}
        if not math.isfinite(contract_size) or contract_size <= 0:
            return {"status": "error", "reason": "invalid entry_price or contract_size"}

        amount = notional / (proposal.entry_price * contract_size)
        if (
            not math.isfinite(risk_usdt)
            or not math.isfinite(notional)
            or not math.isfinite(amount)
            or risk_usdt <= 0
            or notional <= 0
            or amount <= 0
        ):
            return {"status": "error", "reason": "invalid computed order sizing"}

        # 取引所の最小数量 / 最小名目額をチェック
        limits = market.get("limits") or {}
        if not isinstance(limits, dict):
            return {"status": "error", "reason": "invalid market limits"}
        amount_limits = limits.get("amount") or {}
        cost_limits = limits.get("cost") or {}
        if not isinstance(amount_limits, dict) or not isinstance(cost_limits, dict):
            return {"status": "error", "reason": "invalid market limits"}
        min_amount = amount_limits.get("min")
        min_cost = cost_limits.get("min")

        if isinstance(min_amount, bool) or isinstance(min_cost, bool):
            return {"status": "error", "reason": "invalid market limits"}
        try:
            parsed_min_amount = (
                float(min_amount) if min_amount is not None else None
            )
            parsed_min_cost = float(min_cost) if min_cost is not None else None
        except (TypeError, ValueError):
            return {"status": "error", "reason": "invalid market limits"}
        if (
            parsed_min_amount is not None
            and (not math.isfinite(parsed_min_amount) or parsed_min_amount < 0)
        ) or (
            parsed_min_cost is not None
            and (not math.isfinite(parsed_min_cost) or parsed_min_cost < 0)
        ):
            return {"status": "error", "reason": "non-finite market limits"}

        if parsed_min_amount is not None and amount < parsed_min_amount:
            logger.warning(
                "[LIVE] SKIP %s — amount %.6g < min %.6g (notional $%.2f)",
                proposal.symbol, amount, parsed_min_amount, notional,
            )
            return {
                "status": "skipped_below_min_amount",
                "symbol": proposal.symbol,
                "amount": amount,
                "min_amount": parsed_min_amount,
            }
        if parsed_min_cost is not None and notional < parsed_min_cost:
            logger.warning(
                "[LIVE] SKIP %s — notional $%.2f < min $%.2f",
                proposal.symbol, notional, parsed_min_cost,
            )
            return {
                "status": "skipped_below_min_cost",
                "symbol": proposal.symbol,
                "notional": notional,
                "min_cost": parsed_min_cost,
            }

        # 取引所の精度に合わせる
        try:
            amount_str   = self._client.exchange.amount_to_precision(proposal.symbol, amount)
            sl_price_str = self._client.exchange.price_to_precision(proposal.symbol, proposal.stop_loss)
            tp_price_str = self._client.exchange.price_to_precision(proposal.symbol, proposal.take_profit)
            if any(
                isinstance(value, bool)
                for value in (amount_str, sl_price_str, tp_price_str)
            ):
                raise ValueError("boolean precision response")
            amount   = float(amount_str)
            sl_price = float(sl_price_str)
            tp_price = float(tp_price_str)
        except Exception as e:
            return {"status": "error", "reason": f"precision: {e}"}
        if (
            not all(math.isfinite(value) for value in (amount, sl_price, tp_price))
            or amount <= 0
            or sl_price <= 0
            or tp_price <= 0
        ):
            return {
                "status": "error",
                "reason": "precision returned non-finite/non-positive values",
            }

        # ── Idempotency/state audit, then one SL/TP-attached order ───
        # SHORT = sell (open). MEXC perpetual + ccxt は stopLossPrice /
        # takeProfitPrice を params で渡せば 1 注文に attach される。
        external_oid = self._entry_external_oid(
            proposal,
            amount=amount,
            sl_price=sl_price,
            tp_price=tp_price,
        )
        order: dict[str, Any] | None = None
        create_error: Exception | None = None
        reused_existing_order = False
        market_execution: dict[str, Any] | None = None
        try:
            order = self._fetch_order_by_external_oid(
                proposal.symbol,
                external_oid,
            )
        except Exception as error:
            logger.error(
                "[LIVE] preflight externalOid lookup failed closed %s: %s",
                proposal.symbol,
                error,
            )
            return {
                "status": "error",
                "reason": f"external_oid_preflight: {error}",
                "symbol": proposal.symbol,
                "external_oid": external_oid,
            }

        if order is not None:
            reused_existing_order = True
            logger.warning(
                "[LIVE] existing order intent found; reconciling without "
                "new mutation %s external_oid=%s order_id=%s",
                proposal.symbol,
                external_oid,
                self._order_id(order),
            )
        else:
            try:
                self._audit_account_orders(open_positions)
            except Exception as error:
                logger.error(
                    "[LIVE] account-wide order audit failed closed: %s",
                    error,
                )
                return {
                    "status": "error",
                    "reason": f"account_order_audit: {error}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                }

            if existing_symbol_position is not None:
                try:
                    existing_position_protected = (
                        self._existing_position_has_protection(
                            existing_symbol_position
                        )
                    )
                except Exception as error:
                    return {
                        "status": "error",
                        "reason": (
                            "unknown_existing_position_protection_audit: "
                            f"{error}"
                        ),
                        "symbol": proposal.symbol,
                        "external_oid": external_oid,
                    }
                protection_reason = (
                    "protected but does not match this durable intent"
                    if existing_position_protected
                    else "has no confirmed full SL/TP protection"
                )
                logger.error(
                    "[LIVE] unknown existing position blocks %s: %s",
                    proposal.symbol,
                    protection_reason,
                )
                return {
                    "status": "error",
                    "reason": f"unknown_existing_position: {protection_reason}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                    "protection_verified": existing_position_protected,
                }
            if max_positions_reached:
                logger.warning(
                    "[LIVE] SKIP %s — open positions %d >= max %d",
                    proposal.symbol,
                    len(open_positions),
                    self._max_open_positions,
                )
                return {
                    "status": "skipped_max_positions",
                    "symbol": proposal.symbol,
                    "open_count": len(open_positions),
                    "external_oid": external_oid,
                }

            try:
                daily_entries = self._filled_mt_entries_today()
            except Exception as error:
                return {
                    "status": "error",
                    "reason": f"daily_entry_cap_audit: {error}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                }
            if len(daily_entries) >= self._max_new_entries_per_utc_day:
                return {
                    "status": "skipped_daily_entry_cap",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                    "filled_entries_today": len(daily_entries),
                    "daily_entry_cap": self._max_new_entries_per_utc_day,
                }

            try:
                self._audit_empty_symbol_state(proposal.symbol)
            except Exception as error:
                logger.error(
                    "[LIVE] open-order/orphan-stop audit failed closed %s: %s",
                    proposal.symbol,
                    error,
                )
                return {
                    "status": "error",
                    "reason": f"symbol_state_audit: {error}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                }

            try:
                cooldown_order = self._recent_entry_in_cooldown(
                    proposal.symbol,
                    current_external_oid=external_oid,
                )
            except Exception as error:
                logger.error(
                    "[LIVE] re-entry cooldown audit failed closed %s: %s",
                    proposal.symbol,
                    error,
                )
                return {
                    "status": "error",
                    "reason": f"reentry_cooldown_audit: {error}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                }
            if cooldown_order is not None:
                return {
                    "status": "skipped_reentry_cooldown",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                    "prior_order_id": self._order_id(cooldown_order),
                    "prior_external_oid": self._order_external_oid(cooldown_order),
                    "cooldown_hours": self._symbol_reentry_cooldown_hours,
                }

            try:
                market_execution = self._validate_market_execution(
                    proposal.symbol,
                    proposal_entry_price=proposal.entry_price,
                    requested_amount=amount,
                )
            except Exception as error:
                logger.error(
                    "[LIVE] market execution guard failed closed %s: %s",
                    proposal.symbol,
                    error,
                )
                return {
                    "status": "error",
                    "reason": f"market_execution_guard: {error}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                }

            try:
                leverage_response = self._client.exchange.set_leverage(
                    int(self._max_leverage),
                    proposal.symbol,
                    {
                        "openType": self._open_type,
                        "positionType": 2,
                    },
                )
                if not self._response_confirmed_success(leverage_response):
                    raise RuntimeError(
                        "exchange did not explicitly confirm leverage: "
                        f"{leverage_response!r}"
                    )
            except Exception as error:
                logger.error(
                    "[LIVE] set_leverage failed closed for %s: %s",
                    proposal.symbol,
                    error,
                )
                return {
                    "status": "error",
                    "reason": f"set_leverage: {error}",
                    "symbol": proposal.symbol,
                    "external_oid": external_oid,
                }

            try:
                order = self._create_order_once(
                    symbol=proposal.symbol,
                    order_type="market",
                    side="sell",
                    amount=amount,
                    price=None,
                    params={
                        "externalOid": external_oid,
                        "stopLossPrice": sl_price,
                        "takeProfitPrice": tp_price,
                        "reduceOnly": False,
                        "openType": self._open_type,
                        "marginMode": self._margin_mode,
                        "leverage": int(self._max_leverage),
                        "hedged": self._hedged,
                        "positionMode": 1 if self._hedged else 2,
                    },
                )
            except Exception as e:
                create_error = e
                logger.error(
                    "[LIVE] create_order result unknown %s external_oid=%s: %s",
                    proposal.symbol,
                    external_oid,
                    e,
                )

        verification = self._verify_entry_and_protection(
            symbol=proposal.symbol,
            external_oid=external_oid,
            requested_amount=amount,
            sl_price=sl_price,
            tp_price=tp_price,
            initial_order=order,
            allow_position_only=(
                create_error is None or self._is_ambiguous_error(create_error)
            ),
        )
        if not verification["ok"]:
            position = verification.get("position")
            position_amount = self._position_contracts(position)
            emergency_close: dict[str, Any] | None = None
            if position_amount > 0:
                emergency_close = self._emergency_close(
                    proposal.symbol,
                    position_amount,
                    parent_external_oid=external_oid,
                )

            reason = str(verification.get("reason") or "entry verification failed")
            if create_error is not None:
                reason = f"create_order: {create_error}; {reason}"
            logger.critical(
                "[LIVE] entry rejected after verification %s external_oid=%s "
                "fill=%s protection=%s emergency_close=%s",
                proposal.symbol,
                external_oid,
                verification.get("fill_verified"),
                verification.get("protection_verified"),
                emergency_close,
            )
            return {
                "status": "error",
                "reason": reason,
                "symbol": proposal.symbol,
                "external_oid": external_oid,
                "fill_verified": bool(verification.get("fill_verified")),
                "protection_verified": bool(
                    verification.get("protection_verified")
                ),
                "emergency_close": emergency_close,
                "raw": verification.get("order"),
            }

        order = verification["order"]
        order_id = self._order_id(order)
        try:
            post_fill_risk = self._validate_post_fill_risk(
                verification,
                contract_size=contract_size,
                expected_risk_usdt=risk_usdt,
                sl_price=sl_price,
                tp_price=tp_price,
            )
        except Exception as error:
            position_amount = self._position_contracts(
                verification.get("position")
            )
            emergency_close = (
                self._emergency_close(
                    proposal.symbol,
                    position_amount,
                    parent_external_oid=external_oid,
                )
                if position_amount > 0
                else None
            )
            logger.critical(
                "[LIVE] post-fill risk invalid %s: %s; emergency_close=%s",
                proposal.symbol,
                error,
                emergency_close,
            )
            return {
                "status": "error",
                "reason": f"post_fill_risk: {error}",
                "symbol": proposal.symbol,
                "order_id": order_id,
                "external_oid": external_oid,
                "fill_verified": True,
                "protection_verified": True,
                "post_fill_risk_verified": False,
                "emergency_close": emergency_close,
                "raw": order,
            }

        logger.warning(
            "[LIVE] ✓ SHORT %s | size=%.6g notional=$%.2f entry≈$%.6g "
            "SL=$%.6g (+%.2f%%) TP=$%.6g (-%.2f%%) lev=%.0fx order_id=%s",
            proposal.symbol, amount, notional, proposal.entry_price,
            sl_price, proposal.sl_pct, tp_price, proposal.tp_pct,
            self._max_leverage, order_id,
        )
        return {
            "status":        "ok",
            "order_id":      order_id,
            "external_oid":  external_oid,
            "symbol":        proposal.symbol,
            "amount":        amount,
            "filled_amount": verification.get("filled_amount"),
            "average_fill_price": post_fill_risk["average_fill_price"],
            "notional_usdt": notional,
            "actual_notional_usdt": post_fill_risk["actual_notional_usdt"],
            "risk_usdt":     risk_usdt,
            "actual_risk_usdt": post_fill_risk["actual_risk_usdt"],
            "actual_sl_pct": post_fill_risk["actual_sl_pct"],
            "actual_tp_pct": post_fill_risk["actual_tp_pct"],
            "risk_pct_of_account": risk_pct,
            "sl_price":      sl_price,
            "tp_price":      tp_price,
            "leverage":      self._max_leverage,
            "margin_mode":   self._margin_mode,
            "position_mode": self._position_mode,
            "fill_verified": True,
            "protection_verified": True,
            "post_fill_risk_verified": True,
            "recovered_after_error": create_error is not None,
            "reused_existing_order": reused_existing_order,
            "market_execution": market_execution,
            "raw":           order,
        }

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """SHORT ポジションを成行 buy + reduceOnly でクローズする。

        通常は SL/TP が exchange 側で発火するため使われない。
        緊急停止 / 手動介入用。
        """
        if not math.isfinite(amount) or amount <= 0:
            return {"status": "error", "reason": "close amount must be positive"}
        manual_intent = self._derived_external_oid(
            f"manual-close|{symbol}|{amount:.16g}|{time.time_ns()}",
            kind="m",
        )
        result = self._emergency_close(
            symbol,
            amount,
            parent_external_oid=manual_intent,
        )
        if result.get("status") == "ok":
            logger.warning(
                "[LIVE] CLOSE %s amount=%.6g order_id=%s",
                symbol,
                amount,
                result.get("order_id"),
            )
        else:
            logger.error("[LIVE] close_position FAILED %s: %s", symbol, result)
        return result


# ---------------------------------------------------------------------------
# Proposal Builder (ビジネスロジック)
# ---------------------------------------------------------------------------

class ProposalBuilder:
    """AnalysisResult からトレード提案を組み立てるファクトリ。

    SL 幅の決定ルール (損失低減のための volatility-aware 設計):
      1. ATR が取得できれば SL_PCT = clamp(ATR% × ATR_SL_MULT, ATR_SL_MIN, ATR_SL_MAX)
      2. 取得できなければ固定値 STOP_LOSS_PCT を使用
      3. TP は RISK_REWARD_RATIO (デフォルト 2.0) × sl_pct で決定
         → 1:2 リスクリワードを維持することで、勝率 33% でも損益分岐

    ショート前提のため:
        SL = entry_price * (1 + sl_pct / 100)  ← 上方向
        TP = entry_price * (1 - tp_pct / 100)  ← 下方向
    """

    def __init__(self) -> None:
        # 固定フォールバック
        self._fixed_sl_pct: float = float(os.getenv("STOP_LOSS_PCT", "2.0"))
        self._fixed_tp_pct: float = float(os.getenv("TAKE_PROFIT_PCT", "4.0"))

        # ATR ベース
        self._use_atr_sl:  bool  = os.getenv("USE_ATR_SL", "true").lower() != "false"
        self._atr_sl_mult: float = float(os.getenv("ATR_SL_MULT", "1.5"))
        self._atr_sl_min:  float = float(os.getenv("ATR_SL_MIN", "1.0"))
        self._atr_sl_max:  float = float(os.getenv("ATR_SL_MAX", "4.0"))
        self._rr_ratio:    float = float(os.getenv("RISK_REWARD_RATIO", "2.0"))

    def build(
        self,
        result: AnalysisResult,
        fundamental: FundamentalResult | None = None,
    ) -> TradeProposal:
        """AnalysisResult を TradeProposal に変換する。

        Args:
            result: TechnicalAnalyzer の分析結果
            fundamental: FundamentalAnalyzer の考察結果（省略可）
        Returns:
            構造化された TradeProposal
        """
        entry = result.price

        # SL 幅を決定
        if self._use_atr_sl and result.atr_pct is not None and result.atr_pct > 0:
            sl_pct = max(
                self._atr_sl_min,
                min(result.atr_pct * self._atr_sl_mult, self._atr_sl_max),
            )
        else:
            sl_pct = self._fixed_sl_pct

        # TP は RR 比で決定
        tp_pct = sl_pct * self._rr_ratio

        sl = entry * (1 + sl_pct / 100)
        tp = entry * (1 - tp_pct / 100)

        return TradeProposal(
            symbol=result.symbol,
            direction="short",
            entry_price=entry,
            stop_loss=sl,
            take_profit=tp,
            sl_pct=sl_pct,
            tp_pct=tp_pct,
            rsi_at_entry=result.rsi,
            bb_upper_at_entry=result.bb_upper,
            volume_24h_usdt=result.volume_24h_usdt,
            change_1h_pct=result.change_1h_pct,
            fundamental=fundamental,
        )


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

class ExecutorFactory:
    """DRY_RUN 環境変数に基づき適切な Executor を返すファクトリ。

    使用例:
        executor = ExecutorFactory.create(client)
        # DRY_RUN=true  → DryRunExecutor
        # DRY_RUN=false → LiveExecutor (要 Trade 権限)
    """

    @staticmethod
    def create(client: MEXCClient) -> BaseExecutor:
        """環境変数 DRY_RUN の値に応じて Executor インスタンスを生成する。

        Args:
            client: MEXCClient インスタンス
        Returns:
            BaseExecutor のいずれかの具体実装
        """
        dry_run: bool = os.getenv("DRY_RUN", "true").lower() != "false"

        if dry_run:
            logger.info("Executor mode: DRY RUN (no real orders will be placed).")
            return DryRunExecutor()

        live_enabled = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
        live_confirmation = os.getenv("LIVE_TRADING_CONFIRMATION", "")
        if not live_enabled or live_confirmation != "LIVE":
            raise RuntimeError(
                "DRY_RUN=false requested, but live trading is locked. "
                "Set LIVE_TRADING_ENABLED=true and LIVE_TRADING_CONFIRMATION=LIVE "
                "only from the protected live workflow."
            )

        logger.warning(
            "Executor mode: LIVE - Real orders WILL be placed. "
            "Ensure API has Trade permission and risk parameters are correct."
        )
        return LiveExecutor(client)
