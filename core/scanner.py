"""
core/scanner.py
市場監視ロジック: BTCの挙動とアルトコインの急騰検知
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from typing import Any

from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)


@dataclass
class BTCStatus:
    """BTC の現在状態を表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float
    is_bearish: bool      # 1h変化率が BTC_BEARISH_THRESHOLD 以下
    is_stagnant: bool     # 1h変化率が ±BTC_STAGNANT_THRESHOLD 以内
    is_signal_active: bool  # いずれかの条件を満たす場合 True


@dataclass
class SurgeCandidate:
    """急騰銘柄の候補データを表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float
    volume_24h_usdt: float
    ticker_raw: dict[str, Any] = field(default_factory=dict)


class MarketScanner:
    """USDT先物全ペアを監視し、BTCが弱い局面で独歩高している銘柄を検出する。

    検出ロジック:
        1. BTC/USDT の1時間騰落率を確認
        2. BTC が弱気 (≤ BTC_BEARISH_THRESHOLD%) または
           停滞 (|変化率| ≤ BTC_STAGNANT_THRESHOLD%) の場合にシグナル有効化
        3. シグナル有効時、1時間で ALT_SURGE_THRESHOLD% 以上上昇し、
           かつ24時間出来高が MIN_24H_VOLUME_USDT 以上の銘柄を抽出
    """

    BTC_SYMBOL: str = "BTC/USDT:USDT"

    def __init__(self, client: MEXCClient) -> None:
        self._client = client

        self._btc_bearish_threshold: float = float(
            os.getenv("BTC_BEARISH_THRESHOLD", "-0.5")
        )
        self._btc_stagnant_threshold: float = float(
            os.getenv("BTC_STAGNANT_THRESHOLD", "0.2")
        )
        self._alt_surge_threshold: float = float(
            os.getenv("ALT_SURGE_THRESHOLD", "5.0")
        )
        self._min_volume_usdt: float = float(
            os.getenv("MIN_24H_VOLUME_USDT", "1000000")
        )

        logger.debug(
            "MarketScanner initialized | BTC bearish=%.2f%% stagnant=±%.2f%% "
            "surge=+%.2f%% min_vol=$%.0f",
            self._btc_bearish_threshold,
            self._btc_stagnant_threshold,
            self._alt_surge_threshold,
            self._min_volume_usdt,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run_scan(self) -> tuple[BTCStatus, list[SurgeCandidate]]:
        """スキャンを1サイクル実行し、BTC状態と急騰候補リストを返す。

        Returns:
            (btc_status, candidates): BTC の状態と急騰候補のリスト
        """
        logger.info("=== Scan cycle started ===")

        btc_status = self._check_btc_status()
        logger.info(
            "BTC status | price=%.4f 1h_chg=%.2f%% bearish=%s stagnant=%s signal=%s",
            btc_status.price,
            btc_status.change_1h_pct,
            btc_status.is_bearish,
            btc_status.is_stagnant,
            btc_status.is_signal_active,
        )

        if not btc_status.is_signal_active:
            logger.info("BTC signal not active. Skipping alt scan.")
            return btc_status, []

        candidates = self._scan_surge_alts()
        logger.info("Scan complete | %d candidate(s) found.", len(candidates))
        return btc_status, candidates

    # ------------------------------------------------------------------
    # BTC Status
    # ------------------------------------------------------------------

    def _check_btc_status(self) -> BTCStatus:
        """BTC/USDT の1時間騰落率を取得し、シグナル条件を判定する。"""
        try:
            tickers = self._client.fetch_tickers([self.BTC_SYMBOL])
            ticker = tickers.get(self.BTC_SYMBOL, {})

            price: float = float(ticker.get("last") or 0)
            change_1h_pct: float = self._extract_1h_change(ticker)

            is_bearish = change_1h_pct <= self._btc_bearish_threshold
            is_stagnant = abs(change_1h_pct) <= self._btc_stagnant_threshold

            return BTCStatus(
                symbol=self.BTC_SYMBOL,
                price=price,
                change_1h_pct=change_1h_pct,
                is_bearish=is_bearish,
                is_stagnant=is_stagnant,
                is_signal_active=is_bearish or is_stagnant,
            )

        except Exception as e:
            logger.error("Failed to fetch BTC status: %s", e)
            # フェイルセーフ: エラー時はシグナルを無効化して返す
            return BTCStatus(
                symbol=self.BTC_SYMBOL,
                price=0.0,
                change_1h_pct=0.0,
                is_bearish=False,
                is_stagnant=False,
                is_signal_active=False,
            )

    def _extract_1h_change(self, ticker: dict[str, Any]) -> float:
        """ティッカーから1時間騰落率を抽出する。

        ccxt の MEXC実装では 'percentage' が24h変化率であるため、
        1h変化率は info フィールドまたは別途 OHLCV から計算する。
        ここでは 'info' 内の priceChangePercent (1h相当) を優先し、
        存在しない場合は 24h パーセンテージをフォールバックとして利用する。

        Args:
            ticker: ccxt ティッカーオブジェクト
        Returns:
            騰落率 (%) - 正値が上昇
        """
        info: dict[str, Any] = ticker.get("info", {})

        # MEXCの先物APIは riseFallRate が1h変化率に近い場合がある
        for key in ("priceChangePercent1h", "riseFallRate", "priceChangePercent"):
            val = info.get(key)
            if val is not None:
                try:
                    return float(val) * 100 if abs(float(val)) < 10 else float(val)
                except (ValueError, TypeError):
                    continue

        # フォールバック: ccxt 標準の percentage (24h)
        pct = ticker.get("percentage")
        if pct is not None:
            logger.debug(
                "Using 24h percentage as 1h proxy for %s (%.2f%%)",
                ticker.get("symbol"),
                pct,
            )
            return float(pct)

        return 0.0

    # ------------------------------------------------------------------
    # Alt Coin Surge Detection
    # ------------------------------------------------------------------

    def _scan_surge_alts(self) -> list[SurgeCandidate]:
        """全USDT先物ペアを取得し、急騰している銘柄を抽出する。

        Returns:
            条件を満たした SurgeCandidate のリスト（騰落率降順）
        """
        try:
            all_tickers: dict[str, Any] = self._client.fetch_tickers()
        except Exception as e:
            logger.error("Failed to fetch all tickers: %s", e)
            return []

        usdt_swap_symbols = self._filter_usdt_swap_symbols(all_tickers)
        logger.debug("Total USDT swap symbols: %d", len(usdt_swap_symbols))

        candidates: list[SurgeCandidate] = []

        for symbol, ticker in usdt_swap_symbols.items():
            if symbol == self.BTC_SYMBOL:
                continue

            candidate = self._evaluate_ticker(symbol, ticker)
            if candidate is not None:
                candidates.append(candidate)

        # 騰落率の高い順にソート
        candidates.sort(key=lambda c: c.change_1h_pct, reverse=True)
        return candidates

    def _filter_usdt_swap_symbols(
        self, tickers: dict[str, Any]
    ) -> dict[str, Any]:
        """ティッカー辞書から USDT 先物(Swap)ペアのみ抽出する。

        ccxt の MEXC swap マーケットのシンボルは "XXX/USDT:USDT" 形式。
        """
        return {
            sym: t
            for sym, t in tickers.items()
            if sym.endswith("/USDT:USDT")
        }

    def _evaluate_ticker(
        self, symbol: str, ticker: dict[str, Any]
    ) -> SurgeCandidate | None:
        """単一ティッカーが急騰条件を満たすか評価する。

        Args:
            symbol: シンボル名
            ticker: ccxt ティッカーオブジェクト
        Returns:
            条件を満たす場合 SurgeCandidate、そうでなければ None
        """
        try:
            price: float = float(ticker.get("last") or 0)
            change_1h_pct: float = self._extract_1h_change(ticker)

            # 出来高 (quoteVolume が USDT建て24h出来高)
            volume_24h: float = float(ticker.get("quoteVolume") or 0)

            if price <= 0:
                return None

            # 急騰フィルター
            if change_1h_pct < self._alt_surge_threshold:
                return None

            # 出来高フィルター
            if volume_24h < self._min_volume_usdt:
                logger.debug(
                    "Skipping %s: volume $%.0f < threshold $%.0f",
                    symbol,
                    volume_24h,
                    self._min_volume_usdt,
                )
                return None

            return SurgeCandidate(
                symbol=symbol,
                price=price,
                change_1h_pct=change_1h_pct,
                volume_24h_usdt=volume_24h,
                ticker_raw=ticker,
            )

        except (ValueError, TypeError) as e:
            logger.debug("Skipping %s due to parse error: %s", symbol, e)
            return None
