"""
core/analyzer.py
テクニカル指標 (RSI, ボリンジャーバンド) の計算と判定

pandas のみで実装しているため外部の TA ライブラリへの依存なし。
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass

import pandas as pd

from core.scanner import SurgeCandidate
from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)


@dataclass
class AnalysisResult:
    """単一銘柄のテクニカル分析結果を表すデータクラス。"""

    symbol: str
    price: float
    change_1h_pct: float
    volume_24h_usdt: float

    # RSI
    rsi: float | None
    is_rsi_overbought: bool  # RSI >= RSI_OVERBOUGHT (default 75)

    # ボリンジャーバンド
    bb_upper: float | None
    bb_middle: float | None
    bb_lower: float | None
    is_above_bb_upper: bool  # 現在価格 > BB上限(2σ)

    # 総合判定
    is_confirmed_signal: bool  # RSI 過買い AND BB上抜け の両方を満たす場合


class TechnicalAnalyzer:
    """抽出された急騰候補銘柄に対してテクニカル分析を行う。

    判定基準:
        - RSI(14) >= RSI_OVERBOUGHT (default: 75) → 「買われすぎ」状態
        - 現在価格 > ボリンジャーバンド上限(2σ) → 「バンドブレイク」状態
        - 上記 AND 条件 → 擬似ショートの有力シグナルとして確認
    """

    def __init__(self, client: MEXCClient) -> None:
        self._client = client

        self._rsi_period: int = int(os.getenv("RSI_PERIOD", "14"))
        self._rsi_overbought: float = float(os.getenv("RSI_OVERBOUGHT", "75"))
        self._bb_period: int = int(os.getenv("BB_PERIOD", "20"))
        self._bb_std: float = float(os.getenv("BB_STD", "2.0"))
        self._timeframe: str = os.getenv("ANALYSIS_TIMEFRAME", "1h")
        self._ohlcv_limit: int = int(os.getenv("OHLCV_LIMIT", "100"))

        logger.debug(
            "TechnicalAnalyzer initialized | RSI(%d) overbought=%.0f "
            "BB(%d, %.1fσ) timeframe=%s",
            self._rsi_period,
            self._rsi_overbought,
            self._bb_period,
            self._bb_std,
            self._timeframe,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze_candidates(
        self, candidates: list[SurgeCandidate]
    ) -> list[AnalysisResult]:
        """急騰候補リストをテクニカル分析し、確認済みシグナルを返す。

        Args:
            candidates: MarketScanner が抽出した SurgeCandidate リスト
        Returns:
            AnalysisResult のリスト（分析失敗銘柄は除外）
        """
        results: list[AnalysisResult] = []

        for candidate in candidates:
            result = self._analyze_single(candidate)
            if result is not None:
                results.append(result)
                self._log_result(result)

        confirmed = [r for r in results if r.is_confirmed_signal]
        logger.info(
            "Analysis complete | %d analyzed, %d confirmed signal(s).",
            len(results),
            len(confirmed),
        )
        return results

    # ------------------------------------------------------------------
    # Single Symbol Analysis
    # ------------------------------------------------------------------

    def _analyze_single(self, candidate: SurgeCandidate) -> AnalysisResult | None:
        """1銘柄の OHLCV を取得し RSI・BB を計算して返す。

        Args:
            candidate: 分析対象の急騰候補
        Returns:
            AnalysisResult または None（データ取得・計算失敗時）
        """
        try:
            ohlcv = self._client.fetch_ohlcv(
                candidate.symbol,
                timeframe=self._timeframe,
                limit=self._ohlcv_limit,
            )
            if not ohlcv or len(ohlcv) < max(self._rsi_period, self._bb_period) + 5:
                logger.warning(
                    "Insufficient OHLCV data for %s (%d bars).",
                    candidate.symbol,
                    len(ohlcv) if ohlcv else 0,
                )
                return None

            df = self._build_dataframe(ohlcv)
            return self._compute_indicators(candidate, df)

        except Exception as e:
            logger.error("Analysis failed for %s: %s", candidate.symbol, e)
            return None

    def _build_dataframe(self, ohlcv: list[list[float]]) -> pd.DataFrame:
        """ccxt OHLCV リストを pandas DataFrame に変換する。

        Args:
            ohlcv: [[timestamp, open, high, low, close, volume], ...]
        Returns:
            カラム [open, high, low, close, volume] を持つ DataFrame
        """
        df = pd.DataFrame(
            ohlcv,
            columns=["timestamp", "open", "high", "low", "close", "volume"],
        )
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
        df.set_index("timestamp", inplace=True)
        df = df.astype(float)
        return df

    def _compute_indicators(
        self, candidate: SurgeCandidate, df: pd.DataFrame
    ) -> AnalysisResult:
        """RSI と ボリンジャーバンドを計算し AnalysisResult を組み立てる。

        Args:
            candidate: 対象銘柄の基本情報
            df: OHLCV DataFrame
        Returns:
            計算済みの AnalysisResult
        """
        current_price: float = candidate.price

        # --- RSI ---
        rsi_series: pd.Series = self._calc_rsi(df["close"], self._rsi_period)
        rsi_value: float | None = self._last_valid(rsi_series)
        is_rsi_overbought: bool = (
            rsi_value is not None and rsi_value >= self._rsi_overbought
        )

        # --- ボリンジャーバンド ---
        bb_upper_s, bb_middle_s, bb_lower_s = self._calc_bbands(
            df["close"], self._bb_period, self._bb_std
        )
        bb_upper = self._last_valid(bb_upper_s)
        bb_middle = self._last_valid(bb_middle_s)
        bb_lower = self._last_valid(bb_lower_s)
        is_above_bb_upper: bool = (
            bb_upper is not None and current_price > bb_upper
        )

        is_confirmed = is_rsi_overbought and is_above_bb_upper

        return AnalysisResult(
            symbol=candidate.symbol,
            price=current_price,
            change_1h_pct=candidate.change_1h_pct,
            volume_24h_usdt=candidate.volume_24h_usdt,
            rsi=rsi_value,
            is_rsi_overbought=is_rsi_overbought,
            bb_upper=bb_upper,
            bb_middle=bb_middle,
            bb_lower=bb_lower,
            is_above_bb_upper=is_above_bb_upper,
            is_confirmed_signal=is_confirmed,
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _last_valid(series: pd.Series | None) -> float | None:
        """pandas Series の最後の有効な (NaN でない) 値を返す。"""
        if series is None or series.empty:
            return None
        valid = series.dropna()
        if valid.empty:
            return None
        return float(valid.iloc[-1])

    @staticmethod
    def _calc_rsi(close: pd.Series, period: int) -> pd.Series:
        """Wilder の平滑移動平均を使った RSI を計算する。

        RSI = 100 - 100 / (1 + RS)
        RS  = EWM平均上昇幅 / EWM平均下落幅  (com = period - 1)
        """
        delta = close.diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
        avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
        rs = avg_gain / avg_loss.replace(0, float("nan"))
        return 100 - (100 / (1 + rs))

    @staticmethod
    def _calc_bbands(
        close: pd.Series, period: int, std_mult: float
    ) -> tuple[pd.Series, pd.Series, pd.Series]:
        """ボリンジャーバンドを計算する。

        Returns:
            (upper, middle, lower) の Series タプル
        """
        middle = close.rolling(period).mean()
        std = close.rolling(period).std(ddof=0)
        upper = middle + std_mult * std
        lower = middle - std_mult * std
        return upper, middle, lower

    def _log_result(self, result: AnalysisResult) -> None:
        """分析結果をログに出力する。"""
        signal_mark = "[CONFIRMED]" if result.is_confirmed_signal else "[  pass   ]"
        logger.info(
            "%s %s | price=%.6f 1h=+%.2f%% RSI=%.1f(%s) BB_upper=%.6f(%s)",
            signal_mark,
            result.symbol,
            result.price,
            result.change_1h_pct,
            result.rsi if result.rsi is not None else float("nan"),
            "OB" if result.is_rsi_overbought else "ok",
            result.bb_upper if result.bb_upper is not None else float("nan"),
            "BREAK" if result.is_above_bb_upper else "ok",
        )
