"""
utils/mexc_client.py
MEXC APIへのセキュアな接続ラッパー (ccxt ベース)
"""
from __future__ import annotations

import json
import logging
import os
import time
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import ccxt

logger = logging.getLogger(__name__)


class MEXCClient:
    """ccxt.mexc をラップし、Rate Limit 管理と共通エラー処理を提供する。

    Read-only モードでは APIキー無しのパブリックエンドポイントも利用可能。
    APIキーが設定されている場合はプライベートエンドポイントも使用できる。
    """

    # ccxt が報告する Rate Limit の余裕係数（安全マージン）
    RATE_LIMIT_SAFETY_FACTOR: float = 1.2
    # contract.mexc.com was retired in January 2026.
    CONTRACT_API_BASE: str = "https://api.mexc.com/api/v1/contract"
    DIRECT_TIMEOUT_SECONDS: float = float(os.getenv("MEXC_PUBLIC_API_TIMEOUT", "15"))
    KLINE_INTERVALS: dict[str, str] = {
        "1m": "Min1",
        "5m": "Min5",
        "15m": "Min15",
        "30m": "Min30",
        "1h": "Min60",
        "4h": "Hour4",
        "8h": "Hour8",
        "1d": "Day1",
        "1w": "Week1",
        "1M": "Month1",
    }

    def __init__(self) -> None:
        api_key: str = os.getenv("MEXC_API_KEY", "")
        secret_key: str = os.getenv("MEXC_SECRET_KEY", "")

        config: dict[str, Any] = {
            "enableRateLimit": True,
            # defaultType は ccxt が参照する exchange.options に入れる必要がある。
            # トップレベルキーとして渡すと exchange.options に反映されない実装があるため
            # "options" キーでネストして明示的に指定する。
            "options": {
                "defaultType": "swap",  # USDT-M 無期限先物をデフォルトに設定
            },
        }

        if api_key and secret_key:
            config["apiKey"] = api_key
            config["secret"] = secret_key
            logger.info("MEXC client initialized with API credentials (authenticated mode).")
        else:
            logger.info("MEXC client initialized without API credentials (public mode).")

        self._exchange: ccxt.mexc = ccxt.mexc(config)
        self._direct_markets_cache: list[dict[str, Any]] | None = None

    # ------------------------------------------------------------------
    # Market Data (Public)
    # ------------------------------------------------------------------

    def fetch_markets(self) -> list[dict[str, Any]]:
        """全マーケット情報を取得する。"""
        try:
            markets = self._call_with_retry(self._exchange.fetch_markets)
            if not markets:
                raise RuntimeError("ccxt returned no markets")
            return markets
        except Exception as e:
            logger.warning("ccxt fetch_markets failed; using MEXC public API: %s", e)
            return self._fetch_direct_markets()

    def fetch_swap_usdt_symbols(self) -> list[str]:
        """アクティブな USDT建て Swap 銘柄のシンボルリストを返す。

        fetch_tickers() の defaultType が正しく機能しない場合のフォールバックとして、
        fetch_markets() から確実にスワップ銘柄のみを抽出する。
        """
        markets = self.fetch_markets()
        symbols = [
            m["symbol"]
            for m in markets
            if m.get("type") == "swap"
            and m.get("quote") == "USDT"
            and m.get("active", True)
        ]
        if symbols:
            return symbols
        logger.warning(
            "ccxt markets contained no active USDT swaps; using MEXC public API"
        )
        return [
            m["symbol"]
            for m in self._fetch_direct_markets()
            if m.get("active", True)
        ]

    def fetch_tickers(self, symbols: list[str] | None = None) -> dict[str, Any]:
        """ティッカー情報を一括取得する。

        Args:
            symbols: 対象シンボルリスト。None の場合は全ティッカーを取得。
        """
        try:
            if symbols:
                tickers = self._call_with_retry(self._exchange.fetch_tickers, symbols)
            else:
                tickers = self._call_with_retry(self._exchange.fetch_tickers)
            if not tickers:
                raise RuntimeError("ccxt returned no tickers")
            return tickers
        except Exception as e:
            logger.warning("ccxt fetch_tickers failed; using MEXC public API: %s", e)
            rows = self._direct_get("/ticker")
            if not isinstance(rows, list):
                raise RuntimeError("MEXC ticker response is not a list")

            wanted = set(symbols or [])
            tickers: dict[str, Any] = {}
            for row in rows:
                symbol = self._to_unified_symbol(str(row.get("symbol", "")))
                if not symbol or (wanted and symbol not in wanted):
                    continue
                tickers[symbol] = {
                    "symbol": symbol,
                    "last": self._as_float(row.get("lastPrice")),
                    "percentage": self._as_float(row.get("riseFallRate")) * 100,
                    "quoteVolume": self._as_float(row.get("amount24")),
                    "baseVolume": self._as_float(row.get("volume24")),
                    "bid": self._as_float(row.get("bid1")),
                    "ask": self._as_float(row.get("ask1")),
                    "timestamp": int(time.time() * 1000),
                    "info": row,
                }
            if not tickers:
                raise RuntimeError("MEXC public API returned no matching tickers")
            return tickers

    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str = "1h",
        limit: int = 100,
    ) -> list[list[float]]:
        """OHLCVデータを取得する。

        Args:
            symbol: 取得対象のシンボル (例: "BTC/USDT:USDT")
            timeframe: 時間足 (例: "1h", "4h", "1d")
            limit: 取得するローソク足の本数
        Returns:
            [[timestamp, open, high, low, close, volume], ...]
        """
        try:
            candles = self._call_with_retry(
                self._exchange.fetch_ohlcv,
                symbol,
                timeframe,
                None,  # since
                limit,
            )
            if not candles:
                raise RuntimeError("ccxt returned no OHLCV candles")
            return candles
        except Exception as e:
            logger.warning(
                "ccxt fetch_ohlcv failed for %s; using MEXC public API: %s",
                symbol,
                e,
            )
            interval = self.KLINE_INTERVALS.get(timeframe)
            if interval is None:
                raise ValueError(f"Unsupported MEXC kline timeframe: {timeframe}") from e
            data = self._direct_get(
                f"/kline/{self._to_contract_symbol(symbol)}",
                {"interval": interval, "limit": limit},
            )
            if not isinstance(data, dict):
                raise RuntimeError("MEXC kline response is not an object")
            columns = [
                data.get(key, [])
                for key in ("time", "open", "high", "low", "close", "vol")
            ]
            count = min((len(column) for column in columns), default=0)
            candles = [
                [
                    int(columns[0][index]) * 1000,
                    self._as_float(columns[1][index]),
                    self._as_float(columns[2][index]),
                    self._as_float(columns[3][index]),
                    self._as_float(columns[4][index]),
                    self._as_float(columns[5][index]),
                ]
                for index in range(count)
            ]
            if not candles:
                raise RuntimeError("MEXC public API returned no OHLCV candles")
            return candles

    def fetch_order_book(self, symbol: str, limit: int = 20) -> dict[str, Any]:
        """板情報を取得する。"""
        return self._call_with_retry(self._exchange.fetch_order_book, symbol, limit)

    def fetch_funding_rate(self, symbol: str) -> float | None:
        """無期限先物のファンディングレートを取得する (%)。

        ccxt の fundingRate フィールドは小数形式 (0.0001 = 0.01%) なので
        100 を掛けてパーセント値に変換して返す。

        Returns:
            ファンディングレート (%)、例: +0.01 / -0.005 / None (取得失敗)
        """
        try:
            result = self._call_with_retry(self._exchange.fetch_funding_rate, symbol)
            rate = result.get("fundingRate")
            if rate is None:
                raise RuntimeError("ccxt returned no fundingRate")
            return float(rate) * 100  # 小数 → %
        except Exception as e:
            logger.debug(
                "ccxt fetch_funding_rate failed for %s; using MEXC public API: %s",
                symbol,
                e,
            )
            try:
                data = self._direct_get(
                    f"/funding_rate/{self._to_contract_symbol(symbol)}"
                )
                if not isinstance(data, dict) or data.get("fundingRate") is None:
                    raise RuntimeError("MEXC funding response has no fundingRate")
                return float(data["fundingRate"]) * 100
            except Exception as direct_error:
                logger.warning(
                    "fetch_funding_rate unavailable for %s: %s",
                    symbol,
                    direct_error,
                )
                return None

    def fetch_open_interest(self, symbol: str) -> tuple[float | None, float | None]:
        """現在の未決済建玉 (OI) を取得する。

        Returns:
            (open_interest_value_usdt, oi_change_pct_1h) のタプル。
            取得失敗・未サポート時は (None, None)
        """
        try:
            result = self._exchange.fetch_open_interest(symbol)
            oi_value = result.get("openInterestValue") or result.get("openInterest")
            if oi_value is None:
                return None, None
            oi_value = float(oi_value)

            oi_change_pct: float | None = None
            try:
                history = self._exchange.fetch_open_interest_history(
                    symbol, "1h", None, 2
                )
                if history and len(history) >= 2:
                    prev = history[-2].get("openInterestValue") or history[-2].get("openInterest")
                    curr = history[-1].get("openInterestValue") or history[-1].get("openInterest")
                    if prev and curr and float(prev) > 0:
                        oi_change_pct = (float(curr) - float(prev)) / float(prev) * 100
            except Exception as e:
                logger.debug("fetch_open_interest_history failed for %s: %s", symbol, e)

            return oi_value, oi_change_pct

        except Exception as e:
            logger.debug("fetch_open_interest failed for %s: %s", symbol, e)
            return None, None

    def fetch_long_short_ratio(self, symbol: str) -> float | None:
        """グローバルのロング/ショート比率を取得する。

        Returns:
            longShortRatio。取得失敗・未サポート時は None
        """
        try:
            result = self._exchange.fetch_long_short_ratio(symbol, "1h")
            ratio = result.get("longShortRatio") or result.get("longAccount")
            if ratio is None:
                return None
            return float(ratio)
        except Exception as e:
            logger.debug("fetch_long_short_ratio failed for %s: %s", symbol, e)
            return None

    # ------------------------------------------------------------------
    # Private (Trading) - 将来の本番実装用プレースホルダー
    # ------------------------------------------------------------------

    def create_order(
        self,
        symbol: str,
        order_type: str,
        side: str,
        amount: float,
        price: float | None = None,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """注文を1回だけ発行する（Trade権限が必要）。

        DRY_RUN=true の場合は executor.py 側で呼び出しをスキップするため、
        このメソッドは実装済みだが通常は呼ばれない。

        注文のような書き込み系APIは、通信エラー時に結果が不明なまま同じ
        リクエストを再送すると重複約定し得る。そのため読み取り系で使う
        ``_call_with_retry`` は意図的に使わない。呼び出し側は externalOid
        を必ず付け、失敗時は注文・ポジションを照合すること。
        """
        if params is None:
            params = {}
        return self._call_once(
            self._exchange.create_order,
            symbol,
            order_type,
            side,
            amount,
            price,
            params,
        )

    def fetch_order_by_external_id(
        self,
        symbol: str,
        external_oid: str,
    ) -> dict[str, Any] | None:
        """MEXC Futures の externalOid で注文を照合する。

        ccxt の統一 ``fetch_order`` は注文IDを要求するため、MEXC公式の
        ``GET /order/external/{symbol}/{external_oid}`` を利用する。
        見つからない場合は ``None``、API障害時は例外を返して、呼び出し側が
        「未発注」と誤認しないよう fail-closed にする。
        """
        if not external_oid:
            raise ValueError("external_oid is required")
        market = self._exchange.market(symbol)
        method = getattr(
            self._exchange,
            "contractPrivateGetOrderExternalSymbolExternalOid",
            None,
        )
        if method is None:
            raise RuntimeError(
                "Installed ccxt does not expose MEXC external order lookup"
            )
        response = self._call_with_retry(
            method,
            {
                "symbol": market["id"],
                "external_oid": external_oid,
            },
        )
        if not isinstance(response, dict):
            raise RuntimeError("MEXC external order lookup returned invalid data")
        data = response.get("data")
        return data if isinstance(data, dict) and data else None

    def fetch_current_tpsl_orders(self, symbol: str) -> list[dict[str, Any]]:
        """現在有効なMEXC Futures TP/SL注文を取得する。"""
        market = self._exchange.market(symbol)
        method = getattr(
            self._exchange,
            "contractPrivateGetStoporderOpenOrders",
            None,
        )
        if method is None:
            raise RuntimeError(
                "Installed ccxt does not expose MEXC TP/SL order lookup"
            )
        response = self._call_with_retry(method, {"symbol": market["id"]})
        if not isinstance(response, dict):
            raise RuntimeError("MEXC TP/SL lookup returned invalid data")
        data = response.get("data")
        if data is None:
            return []
        if not isinstance(data, list):
            raise RuntimeError("MEXC TP/SL lookup data is not a list")
        return [row for row in data if isinstance(row, dict)]

    def place_position_tpsl(
        self,
        *,
        position_id: int | str,
        amount: float,
        stop_loss_price: float,
        take_profit_price: float,
    ) -> dict[str, Any]:
        """既存ポジションへTP/SLを1回だけ設定する。

        主注文へのattachが確認できない場合の保護フォールバック用。これも
        書き込み系のため自動再試行しない。
        """
        if not position_id:
            raise ValueError("position_id is required")
        if amount <= 0 or stop_loss_price <= 0 or take_profit_price <= 0:
            raise ValueError("amount and TP/SL prices must be positive")
        method = getattr(
            self._exchange,
            "contractPrivatePostStoporderPlace",
            None,
        )
        if method is None:
            raise RuntimeError(
                "Installed ccxt does not expose MEXC position TP/SL placement"
            )
        return self._call_once(
            method,
            {
                "positionId": position_id,
                "vol": amount,
                "stopLossPrice": stop_loss_price,
                "takeProfitPrice": take_profit_price,
                "lossTrend": 2,
                "profitTrend": 1,
                "profitLossVolType": "SAME",
                "volType": 2,
                "takeProfitType": 0,
                "stopLossType": 0,
                "takeProfitOrderPrice": 0,
                "stopLossOrderPrice": 0,
            },
        )

    def fetch_balance(self) -> dict[str, Any]:
        """口座残高を取得する（認証が必要）。"""
        return self._call_with_retry(self._exchange.fetch_balance)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _call_once(self, func: Any, *args: Any) -> Any:
        """書き込み系APIを単回実行し、成功時だけrate-limit余白を取る。"""
        result = func(*args)
        sleep_ms: int = getattr(self._exchange, "rateLimit", 100)
        time.sleep(sleep_ms * self.RATE_LIMIT_SAFETY_FACTOR / 1000)
        return result

    def _direct_get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
    ) -> Any:
        query = f"?{urlencode(params)}" if params else ""
        request = Request(
            f"{self.CONTRACT_API_BASE}{path}{query}",
            headers={"User-Agent": "mexc-momentum-scanner/1.0"},
        )
        with urlopen(request, timeout=self.DIRECT_TIMEOUT_SECONDS) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not isinstance(payload, dict):
            raise RuntimeError("MEXC public API returned an invalid response")
        if payload.get("success") is False or payload.get("code") not in (None, 0):
            raise RuntimeError(
                f"MEXC public API error code={payload.get('code')}: "
                f"{payload.get('message')}"
            )
        if payload.get("data") is None:
            raise RuntimeError("MEXC public API response has no data")
        return payload["data"]

    def _fetch_direct_markets(self) -> list[dict[str, Any]]:
        if self._direct_markets_cache is not None:
            return self._direct_markets_cache
        rows = self._direct_get("/detail")
        if not isinstance(rows, list):
            raise RuntimeError("MEXC contract detail response is not a list")
        markets: list[dict[str, Any]] = []
        for row in rows:
            quote = str(row.get("quoteCoin", ""))
            raw_symbol = str(row.get("symbol", ""))
            symbol = self._to_unified_symbol(raw_symbol)
            if not symbol or quote != "USDT":
                continue
            markets.append(
                {
                    "id": raw_symbol,
                    "symbol": symbol,
                    "base": str(row.get("baseCoin", "")),
                    "quote": quote,
                    "settle": quote,
                    "type": "swap",
                    "swap": True,
                    "active": row.get("state") == 0
                    and row.get("apiAllowed") is not False,
                    "contractSize": self._as_float(row.get("contractSize"), 1.0),
                    "info": row,
                }
            )
        if not markets:
            raise RuntimeError("MEXC public API returned no contract markets")
        self._direct_markets_cache = markets
        return markets

    @staticmethod
    def _to_contract_symbol(symbol: str) -> str:
        return symbol.split(":", 1)[0].replace("/", "_")

    @staticmethod
    def _to_unified_symbol(symbol: str) -> str:
        if not symbol or "_" not in symbol:
            return ""
        base, quote = symbol.rsplit("_", 1)
        return f"{base}/{quote}:{quote}"

    @staticmethod
    def _as_float(value: Any, default: float = 0.0) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    def _call_with_retry(
        self,
        func: Any,
        *args: Any,
        max_retries: int = 3,
        base_sleep: float = 1.0,
    ) -> Any:
        """APIコールをリトライ付きで実行し、Rate Limit を遵守する。

        Args:
            func: 呼び出す ccxt メソッド
            *args: func に渡す引数
            max_retries: 最大リトライ回数
            base_sleep: リトライ待機の基本秒数（指数バックオフ）
        """
        for attempt in range(max_retries):
            try:
                result = func(*args)
                # ccxt の enableRateLimit が内部で処理するが、
                # 追加のバッファとして rateLimit の安全マージンを適用
                sleep_ms: int = getattr(self._exchange, "rateLimit", 100)
                time.sleep(sleep_ms * self.RATE_LIMIT_SAFETY_FACTOR / 1000)
                return result

            except ccxt.RateLimitExceeded as e:
                wait_time = base_sleep * (2 ** attempt)
                logger.warning(
                    "Rate limit exceeded (attempt %d/%d). Sleeping %.1fs. Error: %s",
                    attempt + 1,
                    max_retries,
                    wait_time,
                    e,
                )
                time.sleep(wait_time)

            except ccxt.NetworkError as e:
                wait_time = base_sleep * (2 ** attempt)
                logger.warning(
                    "Network error (attempt %d/%d). Sleeping %.1fs. Error: %s",
                    attempt + 1,
                    max_retries,
                    wait_time,
                    e,
                )
                if attempt == max_retries - 1:
                    raise
                time.sleep(wait_time)

            except ccxt.ExchangeError as e:
                logger.error("Exchange error calling %s: %s", func.__name__, e)
                raise

            except Exception as e:
                logger.error("Unexpected error calling %s: %s", func.__name__, e)
                raise

        raise RuntimeError(f"Max retries ({max_retries}) exceeded for {func.__name__}")

    @property
    def exchange(self) -> ccxt.mexc:
        """生の ccxt インスタンスへのアクセス（高度な利用時）。"""
        return self._exchange
