"""
core/analyzer.py
テクニカル指標 (RSI, ボリンジャーバンド, ATR, 出来高トレンド, 4h RSI) と判定

pandas のみで実装しているため外部の TA ライブラリへの依存なし。

損失を減らすために以下の追加フィルターを適用する:
  1. 出来高トレンド: 急騰中に出来高が増加していたらトレンド継続の可能性
                    → 出来高が減衰 (exhaustion) の銘柄のみショート対象にする
  2. 4h RSI:        4h 足で既に過熱 (>= 70) していたら既存の強いトレンド
                    → 1h 単発の急騰だけを狙う
  3. ATR:           SL 幅をボラティリティに応じて自動調整するためのベース値
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import pandas as pd

from core.scanner import SurgeCandidate
from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)


# 出来高トレンドラベル
VOL_TREND_RISING    = "RISING"     # 直近が平均より明確に多い
VOL_TREND_FLAT      = "FLAT"       # 平均並み
VOL_TREND_DECLINING = "DECLINING"  # 平均より明確に少ない


@dataclass
class AnalysisResult:
    """単一銘柄のテクニカル分析結果を表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float
    relative_strength_pct: float   # alt_1h - btc_1h (乖離度)
    volume_24h_usdt: float

    # RSI
    rsi: float | None
    is_rsi_overbought: bool  # RSI >= RSI_OVERBOUGHT (default 75)

    # 4h RSI (マルチタイムフレーム確認用)
    rsi_4h: float | None
    is_4h_trend_established: bool  # 4h RSI >= RSI_4H_MAX → 既存の強いトレンド

    # ボリンジャーバンド
    bb_upper: float | None
    bb_middle: float | None
    bb_lower: float | None
    is_above_bb_upper: bool  # 現在価格 > BB上限(2σ)

    # 出来高トレンド (exhaustion 検出)
    volume_trend: str         # RISING / FLAT / DECLINING
    volume_trend_ratio: float # 最新足出来高 / 平均出来高
    is_volume_exhaustion: bool  # True なら疲弊 → ショート可

    # ATR (ボラティリティ / SL 幅算出用)
    atr: float | None
    atr_pct: float | None     # ATR / price × 100

    # 総合判定
    is_confirmed_signal: bool
    reject_reasons: list[str] # 却下理由（デバッグ/ログ用）


class TechnicalAnalyzer:
    """抽出された急騰候補銘柄に対してテクニカル分析を行う。

    確認シグナルとなる条件（全てを満たす必要あり）:
        - RSI(14) >= RSI_OVERBOUGHT (default: 75) → 「買われすぎ」
        - 現在価格 > ボリンジャーバンド上限(2σ)    → 「バンドブレイク」
        - 出来高トレンド != RISING                 → 疲弊兆候 (loss reducer)
        - 4h RSI < RSI_4H_MAX (default: 70)        → 既存トレンドではない
    """

    def __init__(self, client: MEXCClient) -> None:
        self._client = client

        self._rsi_period:     int   = int(os.getenv("RSI_PERIOD", "14"))
        self._rsi_overbought: float = float(os.getenv("RSI_OVERBOUGHT", "75"))
        self._bb_period:      int   = int(os.getenv("BB_PERIOD", "20"))
        self._bb_std:         float = float(os.getenv("BB_STD", "2.0"))
        self._timeframe:      str   = os.getenv("ANALYSIS_TIMEFRAME", "1h")
        self._ohlcv_limit:    int   = int(os.getenv("OHLCV_LIMIT", "100"))

        # 損失低減フィルター
        self._rsi_4h_max:         float = float(os.getenv("RSI_4H_MAX", "70"))
        self._vol_lookback:       int   = int(os.getenv("VOLUME_LOOKBACK", "20"))
        self._vol_rising_ratio:   float = float(os.getenv("VOLUME_RISING_RATIO", "1.8"))
        self._vol_declining_ratio:float = float(os.getenv("VOLUME_DECLINING_RATIO", "0.8"))
        self._atr_period:         int   = int(os.getenv("ATR_PERIOD", "14"))
        self._use_volume_filter:  bool  = os.getenv("USE_VOLUME_FILTER", "true").lower() != "false"
        self._use_4h_filter:      bool  = os.getenv("USE_4H_FILTER", "true").lower() != "false"

        logger.debug(
            "TechnicalAnalyzer | RSI(%d) OB=%.0f BB(%d,%.1fσ) 4h<=%s volF=%s",
            self._rsi_period, self._rsi_overbought,
            self._bb_period, self._bb_std,
            self._rsi_4h_max, self._use_volume_filter,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze_candidates(
        self, candidates: list[SurgeCandidate]
    ) -> list[AnalysisResult]:
        """急騰候補リストをテクニカル分析し結果を返す。"""
        results: list[AnalysisResult] = []

        for candidate in candidates:
            result = self._analyze_single(candidate)
            if result is not None:
                results.append(result)
                self._log_result(result)

        confirmed = [r for r in results if r.is_confirmed_signal]
        logger.info(
            "Analysis complete | %d analyzed, %d confirmed signal(s).",
            len(results), len(confirmed),
        )
        return results

    # ------------------------------------------------------------------
    # Single Symbol Analysis
    # ------------------------------------------------------------------

    def _analyze_single(self, candidate: SurgeCandidate) -> AnalysisResult | None:
        """1銘柄の 1h OHLCV + 4h OHLCV を取得し各指標を計算する。"""
        try:
            ohlcv = self._client.fetch_ohlcv(
                candidate.symbol,
                timeframe=self._timeframe,
                limit=self._ohlcv_limit,
            )
            required = max(self._rsi_period, self._bb_period, self._atr_period) + 5
            if not ohlcv or len(ohlcv) < required:
                logger.warning(
                    "Insufficient 1h OHLCV for %s (%d bars).",
                    candidate.symbol, len(ohlcv) if ohlcv else 0,
                )
                return None

            df = self._build_dataframe(ohlcv)

            # 4h RSI をマルチタイムフレーム確認用に取得
            rsi_4h_value: float | None = None
            if self._use_4h_filter:
                rsi_4h_value = self._fetch_rsi_4h(candidate.symbol)

            return self._compute_indicators(candidate, df, rsi_4h_value)

        except Exception as e:
            logger.error("Analysis failed for %s: %s", candidate.symbol, e)
            return None

    def _fetch_rsi_4h(self, symbol: str) -> float | None:
        """4h 足の OHLCV を取得して RSI を計算する。失敗時は None。"""
        try:
            ohlcv_4h = self._client.fetch_ohlcv(
                symbol, timeframe="4h", limit=self._rsi_period + 30
            )
            if not ohlcv_4h or len(ohlcv_4h) < self._rsi_period + 1:
                return None
            df_4h = self._build_dataframe(ohlcv_4h)
            rsi_series = self._calc_rsi(df_4h["close"], self._rsi_period)
            return self._last_valid(rsi_series)
        except Exception as e:
            logger.debug("4h RSI fetch failed for %s: %s", symbol, e)
            return None

    def _build_dataframe(self, ohlcv: list[list[float]]) -> pd.DataFrame:
        """ccxt OHLCV リストを pandas DataFrame に変換する。"""
        df = pd.DataFrame(
            ohlcv,
            columns=["timestamp", "open", "high", "low", "close", "volume"],
        )
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
        df.set_index("timestamp", inplace=True)
        df = df.astype(float)
        return df

    def _compute_indicators(
        self,
        candidate: SurgeCandidate,
        df: pd.DataFrame,
        rsi_4h_value: float | None,
    ) -> AnalysisResult:
        """全指標を計算し AnalysisResult を組み立てる。"""
        current_price: float = candidate.price

        # --- RSI ---
        rsi_series = self._calc_rsi(df["close"], self._rsi_period)
        rsi_value  = self._last_valid(rsi_series)
        is_rsi_ob  = rsi_value is not None and rsi_value >= self._rsi_overbought

        # --- 4h トレンド判定 ---
        is_4h_established = (
            rsi_4h_value is not None and rsi_4h_value >= self._rsi_4h_max
        )

        # --- BB ---
        bb_u_s, bb_m_s, bb_l_s = self._calc_bbands(
            df["close"], self._bb_period, self._bb_std
        )
        bb_upper  = self._last_valid(bb_u_s)
        bb_middle = self._last_valid(bb_m_s)
        bb_lower  = self._last_valid(bb_l_s)
        is_above_bb = bb_upper is not None and current_price > bb_upper

        # --- 出来高トレンド ---
        vol_trend, vol_ratio = self._calc_volume_trend(df["volume"])
        is_exhaustion = vol_trend != VOL_TREND_RISING  # 増加中でなければ OK

        # --- ATR ---
        atr_series = self._calc_atr(df, self._atr_period)
        atr_value  = self._last_valid(atr_series)
        atr_pct    = (atr_value / current_price * 100) if atr_value else None

        # --- 総合判定 + 却下理由収集 ---
        reject_reasons: list[str] = []
        if not is_rsi_ob:
            reject_reasons.append(f"RSI {rsi_value:.1f} < {self._rsi_overbought:.0f}"
                                  if rsi_value is not None else "RSI n/a")
        if not is_above_bb:
            reject_reasons.append("price <= BB upper")
        if self._use_volume_filter and not is_exhaustion:
            reject_reasons.append(f"volume RISING (×{vol_ratio:.2f})")
        if self._use_4h_filter and is_4h_established:
            reject_reasons.append(f"4h RSI {rsi_4h_value:.1f} >= {self._rsi_4h_max:.0f}")

        is_confirmed = len(reject_reasons) == 0

        return AnalysisResult(
            symbol=candidate.symbol,
            price=current_price,
            change_1h_pct=candidate.change_1h_pct,
            relative_strength_pct=candidate.relative_strength_pct,
            volume_24h_usdt=candidate.volume_24h_usdt,
            rsi=rsi_value,
            is_rsi_overbought=is_rsi_ob,
            rsi_4h=rsi_4h_value,
            is_4h_trend_established=is_4h_established,
            bb_upper=bb_upper,
            bb_middle=bb_middle,
            bb_lower=bb_lower,
            is_above_bb_upper=is_above_bb,
            volume_trend=vol_trend,
            volume_trend_ratio=vol_ratio,
            is_volume_exhaustion=is_exhaustion,
            atr=atr_value,
            atr_pct=atr_pct,
            is_confirmed_signal=is_confirmed,
            reject_reasons=reject_reasons,
        )

    # ------------------------------------------------------------------
    # Indicator Calculations
    # ------------------------------------------------------------------

    @staticmethod
    def _last_valid(series: pd.Series | None) -> float | None:
        if series is None or series.empty:
            return None
        valid = series.dropna()
        if valid.empty:
            return None
        return float(valid.iloc[-1])

    @staticmethod
    def _calc_rsi(close: pd.Series, period: int) -> pd.Series:
        """Wilder 平滑化の RSI。"""
        delta = close.diff()
        gain  = delta.clip(lower=0)
        loss  = -delta.clip(upper=0)
        avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
        avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
        rs = avg_gain / avg_loss.replace(0, float("nan"))
        return 100 - (100 / (1 + rs))

    @staticmethod
    def _calc_bbands(
        close: pd.Series, period: int, std_mult: float
    ) -> tuple[pd.Series, pd.Series, pd.Series]:
        middle = close.rolling(period).mean()
        std    = close.rolling(period).std(ddof=0)
        return middle + std_mult * std, middle, middle - std_mult * std

    def _calc_volume_trend(self, volume: pd.Series) -> tuple[str, float]:
        """直近足の出来高 / 過去 N 足の平均出来高 の比率を計算する。

        比率が
            >= VOLUME_RISING_RATIO   → RISING   (出来高増加 = トレンド継続)
            <= VOLUME_DECLINING_RATIO → DECLINING (出来高減少 = 疲弊)
            それ以外                 → FLAT
        """
        if len(volume) < self._vol_lookback + 1:
            return VOL_TREND_FLAT, 1.0

        latest  = float(volume.iloc[-1])
        history = volume.iloc[-(self._vol_lookback + 1):-1]  # 直近足を除く
        avg     = float(history.mean()) if len(history) else 0.0

        if avg <= 0:
            return VOL_TREND_FLAT, 1.0

        ratio = latest / avg
        if ratio >= self._vol_rising_ratio:
            return VOL_TREND_RISING, ratio
        if ratio <= self._vol_declining_ratio:
            return VOL_TREND_DECLINING, ratio
        return VOL_TREND_FLAT, ratio

    @staticmethod
    def _calc_atr(df: pd.DataFrame, period: int) -> pd.Series:
        """ATR (Wilder)。True Range の EWM 平均。"""
        high  = df["high"]
        low   = df["low"]
        close = df["close"]
        prev_close = close.shift(1)

        tr = pd.concat(
            [
                high - low,
                (high - prev_close).abs(),
                (low  - prev_close).abs(),
            ],
            axis=1,
        ).max(axis=1)

        return tr.ewm(com=period - 1, min_periods=period).mean()

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------

    def _log_result(self, result: AnalysisResult) -> None:
        """分析結果をログに出力する。"""
        signal_mark = "[CONFIRMED]" if result.is_confirmed_signal else "[  pass   ]"
        rsi_4h_str  = f"{result.rsi_4h:.1f}" if result.rsi_4h is not None else "n/a"
        atr_str     = f"{result.atr_pct:.2f}%" if result.atr_pct is not None else "n/a"
        logger.info(
            "%s %s | price=%.6g 1h=+%.2f%% RSI=%.1f(%s) BB=%s vol=%s(×%.2f) 4hRSI=%s ATR=%s",
            signal_mark,
            result.symbol,
            result.price,
            result.change_1h_pct,
            result.rsi if result.rsi is not None else float("nan"),
            "OB" if result.is_rsi_overbought else "ok",
            "BREAK" if result.is_above_bb_upper else "  ok ",
            result.volume_trend,
            result.volume_trend_ratio,
            rsi_4h_str,
            atr_str,
        )
        if result.reject_reasons:
            logger.info("    reject: %s", ", ".join(result.reject_reasons))
