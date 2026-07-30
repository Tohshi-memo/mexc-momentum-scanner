"""
core/analyzer.py
テクニカル指標 (RSI, ボリンジャーバンド, ATR, 出来高トレンド, 4h RSI) と判定

pandas のみで実装しているため外部の TA ライブラリへの依存なし。

STRICT v2 (データ駆動で 2026-04 に見直し):
  - 4h RSI < RSI_4H_MAX: 『未過熱』の新鮮な急騰を狙う (核フィルター)
  - ATR:                 SL 幅をボラティリティに応じて自動調整

旧 STRICT v1 で使っていた RSI(1h) ≥ 70 / BB break / Volume NOT RISING は
シャドウ集計で期待値がフラット〜マイナスだったため撤廃。代わりに Volume
RISING や ATR% を live_filter.py の tier 判定に活用する。
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
    is_4h_overheated: bool  # 4h RSI < RSI_4H_MAX → 未過熱 (STRICT v2 の核)

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

    # スイング安値 (フィボナッチ・エクステンション計算用)
    # 直近 10 本の 1h 足安値の最小値（急騰足は除く）
    swing_low_1h: float | None

    # ファンディングレート (記録のみ。フィルターとしては未使用)
    # 正値 = ロングがショートに支払う (強気相場) → ショートに有利
    # 負値 = ショートがロングに支払う (弱気相場) → ショートに不利な可能性
    funding_rate: float | None  # %表記 (0.01 = 0.01%)

    # OBV ダイバージェンス (記録のみ。フィルターとしては未使用)
    # BEARISH_DIV: 価格↑ OBV↓ → 分配フェーズ (ショート根拠)
    # BULLISH_DIV: 価格↓ OBV↑ → 蓄積フェーズ
    # NONE:        ダイバージェンスなし
    obv_divergence: str | None  # "BEARISH_DIV" / "BULLISH_DIV" / "NONE"

    # オープンインタレスト (記録のみ。フィルターとしては未使用)
    # 価格↑ OI↑ = 新規ロング増加 → 反転リスク大
    open_interest_usd: float | None   # OI の USDT 建て総額
    oi_change_pct:     float | None   # 直近1h OI 変化率 (%)

    # ロング/ショート比率 (記録のみ。フィルターとしては未使用)
    # > 1.0 = ロングが多い → ショートに有利な環境
    long_short_ratio: float | None

    # 価格行動の質 (記録のみ。フィルターとしては未使用)
    # 上ヒゲ比率: (high - max(open,close)) / (high - low)
    # 1.0 に近いほど上ヒゲが長い = 売り圧力が強い
    upper_wick_ratio_1h: float | None  # 直前完成1h足の上ヒゲ比率

    # 連続陽線数: 検出直前に何本連続で陽線 (close > open) が続いたか
    # 多いほど一方的な上昇 = 過熱感
    consecutive_green_1h: int | None   # 1h足の連続陽線数
    consecutive_green_4h: int | None   # 4h足の連続陽線数

    # 追加パッシブ指標 (記録のみ。フィルターとしては未使用)
    # BB バンド幅 %: (upper - lower) / middle × 100
    # 高いほどボラ大。スクイーズ直後に爆発力が大きい傾向。
    bb_width_pct: float | None

    # 20MA 乖離率 (%): (price - MA20) / MA20 × 100
    # 正値 = 上方乖離。大きいほど平均回帰リスクが高い。
    # ※ BB 中心線 (bb_middle) が 20MA なのでそのまま流用。
    ma20_deviation_pct: float | None

    # ローソク足実体比率: |close - open| / (high - low)
    # 1.0 に近い = 実体が大きく方向性が明確。0 に近い = ヒゲばかり。
    candle_body_ratio: float | None

    # 15分足 RSI(14): 短期の過熱感。
    # 1h で検出された急騰が 15m 視点でも過熱しているかを確認。
    rsi_15m: float | None

    # 日足の方向: 直前完成1d足の方向。マクロトレンドとの一致/逆行を記録。
    # "GREEN" = close > open  "RED" = close < open  "DOJI" = ≈ フラット
    daily_direction: str | None

    # 総合判定
    is_confirmed_signal: bool
    reject_reasons: list[str] # 却下理由（デバッグ/ログ用）

    # この判定に使った最新の確定 1h 足。Live 注文の冪等キーに使う。
    # 形成中の足や現在時刻を使うと再実行時に別注文になり得るため、
    # 必ず取引所 OHLCV の確定足時刻を保持する。
    signal_candle_at: str | None = None


class TechnicalAnalyzer:
    """抽出された急騰候補銘柄に対してテクニカル分析を行う。

    STRICT v2 (is_confirmed_signal) の条件:
        - 4h RSI < RSI_4H_MAX (default: 65) → 『未過熱』の新鮮な急騰
          (shadow n=193 exp +0.94% の唯一の勝ちフィルター)

    RSI(1h) / BB / Volume はすべての候補で計算するが、confirmed の
    ゲートには使わない (データで有意差なし〜逆効果)。block zone や
    tier 判定は core/live_filter.py が担当する。
    """

    def __init__(self, client: MEXCClient) -> None:
        self._client = client

        self._rsi_period:     int   = int(os.getenv("RSI_PERIOD", "14"))
        self._rsi_overbought: float = float(os.getenv("RSI_OVERBOUGHT", "70"))
        self._bb_period:      int   = int(os.getenv("BB_PERIOD", "20"))
        self._bb_std:         float = float(os.getenv("BB_STD", "2.0"))
        self._timeframe:      str   = os.getenv("ANALYSIS_TIMEFRAME", "1h")
        self._ohlcv_limit:    int   = int(os.getenv("OHLCV_LIMIT", "100"))

        # 損失低減フィルター
        # 4h RSI は『未過熱』を要求する (< 閾値) — シャドウ集計 n=193 exp +0.94%
        self._rsi_4h_max:         float = float(os.getenv("RSI_4H_MAX", "65"))
        self._vol_lookback:       int   = int(os.getenv("VOLUME_LOOKBACK", "20"))
        self._vol_rising_ratio:   float = float(os.getenv("VOLUME_RISING_RATIO", "1.8"))
        self._vol_declining_ratio:float = float(os.getenv("VOLUME_DECLINING_RATIO", "0.8"))
        self._atr_period:         int   = int(os.getenv("ATR_PERIOD", "14"))
        self._use_4h_filter:      bool  = os.getenv("USE_4H_FILTER", "true").lower() != "false"

        logger.debug(
            "TechnicalAnalyzer | RSI(%d) OB=%.0f BB(%d,%.1fσ) 4h<%s",
            self._rsi_period, self._rsi_overbought,
            self._bb_period, self._bb_std,
            self._rsi_4h_max,
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

            # 4h RSI + DataFrame をマルチタイムフレーム確認用に取得
            rsi_4h_value: float | None = None
            df_4h: pd.DataFrame | None = None
            if self._use_4h_filter:
                rsi_4h_value, df_4h = self._fetch_4h_data(candidate.symbol)
            else:
                _, df_4h = self._fetch_4h_data(candidate.symbol)

            # ファンディングレートを取得 (記録のみ・失敗しても解析継続)
            funding_rate: float | None = self._client.fetch_funding_rate(candidate.symbol)

            # OI・ロングショート比率を取得 (記録のみ・失敗しても解析継続)
            oi_usd, oi_change = self._client.fetch_open_interest(candidate.symbol)
            ls_ratio = self._client.fetch_long_short_ratio(candidate.symbol)

            # 15m RSI を取得 (記録のみ)
            rsi_15m = self._fetch_rsi_for_timeframe(candidate.symbol, "15m")

            # 日足の方向を取得 (記録のみ)
            daily_dir = self._fetch_daily_direction(candidate.symbol)

            return self._compute_indicators(
                candidate, df, rsi_4h_value, df_4h,
                funding_rate, oi_usd, oi_change, ls_ratio,
                rsi_15m=rsi_15m,
                daily_direction=daily_dir,
            )

        except Exception as e:
            logger.error("Analysis failed for %s: %s", candidate.symbol, e)
            return None

    def _fetch_4h_data(self, symbol: str) -> tuple[float | None, pd.DataFrame | None]:
        """4h 足の OHLCV を取得して RSI と DataFrame を返す。失敗時は (None, None)。"""
        try:
            ohlcv_4h = self._client.fetch_ohlcv(
                symbol, timeframe="4h", limit=self._rsi_period + 30
            )
            if not ohlcv_4h or len(ohlcv_4h) < self._rsi_period + 1:
                return None, None
            df_4h = self._build_dataframe(ohlcv_4h)
            rsi_series = self._calc_rsi(df_4h["close"], self._rsi_period)
            return self._last_valid(rsi_series), df_4h
        except Exception as e:
            logger.debug("4h data fetch failed for %s: %s", symbol, e)
            return None, None

    def _fetch_rsi_for_timeframe(self, symbol: str, timeframe: str) -> float | None:
        """指定タイムフレームの RSI(14) を取得する。失敗時は None。"""
        try:
            ohlcv = self._client.fetch_ohlcv(
                symbol, timeframe=timeframe, limit=self._rsi_period + 10
            )
            if not ohlcv or len(ohlcv) < self._rsi_period + 1:
                return None
            df = self._build_dataframe(ohlcv)
            rsi_series = self._calc_rsi(df["close"], self._rsi_period)
            return self._last_valid(rsi_series)
        except Exception as e:
            logger.debug("%s RSI fetch failed for %s: %s", timeframe, symbol, e)
            return None

    def _fetch_daily_direction(self, symbol: str) -> str | None:
        """直前完成1d足の方向を返す。

        Returns:
            "GREEN" = close > open (陽線)
            "RED"   = close < open (陰線)
            "DOJI"  = |close - open| / open < 0.1% (十字線)
            None    = データ取得失敗
        """
        try:
            ohlcv = self._client.fetch_ohlcv(symbol, timeframe="1d", limit=3)
            if not ohlcv or len(ohlcv) < 2:
                return None
            df = self._build_dataframe(ohlcv)
            # iloc[-2] = 直前完成足 (最新足はまだ形成中)
            row = df.iloc[-2]
            op    = float(row["open"])
            close = float(row["close"])
            if op <= 0:
                return None
            diff_pct = abs(close - op) / op * 100
            if diff_pct < 0.1:
                return "DOJI"
            return "GREEN" if close > op else "RED"
        except Exception as e:
            logger.debug("daily direction fetch failed for %s: %s", symbol, e)
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
        df_4h: pd.DataFrame | None = None,
        funding_rate: float | None = None,
        open_interest_usd: float | None = None,
        oi_change_pct: float | None = None,
        long_short_ratio: float | None = None,
        rsi_15m: float | None = None,
        daily_direction: str | None = None,
    ) -> AnalysisResult:
        """全指標を計算し AnalysisResult を組み立てる。"""
        current_price: float = candidate.price

        # --- RSI ---
        rsi_series = self._calc_rsi(df["close"], self._rsi_period)
        rsi_value  = self._last_valid(rsi_series)
        is_rsi_ob  = rsi_value is not None and rsi_value >= self._rsi_overbought

        # --- 4h 『未過熱』判定 (新鮮な急騰 = 4h RSI が低い) ---
        # データ分析: 4h RSI < 65 の n=193 で期待値 +0.94% (STRICT v2 の核)
        is_4h_oh = (
            rsi_4h_value is not None and rsi_4h_value < self._rsi_4h_max
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

        # --- スイング安値 (フィボナッチ用) ---
        # 直近10本を除外した範囲…ではなく、「急騰足の直前10本の安値」を使う。
        # iloc[-11:-1] = 最新足の1本前から10本分の安値
        swing_low_1h: float | None = None
        if len(df) >= 11:
            swing_low_1h = float(df["low"].iloc[-11:-1].min())

        # --- OBV ダイバージェンス ---
        obv_divergence = self._calc_obv_divergence(df["close"], df["volume"])

        # --- 価格行動の質 ---
        # 上ヒゲ比率: 直前完成足 (iloc[-2]) を使う (最新足はまだ形成中)
        upper_wick_ratio_1h = self._calc_upper_wick_ratio(df, idx=-2)
        consecutive_green_1h = self._calc_consecutive_green(df)
        consecutive_green_4h = self._calc_consecutive_green(df_4h) if df_4h is not None else None

        # --- 追加パッシブ指標 ---
        # BB バンド幅 %: (upper - lower) / middle × 100
        bb_width_pct: float | None = None
        if bb_upper is not None and bb_lower is not None and bb_middle and bb_middle > 0:
            bb_width_pct = round((bb_upper - bb_lower) / bb_middle * 100, 4)

        # 20MA 乖離率: bb_middle が 20MA なのでそのまま流用
        ma20_deviation_pct: float | None = None
        if bb_middle and bb_middle > 0:
            ma20_deviation_pct = round((current_price - bb_middle) / bb_middle * 100, 4)

        # ローソク足実体比率 (直前完成1h足)
        candle_body_ratio = self._calc_candle_body_ratio(df, idx=-2)
        signal_candle_at = (
            df.index[-2].isoformat()
            if len(df) >= 2 and df.index[-2].tzinfo is not None
            else None
        )

        # --- 総合判定 + 却下理由収集 (STRICT v2) ---
        # データ分析結果 (data/experiment_report.md):
        #   - 4h RSI < 65: n=193 exp +0.94% ← 唯一の勝ちフィルター、必須
        #   - RSI(1h) ≥ 70: データでは無効 (exp -0.35%) → 情報表示のみ
        #   - BB ブレイク: データで無効 (exp -0.24%) → 除外
        #   - Volume NOT RISING: RISING と combined で +2.46% → 除外
        # is_confirmed_signal は『4h 未過熱』のみをゲート条件とし、
        # 残りは live_filter が tier 判定 + block zone で絞り込む。
        reject_reasons: list[str] = []
        if self._use_4h_filter and not is_4h_oh:
            reject_reasons.append(
                f"4h RSI {rsi_4h_value:.1f} >= {self._rsi_4h_max:.0f}"
                if rsi_4h_value is not None else "4h RSI n/a"
            )

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
            is_4h_overheated=is_4h_oh,
            bb_upper=bb_upper,
            bb_middle=bb_middle,
            bb_lower=bb_lower,
            is_above_bb_upper=is_above_bb,
            volume_trend=vol_trend,
            volume_trend_ratio=vol_ratio,
            is_volume_exhaustion=is_exhaustion,
            atr=atr_value,
            atr_pct=atr_pct,
            swing_low_1h=swing_low_1h,
            funding_rate=funding_rate,
            obv_divergence=obv_divergence,
            open_interest_usd=open_interest_usd,
            oi_change_pct=oi_change_pct,
            long_short_ratio=long_short_ratio,
            upper_wick_ratio_1h=upper_wick_ratio_1h,
            consecutive_green_1h=consecutive_green_1h,
            consecutive_green_4h=consecutive_green_4h,
            bb_width_pct=bb_width_pct,
            ma20_deviation_pct=ma20_deviation_pct,
            candle_body_ratio=candle_body_ratio,
            rsi_15m=rsi_15m,
            daily_direction=daily_direction,
            is_confirmed_signal=is_confirmed,
            reject_reasons=reject_reasons,
            signal_candle_at=signal_candle_at,
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

    @staticmethod
    def _calc_obv_divergence(
        close: pd.Series,
        volume: pd.Series,
        lookback: int = 14,
    ) -> str | None:
        """OBV と価格のダイバージェンスを検出する。

        OBV = 前日比で上昇なら +volume、下落なら -volume の累積和。
        直近 lookback 本の価格トレンドと OBV トレンドを線形回帰の傾きで比較し、
        方向が逆であればダイバージェンスと判定する。

        Returns:
            "BEARISH_DIV" : 価格↑ OBV↓ (分配フェーズ = ショート根拠)
            "BULLISH_DIV" : 価格↓ OBV↑ (蓄積フェーズ)
            "NONE"        : ダイバージェンスなし
            None          : データ不足
        """
        if len(close) < lookback + 1:
            return None

        # OBV 計算
        direction = close.diff().apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
        obv = (direction * volume).cumsum()

        # 直近 lookback 本の傾き (線形回帰の代わりに終値 - 始値で近似)
        price_window = close.iloc[-lookback:]
        obv_window   = obv.iloc[-lookback:]

        price_slope = float(price_window.iloc[-1] - price_window.iloc[0])
        obv_slope   = float(obv_window.iloc[-1]   - obv_window.iloc[0])

        # ノイズ除去: 価格変化が 0.5% 未満なら判定しない
        price_chg_pct = abs(price_slope) / float(price_window.iloc[0]) * 100
        if price_chg_pct < 0.5:
            return "NONE"

        price_up = price_slope > 0
        obv_up   = obv_slope   > 0

        if price_up and not obv_up:
            return "BEARISH_DIV"
        if not price_up and obv_up:
            return "BULLISH_DIV"
        return "NONE"

    # ------------------------------------------------------------------
    # Logging
    @staticmethod
    def _calc_upper_wick_ratio(df: pd.DataFrame, idx: int = -2) -> float | None:
        """指定インデックスの足の上ヒゲ比率を返す。

        上ヒゲ比率 = (high - max(open, close)) / (high - low)
        1.0 に近いほど上ヒゲが長い (売り圧力が強い)。

        idx=-2: 直前完成足 (最新足はまだ形成中のため除外)
        """
        try:
            if len(df) < abs(idx):
                return None
            row = df.iloc[idx]
            high  = float(row["high"])
            low   = float(row["low"])
            op    = float(row["open"])
            close = float(row["close"])
            candle_range = high - low
            if candle_range <= 0:
                return None
            upper_wick = high - max(op, close)
            return round(upper_wick / candle_range, 4)
        except Exception:
            return None

    @staticmethod
    def _calc_candle_body_ratio(df: pd.DataFrame, idx: int = -2) -> float | None:
        """指定インデックスの足の実体比率を返す。

        実体比率 = |close - open| / (high - low)
        1.0 に近いほど実体が大きく方向性が明確。0 に近いほどヒゲ主体。

        idx=-2: 直前完成足 (最新足はまだ形成中のため除外)
        """
        try:
            if len(df) < abs(idx):
                return None
            row = df.iloc[idx]
            high  = float(row["high"])
            low   = float(row["low"])
            op    = float(row["open"])
            close = float(row["close"])
            candle_range = high - low
            if candle_range <= 0:
                return None
            body = abs(close - op)
            return round(body / candle_range, 4)
        except Exception:
            return None

    @staticmethod
    def _calc_consecutive_green(df: pd.DataFrame | None) -> int | None:
        """直前完成足から遡って連続陽線数を返す。

        陽線 = close > open。最新足は形成中のため除外 (iloc[-2] から遡る)。
        """
        if df is None or len(df) < 2:
            return None
        count = 0
        # iloc[-2] から遡る（最新足除外）
        for i in range(len(df) - 2, -1, -1):
            row = df.iloc[i]
            if float(row["close"]) > float(row["open"]):
                count += 1
            else:
                break
        return count

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
