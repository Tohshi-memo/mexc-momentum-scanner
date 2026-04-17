"""
tools/strategy_selector.py
experiments.json から「いま機能している戦略」を選定する。

各 entry_variants (MARKET / ASK / LIMIT_Xpct(_LONG) / LIMIT_BB3S / LIMIT_ATR /
LIMIT_FIB1272(_LONG) / LIMIT_FIB1618(_LONG) etc.) について、直近 N 件の
filled trades から実質期待値 (fill率 × avg PnL) を計算し、LONG/SHORT それぞれ
のチャンピオン戦略を返す。

出力は辞書:
    {
        "short": {
            "strategy": "LIMIT_5PCT",
            "recent_filled": 10,
            "recent_avg_pnl": 3.49,
            "recent_expectancy": 1.74,
            "overall_filled": 386,
            "overall_avg_pnl": 0.92,
            "overall_expectancy": 0.36,
            "alive": True,                    # 期待値プラスなら採用
        },
        "long": {...},
        "meta": {"total_closed": 1043, "recent_window": 20, "min_filled": 5},
    }

alive=False なら該当方向のキルスイッチ ON（その方向では発注しない）。
"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

EXPERIMENT_FILE = Path("data/experiments.json")

RECENT_WINDOW = 20   # 直近 N クローズ済みトレードを相場感の指標にする
MIN_FILLED    = 5    # 直近 window で最低これだけ filled が必要 (ノイズ除去)


@dataclass
class VariantStats:
    strategy: str
    recent_filled: int
    recent_total: int
    recent_avg_pnl: float
    recent_expectancy: float
    overall_filled: int
    overall_total: int
    overall_avg_pnl: float
    overall_expectancy: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "strategy": self.strategy,
            "recent_filled": self.recent_filled,
            "recent_total": self.recent_total,
            "recent_avg_pnl": round(self.recent_avg_pnl, 4),
            "recent_expectancy": round(self.recent_expectancy, 4),
            "overall_filled": self.overall_filled,
            "overall_total": self.overall_total,
            "overall_avg_pnl": round(self.overall_avg_pnl, 4),
            "overall_expectancy": round(self.overall_expectancy, 4),
        }


def _load() -> list[dict[str, Any]]:
    if not EXPERIMENT_FILE.exists():
        return []
    with EXPERIMENT_FILE.open(encoding="utf-8") as f:
        data = json.load(f)
    closed = data.get("closed", [])
    return closed if isinstance(closed, list) else []


def _collect_variant_pnls(
    closed: list[dict[str, Any]],
) -> tuple[
    dict[str, list[float]],
    dict[str, int],
    dict[str, list[float]],
    dict[str, int],
]:
    overall_pnls:  dict[str, list[float]] = defaultdict(list)
    overall_total: dict[str, int]         = defaultdict(int)

    sorted_trades = sorted(closed, key=lambda t: t.get("detected_at", ""))
    recent_trades = sorted_trades[-RECENT_WINDOW:]

    def _accumulate(
        trades: list[dict[str, Any]],
        pnls: dict[str, list[float]],
        total: dict[str, int],
    ) -> None:
        for t in trades:
            for v in (t.get("entry_variants") or []):
                s = v.get("strategy")
                if not s:
                    continue
                total[s] += 1
                if v.get("filled") and v.get("pnl_pct") is not None:
                    pnls[s].append(float(v["pnl_pct"]))

    _accumulate(sorted_trades, overall_pnls, overall_total)

    recent_pnls:  dict[str, list[float]] = defaultdict(list)
    recent_total: dict[str, int]         = defaultdict(int)
    _accumulate(recent_trades, recent_pnls, recent_total)

    return overall_pnls, overall_total, recent_pnls, recent_total


def _compute_stats(
    overall_pnls: dict[str, list[float]],
    overall_total: dict[str, int],
    recent_pnls:  dict[str, list[float]],
    recent_total: dict[str, int],
) -> list[VariantStats]:
    stats: list[VariantStats] = []
    for strategy, recent_list in recent_pnls.items():
        r_filled = len(recent_list)
        r_total  = recent_total.get(strategy, 0)
        if r_filled < MIN_FILLED or r_total == 0:
            continue
        r_avg   = sum(recent_list) / r_filled
        r_fill  = r_filled / r_total
        r_exp   = r_fill * r_avg

        o_list   = overall_pnls.get(strategy, [])
        o_filled = len(o_list)
        o_total  = overall_total.get(strategy, 0) or 1
        o_avg    = (sum(o_list) / o_filled) if o_filled > 0 else 0.0
        o_fill   = o_filled / o_total
        o_exp    = o_fill * o_avg

        stats.append(VariantStats(
            strategy=strategy,
            recent_filled=r_filled,
            recent_total=r_total,
            recent_avg_pnl=r_avg,
            recent_expectancy=r_exp,
            overall_filled=o_filled,
            overall_total=o_total,
            overall_avg_pnl=o_avg,
            overall_expectancy=o_exp,
        ))
    return stats


def select_leaders() -> dict[str, Any]:
    """LONG/SHORT 方向ごとの現チャンピオン戦略を返す。"""
    closed = _load()
    overall_pnls, overall_total, recent_pnls, recent_total = _collect_variant_pnls(closed)
    all_stats = _compute_stats(overall_pnls, overall_total, recent_pnls, recent_total)

    long_stats  = [s for s in all_stats if s.strategy.endswith("_LONG")]
    short_stats = [s for s in all_stats if not s.strategy.endswith("_LONG")]

    long_stats.sort(key=lambda s: s.recent_expectancy, reverse=True)
    short_stats.sort(key=lambda s: s.recent_expectancy, reverse=True)

    def _pack(stats_list: list[VariantStats]) -> dict[str, Any]:
        if not stats_list:
            return {"strategy": None, "alive": False, "reason": "no_data"}
        top = stats_list[0]
        alive = top.recent_expectancy > 0
        payload = top.to_dict()
        payload["alive"] = alive
        if not alive:
            payload["reason"] = "negative_recent_expectancy"
        return payload

    return {
        "short": _pack(short_stats),
        "long":  _pack(long_stats),
        "meta": {
            "total_closed": len(closed),
            "recent_window": RECENT_WINDOW,
            "min_filled":    MIN_FILLED,
        },
    }


if __name__ == "__main__":
    import sys
    leaders = select_leaders()
    json.dump(leaders, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
