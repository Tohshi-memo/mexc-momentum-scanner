"""
core/live_filter.py
実トレード用フィルター (Tier 分け方式)

現行 STRICT (RSI≥70 & 4h≥65 & ¬RISING) は n=311 で期待値 -0.18% と
シャドウ集計で全件 (-0.19%) に対する優位性を示せていない。
本モジュールは data/experiment_report.md の分析結果を反映し、
**期待値プラスが統計的に確認された組み合わせのみ** を実トレードに昇格させる。

Tier 定義 (実トレード時はこの順に優先度を評価):
    S: 4h RSI < 65 & Volume RISING                 n=32  exp +2.46% WR 50.0%
    A: 4h RSI < 65 & ATR ≥ 11%                     n=53  exp +0.98% WR 41.5%
    B: 4h RSI < 65 (単独)                          n=193 exp +0.94% WR 38.3%
  (いずれも RSI(1h) ≥ 70 は前提)

Tier S/A を優先し、埋まらなければ Tier B をフォールバックとして使う運用を想定。
追加の『ブースター』条件 (Funding≥0.1%, 日足RED, BEARISH_DIV 等) が
重なるほど確信度が上がる設計。

Block リスト (統計的に劣るゾーン — 強制却下):
    - 連続陽線 1h ≥ 8                        exp -0.70%
    - BB 幅 15〜20%                          exp -1.17%
    - 20MA 乖離 5〜10%                       exp -1.13%
    - ATR 5〜7%                              exp -0.55%
    - 上ヒゲ比率 ≥ 0.6 (究極反転ヒゲ以外)    exp -0.62%

使用例:
    filt = LiveTradeFilter()
    decision = filt.evaluate(result, regime=regime, stats=stats)
    if decision.passed:
        plan = strategy.build(result, decision, account=account)
        executor.execute(plan)
"""
from __future__ import annotations

import logging
import math
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from core.analyzer import AnalysisResult, VOL_TREND_RISING
from core.live_policy import live_policy_fingerprint

if TYPE_CHECKING:
    from core.stats import StatsManager

logger = logging.getLogger(__name__)


# ─── Tier 定義 ────────────────────────────────────────────────────────
TIER_S = "S"   # 最強確信 (4h<65 & RISING)
TIER_A = "A"   # 高確信   (4h<65 & ATR≥11%)
TIER_B = "B"   # 標準確信 (4h<65 単独)
TIER_REJECT = "REJECT"
DATA_DRIVEN_MARKET_SHORT_ID = "market_short_daily_red_green_3_4_v2"


@dataclass
class LiveFilterDecision:
    """実トレード可否判定の結果。"""

    passed: bool
    tier: str                    # S / A / B / REJECT
    reasons: list[str] = field(default_factory=list)
    block_reasons: list[str] = field(default_factory=list)
    boosters: list[str] = field(default_factory=list)
    score: float = 0.0           # ブースター加点後の確信度スコア
    strategy_id: str = ""

    def summary(self) -> str:
        if not self.passed:
            return f"REJECT ({', '.join(self.block_reasons) or ', '.join(self.reasons)})"
        tag = f"tier={self.tier} score={self.score:.2f}"
        if self.boosters:
            tag += f" boost=[{', '.join(self.boosters)}]"
        return tag


class LiveTradeFilter:
    """AnalysisResult を実トレード可否に振り分ける。

    テクニカルアナライザー側で ``is_confirmed_signal`` は既に計算されているが、
    このクラスは **別途より厳しい** tier 判定を行う。confirmed でなくても
    データ上 tier S/A に該当するパターンは拾い、confirmed でも block
    条件に当たれば却下する。

    サーキットブレーカー / クールダウンは呼び出し側 (main.py) で既に判定
    されるため、このフィルターでは触れない。
    """

    def __init__(self) -> None:
        self._data_driven_market_short_v2: bool = (
            os.getenv("LIVE_DATA_DRIVEN_MARKET_SHORT_V2", "true").lower()
            != "false"
        )
        # ─── Tier gating thresholds (STRICT v2) ──────────────────────
        # LIVE_RSI_MIN: RSI(1h) ゲートは無効化がデフォルト (シャドウで効果なし)。
        # LIVE_ATR_HIGH: Tier A 昇格閾値は 9% (旧 11%)、サンプル増で判定安定化。
        self._rsi_min: float     = float(os.getenv("LIVE_RSI_MIN",     "0"))
        self._rsi_4h_max: float  = float(os.getenv("LIVE_RSI_4H_MAX",  "65"))
        self._atr_high: float    = float(os.getenv("LIVE_ATR_HIGH",    "9.0"))
        self._rel_strength_min: float = float(os.getenv("LIVE_REL_STRENGTH_MIN", "5.0"))

        # ─── Block (強制却下) thresholds ─────────────────────────────
        self._block_consec_green_1h: int   = int(os.getenv("BLOCK_CONSEC_GREEN_1H", "8"))
        self._block_bbw_lo: float          = float(os.getenv("BLOCK_BBW_LO",        "15.0"))
        self._block_bbw_hi: float          = float(os.getenv("BLOCK_BBW_HI",        "20.0"))
        self._block_ma_dev_lo: float       = float(os.getenv("BLOCK_MA_DEV_LO",     "5.0"))
        self._block_ma_dev_hi: float       = float(os.getenv("BLOCK_MA_DEV_HI",    "10.0"))
        self._block_atr_lo: float          = float(os.getenv("BLOCK_ATR_LO",        "5.0"))
        self._block_atr_hi: float          = float(os.getenv("BLOCK_ATR_HI",        "7.0"))
        self._block_wick_ratio: float      = float(os.getenv("BLOCK_WICK_RATIO",    "0.6"))

        # ─── Booster thresholds (加点のみ、却下には使わない) ─────────
        self._boost_funding: float         = float(os.getenv("BOOST_FUNDING_RATE", "0.10"))
        self._require_fundamental_pass: bool = (
            os.getenv("LIVE_REQUIRE_FUND_NON_AVOID", "true").lower() != "false"
        )
        self._allowed_fundamental: set[str] = {
            value.strip().upper()
            for value in os.getenv(
                "LIVE_ALLOWED_FUNDAMENTAL_CONVICTIONS",
                "HIGH,MEDIUM,UNKNOWN",
            ).split(",")
            if value.strip()
        }
        self._require_complete_technical: bool = (
            os.getenv("LIVE_REQUIRE_COMPLETE_TECHNICAL_DATA", "true").lower()
            != "false"
        )
        self._require_funding_data: bool = (
            os.getenv("LIVE_REQUIRE_FUNDING_DATA", "true").lower() != "false"
        )
        self._min_funding_rate_pct: float = float(
            os.getenv("LIVE_MIN_FUNDING_RATE_PCT", "-0.05")
        )
        self._signal_max_age_hours: float = float(
            os.getenv("LIVE_SIGNAL_MAX_AGE_HOURS", "3.0")
        )
        self._max_historical_spread_pct: float = float(
            os.getenv("LIVE_MAX_SPREAD_PCT", "0.10")
        )
        if (
            not math.isfinite(self._signal_max_age_hours)
            or self._signal_max_age_hours <= 0
        ):
            raise ValueError(
                "LIVE_SIGNAL_MAX_AGE_HOURS must be a finite positive number"
            )
        if (
            not math.isfinite(self._max_historical_spread_pct)
            or self._max_historical_spread_pct < 0
        ):
            raise ValueError(
                "LIVE_MAX_SPREAD_PCT must be finite and non-negative"
            )
        # 最新のフォワード集計では上ヒゲ>=0.6は負け条件ではなかったため、
        # 古い仮説を既定の強制blockには使わない。再検証時だけ明示的に有効化。
        self._block_upper_wick: bool = (
            os.getenv("LIVE_BLOCK_UPPER_WICK", "false").lower() == "true"
        )
        self._policy_fingerprint = live_policy_fingerprint()

        numeric_config = {
            "LIVE_RSI_MIN": self._rsi_min,
            "LIVE_RSI_4H_MAX": self._rsi_4h_max,
            "LIVE_ATR_HIGH": self._atr_high,
            "LIVE_REL_STRENGTH_MIN": self._rel_strength_min,
            "BLOCK_BBW_LO": self._block_bbw_lo,
            "BLOCK_BBW_HI": self._block_bbw_hi,
            "BLOCK_MA_DEV_LO": self._block_ma_dev_lo,
            "BLOCK_MA_DEV_HI": self._block_ma_dev_hi,
            "BLOCK_ATR_LO": self._block_atr_lo,
            "BLOCK_ATR_HI": self._block_atr_hi,
            "BLOCK_WICK_RATIO": self._block_wick_ratio,
            "BOOST_FUNDING_RATE": self._boost_funding,
            "LIVE_MIN_FUNDING_RATE_PCT": self._min_funding_rate_pct,
        }
        invalid_names = [
            name
            for name, value in numeric_config.items()
            if not math.isfinite(value)
        ]
        if invalid_names:
            raise ValueError(
                "Live filter config must be finite: "
                + ", ".join(invalid_names)
            )
        if self._block_consec_green_1h <= 0:
            raise ValueError("BLOCK_CONSEC_GREEN_1H must be positive")
        if not (
            self._block_bbw_lo < self._block_bbw_hi
            and self._block_ma_dev_lo < self._block_ma_dev_hi
            and self._block_atr_lo < self._block_atr_hi
        ):
            raise ValueError("Live filter block ranges must have lo < hi")
        if not 0 <= self._block_wick_ratio <= 1:
            raise ValueError("BLOCK_WICK_RATIO must be between 0 and 1")
        if not self._allowed_fundamental:
            raise ValueError(
                "LIVE_ALLOWED_FUNDAMENTAL_CONVICTIONS must not be empty"
            )

        logger.info(
            "LiveTradeFilter | RSI≥%.0f 4h<%.0f ATR_high=%.1f | "
            "blocks: green≥%d bbw=%.0f-%.0f ma_dev=%.0f-%.0f atr=%.0f-%.0f wick≥%.2f",
            self._rsi_min, self._rsi_4h_max, self._atr_high,
            self._block_consec_green_1h,
            self._block_bbw_lo, self._block_bbw_hi,
            self._block_ma_dev_lo, self._block_ma_dev_hi,
            self._block_atr_lo, self._block_atr_hi,
            self._block_wick_ratio,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def evaluate(
        self,
        result: AnalysisResult,
        *,
        regime: str = "UNKNOWN",
        stats: "StatsManager | None" = None,
        fundamental_conviction: str | None = None,
    ) -> LiveFilterDecision:
        """AnalysisResult を実トレード可否に振り分ける。

        Args:
            result: テクニカル分析結果。
            regime: BTC レジーム (BEARISH/STAGNANT/BULLISH)。
            stats: 直近成績 (必要なら regime 別の追加抑制に使用)。
            fundamental_conviction: ファンダ結果 (AVOID の場合は却下)。
        """
        if self._data_driven_market_short_v2:
            return self._evaluate_data_driven_market_short(
                result,
                fundamental_conviction=fundamental_conviction,
            )

        # ─── 前提条件 (全 tier 共通) ────────────────────────────────
        pre_reasons: list[str] = []

        signal_time_error = self._signal_candle_error(
            getattr(result, "signal_candle_at", None)
        )
        if signal_time_error:
            pre_reasons.append(signal_time_error)

        if not self._is_finite_number(result.rsi):
            pre_reasons.append("RSI(1h) n/a or non-finite")
        elif float(result.rsi) < self._rsi_min:
            pre_reasons.append(
                f"RSI(1h) {float(result.rsi):.1f} < {self._rsi_min:.0f}"
            )

        if not self._is_finite_number(result.rsi_4h):
            pre_reasons.append("4h RSI n/a or non-finite")

        if not self._is_finite_number(result.relative_strength_pct):
            pre_reasons.append("rel_strength n/a or non-finite")
        elif float(result.relative_strength_pct) < self._rel_strength_min:
            pre_reasons.append(
                f"rel_strength {float(result.relative_strength_pct):.1f} "
                f"< {self._rel_strength_min:.0f}"
            )

        if self._require_complete_technical:
            required_fields = {
                "ATR": result.atr_pct,
                "consec_green_1h": result.consecutive_green_1h,
                "BB width": result.bb_width_pct,
                "MA20 deviation": result.ma20_deviation_pct,
            }
            if self._block_upper_wick:
                required_fields["upper_wick"] = result.upper_wick_ratio_1h
            missing = [
                name
                for name, value in required_fields.items()
                if not self._is_finite_number(value)
            ]
            if not result.volume_trend:
                missing.append("volume_trend")
            if missing:
                pre_reasons.append(
                    "required technical data n/a: " + ", ".join(missing)
                )

        if self._require_funding_data:
            if not self._is_finite_number(result.funding_rate):
                pre_reasons.append("funding_rate n/a or non-finite")
            elif float(result.funding_rate) < self._min_funding_rate_pct:
                pre_reasons.append(
                    f"funding_rate {float(result.funding_rate):+.3f}% "
                    f"< {self._min_funding_rate_pct:+.3f}%"
                )

        if self._require_fundamental_pass:
            conviction = (fundamental_conviction or "UNKNOWN").upper()
            if conviction not in self._allowed_fundamental:
                pre_reasons.append(
                    f"fundamental={conviction} not in "
                    f"{sorted(self._allowed_fundamental)}"
                )

        if pre_reasons:
            return LiveFilterDecision(
                passed=False, tier=TIER_REJECT, reasons=pre_reasons,
            )

        # ─── Block 条件 (統計的に劣るゾーンを強制却下) ──────────────
        block = self._check_blocks(result)
        if block:
            return LiveFilterDecision(
                passed=False, tier=TIER_REJECT, block_reasons=block,
            )

        # ─── Tier 判定 ───────────────────────────────────────────────
        tier = self._classify_tier(result)
        if tier == TIER_REJECT:
            return LiveFilterDecision(
                passed=False, tier=TIER_REJECT,
                reasons=[
                    f"4h RSI {result.rsi_4h:.1f} ≥ {self._rsi_4h_max:.0f} "
                    "(no tier match)"
                ],
            )

        # ─── Booster 加点 (却下しないが確信度に寄与) ────────────────
        boosters, score = self._calc_boosters(result, regime)

        return LiveFilterDecision(
            passed=True, tier=tier, reasons=[],
            boosters=boosters, score=score,
        )

    def _evaluate_data_driven_market_short(
        self,
        result: AnalysisResult,
        *,
        fundamental_conviction: str | None,
    ) -> LiveFilterDecision:
        """Evaluate the OOS-reproduced MARKET-short setup.

        This deliberately does not reuse the old RSI/ATR tier blocks.  The
        joined shadow sample showed that those blocks removed the profitable
        live population.  Exchange-time spread, drift and depth checks remain
        in the independent live runner.
        """
        reasons: list[str] = []
        signal_time_error = self._signal_candle_error(
            getattr(result, "signal_candle_at", None)
        )
        if signal_time_error:
            reasons.append(signal_time_error)

        daily_direction = str(
            getattr(result, "daily_direction", "") or ""
        ).upper()
        consecutive_green = getattr(result, "consecutive_green_1h", None)
        funding_rate = getattr(result, "funding_rate", None)
        if not daily_direction:
            reasons.append("daily_direction n/a")
        if not self._is_finite_number(consecutive_green):
            reasons.append("consecutive_green_1h n/a or non-finite")
        if not self._is_finite_number(funding_rate):
            reasons.append("funding_rate n/a or non-finite")
        elif float(funding_rate) < self._min_funding_rate_pct:
            reasons.append(
                f"funding_rate {float(funding_rate):+.3f}% "
                f"< {self._min_funding_rate_pct:+.3f}%"
            )

        conviction = (fundamental_conviction or "UNKNOWN").upper()
        if conviction == "AVOID":
            reasons.append("fundamental=AVOID")
        if reasons:
            return LiveFilterDecision(
                passed=False,
                tier=TIER_REJECT,
                reasons=reasons,
                strategy_id=DATA_DRIVEN_MARKET_SHORT_ID,
            )

        setup_misses: list[str] = []
        if daily_direction != "RED":
            setup_misses.append(f"daily_direction={daily_direction} != RED")
        green_value = int(float(consecutive_green))
        if green_value not in (3, 4):
            setup_misses.append(
                f"consecutive_green_1h={green_value} not in [3,4]"
            )
        if setup_misses:
            return LiveFilterDecision(
                passed=False,
                tier=TIER_REJECT,
                block_reasons=setup_misses,
                strategy_id=DATA_DRIVEN_MARKET_SHORT_ID,
            )

        boosters = ["daily_RED", f"1h_green={green_value}"]
        if conviction in {"HIGH", "MEDIUM"}:
            boosters.append(f"fundamental_{conviction}")
        return LiveFilterDecision(
            passed=True,
            tier=TIER_S,
            boosters=boosters,
            score=0.0,
            strategy_id=DATA_DRIVEN_MARKET_SHORT_ID,
        )

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _signal_candle_error(self, raw_timestamp: object) -> str | None:
        if not isinstance(raw_timestamp, str) or not raw_timestamp.strip():
            return "signal_candle_at n/a"
        timestamp = raw_timestamp.strip()
        normalized = (
            f"{timestamp[:-1]}+00:00"
            if timestamp.endswith(("Z", "z"))
            else timestamp
        )
        try:
            parsed = datetime.fromisoformat(normalized)
        except ValueError:
            return "signal_candle_at invalid"
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            return "signal_candle_at has no timezone"

        age_hours = (
            datetime.now(timezone.utc) - parsed.astimezone(timezone.utc)
        ).total_seconds() / 3600
        if not math.isfinite(age_hours):
            return "signal_candle_at age non-finite"
        if age_hours < 0:
            return "signal_candle_at is in the future"
        if age_hours > self._signal_max_age_hours:
            return (
                f"signal_candle_at stale ({age_hours:.2f}h > "
                f"{self._signal_max_age_hours:.2f}h)"
            )
        return None

    def _check_blocks(self, r: AnalysisResult) -> list[str]:
        """Block 条件 (強制却下) に該当するかチェック。"""
        hits: list[str] = []

        if (
            r.consecutive_green_1h is not None
            and r.consecutive_green_1h >= self._block_consec_green_1h
        ):
            hits.append(
                f"consec_green_1h={r.consecutive_green_1h} ≥ {self._block_consec_green_1h}"
            )

        if (
            r.bb_width_pct is not None
            and self._block_bbw_lo <= r.bb_width_pct < self._block_bbw_hi
        ):
            hits.append(
                f"BB width {r.bb_width_pct:.1f}% in [{self._block_bbw_lo:.0f},"
                f"{self._block_bbw_hi:.0f})"
            )

        if (
            r.ma20_deviation_pct is not None
            and self._block_ma_dev_lo <= r.ma20_deviation_pct < self._block_ma_dev_hi
        ):
            hits.append(
                f"MA20 dev {r.ma20_deviation_pct:.1f}% in "
                f"[{self._block_ma_dev_lo:.0f},{self._block_ma_dev_hi:.0f})"
            )

        if (
            r.atr_pct is not None
            and self._block_atr_lo <= r.atr_pct < self._block_atr_hi
        ):
            hits.append(
                f"ATR {r.atr_pct:.1f}% in "
                f"[{self._block_atr_lo:.0f},{self._block_atr_hi:.0f})"
            )

        if (
            self._block_upper_wick
            and
            r.upper_wick_ratio_1h is not None
            and r.upper_wick_ratio_1h >= self._block_wick_ratio
        ):
            hits.append(
                f"upper_wick {r.upper_wick_ratio_1h:.2f} ≥ {self._block_wick_ratio:.2f}"
            )

        return hits

    def _classify_tier(self, r: AnalysisResult) -> str:
        """4h RSI / 出来高 / ATR の組み合わせで tier を決定。

        Tier S: 4h RSI < X & Volume RISING
        Tier A: 4h RSI < X & ATR ≥ HIGH
        Tier B: 4h RSI < X 単独
        いずれも外れれば REJECT。
        """
        if r.rsi_4h is None or r.rsi_4h >= self._rsi_4h_max:
            return TIER_REJECT

        # 4h < X が確定した上で優位条件を重ねる
        if r.volume_trend == VOL_TREND_RISING:
            return TIER_S

        if r.atr_pct is not None and r.atr_pct >= self._atr_high:
            return TIER_A

        return TIER_B

    def _calc_boosters(
        self, r: AnalysisResult, regime: str,
    ) -> tuple[list[str], float]:
        """エッジ条件を重ねるほど score を加点する。

        スコアは 0〜1 目安だが上限なし。戦略側でポジションサイズの
        傾き付けに利用するための相対値として扱う。
        """
        boosters: list[str] = []
        score: float = 0.0

        # Funding rate >= 0.1% (ロング過熱) → ショートに追い風 (exp +0.66%)
        if r.funding_rate is not None and r.funding_rate >= self._boost_funding:
            boosters.append(f"FR≥{self._boost_funding:.2f}")
            score += 0.25

        # OBV BEARISH_DIV → 価格↑ OBV↓ の分配フェーズ (exp +0.33%)
        if r.obv_divergence == "BEARISH_DIV":
            boosters.append("OBV_BEAR_DIV")
            score += 0.15

        # 日足 RED (exp +0.53%): 下降中の急騰 = 反転期待
        if r.daily_direction == "RED":
            boosters.append("daily_RED")
            score += 0.20

        # 4h 連続陽線 5〜7 本 (exp +0.62%): 過熱ピーク
        if r.consecutive_green_4h is not None and 5 <= r.consecutive_green_4h <= 7:
            boosters.append(f"4h_green={r.consecutive_green_4h}")
            score += 0.15

        # BEARISH レジームは逆張りショートには慎重に評価 (exp -0.79%)
        #   → 加点はせず、ニュートラル扱い
        # BULLISH / STAGNANT はエッジが平均的に存在するのでそのまま
        if regime == "BEARISH":
            score *= 0.8  # 慎重側に割引

        return boosters, score

    def historical_trade_passes(self, trade: object) -> bool:
        """現在のlive母集団に入る過去シャドートレードだけを返す。

        StrategyRanker の実弾ゲートへ渡すpredicate。現在の候補はlive filter
        通過後なのに、EVだけ全候補から計算する母集団不一致を防ぐ。
        不足・不明値はすべてFalseとして扱う。
        """
        try:
            if self._data_driven_market_short_v2:
                filters = getattr(trade, "filters", None)
                if filters is None:
                    return False
                daily_direction = str(
                    getattr(filters, "daily_direction", "") or ""
                ).upper()
                consecutive_green = getattr(
                    filters, "consecutive_green_1h", None
                )
                funding_rate = getattr(filters, "funding_rate", None)
                conviction = str(
                    getattr(trade, "short_conviction", "UNKNOWN")
                    or "UNKNOWN"
                ).upper()
                return (
                    daily_direction == "RED"
                    and self._is_finite_number(consecutive_green)
                    and int(float(consecutive_green)) in (3, 4)
                    and self._is_finite_number(funding_rate)
                    and float(funding_rate) >= self._min_funding_rate_pct
                    and conviction != "AVOID"
                )

            required_policy_version = os.getenv(
                "LIVE_POLICY_VERSION", ""
            ).strip()
            if (
                required_policy_version
                and getattr(trade, "policy_version", None)
                != required_policy_version
            ):
                return False
            if (
                required_policy_version
                and getattr(trade, "policy_fingerprint", None)
                != self._policy_fingerprint
            ):
                return False
            if not bool(getattr(trade, "confirmed_strict", False)):
                return False
            filters = getattr(trade, "filters", None)
            if filters is None:
                return False

            rsi = getattr(filters, "rsi", None)
            rsi_4h = getattr(filters, "rsi_4h", None)
            relative_strength = getattr(filters, "relative_strength", None)
            atr_pct = getattr(filters, "atr_pct", None)
            consecutive_green = getattr(filters, "consecutive_green_1h", None)
            bb_width = getattr(filters, "bb_width_pct", None)
            ma_deviation = getattr(filters, "ma20_deviation_pct", None)
            upper_wick = getattr(filters, "upper_wick_ratio_1h", None)
            volume_trend = getattr(filters, "volume_trend", None)
            funding_rate = getattr(filters, "funding_rate", None)
            spread_pct = getattr(trade, "spread_pct", None)

            if (
                not self._is_finite_number(rsi)
                or not self._is_finite_number(rsi_4h)
                or not self._is_finite_number(relative_strength)
                or float(rsi) < self._rsi_min
                or float(rsi_4h) >= self._rsi_4h_max
                or float(relative_strength) < self._rel_strength_min
            ):
                return False

            if self._require_complete_technical and (
                not self._is_finite_number(atr_pct)
                or not self._is_finite_number(consecutive_green)
                or not self._is_finite_number(bb_width)
                or not self._is_finite_number(ma_deviation)
                or not volume_trend
                or (
                    self._block_upper_wick
                    and not self._is_finite_number(upper_wick)
                )
            ):
                return False

            if self._require_funding_data and (
                not self._is_finite_number(funding_rate)
                or float(funding_rate) < self._min_funding_rate_pct
            ):
                return False
            if (
                not self._is_finite_number(spread_pct)
                or float(spread_pct) < 0
                or float(spread_pct) > self._max_historical_spread_pct
            ):
                return False

            conviction = str(
                getattr(trade, "short_conviction", "UNKNOWN") or "UNKNOWN"
            ).upper()
            if (
                self._require_fundamental_pass
                and conviction not in self._allowed_fundamental
            ):
                return False

            if (
                consecutive_green is not None
                and int(consecutive_green) >= self._block_consec_green_1h
            ):
                return False
            if (
                bb_width is not None
                and self._block_bbw_lo
                <= float(bb_width)
                < self._block_bbw_hi
            ):
                return False
            if (
                ma_deviation is not None
                and self._block_ma_dev_lo
                <= float(ma_deviation)
                < self._block_ma_dev_hi
            ):
                return False
            if (
                atr_pct is not None
                and self._block_atr_lo
                <= float(atr_pct)
                < self._block_atr_hi
            ):
                return False
            if (
                self._block_upper_wick
                and upper_wick is not None
                and float(upper_wick) >= self._block_wick_ratio
            ):
                return False

            return True
        except (TypeError, ValueError, OverflowError):
            return False

    @staticmethod
    def _is_finite_number(value: object) -> bool:
        try:
            return math.isfinite(float(value))
        except (TypeError, ValueError, OverflowError):
            return False
