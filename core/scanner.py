"""
core/scanner.py
市場監視ロジック: BTCの挙動とアルトコインの急騰検知

1h変化率の算出はすべて OHLCV (2本) から計算する。
MEXC先物ティッカーには信頼できる1hフィールドが存在しないため。

スキャン手順:
    1. BTC/USDT の1h OHLCV (2本) から正確な1h騰落率を算出し regime 判定
    2. 全ティッカーを一括取得し出来高フィルターを適用
    3. 24h変化率の高い順に上位 MAX_OHLCV_CHECKS 件を選定
    4. 選定した銘柄のみ1h OHLCV を取得して実際の1h変化率を確認
    5. 絶対サージ閾値 + 相対強度閾値 の両方を満たした銘柄を返す
       (相対強度 = alt 1h変化率 - BTC 1h変化率)

regime:
    BEARISH  → BTC下落 (従来の逆張りショート対象)
    STAGNANT → BTC停滞
    BULLISH  → BTC上昇 (乖離した独歩高のみを拾う)
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from typing import Any

from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)

# ─── Market regime constants ─────────────────────────────────────────
REGIME_BEARISH  = "BEARISH"
REGIME_STAGNANT = "STAGNANT"
REGIME_BULLISH  = "BULLISH"


@dataclass
class BTCStatus:
    """BTC の現在状態を表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float
    is_bearish: bool
    is_stagnant: bool
    is_signal_active: bool
    regime: str = REGIME_STAGNANT


@dataclass
class SurgeCandidate:
    """急騰銘柄の候補データを表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float            # OHLCV から計算した実際の1h変化率
    relative_strength_pct: float    # change_1h_pct - btc_change_1h_pct
    volume_24h_usdt: float
    ticker_raw: dict[str, Any] = field(default_factory=dict)


class MarketScanner:
    """USDT先物全ペアを監視し、BTC相対で独歩高している銘柄を検出する。

    BTC が弱い時はもちろん、BTC が上がっている時でも
    「他と乖離して異常に上がっている」アルトを拾う。
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
        # 相対強度閾値: alt_1h - btc_1h >= threshold
        # BTCが上がっている局面でも「乖離して異常に上がっている」銘柄を検出する。
        self._relative_strength_threshold: float = float(
            os.getenv("RELATIVE_STRENGTH_THRESHOLD", "5.0")
        )
        self._min_volume_usdt: float = float(
            os.getenv("MIN_24H_VOLUME_USDT", "1000000")
        )
        # OHLCV取得対象の上限数（24h変化率上位N件に絞る）
        self._max_ohlcv_checks: int = int(os.getenv("MAX_OHLCV_CHECKS", "50"))

        # fetch_markets() で取得したスワップ銘柄リストのキャッシュ
        self._swap_symbols: list[str] = []
        self._context_top_limit: int = int(
            os.getenv("MARKET_CONTEXT_TOP_SYMBOLS", "20")
        )
        self._context_near_miss_limit: int = int(
            os.getenv("MARKET_CONTEXT_NEAR_MISS_LIMIT", "30")
        )
        self._last_scan_context: dict[str, Any] = {}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run_scan(self) -> tuple[BTCStatus, list[SurgeCandidate]]:
        """スキャンを1サイクル実行し、BTC状態と急騰候補リストを返す。

        regime に関わらず常にアルトスキャンを実行する:
            - BEARISH / STAGNANT: 従来の絶対閾値での急騰検出
            - BULLISH: 絶対閾値 + 相対強度閾値で「乖離した独歩高」のみ抽出
        """
        logger.info("=== Scan cycle started ===")

        btc_status = self._check_btc_status()
        logger.info(
            "BTC status | price=%.4f 1h_chg=%.2f%% regime=%s",
            btc_status.price,
            btc_status.change_1h_pct,
            btc_status.regime,
        )

        # BTC データが取れなかった場合のみ scan をスキップ
        if not btc_status.is_signal_active:
            logger.warning("BTC data unavailable. Skipping alt scan.")
            self._last_scan_context = {
                "available": False,
                "skip_reason": "btc_unavailable",
                "thresholds": self._scan_thresholds(),
                "symbol_counts": {},
            }
            return btc_status, []

        candidates = self._scan_surge_alts(btc_status.change_1h_pct)
        logger.info(
            "Scan complete | regime=%s candidates=%d",
            btc_status.regime, len(candidates),
        )
        return btc_status, candidates

    @property
    def last_scan_context(self) -> dict[str, Any]:
        """Return the lightweight pre-detection context from the latest scan."""
        return dict(self._last_scan_context)

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

            is_bearish  = change_1h_pct <= self._btc_bearish_threshold
            is_stagnant = abs(change_1h_pct) <= self._btc_stagnant_threshold

            if is_bearish:
                regime = REGIME_BEARISH
            elif is_stagnant:
                regime = REGIME_STAGNANT
            else:
                regime = REGIME_BULLISH

            return BTCStatus(
                symbol=self.BTC_SYMBOL,
                price=price,
                change_1h_pct=change_1h_pct,
                is_bearish=is_bearish,
                is_stagnant=is_stagnant,
                # BTC データが取れていれば常に scan を実行する
                is_signal_active=True,
                regime=regime,
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
                regime=REGIME_STAGNANT,
            )

    # ------------------------------------------------------------------
    # Alt Coin Surge Detection
    # ------------------------------------------------------------------

    def _scan_surge_alts(self, btc_change_1h: float) -> list[SurgeCandidate]:
        """2段階フィルターで急騰銘柄を検出する。

        Step1: fetch_markets() でスワップ銘柄リストを取得（キャッシュ）
               → fetch_tickers(explicit_list) でティッカー取得
               → 出来高フィルター → 24h変化率上位N件に絞る
        Step2: 選定銘柄のみ 1h OHLCV を取得して実際の1h変化率を確認し、
               絶対サージ閾値 + 相対強度閾値 の両方を満たしたものを返す。

        Args:
            btc_change_1h: BTC の1h変化率 (%)。相対強度の計算に用いる。
        """
        context = self._new_scan_context()
        self._last_scan_context = context

        # スワップ銘柄リストをキャッシュから取得（初回のみ API 呼び出し）
        if not self._swap_symbols:
            try:
                self._swap_symbols = self._client.fetch_swap_usdt_symbols()
                logger.info(
                    "Loaded %d USDT swap symbols via fetch_markets().",
                    len(self._swap_symbols),
                )
            except Exception as e:
                logger.error("Failed to fetch swap markets: %s", e)
                context["available"] = False
                context["skip_reason"] = "swap_market_fetch_failed"
                return []

        target_symbols = [s for s in self._swap_symbols if s != self.BTC_SYMBOL]
        context["symbol_counts"]["target_symbols"] = len(target_symbols)
        logger.info("USDT swap symbols: %d total", len(target_symbols))

        try:
            all_tickers: dict[str, Any] = self._client.fetch_tickers(target_symbols)
        except Exception as e:
            logger.error("Failed to fetch tickers: %s", e)
            context["available"] = False
            context["skip_reason"] = "ticker_fetch_failed"
            return []
        context["symbol_counts"]["tickers_fetched"] = len(all_tickers)

        usdt_swap = {
            sym: t
            for sym, t in all_tickers.items()
            if sym != self.BTC_SYMBOL
        }
        context["symbol_counts"]["usdt_swap_tickers"] = len(usdt_swap)

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
        context["symbol_counts"]["liquid_symbols"] = len(liquid)

        if not liquid:
            logger.warning(
                "No liquid symbols found. Check MIN_24H_VOLUME_USDT setting "
                "or verify MEXC API is returning swap tickers correctly."
            )
            context["skip_reason"] = "no_liquid_symbols"
            return []

        # 24h変化率の高い順に上位N件を選定（OHLCV呼び出し数を抑制）
        sorted_by_24h = sorted(
            liquid.items(),
            key=lambda x: float(x[1].get("percentage") or 0),
            reverse=True,
        )
        pre_candidates = sorted_by_24h[: self._max_ohlcv_checks]
        context["symbol_counts"]["pre_candidates"] = len(pre_candidates)
        context["top_by_24h"] = self._ticker_rows(
            pre_candidates, self._context_top_limit
        )

        logger.info(
            "Top 5 by 24h change: %s",
            "  |  ".join(
                f"{sym} {float(t.get('percentage') or 0):+.1f}%"
                for sym, t in pre_candidates[:5]
            ),
        )

        # 各銘柄の1h変化率を OHLCV から正確に計算
        candidates: list[SurgeCandidate] = []
        checked_1h: list[float] = []
        checked_relative: list[float] = []
        near_misses: list[dict[str, Any]] = []
        reject_counts: dict[str, int] = {
            "below_1h_threshold": 0,
            "below_relative_strength": 0,
            "invalid_ohlcv": 0,
            "errors": 0,
        }

        for symbol, ticker in pre_candidates:
            try:
                ohlcv = self._client.fetch_ohlcv(symbol, timeframe="1h", limit=2)
                if len(ohlcv) < 2:
                    reject_counts["invalid_ohlcv"] += 1
                    continue

                prev_close = float(ohlcv[0][4])
                curr_close = float(ohlcv[1][4])
                if prev_close <= 0:
                    reject_counts["invalid_ohlcv"] += 1
                    continue

                change_1h_pct = (curr_close - prev_close) / prev_close * 100
                relative_pct  = change_1h_pct - btc_change_1h
                checked_1h.append(change_1h_pct)
                checked_relative.append(relative_pct)

                # 絶対サージ閾値 (最低限の動き)
                if change_1h_pct < self._alt_surge_threshold:
                    reject_counts["below_1h_threshold"] += 1
                    near_misses.append(
                        self._candidate_context_row(
                            symbol, ticker, curr_close, change_1h_pct,
                            relative_pct, "below_1h_threshold",
                        )
                    )
                    continue
                # 相対強度閾値 (BTCからの乖離)
                # BEARISH 局面では btc_change_1h が負なので自然に通過する。
                # BULLISH 局面ではここで「乖離した独歩高」だけが残る。
                if relative_pct < self._relative_strength_threshold:
                    reject_counts["below_relative_strength"] += 1
                    near_misses.append(
                        self._candidate_context_row(
                            symbol, ticker, curr_close, change_1h_pct,
                            relative_pct, "below_relative_strength",
                        )
                    )
                    continue

                volume_24h = float(ticker.get("quoteVolume") or 0)
                candidates.append(
                    SurgeCandidate(
                        symbol=symbol,
                        price=float(ticker.get("last") or curr_close),
                        change_1h_pct=change_1h_pct,
                        relative_strength_pct=relative_pct,
                        volume_24h_usdt=volume_24h,
                        ticker_raw=ticker,
                    )
                )

            except Exception as e:
                reject_counts["errors"] += 1
                logger.debug("Skipping %s: %s", symbol, e)

        # 相対強度の高い順にソート (より乖離しているものを優先)
        candidates.sort(key=lambda c: c.relative_strength_pct, reverse=True)
        near_misses.sort(
            key=lambda x: (
                float(x.get("change_1h_pct") or 0),
                float(x.get("relative_strength_pct") or 0),
            ),
            reverse=True,
        )
        context["symbol_counts"]["ohlcv_checked"] = len(checked_1h)
        context["symbol_counts"]["surge_candidates"] = len(candidates)
        context["reject_counts"] = reject_counts
        context["checked_1h_summary"] = self._numeric_summary(checked_1h)
        context["relative_strength_summary"] = self._numeric_summary(checked_relative)
        context["near_misses"] = near_misses[: self._context_near_miss_limit]
        return candidates

    # ------------------------------------------------------------------
    # Lightweight market context helpers
    # ------------------------------------------------------------------

    def _new_scan_context(self) -> dict[str, Any]:
        return {
            "available": True,
            "thresholds": self._scan_thresholds(),
            "symbol_counts": {
                "target_symbols": 0,
                "tickers_fetched": 0,
                "usdt_swap_tickers": 0,
                "liquid_symbols": 0,
                "pre_candidates": 0,
                "ohlcv_checked": 0,
                "surge_candidates": 0,
            },
            "top_by_24h": [],
            "near_misses": [],
            "reject_counts": {},
            "checked_1h_summary": {},
            "relative_strength_summary": {},
        }

    def _scan_thresholds(self) -> dict[str, float | int]:
        return {
            "alt_surge_pct": self._alt_surge_threshold,
            "relative_strength_pct": self._relative_strength_threshold,
            "min_volume_usdt": self._min_volume_usdt,
            "max_ohlcv_checks": self._max_ohlcv_checks,
        }

    def _ticker_rows(
        self, rows: list[tuple[str, Any]], limit: int
    ) -> list[dict[str, Any]]:
        return [
            self._ticker_context_row(symbol, ticker)
            for symbol, ticker in rows[: max(0, limit)]
        ]

    def _ticker_context_row(self, symbol: str, ticker: Any) -> dict[str, Any]:
        return {
            "symbol": symbol,
            "last": self._rounded(ticker.get("last")),
            "change_24h_pct": self._rounded(ticker.get("percentage")),
            "volume_24h_usdt": self._rounded(ticker.get("quoteVolume"), 2),
        }

    def _candidate_context_row(
        self,
        symbol: str,
        ticker: Any,
        close: float,
        change_1h_pct: float,
        relative_pct: float,
        reject_reason: str,
    ) -> dict[str, Any]:
        row = self._ticker_context_row(symbol, ticker)
        row.update(
            {
                "close_1h": self._rounded(close),
                "change_1h_pct": self._rounded(change_1h_pct),
                "relative_strength_pct": self._rounded(relative_pct),
                "reject_reason": reject_reason,
            }
        )
        return row

    @staticmethod
    def _rounded(value: Any, digits: int = 4) -> float | None:
        if value is None:
            return None
        try:
            return round(float(value), digits)
        except (TypeError, ValueError):
            return None

    @classmethod
    def _numeric_summary(cls, values: list[float]) -> dict[str, float | int]:
        if not values:
            return {"count": 0}
        ordered = sorted(float(v) for v in values)
        n = len(ordered)

        def pick(q: float) -> float:
            idx = min(n - 1, max(0, int((n - 1) * q)))
            return cls._rounded(ordered[idx]) or 0.0

        return {
            "count": n,
            "min": cls._rounded(ordered[0]) or 0.0,
            "p50": pick(0.50),
            "p90": pick(0.90),
            "p95": pick(0.95),
            "max": cls._rounded(ordered[-1]) or 0.0,
            "avg": cls._rounded(sum(ordered) / n) or 0.0,
        }
