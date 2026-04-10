"""
core/scanner.py
市場監視ロジック: BTCの挙動とアルトコインの急騰検知

1h変化率の算出はすべて OHLCV (2本) から計算する。
MEXC先物ティッカーには信頼できる1hフィールドが存在しないため。

スキャン手順:
    1. BTC/USDT の1h OHLCV (2本) から正確な1h騰落率を算出
    2. 全ティッカーを一括取得し出来高フィルターを適用
    3. 24h変化率の高い順に上位 MAX_OHLCV_CHECKS 件を選定
    4. 選定した銘柄のみ1h OHLCV を取得して実際の1h変化率を確認
    5. ALT_SURGE_THRESHOLD 以上の銘柄を候補として返す
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
    is_bearish: bool
    is_stagnant: bool
    is_signal_active: bool


@dataclass
class SurgeCandidate:
    """急騰銘柄の候補データを表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float       # OHLCV から計算した実際の1h変化率
    volume_24h_usdt: float
    ticker_raw: dict[str, Any] = field(default_factory=dict)


class MarketScanner:
    """USDT先物全ペアを監視し、BTCが弱い局面で独歩高している銘柄を検出する。"""

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
        # OHLCV取得対象の上限数（24h変化率上位N件に絞る）
        self._max_ohlcv_checks: int = int(os.getenv("MAX_OHLCV_CHECKS", "50"))

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run_scan(self) -> tuple[BTCStatus, list[SurgeCandidate]]:
        """スキャンを1サイクル実行し、BTC状態と急騰候補リストを返す。"""
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
    # BTC Status (OHLCV ベース)
    # ------------------------------------------------------------------

    def _check_btc_status(self) -> BTCStatus:
        """BTC/USDT の1h OHLCV (2本) から正確な1h騰落率を算出する。"""
        try:
            ohlcv = self._client.fetch_ohlcv(
                self.BTC_SYMBOL, timeframe="1h", limit=2
            )
            if len(ohlcv) < 2:
                raise ValueError("BTC OHLCV returned fewer than 2 bars")

            prev_close = float(ohlcv[0][4])
            curr_close = float(ohlcv[1][4])
            price = curr_close
            change_1h_pct = (
                (curr_close - prev_close) / prev_close * 100
                if prev_close > 0 else 0.0
            )

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
            return BTCStatus(
                symbol=self.BTC_SYMBOL,
                price=0.0,
                change_1h_pct=0.0,
                is_bearish=False,
                is_stagnant=False,
                is_signal_active=False,
            )

    # ------------------------------------------------------------------
    # Alt Coin Surge Detection
    # ------------------------------------------------------------------

    def _scan_surge_alts(self) -> list[SurgeCandidate]:
        """2段階フィルターで急騰銘柄を検出する。

        Step1: 全ティッカー一括取得 → 出来高フィルター → 24h変化率上位N件
        Step2: 選定銘柄のみ 1h OHLCV を取得して実際の1h変化率を確認
        """
        try:
            all_tickers: dict[str, Any] = self._client.fetch_tickers()
        except Exception as e:
            logger.error("Failed to fetch all tickers: %s", e)
            return []

        # USDT先物ペアのみ抽出（ccxt MEXC swap: "XXX/USDT:USDT" 形式）
        usdt_swap = {
            sym: t
            for sym, t in all_tickers.items()
            if sym.endswith("/USDT:USDT") and sym != self.BTC_SYMBOL
        }
        logger.info("USDT swap symbols: %d total", len(usdt_swap))

        # 出来高フィルター
        liquid = {
            sym: t
            for sym, t in usdt_swap.items()
            if float(t.get("last") or 0) > 0
            and float(t.get("quoteVolume") or 0) >= self._min_volume_usdt
        }
        logger.info(
            "After volume filter (>$%.0f): %d symbols", self._min_volume_usdt, len(liquid)
        )

        if not liquid:
            logger.warning(
                "No liquid symbols found. Check MIN_24H_VOLUME_USDT setting "
                "or verify MEXC API is returning swap tickers correctly."
            )
            return []

        # 24h変化率の高い順に上位N件を選定（OHLCV呼び出し数を抑制）
        sorted_by_24h = sorted(
            liquid.items(),
            key=lambda x: float(x[1].get("percentage") or 0),
            reverse=True,
        )
        pre_candidates = sorted_by_24h[: self._max_ohlcv_checks]

        logger.info(
            "Top 5 by 24h change: %s",
            "  |  ".join(
                f"{sym} {float(t.get('percentage') or 0):+.1f}%"
                for sym, t in pre_candidates[:5]
            ),
        )

        # 各銘柄の1h変化率を OHLCV から正確に計算
        candidates: list[SurgeCandidate] = []

        for symbol, ticker in pre_candidates:
            try:
                ohlcv = self._client.fetch_ohlcv(symbol, timeframe="1h", limit=2)
                if len(ohlcv) < 2:
                    continue

                prev_close = float(ohlcv[0][4])
                curr_close = float(ohlcv[1][4])
                if prev_close <= 0:
                    continue

                change_1h_pct = (curr_close - prev_close) / prev_close * 100

                if change_1h_pct < self._alt_surge_threshold:
                    continue

                volume_24h = float(ticker.get("quoteVolume") or 0)
                candidates.append(
                    SurgeCandidate(
                        symbol=symbol,
                        price=float(ticker.get("last") or curr_close),
                        change_1h_pct=change_1h_pct,
                        volume_24h_usdt=volume_24h,
                        ticker_raw=ticker,
                    )
                )

            except Exception as e:
                logger.debug("Skipping %s: %s", symbol, e)

        candidates.sort(key=lambda c: c.change_1h_pct, reverse=True)
        return candidates
