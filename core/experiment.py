"""
core/experiment.py
シャドウトレード追跡: フィルター粒度別 PnL 実験用

スキャナーが拾った全候補（STRICT フィルター confirmed/rejected 問わず）を
仮想エントリーとして追跡し、各候補のフィルター値・outcome・PnL を
data/experiments.json に蓄積する。

これにより、後から「もし RSI 閾値を 70 に下げていたら？」「4h フィルターを
無効にしていたら？」のような re-evaluation が同じデータセットから可能になる。
実トレード（StatsManager）には影響しない。完全に独立した実験データ。

設計のポイント:
    - confirmed_strict フラグで現行フィルター通過の有無を記録
    - filters スナップショットで全指標値を保存（後で任意の閾値で再評価可能）
    - 古い記録は MAX_CLOSED_RECORDS で自動的に切り捨て（ファイルサイズ抑制）
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)

EXPERIMENT_FILE = Path("data/experiments.json")

OUTCOME_ACTIVE  = "ACTIVE"
OUTCOME_TP_HIT  = "TP_HIT"
OUTCOME_SL_HIT  = "SL_HIT"
OUTCOME_EXPIRED = "EXPIRED"


@dataclass
class FilterSnapshot:
    """検出時の全フィルター指標値。後から任意の閾値で再評価できる。"""
    rsi:               float | None
    rsi_4h:            float | None
    bb_upper:          float | None
    price_vs_bb:       float           # price / bb_upper (1.0 超で BB break)
    volume_ratio:      float           # 直近1足 vol / 過去N足平均
    volume_trend:      str             # RISING / FLAT / DECLINING
    atr_pct:           float | None
    change_1h:         float
    relative_strength: float           # alt_1h - btc_1h
    btc_change_1h:     float


@dataclass
class ExperimentTrade:
    """シャドウトレード（仮想エントリーの追跡）"""
    symbol: str
    detected_at: str
    expires_at: str
    entry_price: float
    sl_price: float
    tp_price: float
    sl_pct: float
    tp_pct: float

    market_regime: str
    confirmed_strict: bool             # 現行 STRICT フィルター通過したか
    filters: FilterSnapshot

    # 状態
    outcome: str = OUTCOME_ACTIVE
    outcome_at: str | None = None
    outcome_price: float | None = None
    pnl_pct: float | None = None
    hours_held: float | None = None

    # 期間中の最大値（追加分析用）
    max_favorable_pct: float = 0.0     # ショート視点の最大利益（最大下落%）
    max_adverse_pct: float = 0.0       # ショート視点の最大損失（最大上昇%）
    last_price: float | None = None


class ExperimentTracker:
    """全候補を仮想追跡してフィルター粒度別の PnL データを蓄積する。

    実トレード（SymbolTracker / StatsManager）から完全に独立しており、
    confirmed/rejected 問わず全候補を記録する。

    使い方:
        exp = ExperimentTracker()
        exp.add_candidate(symbol, entry, sl, tp, ..., filters, confirmed_strict)
        exp.update(client)  # 各サイクルで価格更新 + outcome 確定
        exp.save()
    """

    MAX_CLOSED_RECORDS = 1000  # 古い記録は自動的に切り捨て

    def __init__(self, file_path: Path = EXPERIMENT_FILE) -> None:
        self._file = file_path
        self._tracking_hours = int(os.getenv("EXPERIMENT_TRACKING_HOURS", "8"))
        self._active: dict[str, ExperimentTrade] = {}
        self._closed: list[ExperimentTrade] = []
        self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_candidate(
        self,
        symbol: str,
        entry_price: float,
        sl_price: float,
        tp_price: float,
        sl_pct: float,
        tp_pct: float,
        market_regime: str,
        filters: FilterSnapshot,
        confirmed_strict: bool,
    ) -> bool:
        """新規シャドウトレードを登録。同銘柄追跡中なら何もしない。"""
        if symbol in self._active:
            return False

        now     = datetime.now(timezone.utc)
        expires = now + timedelta(hours=self._tracking_hours)

        self._active[symbol] = ExperimentTrade(
            symbol=symbol,
            detected_at=now.isoformat(),
            expires_at=expires.isoformat(),
            entry_price=entry_price,
            sl_price=sl_price,
            tp_price=tp_price,
            sl_pct=sl_pct,
            tp_pct=tp_pct,
            market_regime=market_regime,
            confirmed_strict=confirmed_strict,
            filters=filters,
            last_price=entry_price,
        )
        logger.debug(
            "Shadow trade added: %s (strict=%s, regime=%s)",
            symbol, confirmed_strict, market_regime,
        )
        return True

    def update(self, client: "MEXCClient") -> list[ExperimentTrade]:
        """全アクティブシャドウの outcome を更新。新規確定したものを返す。"""
        if not self._active:
            return []

        symbols_list = list(self._active.keys())
        try:
            tickers = client.fetch_tickers(symbols_list)
        except Exception as e:
            logger.error("Failed to fetch experiment tickers: %s", e)
            return []

        newly_closed: list[ExperimentTrade] = []
        now = datetime.now(timezone.utc)
        now_str = now.isoformat()

        for symbol in symbols_list:
            trade = self._active[symbol]
            ticker = tickers.get(symbol, {})
            price = float(ticker.get("last") or 0)

            expired = datetime.fromisoformat(trade.expires_at) <= now

            if price > 0:
                trade.last_price = price

                # MFE / MAE 更新（ショート視点：価格下落 = 利益）
                change_pct = (trade.entry_price - price) / trade.entry_price * 100
                if change_pct > trade.max_favorable_pct:
                    trade.max_favorable_pct = change_pct
                if change_pct < trade.max_adverse_pct:
                    trade.max_adverse_pct = change_pct

                # outcome 判定（先に到達した方で確定）
                if price <= trade.tp_price:
                    self._close(trade, OUTCOME_TP_HIT, price, now_str)
                    newly_closed.append(trade)
                    continue
                if price >= trade.sl_price:
                    # SL は設定値で固定（5分スリッページで損失が膨らまないよう）
                    self._close(trade, OUTCOME_SL_HIT, trade.sl_price, now_str)
                    newly_closed.append(trade)
                    continue

            if expired:
                self._close(
                    trade, OUTCOME_EXPIRED,
                    trade.last_price or trade.entry_price, now_str,
                )
                newly_closed.append(trade)

        if newly_closed:
            self._enforce_history_cap()
            self._save()
        return newly_closed

    def active_count(self) -> int:
        return len(self._active)

    def closed_count(self) -> int:
        return len(self._closed)

    def save(self) -> None:
        self._save()

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _close(
        self,
        trade: ExperimentTrade,
        outcome: str,
        exit_price: float,
        now_str: str,
    ) -> None:
        trade.outcome = outcome
        trade.outcome_at = now_str
        trade.outcome_price = exit_price
        trade.pnl_pct = (trade.entry_price - exit_price) / trade.entry_price * 100

        detected = datetime.fromisoformat(trade.detected_at)
        closed   = datetime.fromisoformat(now_str)
        trade.hours_held = (closed - detected).total_seconds() / 3600

        self._closed.append(trade)
        del self._active[trade.symbol]

        logger.info(
            "[EXP %s] %s pnl=%+.2f%% (held %.1fh, regime=%s, strict=%s)",
            outcome, trade.symbol,
            trade.pnl_pct or 0.0,
            trade.hours_held or 0.0,
            trade.market_regime,
            trade.confirmed_strict,
        )

    def _enforce_history_cap(self) -> None:
        if len(self._closed) > self.MAX_CLOSED_RECORDS:
            drop = len(self._closed) - self.MAX_CLOSED_RECORDS
            self._closed = self._closed[drop:]
            logger.debug("Pruned %d old experiment record(s).", drop)

    def _save(self) -> None:
        self._file.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "active": [self._serialize(t) for t in self._active.values()],
            "closed": [self._serialize(t) for t in self._closed],
        }
        with self._file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        logger.debug(
            "Experiments saved: %d active, %d closed.",
            len(self._active), len(self._closed),
        )

    @staticmethod
    def _serialize(t: ExperimentTrade) -> dict:
        return asdict(t)

    def _load(self) -> None:
        if not self._file.exists():
            return
        try:
            with self._file.open(encoding="utf-8") as f:
                data = json.load(f)

            for entry in data.get("active", []):
                trade = self._build_trade(entry)
                self._active[trade.symbol] = trade

            for entry in data.get("closed", []):
                self._closed.append(self._build_trade(entry))

            logger.info(
                "Loaded experiments: %d active, %d closed.",
                len(self._active), len(self._closed),
            )
        except Exception as e:
            logger.warning("Failed to load experiments file: %s", e)

    @staticmethod
    def _build_trade(entry: dict) -> ExperimentTrade:
        filters_dict = entry.pop("filters", {})
        # 互換性: 欠落フィールドを 0 / None で埋める
        filters_dict.setdefault("btc_change_1h", 0.0)
        filters_dict.setdefault("relative_strength", 0.0)
        filters = FilterSnapshot(**filters_dict)
        return ExperimentTrade(filters=filters, **entry)
