"""
core/live_strategy.py
実トレード戦略: 方向・エントリー方式・サイズ・SL/TP の統合プラン

data/experiment_report.md の analysis を踏まえて、シャドウで勝率・期待値を
確認できた戦略のみを『実装すべき戦略』として組み込む。

方向判定 (短期 + 長期のハイブリッド):
  - 直近 10〜20 件の LONG vs SHORT 優位率でバイアスを決定
  - 拮抗 (40〜60%) かつ全期間でも拮抗 → 取引見送り
  - ショート優位 → 現行ロジック (急騰後の反転を狙う)
  - ロング優位 → 押し目買い戦略 (LIMIT_2PCT_LONG / LIMIT_ATR_LONG)

エントリー方式 (tier とレジームで切り替え):
  - Tier S / 直近ショート優位 (>55%): MARKET (+2.71% 直近) で即時エントリー
  - Tier A / 通常: MARKET 半分 + LIMIT_7PCT 半分 でスケールイン
                   (LIMIT_7PCT は全期間 #1: 実質期待値 +0.59%)
  - Tier B: LIMIT_6PCT または LIMIT_7PCT 単独 (機会損失許容、指値待ち)

ポジションサイズ (Kelly / Fixed-fractional のハイブリッド):
  - base_risk_pct × tier_multiplier × (1 + booster_score × BOOST_MULT)
  - 1 トレードあたりの最大 risk は MAX_RISK_PCT_PER_TRADE でクリップ
  - 口座残高 × risk_pct を SL 幅で割ってロット数を決定

SL / TP:
  - 既存の ProposalBuilder (ATR ベース) をそのまま流用
  - Trailing SL: tier S/A に限り TP の 50% に達したら SL を BE (損益分岐) に移動
"""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field
from typing import Literal

from core.analyzer import AnalysisResult
from core.executor import ProposalBuilder, TradeProposal
from core.live_filter import LiveFilterDecision, TIER_A, TIER_B, TIER_S

logger = logging.getLogger(__name__)


# ─── Direction & Entry type constants ────────────────────────────────
DIR_SHORT = "short"
DIR_LONG  = "long"
DIR_SKIP  = "skip"

ENTRY_MARKET        = "MARKET"
ENTRY_LIMIT_SCALE   = "LIMIT_SCALE"   # 2段指値
ENTRY_LIMIT_PATIENT = "LIMIT_PATIENT" # 1本の深い指値


@dataclass
class EntryLeg:
    """スケールイン時の個別注文 1 本。"""

    kind: Literal["MARKET", "LIMIT"]
    price: float             # 指値価格 (MARKET の場合は参考 last)
    weight: float            # 全体サイズに対する比率 (合計 1.0)


@dataclass
class LiveTradePlan:
    """実トレード 1 件分の完全な実行プラン。"""

    symbol: str
    direction: str                   # "short" | "long" | "skip"
    entry_style: str                 # MARKET / LIMIT_SCALE / LIMIT_PATIENT
    legs: list[EntryLeg] = field(default_factory=list)
    stop_loss: float = 0.0
    take_profit: float = 0.0
    sl_pct: float = 0.0
    tp_pct: float = 0.0

    # サイズ情報
    risk_pct_of_account: float = 0.0   # 1 トレードで失う可能性のある残高比率
    position_usdt: float = 0.0         # 全 leg 合計の想定ポジション名目額

    # トレーリング & 部分利確
    move_sl_to_be_at_rr: float | None = None   # e.g. 1.0 なら RR=1.0 到達で BE 移動
    partial_tp_at_rr: float | None = None      # 一部利確タイミング (RR 基準)
    partial_tp_ratio: float = 0.0              # 一部利確する割合 (0〜1)

    # メタ
    tier: str = ""
    reasons: list[str] = field(default_factory=list)
    created_from_proposal: TradeProposal | None = None


class LiveStrategyBuilder:
    """AnalysisResult + LiveFilterDecision から LiveTradePlan を構築する。

    ProposalBuilder に SL/TP 計算は委譲し、本クラスは『方向・エントリー方式・
    サイズ・トレーリング』を決定する。
    """

    def __init__(self, proposal_builder: ProposalBuilder | None = None) -> None:
        self._proposal = proposal_builder or ProposalBuilder()

        # ─── リスク設定 ──────────────────────────────────────────────
        # 口座残高のうち 1 トレードで失って良い比率 (%)
        self._base_risk_pct:  float = float(os.getenv("LIVE_BASE_RISK_PCT",  "0.5"))
        self._max_risk_pct:   float = float(os.getenv("LIVE_MAX_RISK_PCT",   "1.5"))
        self._max_leverage:   float = float(os.getenv("LIVE_MAX_LEVERAGE",   "3.0"))

        # Tier ごとのサイズ倍率
        self._tier_mult_s: float = float(os.getenv("LIVE_TIER_MULT_S", "1.50"))
        self._tier_mult_a: float = float(os.getenv("LIVE_TIER_MULT_A", "1.20"))
        self._tier_mult_b: float = float(os.getenv("LIVE_TIER_MULT_B", "0.80"))

        # ブースターによる加点の影響度
        self._boost_mult: float = float(os.getenv("LIVE_BOOST_MULT", "0.40"))

        # ─── エントリーパラメーター ──────────────────────────────────
        # スケールインの LIMIT 側オフセット (%)
        self._limit_offset_pct: float  = float(os.getenv("LIVE_LIMIT_OFFSET_PCT",  "7.0"))
        self._patient_offset_pct: float= float(os.getenv("LIVE_PATIENT_OFFSET_PCT","6.0"))
        # MARKET / LIMIT の比率 (LIMIT_SCALE 戦略)
        self._scale_market_weight: float = float(
            os.getenv("LIVE_SCALE_MARKET_WEIGHT", "0.4")
        )

        # ─── 方向判定の閾値 ──────────────────────────────────────────
        # 直近 N 件のロング優位率がこれ以上なら LONG バイアス
        self._long_bias_pct: float  = float(os.getenv("LIVE_LONG_BIAS_PCT",  "60.0"))
        self._short_bias_pct: float = float(os.getenv("LIVE_SHORT_BIAS_PCT", "40.0"))

        # ─── トレーリング ────────────────────────────────────────────
        self._move_be_at_rr: float     = float(os.getenv("LIVE_MOVE_BE_AT_RR",  "1.0"))
        self._partial_tp_at_rr: float  = float(os.getenv("LIVE_PARTIAL_TP_RR",  "1.0"))
        self._partial_tp_ratio: float  = float(os.getenv("LIVE_PARTIAL_TP_RATIO","0.5"))

        logger.info(
            "LiveStrategyBuilder | base_risk=%.2f%% max_risk=%.2f%% "
            "tier_mult S=%.2f A=%.2f B=%.2f boost=%.2f",
            self._base_risk_pct, self._max_risk_pct,
            self._tier_mult_s, self._tier_mult_a, self._tier_mult_b,
            self._boost_mult,
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def build(
        self,
        result: AnalysisResult,
        decision: LiveFilterDecision,
        *,
        account_balance_usdt: float,
        recent_short_edge_pct: float | None = None,
    ) -> LiveTradePlan:
        """AnalysisResult + フィルター判定から実行プランを生成する。

        Args:
            result: テクニカル分析結果
            decision: LiveTradeFilter の判定結果 (passed=True 前提)
            account_balance_usdt: 現在の残高 (USDT)
            recent_short_edge_pct: 直近のショート優位率 (0〜100)
                 None の場合は experiment_report の現行値 55.0 を既定値とする。
        """
        if not decision.passed:
            return LiveTradePlan(
                symbol=result.symbol,
                direction=DIR_SKIP,
                entry_style=ENTRY_MARKET,
                reasons=["filter rejected"],
            )

        # SL/TP は既存の ATR ベースロジックで計算
        proposal = self._proposal.build(result)

        direction = self._decide_direction(recent_short_edge_pct)
        if direction == DIR_SKIP:
            return LiveTradePlan(
                symbol=result.symbol,
                direction=DIR_SKIP,
                entry_style=ENTRY_MARKET,
                reasons=["direction unclear (SHORT/LONG edge 拮抗)"],
                created_from_proposal=proposal,
            )

        entry_style, legs = self._build_entry_legs(
            price=result.price,
            direction=direction,
            tier=decision.tier,
            recent_short_edge_pct=recent_short_edge_pct,
        )

        risk_pct = self._position_risk_pct(decision.tier, decision.score)
        position_usdt = self._position_notional(
            account_balance_usdt=account_balance_usdt,
            risk_pct=risk_pct,
            sl_pct=proposal.sl_pct,
        )

        # Tier S/A は部分利確＋BE 移動でリスク管理を強化
        move_be_rr: float | None = None
        partial_tp_rr: float | None = None
        partial_tp_ratio: float = 0.0
        if decision.tier in (TIER_S, TIER_A):
            move_be_rr      = self._move_be_at_rr
            partial_tp_rr   = self._partial_tp_at_rr
            partial_tp_ratio= self._partial_tp_ratio

        # 方向によって SL/TP を反転 (LONG は上下逆)
        sl_price, tp_price = self._apply_direction(
            entry=result.price,
            sl_pct=proposal.sl_pct,
            tp_pct=proposal.tp_pct,
            direction=direction,
        )

        reasons = [f"tier={decision.tier}"] + decision.boosters
        if recent_short_edge_pct is not None:
            reasons.append(f"short_edge={recent_short_edge_pct:.0f}%")

        return LiveTradePlan(
            symbol=result.symbol,
            direction=direction,
            entry_style=entry_style,
            legs=legs,
            stop_loss=sl_price,
            take_profit=tp_price,
            sl_pct=proposal.sl_pct,
            tp_pct=proposal.tp_pct,
            risk_pct_of_account=risk_pct,
            position_usdt=position_usdt,
            move_sl_to_be_at_rr=move_be_rr,
            partial_tp_at_rr=partial_tp_rr,
            partial_tp_ratio=partial_tp_ratio,
            tier=decision.tier,
            reasons=reasons,
            created_from_proposal=proposal,
        )

    # ------------------------------------------------------------------
    # Internal: direction decision
    # ------------------------------------------------------------------

    def _decide_direction(
        self, recent_short_edge_pct: float | None,
    ) -> str:
        """直近のショート優位率から方向を決定する。

        experiment_report セクション 22 の『ロング優位%』の逆数を期待値として受け取る。
            short_edge = 100 - long_edge
        """
        edge = recent_short_edge_pct
        if edge is None:
            # データなし → 現行の SHORT 路線をデフォルトに
            return DIR_SHORT

        if edge >= self._long_bias_pct:  # ショート優位
            return DIR_SHORT
        if edge <= self._short_bias_pct:  # ロング優位 (≤ 40%)
            return DIR_LONG
        # 拮抗 (40〜60%) → スキップ
        return DIR_SKIP

    # ------------------------------------------------------------------
    # Internal: entry leg construction
    # ------------------------------------------------------------------

    def _build_entry_legs(
        self,
        *,
        price: float,
        direction: str,
        tier: str,
        recent_short_edge_pct: float | None,
    ) -> tuple[str, list[EntryLeg]]:
        """tier × 直近エッジ から entry style と legs を決定。

        SHORT の場合:
            MARKET は今の価格
            LIMIT は現値より +offset% 上
        LONG の場合:
            MARKET は今の価格
            LIMIT は現値より -offset% 下

        Tier S / 短期エッジ 強 → MARKET のみ (すぐ乗る)
        Tier A           → MARKET + LIMIT_7PCT のハイブリッド
        Tier B           → LIMIT_6PCT 単独 (機会損失許容)
        """
        # Tier S or 強い短期エッジ
        if tier == TIER_S or (
            recent_short_edge_pct is not None and recent_short_edge_pct >= 70.0
        ):
            return ENTRY_MARKET, [
                EntryLeg(kind="MARKET", price=price, weight=1.0),
            ]

        if tier == TIER_A:
            limit_price = self._offset_price(price, direction, self._limit_offset_pct)
            market_w = max(0.0, min(1.0, self._scale_market_weight))
            limit_w  = 1.0 - market_w
            return ENTRY_LIMIT_SCALE, [
                EntryLeg(kind="MARKET", price=price,       weight=market_w),
                EntryLeg(kind="LIMIT",  price=limit_price, weight=limit_w),
            ]

        # Tier B or fallback
        limit_price = self._offset_price(price, direction, self._patient_offset_pct)
        return ENTRY_LIMIT_PATIENT, [
            EntryLeg(kind="LIMIT", price=limit_price, weight=1.0),
        ]

    @staticmethod
    def _offset_price(price: float, direction: str, offset_pct: float) -> float:
        """direction に応じて指値価格を計算。

        SHORT: 現値より +offset% 上で指値 (上ヒゲを付けた所でショート)
        LONG:  現値より -offset% 下で指値 (押し目買い)
        """
        if direction == DIR_SHORT:
            return price * (1 + offset_pct / 100)
        return price * (1 - offset_pct / 100)

    # ------------------------------------------------------------------
    # Internal: SL/TP direction flip
    # ------------------------------------------------------------------

    @staticmethod
    def _apply_direction(
        *, entry: float, sl_pct: float, tp_pct: float, direction: str,
    ) -> tuple[float, float]:
        """direction に応じて SL/TP の上下を入れ替える。"""
        if direction == DIR_LONG:
            sl = entry * (1 - sl_pct / 100)
            tp = entry * (1 + tp_pct / 100)
        else:  # SHORT
            sl = entry * (1 + sl_pct / 100)
            tp = entry * (1 - tp_pct / 100)
        return sl, tp

    # ------------------------------------------------------------------
    # Internal: position sizing
    # ------------------------------------------------------------------

    def _position_risk_pct(self, tier: str, booster_score: float) -> float:
        """tier とブースタースコアからリスク比率を決定する。

        risk_pct = base × tier_mult × (1 + score × BOOST_MULT)
                   → MAX_RISK_PCT でクリップ
        """
        tier_mult = {
            TIER_S: self._tier_mult_s,
            TIER_A: self._tier_mult_a,
            TIER_B: self._tier_mult_b,
        }.get(tier, self._tier_mult_b)

        boost_factor = 1.0 + max(0.0, booster_score) * self._boost_mult
        risk = self._base_risk_pct * tier_mult * boost_factor
        return min(risk, self._max_risk_pct)

    def _position_notional(
        self,
        *,
        account_balance_usdt: float,
        risk_pct: float,
        sl_pct: float,
    ) -> float:
        """SL 幅からロット名目額を算出する。

        risk_usdt      = account × risk_pct%
        notional_usdt  = risk_usdt / (sl_pct / 100)
                        → 価格が SL 幅だけ逆行したとき損失が risk_usdt になるサイズ
        レバレッジ上限で notional を更にクリップ。
        """
        if account_balance_usdt <= 0 or sl_pct <= 0:
            return 0.0

        risk_usdt = account_balance_usdt * risk_pct / 100
        notional  = risk_usdt / (sl_pct / 100)

        # レバレッジ上限: notional ≤ account × MAX_LEVERAGE
        notional_cap = account_balance_usdt * self._max_leverage
        return min(notional, notional_cap)

    # ------------------------------------------------------------------
    # Logging helper
    # ------------------------------------------------------------------

    @staticmethod
    def describe_plan(plan: LiveTradePlan) -> str:
        """LiveTradePlan を 1 行サマリー。ログ出力用。"""
        if plan.direction == DIR_SKIP:
            return f"{plan.symbol}: SKIP ({', '.join(plan.reasons)})"

        legs_str = " + ".join(
            f"{leg.kind}×{leg.weight:.0%}@${leg.price:.6g}" for leg in plan.legs
        )
        trail = ""
        if plan.move_sl_to_be_at_rr is not None:
            trail = f" | BE@RR={plan.move_sl_to_be_at_rr:.1f}"
        if plan.partial_tp_at_rr is not None:
            trail += f" | partial_TP({plan.partial_tp_ratio:.0%})@RR={plan.partial_tp_at_rr:.1f}"

        return (
            f"{plan.symbol} {plan.direction.upper()} {plan.entry_style} "
            f"tier={plan.tier} risk={plan.risk_pct_of_account:.2f}% "
            f"notional=${plan.position_usdt:,.0f} legs=[{legs_str}] "
            f"SL=${plan.stop_loss:.6g} ({plan.sl_pct:.2f}%) "
            f"TP=${plan.take_profit:.6g} ({plan.tp_pct:.2f}%){trail}"
        )
