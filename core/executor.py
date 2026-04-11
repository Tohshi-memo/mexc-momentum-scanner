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
# Live Executor (将来実装 - Trade権限取得後に有効化)
# ---------------------------------------------------------------------------

class LiveExecutor(BaseExecutor):
    """実際の API 注文を発行する本番実装。

    現時点では NotImplementedError を返す。
    Trade権限を取得した際に各メソッドを実装することで、
    main.py や上位ロジックを変更せずに本番運用へ移行できる。
    """

    def __init__(self, client: MEXCClient) -> None:
        self._client = client

    def execute(self, proposal: TradeProposal) -> dict[str, Any]:
        """実際のショート注文を発行する（未実装）。

        実装時の TODO:
            1. 口座残高を取得してポジションサイズを計算
            2. エントリー: 成行または分散指値でショートエントリー
            3. SL/TP: 取引所の stopLoss / takeProfit パラメーターを利用
            4. 注文 ID を記録して後続管理に引き渡す
        """
        raise NotImplementedError(
            "LiveExecutor.execute() is not yet implemented. "
            "Set DRY_RUN=true or implement live order logic."
        )

    def close_position(self, symbol: str, amount: float) -> dict[str, Any]:
        """ポジションをクローズする（未実装）。"""
        raise NotImplementedError(
            "LiveExecutor.close_position() is not yet implemented."
        )


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
        else:
            logger.warning(
                "Executor mode: LIVE - Real orders WILL be placed. "
                "Ensure API has Trade permission and risk parameters are correct."
            )
            return LiveExecutor(client)
