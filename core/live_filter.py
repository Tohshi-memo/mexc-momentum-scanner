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
import os
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from core.analyzer import AnalysisResult, VOL_TREND_RISING

if TYPE_CHECKING:
    from core.stats import StatsManager

logger = logging.getLogger(__name__)


# ─── Tier 定義 ────────────────────────────────────────────────────────
TIER_S = "S"   # 最強確信 (4h<65 & RISING)
TIER_A = "A"   # 高確信   (4h<65 & ATR≥11%)
TIER_B = "B"   # 標準確信 (4h<65 単独)
TIER_REJECT = "REJECT"


@dataclass
class LiveFilterDecision:
    """実トレード可否判定の結果。"""

    passed: bool
    tier: str                    # S / A / B / REJECT
    reasons: list[str] = field(default_factory=list)
    block_reasons: list[str] = field(default_factory=list)
    boosters: list[str] = field(default_factory=list)
    score: float = 0.0           # ブースター加点後の確信度スコア

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
        # ─── Tier gating thresholds ──────────────────────────────────
        self._rsi_min: float     = float(os.getenv("LIVE_RSI_MIN",     "70"))
        self._rsi_4h_max: float  = float(os.getenv("LIVE_RSI_4H_MAX",  "65"))
        self._atr_high: float    = float(os.getenv("LIVE_ATR_HIGH",    "11.0"))
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
        # ─── 前提条件 (全 tier 共通) ────────────────────────────────
        pre_reasons: list[str] = []

        if result.rsi is None or result.rsi < self._rsi_min:
            pre_reasons.append(
                f"RSI(1h) {result.rsi:.1f} < {self._rsi_min:.0f}"
                if result.rsi is not None else "RSI(1h) n/a"
            )

        if result.rsi_4h is None:
            pre_reasons.append("4h RSI n/a")

        if result.relative_strength_pct < self._rel_strength_min:
            pre_reasons.append(
                f"rel_strength {result.relative_strength_pct:.1f} < {self._rel_strength_min:.0f}"
            )

        if self._require_fundamental_pass and fundamental_conviction == "AVOID":
            pre_reasons.append("fundamental=AVOID (正材料あり)")

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

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

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
