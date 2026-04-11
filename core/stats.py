"""
core/stats.py
バックテスト的な勝率・損益集計マネージャー

data/stats.json にクローズしたトレード (TrackedSymbol) を追記していき、
勝率・平均損益・ドローダウンなどのサマリーをいつでも取得できる。

このファイルから得られる情報をもとに、以下の機能を構築している:
    - クールダウン: 直近 SL 銘柄を一定時間再エントリー禁止
    - サーキットブレーカー: 直近 N 件で損失が閾値超なら当サイクル全スキップ
    - ヘッダー表示: 稼働状況を一目で確認

GitHub Actions が毎サイクルで data/stats.json をコミットするため、
Run をまたいでも記録が永続化される。
"""
from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from core.tracker import (
    OUTCOME_EXPIRED,
    OUTCOME_SL_HIT,
    OUTCOME_TP_HIT,
    TrackedSymbol,
)

logger = logging.getLogger(__name__)

STATS_FILE = Path("data/stats.json")


@dataclass
class TradeRecord:
    """クローズしたトレード1件の記録。"""

    symbol: str
    detected_at: str
    closed_at: str
    outcome: str            # TP_HIT | SL_HIT | EXPIRED
    entry_price: float
    exit_price: float
    sl_price: float
    tp_price: float
    pnl_pct: float          # ショート視点の損益率 (%)
    hours_held: float
    conviction: str
    catalyst_type: str
    detection_rsi: float | None
    detection_1h_change: float

    @classmethod
    def from_tracked(cls, t: TrackedSymbol) -> "TradeRecord":
        """TrackedSymbol から TradeRecord を組み立てる。"""
        exit_price = (
            t.outcome_price
            if t.outcome_price is not None
            else t.current_price
        )
        pnl = (t.detection_price - exit_price) / t.detection_price * 100

        # 経過時間
        closed_at = t.outcome_at or datetime.now(timezone.utc).isoformat()
        detected  = datetime.fromisoformat(t.detected_at)
        closed    = datetime.fromisoformat(closed_at)
        hours_held = (closed - detected).total_seconds() / 3600

        return cls(
            symbol=t.symbol,
            detected_at=t.detected_at,
            closed_at=closed_at,
            outcome=t.outcome,
            entry_price=t.detection_price,
            exit_price=exit_price,
            sl_price=t.sl_price,
            tp_price=t.tp_price,
            pnl_pct=pnl,
            hours_held=hours_held,
            conviction=t.conviction,
            catalyst_type=t.catalyst_type,
            detection_rsi=t.detection_rsi,
            detection_1h_change=t.detection_1h_change,
        )


@dataclass
class StatsSummary:
    """集計サマリー。UI 表示やログ用。"""
    total: int          = 0
    wins: int           = 0   # TP_HIT
    losses: int         = 0   # SL_HIT
    expired: int        = 0
    win_rate: float     = 0.0   # wins / decided (TP + SL のみ)
    avg_pnl: float      = 0.0   # 全トレードの平均損益率
    avg_win: float      = 0.0   # 勝ちトレードの平均利益率
    avg_loss: float     = 0.0   # 負けトレードの平均損失率 (負の値)
    expectancy: float   = 0.0   # 期待値
    total_pnl_pct: float = 0.0  # 累積損益率（%の総和）
    recent_losses: int  = 0     # 直近ウィンドウ内の SL 数
    recent_window: int  = 10    # 直近ウィンドウサイズ


class StatsManager:
    """トレード記録の永続化と集計。"""

    def __init__(self, file_path: Path = STATS_FILE) -> None:
        self._file = file_path
        self._records: list[TradeRecord] = []
        self._load()

    # ------------------------------------------------------------------
    # Recording
    # ------------------------------------------------------------------

    def record_closed(self, tracked: TrackedSymbol) -> TradeRecord:
        """クローズした TrackedSymbol をトレード記録に追加して保存する。"""
        record = TradeRecord.from_tracked(tracked)
        self._records.append(record)
        self.save()
        logger.info(
            "Stats: recorded %s | outcome=%s pnl=%+.2f%%",
            record.symbol, record.outcome, record.pnl_pct,
        )
        return record

    def record_many(self, tracked_list: list[TrackedSymbol]) -> list[TradeRecord]:
        """複数 TrackedSymbol を一度に記録する（保存は最後に1回）。"""
        new_records: list[TradeRecord] = []
        for t in tracked_list:
            if t.outcome in (OUTCOME_TP_HIT, OUTCOME_SL_HIT, OUTCOME_EXPIRED):
                record = TradeRecord.from_tracked(t)
                self._records.append(record)
                new_records.append(record)
                logger.info(
                    "Stats: recorded %s | outcome=%s pnl=%+.2f%%",
                    record.symbol, record.outcome, record.pnl_pct,
                )
        if new_records:
            self.save()
        return new_records

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def summary(self, recent_window: int = 10) -> StatsSummary:
        """全トレード集計サマリーを返す。"""
        if not self._records:
            return StatsSummary(recent_window=recent_window)

        wins    = [r for r in self._records if r.outcome == OUTCOME_TP_HIT]
        losses  = [r for r in self._records if r.outcome == OUTCOME_SL_HIT]
        expired = [r for r in self._records if r.outcome == OUTCOME_EXPIRED]
        decided = len(wins) + len(losses)

        win_rate = (len(wins) / decided * 100) if decided > 0 else 0.0

        avg_pnl  = sum(r.pnl_pct for r in self._records) / len(self._records)
        avg_win  = (sum(r.pnl_pct for r in wins)   / len(wins))   if wins   else 0.0
        avg_loss = (sum(r.pnl_pct for r in losses) / len(losses)) if losses else 0.0

        # 期待値 = (勝率 × 平均利益) + ((1 - 勝率) × 平均損失)
        wr = win_rate / 100
        expectancy = wr * avg_win + (1 - wr) * avg_loss if decided > 0 else 0.0

        total_pnl = sum(r.pnl_pct for r in self._records)

        recent = self._records[-recent_window:]
        recent_losses = sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT)

        return StatsSummary(
            total=len(self._records),
            wins=len(wins),
            losses=len(losses),
            expired=len(expired),
            win_rate=win_rate,
            avg_pnl=avg_pnl,
            avg_win=avg_win,
            avg_loss=avg_loss,
            expectancy=expectancy,
            total_pnl_pct=total_pnl,
            recent_losses=recent_losses,
            recent_window=recent_window,
        )

    def had_sl_within(self, symbol: str, hours: int) -> bool:
        """指定銘柄が `hours` 以内に SL_HIT で終わっていれば True。

        クールダウンに使う。
        """
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        for r in reversed(self._records):
            if r.symbol != symbol:
                continue
            try:
                closed_dt = datetime.fromisoformat(r.closed_at)
            except ValueError:
                continue
            if closed_dt < cutoff:
                return False
            if r.outcome == OUTCOME_SL_HIT:
                return True
        return False

    def circuit_breaker_active(
        self,
        window: int = 10,
        loss_threshold: int = 5,
    ) -> bool:
        """直近 `window` 件中 SL が `loss_threshold` 以上なら True。

        True の時は当サイクルのエントリーを全スキップする。
        """
        if len(self._records) < window:
            return False
        recent = self._records[-window:]
        recent_losses = sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT)
        return recent_losses >= loss_threshold

    def summary_by_conviction(self) -> dict[str, dict[str, Any]]:
        """conviction 別のミニサマリー（勝率分析用）。"""
        groups: dict[str, list[TradeRecord]] = {}
        for r in self._records:
            groups.setdefault(r.conviction, []).append(r)

        out: dict[str, dict[str, Any]] = {}
        for conv, records in groups.items():
            wins   = sum(1 for r in records if r.outcome == OUTCOME_TP_HIT)
            losses = sum(1 for r in records if r.outcome == OUTCOME_SL_HIT)
            decided = wins + losses
            wr = (wins / decided * 100) if decided > 0 else 0.0
            avg = sum(r.pnl_pct for r in records) / len(records) if records else 0.0
            out[conv] = {
                "total":    len(records),
                "wins":     wins,
                "losses":   losses,
                "win_rate": wr,
                "avg_pnl":  avg,
            }
        return out

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self) -> None:
        """トレード記録を JSON ファイルに保存する。"""
        self._file.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(r) for r in self._records]
        with self._file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        logger.debug("Stats saved: %d record(s).", len(self._records))

    def _load(self) -> None:
        """JSON ファイルから記録を読み込む。"""
        if not self._file.exists():
            logger.debug("No stats file found. Starting fresh.")
            return
        try:
            with self._file.open(encoding="utf-8") as f:
                data = json.load(f)
            self._records = [TradeRecord(**entry) for entry in data]
            logger.info("Loaded %d trade record(s) from stats file.", len(self._records))
        except Exception as e:
            logger.warning("Failed to load stats file: %s", e)
            self._records = []
