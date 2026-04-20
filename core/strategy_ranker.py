"""
core/strategy_ranker.py
直近 N サイクルの experiment_tracker データから
エントリー戦略の実質期待値ランキングを計算する。

実質期待値 (effective_ev) = fill_rate × avg_pnl
    - fill_rate: 戦略バリアントが実際に約定した割合 (未約定の機会損失を加味)
    - avg_pnl:   約定トレードの平均 PnL (%)

この値が高い戦略 = 現在の相場で最も利益を出している決定。
ライブ戦略は毎サイクル最新ランキングを参照し、
最もEVが高い実装可能戦略 (かつ EV > 0) を採用する。

出力は data/experiment_report.md セクション0「意思決定サマリー」と同じ値。
ロジックは tools/analyze_experiments._compute_strategy_ev を
ライブ側で再利用できる形に切り出したもの。
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.experiment import ExperimentTracker

logger = logging.getLogger(__name__)


@dataclass
class StrategyStat:
    strategy: str           # e.g. "MARKET", "LIMIT_1PCT", "LIMIT_9PCT_LONG"
    filled: int
    total: int
    avg_pnl: float          # 約定トレードの平均 PnL (%)
    fill_rate: float        # 0.0〜1.0
    effective_ev: float     # fill_rate × avg_pnl

    @property
    def is_long(self) -> bool:
        return self.strategy.endswith("_LONG")


class StrategyRanker:
    """experiment_tracker._closed から戦略ランキングを計算する。

    build() ごとに compute() を再計算する設計 (サイクル中に
    新しい確定トレードが加わっても即反映)。コストは直近 N 件 ×
    1トレード 30 variants 程度なので無視できる。
    """

    def __init__(
        self,
        experiment_tracker: "ExperimentTracker",
        *,
        recent_n: int = 20,
        min_filled: int = 2,
    ) -> None:
        self._exp = experiment_tracker
        self._recent_n = recent_n
        self._min_filled = min_filled

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def compute(self) -> list[StrategyStat]:
        """直近 N 件の closed shadow trades から戦略ごとの EV を計算し、
        effective_ev 降順でソートして返す。
        """
        closed = getattr(self._exp, "_closed", None) or []
        trades = closed[-self._recent_n:] if self._recent_n > 0 else closed

        totals: dict[str, int] = {}
        pnls: dict[str, list[float]] = {}

        for t in trades:
            variants = getattr(t, "entry_variants", None)
            if not variants:
                continue
            for v in variants:
                strat = getattr(v, "strategy", None)
                if not strat:
                    continue
                totals[strat] = totals.get(strat, 0) + 1
                pnl = getattr(v, "pnl_pct", None)
                if getattr(v, "filled", False) and pnl is not None:
                    pnls.setdefault(strat, []).append(float(pnl))

        stats: list[StrategyStat] = []
        for strat, total in totals.items():
            arr = pnls.get(strat, [])
            filled = len(arr)
            if filled == 0:
                continue
            avg_pnl = sum(arr) / filled
            fill_rate = filled / total
            ev = fill_rate * avg_pnl
            stats.append(StrategyStat(
                strategy=strat,
                filled=filled,
                total=total,
                avg_pnl=avg_pnl,
                fill_rate=fill_rate,
                effective_ev=ev,
            ))

        stats.sort(key=lambda s: s.effective_ev, reverse=True)
        return stats

    def top(
        self,
        *,
        is_long: bool | None = None,
        allow: set[str] | None = None,
    ) -> StrategyStat | None:
        """条件に合う戦略のうち最も effective_ev が高いものを返す。

        Args:
            is_long: None なら方向不問、True なら LONG のみ、False なら SHORT のみ
            allow:   許可する戦略名セット (None なら全戦略)
        """
        for s in self.compute():
            if s.filled < self._min_filled:
                continue
            if is_long is not None and s.is_long != is_long:
                continue
            if allow is not None and s.strategy not in allow:
                continue
            return s
        return None
