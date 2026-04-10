"""
utils/mexc_client.py
MEXC APIへのセキュアな接続ラッパー (ccxt ベース)
"""
from __future__ import annotations

import logging
import os
import time
from typing import Any

import ccxt

logger = logging.getLogger(__name__)


class MEXCClient:
    """ccxt.mexc をラップし、Rate Limit 管理と共通エラー処理を提供する。

    Read-only モードでは APIキー無しのパブリックエンドポイントも利用可能。
    APIキーが設定されている場合はプライベートエンドポイントも使用できる。
    """

    # ccxt が報告する Rate Limit の余裕係数（安全マージン）
    RATE_LIMIT_SAFETY_FACTOR: float = 1.2

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

    # ------------------------------------------------------------------
    # Market Data (Public)
    # ------------------------------------------------------------------

    def fetch_markets(self) -> list[dict[str, Any]]:
        """全マーケット情報を取得する。"""
        return self._call_with_retry(self._exchange.fetch_markets)

    def fetch_swap_usdt_symbols(self) -> list[str]:
        """アクティブな USDT建て Swap 銘柄のシンボルリストを返す。

        fetch_tickers() の defaultType が正しく機能しない場合のフォールバックとして、
        fetch_markets() から確実にスワップ銘柄のみを抽出する。
        """
        markets = self._call_with_retry(self._exchange.fetch_markets)
        return [
            m["symbol"]
            for m in markets
            if m.get("type") == "swap"
            and m.get("quote") == "USDT"
            and m.get("active", True)
        ]

    def fetch_tickers(self, symbols: list[str] | None = None) -> dict[str, Any]:
        """ティッカー情報を一括取得する。

        Args:
            symbols: 対象シンボルリスト。None の場合は全ティッカーを取得。
        """
        if symbols:
            return self._call_with_retry(self._exchange.fetch_tickers, symbols)
        return self._call_with_retry(self._exchange.fetch_tickers)

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
        return self._call_with_retry(
            self._exchange.fetch_ohlcv,
            symbol,
            timeframe,
            None,  # since
            limit,
        )

    def fetch_order_book(self, symbol: str, limit: int = 20) -> dict[str, Any]:
        """板情報を取得する。"""
        return self._call_with_retry(self._exchange.fetch_order_book, symbol, limit)

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
        """注文を発行する（Trade権限が必要）。

        DRY_RUN=true の場合は executor.py 側で呼び出しをスキップするため、
        このメソッドは実装済みだが通常は呼ばれない。
        """
        if params is None:
            params = {}
        return self._call_with_retry(
            self._exchange.create_order,
            symbol,
            order_type,
            side,
            amount,
            price,
            params,
        )

    def fetch_balance(self) -> dict[str, Any]:
        """口座残高を取得する（認証が必要）。"""
        return self._call_with_retry(self._exchange.fetch_balance)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

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
