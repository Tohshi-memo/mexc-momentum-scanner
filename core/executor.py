"""
core/executor.py
注文実行管理 - DRY RUN (Mock) モードと将来の Live モードの共通インターフェース

設計方針:
    - BaseExecutor: 注文インターフェースの抽象基底クラス
    - DryRunExecutor: ログ出力のみ（現在のデフォルト）
    - LiveExecutor: 実際の API 注文（Trade権限取得後に有効化）
    - ExecutorFactory: DRY_RUN 環境変数に基づいて適切な実装を返す
"""
from __future__ import annotations

import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from core.analyzer import AnalysisResult
from core.fundamental import FundamentalResult
from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Trade Proposal データクラス
# ---------------------------------------------------------------------------

@dataclass
class TradeProposal:
    """擬似（または実際の）トレード提案を表すデータクラス。

    エントリー根拠、損切りライン、利確目標を一元管理する。
    将来の Live 実行時はこの構造を変えずにインターフェースのみ差し替える。
    """

    symbol: str
    direction: str          # "short" (擬似ショート)
    entry_price: float      # エントリー参考価格
    stop_loss: float        # 損切りライン (SL)
    take_profit: float      # 利確目標 (TP)
    sl_pct: float           # SL 幅 (%)
    tp_pct: float           # TP 幅 (%)
    rsi_at_entry: float | None
    bb_upper_at_entry: float | None
    volume_24h_usdt: float
    change_1h_pct: float
    fundamental: FundamentalResult | None = None  # ファンダ考察結果
    created_at: str = ""    # ISO 8601 タイムスタンプ

    def __post_init__(self) -> None:
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Abstract Base Class
# ---------------------------------------------------------------------------

class BaseExecutor(ABC):
    """注文実行の共通インターフェース。

    DryRunExecutor と LiveExecutor はこのクラスを継承し、
    execute() メソッドを実装する。
    main.py や scanner ループは BaseExecutor 型として扱うため、
    実装を切り替えても呼び出し側のコードは変更不要。
    """

    @abstractmethod
    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """トレード提案を実行する（またはモック出力する）。

        Args:
            proposal: TradeProposal オブジェクト
        Returns:
            実行結果の辞書。DRY RUN 時はモック結果、Live 時は取引所レスポンス。
        """
        ...

    @abstractmethod
    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """ポジションをクローズする（将来実装）。

        Args:
            symbol: クローズ対象シンボル
            amount: クローズ数量
        Returns:
            実行結果の辞書
        """
        ...


# ---------------------------------------------------------------------------
# Dry Run Executor (現在のデフォルト)
# ---------------------------------------------------------------------------

class DryRunExecutor(BaseExecutor):
    """トレード提案を構造化ログとして出力するモック実装。

    実際の API 注文は一切発行しない。
    将来 LiveExecutor に切り替える際は ExecutorFactory の分岐を変更するだけ。
    """

    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """擬似トレード提案をログ出力し、モック結果を返す。

        出力形式:
            [DRY RUN] ========================================
            Symbol     : XXX/USDT:USDT
            Direction  : SHORT (擬似ショート)
            Entry Ref  : $0.0001234
            Stop Loss  : $0.0001258 (+2.00%) ← 上方向（ショートのSLは上）
            Take Profit: $0.0001185 (-4.00%) ← 下方向（ショートのTPは下）
            RSI        : 82.4 (OVERBOUGHT)
            BB Upper   : $0.0001230 (BREAK)
            1h Change  : +7.85%
            Volume 24h : $5,234,567 USDT
            Timestamp  : 2025-01-01T00:00:00+00:00
        """
        # AVOID 判定の場合は出力してスキップ
        if (
            proposal.fundamental is not None
            and proposal.fundamental.short_conviction == "AVOID"
        ):
            logger.warning(
                "[DRY RUN] SKIPPED (AVOID) %s — Fundamental: %s",
                proposal.symbol,
                proposal.fundamental.reason,
            )
            return {"status": "skipped_avoid", "symbol": proposal.symbol}

        logger.info("=" * 60)
        logger.info("[DRY RUN] Trade Proposal Generated")
        logger.info("  Symbol      : %s", proposal.symbol)
        logger.info("  Direction   : %s (擬似ショート)", proposal.direction.upper())
        logger.info("  Entry Ref   : $%.8g", proposal.entry_price)
        logger.info(
            "  Stop Loss   : $%.8g (+%.2f%%) ← ショートSLは上方向",
            proposal.stop_loss,
            proposal.sl_pct,
        )
        logger.info(
            "  Take Profit : $%.8g (-%.2f%%) ← ショートTPは下方向",
            proposal.take_profit,
            proposal.tp_pct,
        )
        logger.info(
            "  RSI         : %s",
            f"{proposal.rsi_at_entry:.1f} (OVERBOUGHT)"
            if proposal.rsi_at_entry is not None
            else "N/A",
        )
        logger.info(
            "  BB Upper    : %s",
            f"${proposal.bb_upper_at_entry:.8g} (BREAK)"
            if proposal.bb_upper_at_entry is not None
            else "N/A",
        )
        logger.info("  1h Change   : +%.2f%%", proposal.change_1h_pct)
        logger.info("  Volume 24h  : $%s USDT", f"{proposal.volume_24h_usdt:,.0f}")
        # ファンダ考察サマリー
        if proposal.fundamental is not None and proposal.fundamental.news_count >= 0:
            logger.info(
                "  Fundamental : catalyst=%s conviction=%s news=%d件",
                proposal.fundamental.catalyst_type,
                proposal.fundamental.short_conviction,
                proposal.fundamental.news_count,
            )
            logger.info("  Fund Reason : %s", proposal.fundamental.reason)
        logger.info("  Timestamp   : %s", proposal.created_at)
        logger.info("=" * 60)

        return {
            "status": "dry_run",
            "symbol": proposal.symbol,
            "direction": proposal.direction,
            "entry_price": proposal.entry_price,
            "stop_loss": proposal.stop_loss,
            "take_profit": proposal.take_profit,
            "timestamp": proposal.created_at,
        }

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """擬似クローズをログ出力する。"""
        logger.info("[DRY RUN] Close position | symbol=%s amount=%.6f", symbol, amount)
        return {"status": "dry_run_close", "symbol": symbol, "amount": amount}


# ---------------------------------------------------------------------------
# Live Executor (本番実装)
# ---------------------------------------------------------------------------

class LiveExecutor(BaseExecutor):
    """MEXC USDT-M 先物への実発注を行う本番実装。

    安全設計:
        - 必ず SL/TP を注文と同時に attach (約定後に別注文ではない)
        - AVOID シグナルは発注しない
        - 残高 < LIVE_MIN_BALANCE_USDT なら発注しない
        - 既存ポジションがあるシンボルは重複エントリー禁止
        - 計算後の数量 / 名目額が取引所の最小値を下回ったらスキップ
        - LIVE_MAX_OPEN_POSITIONS を超える同時保有は禁止
        - エラー時はリトライせずログ + 状態を返す (上位で stats / tracker に
          反映しないこと)

    ポジションサイズ:
        risk_usdt   = balance × LIVE_BASE_RISK_PCT%   (≤ LIVE_MAX_RISK_PCT)
        notional    = risk_usdt / (sl_pct / 100)
        notional   ≤ balance × LIVE_MAX_LEVERAGE
        amount      = notional / (entry_price × contract_size)
    """

    def __init__(self, client: MEXCClient) -> None:
        self._client = client
        # ポジションサイジング
        self._base_risk_pct: float = float(os.getenv("LIVE_BASE_RISK_PCT", "0.5"))
        self._max_risk_pct:  float = float(os.getenv("LIVE_MAX_RISK_PCT",  "1.5"))
        self._max_leverage:  float = float(os.getenv("LIVE_MAX_LEVERAGE",  "3.0"))
        # 安全装置
        self._min_balance_usdt:    float = float(os.getenv("LIVE_MIN_BALANCE_USDT", "5.0"))
        self._max_open_positions:  int   = int(os.getenv("LIVE_MAX_OPEN_POSITIONS", "3"))

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """SHORT エントリーを 1 件発注する (SL/TP 同時 attach)。

        失敗時は status="error" を返す。上位 (main.py) はこれを見て
        tracker / stats に登録しないようにすること。
        """
        # ── ガード 1: AVOID ──────────────────────────────────────────
        if (
            proposal.fundamental is not None
            and proposal.fundamental.short_conviction == "AVOID"
        ):
            logger.warning(
                "[LIVE] SKIP %s — fundamental AVOID (%s)",
                proposal.symbol, proposal.fundamental.reason,
            )
            return {"status": "skipped_avoid", "symbol": proposal.symbol}

        # ── ガード 2: 残高 ────────────────────────────────────────────
        try:
            balance = self._client.fetch_balance()
        except Exception as e:
            logger.error("[LIVE] fetch_balance failed: %s", e)
            return {"status": "error", "reason": f"fetch_balance: {e}"}

        usdt_info  = balance.get("USDT", {}) or {}
        free_usdt  = float(usdt_info.get("free")  or 0.0)
        total_usdt = float(usdt_info.get("total") or 0.0)

        if free_usdt < self._min_balance_usdt:
            logger.warning(
                "[LIVE] SKIP %s — free $%.2f < min $%.2f",
                proposal.symbol, free_usdt, self._min_balance_usdt,
            )
            return {
                "status": "skipped_low_balance",
                "symbol": proposal.symbol,
                "free_usdt": free_usdt,
            }

        # ── ガード 3: 既存ポジション + 同時保有数 ────────────────────
        try:
            all_positions = self._client.exchange.fetch_positions()
        except Exception as e:
            logger.error("[LIVE] fetch_positions failed: %s", e)
            return {"status": "error", "reason": f"fetch_positions: {e}"}

        open_positions = [
            p for p in all_positions
            if float(p.get("contracts") or 0) > 0
        ]
        for p in open_positions:
            if p.get("symbol") == proposal.symbol:
                logger.warning(
                    "[LIVE] SKIP %s — position already open (%.6g contracts)",
                    proposal.symbol, float(p.get("contracts") or 0),
                )
                return {"status": "skipped_already_open", "symbol": proposal.symbol}

        if len(open_positions) >= self._max_open_positions:
            logger.warning(
                "[LIVE] SKIP %s — open positions %d ≥ max %d",
                proposal.symbol, len(open_positions), self._max_open_positions,
            )
            return {
                "status": "skipped_max_positions",
                "symbol": proposal.symbol,
                "open_count": len(open_positions),
            }

        # ── ガード 4: SL/TP 健全性 ──────────────────────────────────
        if proposal.sl_pct <= 0 or proposal.tp_pct <= 0:
            return {"status": "error", "reason": "sl_pct or tp_pct <= 0"}
        if proposal.stop_loss <= proposal.entry_price:
            # SHORT: SL は entry より上であるべき
            return {"status": "error", "reason": "SHORT SL must be above entry"}
        if proposal.take_profit >= proposal.entry_price:
            # SHORT: TP は entry より下であるべき
            return {"status": "error", "reason": "SHORT TP must be below entry"}

        # ── ポジションサイズ ─────────────────────────────────────────
        risk_pct  = min(self._base_risk_pct, self._max_risk_pct)
        risk_usdt = total_usdt * risk_pct / 100
        notional  = risk_usdt / (proposal.sl_pct / 100)
        notional  = min(notional, total_usdt * self._max_leverage)

        try:
            market = self._client.exchange.market(proposal.symbol)
        except Exception as e:
            return {"status": "error", "reason": f"market_meta: {e}"}

        contract_size = float(market.get("contractSize") or 1)
        if proposal.entry_price <= 0 or contract_size <= 0:
            return {"status": "error", "reason": "invalid entry_price or contract_size"}

        amount = notional / (proposal.entry_price * contract_size)

        # 取引所の最小数量 / 最小名目額をチェック
        limits     = market.get("limits") or {}
        min_amount = (limits.get("amount") or {}).get("min")
        min_cost   = (limits.get("cost")   or {}).get("min")

        if min_amount is not None and amount < float(min_amount):
            logger.warning(
                "[LIVE] SKIP %s — amount %.6g < min %.6g (notional $%.2f)",
                proposal.symbol, amount, float(min_amount), notional,
            )
            return {
                "status": "skipped_below_min_amount",
                "symbol": proposal.symbol,
                "amount": amount,
                "min_amount": float(min_amount),
            }
        if min_cost is not None and notional < float(min_cost):
            logger.warning(
                "[LIVE] SKIP %s — notional $%.2f < min $%.2f",
                proposal.symbol, notional, float(min_cost),
            )
            return {
                "status": "skipped_below_min_cost",
                "symbol": proposal.symbol,
                "notional": notional,
                "min_cost": float(min_cost),
            }

        # 取引所の精度に合わせる
        try:
            amount_str   = self._client.exchange.amount_to_precision(proposal.symbol, amount)
            sl_price_str = self._client.exchange.price_to_precision(proposal.symbol, proposal.stop_loss)
            tp_price_str = self._client.exchange.price_to_precision(proposal.symbol, proposal.take_profit)
            amount   = float(amount_str)
            sl_price = float(sl_price_str)
            tp_price = float(tp_price_str)
        except Exception as e:
            return {"status": "error", "reason": f"precision: {e}"}

        # ── レバレッジ設定 (失敗しても発注は続行) ────────────────────
        try:
            self._client.exchange.set_leverage(int(self._max_leverage), proposal.symbol)
        except Exception as e:
            logger.warning("[LIVE] set_leverage failed for %s: %s", proposal.symbol, e)

        # ── 発注 (SL/TP attached) ────────────────────────────────────
        # SHORT = sell (open). MEXC perpetual + ccxt は stopLossPrice /
        # takeProfitPrice を params で渡せば 1 注文に attach される。
        try:
            order = self._client.create_order(
                symbol=proposal.symbol,
                order_type="market",
                side="sell",
                amount=amount,
                price=None,
                params={
                    "stopLossPrice":   sl_price,
                    "takeProfitPrice": tp_price,
                    "reduceOnly":      False,
                },
            )
        except Exception as e:
            logger.error(
                "[LIVE] create_order FAILED %s amount=%.6g sl=%.6g tp=%.6g: %s",
                proposal.symbol, amount, sl_price, tp_price, e,
            )
            return {"status": "error", "reason": f"create_order: {e}"}

        logger.warning(
            "[LIVE] ✓ SHORT %s | size=%.6g notional=$%.2f entry≈$%.6g "
            "SL=$%.6g (+%.2f%%) TP=$%.6g (-%.2f%%) lev=%.0fx order_id=%s",
            proposal.symbol, amount, notional, proposal.entry_price,
            sl_price, proposal.sl_pct, tp_price, proposal.tp_pct,
            self._max_leverage, order.get("id"),
        )
        return {
            "status":        "ok",
            "order_id":      order.get("id"),
            "symbol":        proposal.symbol,
            "amount":        amount,
            "notional_usdt": notional,
            "risk_usdt":     risk_usdt,
            "sl_price":      sl_price,
            "tp_price":      tp_price,
            "leverage":      self._max_leverage,
            "raw":           order,
        }

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """SHORT ポジションを成行 buy + reduceOnly でクローズする。

        通常は SL/TP が exchange 側で発火するため使われない。
        緊急停止 / 手動介入用。
        """
        try:
            order = self._client.create_order(
                symbol=symbol,
                order_type="market",
                side="buy",
                amount=amount,
                price=None,
                params={"reduceOnly": True},
            )
            logger.warning(
                "[LIVE] CLOSE %s amount=%.6g order_id=%s",
                symbol, amount, order.get("id"),
            )
            return {"status": "ok", "order_id": order.get("id"), "raw": order}
        except Exception as e:
            logger.error("[LIVE] close_position FAILED %s: %s", symbol, e)
            return {"status": "error", "reason": str(e)}


# ---------------------------------------------------------------------------
# Proposal Builder (ビジネスロジック)
# ---------------------------------------------------------------------------

class ProposalBuilder:
    """AnalysisResult からトレード提案を組み立てるファクトリ。

    SL 幅の決定ルール (損失低減のための volatility-aware 設計):
      1. ATR が取得できれば SL_PCT = clamp(ATR% × ATR_SL_MULT, ATR_SL_MIN, ATR_SL_MAX)
      2. 取得できなければ固定値 STOP_LOSS_PCT を使用
      3. TP は RISK_REWARD_RATIO (デフォルト 2.0) × sl_pct で決定
         → 1:2 リスクリワードを維持することで、勝率 33% でも損益分岐

    ショート前提のため:
        SL = entry_price * (1 + sl_pct / 100)  ← 上方向
        TP = entry_price * (1 - tp_pct / 100)  ← 下方向
    """

    def __init__(self) -> None:
        # 固定フォールバック
        self._fixed_sl_pct: float = float(os.getenv("STOP_LOSS_PCT", "2.0"))
        self._fixed_tp_pct: float = float(os.getenv("TAKE_PROFIT_PCT", "4.0"))

        # ATR ベース
        self._use_atr_sl:  bool  = os.getenv("USE_ATR_SL", "true").lower() != "false"
        self._atr_sl_mult: float = float(os.getenv("ATR_SL_MULT", "1.5"))
        self._atr_sl_min:  float = float(os.getenv("ATR_SL_MIN", "1.0"))
        self._atr_sl_max:  float = float(os.getenv("ATR_SL_MAX", "4.0"))
        self._rr_ratio:    float = float(os.getenv("RISK_REWARD_RATIO", "2.0"))

    def build(
        self,
        result: AnalysisResult,
        fundamental: FundamentalResult | None = None,
    ) -> TradeProposal:
        """AnalysisResult を TradeProposal に変換する。

        Args:
            result: TechnicalAnalyzer の分析結果
            fundamental: FundamentalAnalyzer の考察結果（省略可）
        Returns:
            構造化された TradeProposal
        """
        entry = result.price

        # SL 幅を決定
        if self._use_atr_sl and result.atr_pct is not None and result.atr_pct > 0:
            sl_pct = max(
                self._atr_sl_min,
                min(result.atr_pct * self._atr_sl_mult, self._atr_sl_max),
            )
        else:
            sl_pct = self._fixed_sl_pct

        # TP は RR 比で決定
        tp_pct = sl_pct * self._rr_ratio

        sl = entry * (1 + sl_pct / 100)
        tp = entry * (1 - tp_pct / 100)

        return TradeProposal(
            symbol=result.symbol,
            direction="short",
            entry_price=entry,
            stop_loss=sl,
            take_profit=tp,
            sl_pct=sl_pct,
            tp_pct=tp_pct,
            rsi_at_entry=result.rsi,
            bb_upper_at_entry=result.bb_upper,
            volume_24h_usdt=result.volume_24h_usdt,
            change_1h_pct=result.change_1h_pct,
            fundamental=fundamental,
        )


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

class ExecutorFactory:
    """DRY_RUN 環境変数に基づき適切な Executor を返すファクトリ。

    使用例:
        executor = ExecutorFactory.create(client)
        # DRY_RUN=true  → DryRunExecutor
        # DRY_RUN=false → LiveExecutor (要 Trade 権限)
    """

    @staticmethod
    def create(client: MEXCClient) -> BaseExecutor:
        """環境変数 DRY_RUN の値に応じて Executor インスタンスを生成する。

        Args:
            client: MEXCClient インスタンス
        Returns:
            BaseExecutor のいずれかの具体実装
        """
        dry_run: bool = os.getenv("DRY_RUN", "true").lower() != "false"

        if dry_run:
            logger.info("Executor mode: DRY RUN (no real orders will be placed).")
            return DryRunExecutor()

        live_enabled = os.getenv("LIVE_TRADING_ENABLED", "false").lower() == "true"
        live_confirmation = os.getenv("LIVE_TRADING_CONFIRMATION", "")
        if not live_enabled or live_confirmation != "LIVE":
            raise RuntimeError(
                "DRY_RUN=false requested, but live trading is locked. "
                "Set LIVE_TRADING_ENABLED=true and LIVE_TRADING_CONFIRMATION=LIVE "
                "only from the protected live workflow."
            )

        logger.warning(
            "Executor mode: LIVE - Real orders WILL be placed. "
            "Ensure API has Trade permission and risk parameters are correct."
        )
        return LiveExecutor(client)
