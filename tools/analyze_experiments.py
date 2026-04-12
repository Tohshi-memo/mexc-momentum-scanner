"""
tools/analyze_experiments.py
シャドウトレード（data/experiments.json）の集計レポート生成。

目的:
    現在の STRICT フィルターは厳しすぎる可能性がある。
    全候補を仮想追跡しているシャドウトレードのデータから、
    各フィルターの「閾値ごとの PnL 性能」を測定する。
    結果は data/experiment_report.md に Markdown で書き出され、
    Claude (このリポジトリを読んだ次回セッション) が再評価できる。

レポート内容:
    1. ベースライン (全候補 / STRICT 通過 / STRICT 外)
    2. RSI 1h 閾値スイープ
    3. RSI 4h 上限スイープ
    4. BB ブレイク要否
    5. 出来高トレンドフィルター粒度
    6. 相対強度 (vs BTC) 閾値スイープ
    7. マーケットレジーム別
    8. 組み合わせ (RSI × 4h × Volume) ヒートマップ
    9. 勝敗別の指標分布 (winners vs losers)

CLI:
    python tools/analyze_experiments.py
    python tools/analyze_experiments.py --in data/experiments.json --out data/experiment_report.md

main.py から内部的にも呼び出される (各サイクル後にレポートを再生成)。
"""
from __future__ import annotations

import argparse
import json
import logging
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

logger = logging.getLogger(__name__)

DEFAULT_INPUT  = Path("data/experiments.json")
DEFAULT_OUTPUT = Path("data/experiment_report.md")

OUTCOME_TP_HIT  = "TP_HIT"
OUTCOME_SL_HIT  = "SL_HIT"
OUTCOME_EXPIRED = "EXPIRED"


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

@dataclass
class ClosedTrade:
    """experiments.json から復元したクローズ済みシャドウトレード。

    フラットな辞書に近い構造に変換しておくことで、
    集計関数からは属性アクセスのみで済む。
    """
    symbol: str
    detected_at: str
    confirmed_strict: bool
    market_regime: str
    outcome: str
    pnl_pct: float
    hours_held: float
    sl_pct: float
    tp_pct: float
    max_favorable_pct: float
    max_adverse_pct: float

    # filters snapshot
    rsi: float | None
    rsi_4h: float | None
    bb_upper: float | None
    price_vs_bb: float
    volume_ratio: float
    volume_trend: str
    atr_pct: float | None
    change_1h: float
    relative_strength: float
    btc_change_1h: float


def _load_closed(path: Path) -> list[ClosedTrade]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    closed: list[ClosedTrade] = []
    for entry in data.get("closed", []):
        if entry.get("pnl_pct") is None:
            continue
        f_dict = entry.get("filters") or {}
        closed.append(
            ClosedTrade(
                symbol=entry.get("symbol", ""),
                detected_at=entry.get("detected_at", ""),
                confirmed_strict=bool(entry.get("confirmed_strict", False)),
                market_regime=entry.get("market_regime", "UNKNOWN"),
                outcome=entry.get("outcome", ""),
                pnl_pct=float(entry.get("pnl_pct") or 0.0),
                hours_held=float(entry.get("hours_held") or 0.0),
                sl_pct=float(entry.get("sl_pct") or 0.0),
                tp_pct=float(entry.get("tp_pct") or 0.0),
                max_favorable_pct=float(entry.get("max_favorable_pct") or 0.0),
                max_adverse_pct=float(entry.get("max_adverse_pct") or 0.0),
                rsi=f_dict.get("rsi"),
                rsi_4h=f_dict.get("rsi_4h"),
                bb_upper=f_dict.get("bb_upper"),
                price_vs_bb=float(f_dict.get("price_vs_bb") or 0.0),
                volume_ratio=float(f_dict.get("volume_ratio") or 0.0),
                volume_trend=f_dict.get("volume_trend", "FLAT"),
                atr_pct=f_dict.get("atr_pct"),
                change_1h=float(f_dict.get("change_1h") or 0.0),
                relative_strength=float(f_dict.get("relative_strength") or 0.0),
                btc_change_1h=float(f_dict.get("btc_change_1h") or 0.0),
            )
        )
    return closed


# ---------------------------------------------------------------------------
# Aggregation primitives
# ---------------------------------------------------------------------------

@dataclass
class Stats:
    """1グループ分の集計結果。"""
    n: int
    wins: int       # TP_HIT
    losses: int     # SL_HIT
    expired: int    # EXPIRED
    win_rate: float
    avg_win: float
    avg_loss: float
    expectancy: float  # 平均 pnl_pct
    total_pnl: float
    median_hold_h: float


EMPTY_STATS = Stats(0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)


def _compute_stats(trades: Iterable[ClosedTrade]) -> Stats:
    items = list(trades)
    if not items:
        return EMPTY_STATS

    wins    = [t for t in items if t.outcome == OUTCOME_TP_HIT]
    losses  = [t for t in items if t.outcome == OUTCOME_SL_HIT]
    expired = [t for t in items if t.outcome == OUTCOME_EXPIRED]

    n = len(items)
    win_rate    = len(wins) / n * 100 if n else 0.0
    avg_win     = statistics.mean(t.pnl_pct for t in wins)   if wins   else 0.0
    avg_loss    = statistics.mean(t.pnl_pct for t in losses) if losses else 0.0
    expectancy  = statistics.mean(t.pnl_pct for t in items)
    total_pnl   = sum(t.pnl_pct for t in items)
    median_hold = statistics.median(t.hours_held for t in items)

    return Stats(
        n=n,
        wins=len(wins),
        losses=len(losses),
        expired=len(expired),
        win_rate=win_rate,
        avg_win=avg_win,
        avg_loss=avg_loss,
        expectancy=expectancy,
        total_pnl=total_pnl,
        median_hold_h=median_hold,
    )


def _filter(
    trades: list[ClosedTrade],
    predicate: Callable[[ClosedTrade], bool],
) -> list[ClosedTrade]:
    return [t for t in trades if predicate(t)]


# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------

def _row(label: str, s: Stats) -> str:
    if s.n == 0:
        return f"| {label} | 0 | – | – | – | – | – | – | – |"
    return (
        f"| {label} | {s.n} | {s.wins}/{s.losses}/{s.expired} | "
        f"{s.win_rate:.1f}% | {s.avg_win:+.2f}% | {s.avg_loss:+.2f}% | "
        f"{s.expectancy:+.2f}% | {s.total_pnl:+.1f}% | {s.median_hold_h:.1f}h |"
    )


TABLE_HEADER = (
    "| group | n | W/L/E | win% | avg win | avg loss | expectancy | total PnL | median hold |\n"
    "|-------|---|-------|------|---------|----------|------------|-----------|-------------|"
)


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def _section_baseline(closed: list[ClosedTrade]) -> str:
    strict   = _filter(closed, lambda t: t.confirmed_strict)
    relaxed  = _filter(closed, lambda t: not t.confirmed_strict)
    lines = [
        "## 1. Baseline",
        "",
        TABLE_HEADER,
        _row("ALL candidates",      _compute_stats(closed)),
        _row("STRICT (current)",    _compute_stats(strict)),
        _row("REJECTED by STRICT",  _compute_stats(relaxed)),
        "",
        "**読み方**: STRICT が REJECTED より expectancy が高ければ現フィルターは有効。"
        "REJECTED の方が良ければフィルターを緩めるべき。",
    ]
    return "\n".join(lines)


def _section_rsi_sweep(closed: list[ClosedTrade]) -> str:
    """RSI 1h 閾値ごとに『その閾値以上を採用していたら』の集計。"""
    thresholds = [60.0, 65.0, 70.0, 75.0, 80.0]
    lines = [
        "## 2. RSI(1h) threshold sweep",
        "",
        "現行 STRICT は RSI ≥ 75。閾値を変えた場合の仮想成績。",
        "",
        TABLE_HEADER,
    ]
    for th in thresholds:
        subset = _filter(closed, lambda t, th=th: t.rsi is not None and t.rsi >= th)
        lines.append(_row(f"RSI ≥ {th:.0f}", _compute_stats(subset)))
    lines.append("")
    return "\n".join(lines)


def _section_rsi_4h_sweep(closed: list[ClosedTrade]) -> str:
    """4h RSI 上限スイープ。OFF は 4h フィルター無効と等価。"""
    thresholds = [60.0, 65.0, 70.0, 75.0]
    lines = [
        "## 3. RSI(4h) maximum sweep",
        "",
        "現行 STRICT は 4h RSI < 70。低いほど厳しい (既存トレンドを除外)。",
        "OFF = 4h フィルター無効。",
        "",
        TABLE_HEADER,
    ]
    for th in thresholds:
        subset = _filter(
            closed,
            lambda t, th=th: t.rsi_4h is None or t.rsi_4h < th,
        )
        lines.append(_row(f"4h RSI < {th:.0f}", _compute_stats(subset)))
    lines.append(_row("OFF (no 4h filter)", _compute_stats(closed)))
    lines.append("")
    return "\n".join(lines)


def _section_bb(closed: list[ClosedTrade]) -> str:
    bb_break  = _filter(closed, lambda t: t.price_vs_bb > 1.0)
    no_break  = _filter(closed, lambda t: t.price_vs_bb <= 1.0)
    lines = [
        "## 4. BB upper break requirement",
        "",
        "現行 STRICT は price > BB upper(2σ) 必須。",
        "",
        TABLE_HEADER,
        _row("BB break required",  _compute_stats(bb_break)),
        _row("BB break NOT required (all)", _compute_stats(closed)),
        _row("BB no-break only",    _compute_stats(no_break)),
        "",
    ]
    return "\n".join(lines)


def _section_volume(closed: list[ClosedTrade]) -> str:
    not_rising  = _filter(closed, lambda t: t.volume_trend != "RISING")
    declining   = _filter(closed, lambda t: t.volume_trend == "DECLINING")
    flat        = _filter(closed, lambda t: t.volume_trend == "FLAT")
    rising      = _filter(closed, lambda t: t.volume_trend == "RISING")
    lines = [
        "## 5. Volume trend filter",
        "",
        "現行 STRICT は『RISING を除外』(疲弊兆候のみショート)。",
        "",
        TABLE_HEADER,
        _row("ALL volume trends",         _compute_stats(closed)),
        _row("NOT RISING (current)",      _compute_stats(not_rising)),
        _row("DECLINING only (strictest)", _compute_stats(declining)),
        _row("FLAT only",                 _compute_stats(flat)),
        _row("RISING only",               _compute_stats(rising)),
        "",
    ]
    return "\n".join(lines)


def _section_relative_strength(closed: list[ClosedTrade]) -> str:
    thresholds = [0.0, 3.0, 5.0, 7.0, 10.0]
    lines = [
        "## 6. Relative strength (vs BTC) threshold sweep",
        "",
        "現行スキャナーは alt_1h - btc_1h ≥ 5.0% でフィルター。",
        "閾値を変えた場合の仮想成績。",
        "",
        TABLE_HEADER,
    ]
    for th in thresholds:
        subset = _filter(closed, lambda t, th=th: t.relative_strength >= th)
        lines.append(_row(f"rel strength ≥ {th:.0f}%", _compute_stats(subset)))
    lines.append("")
    return "\n".join(lines)


def _section_regime(closed: list[ClosedTrade]) -> str:
    regimes = ["BEARISH", "STAGNANT", "BULLISH"]
    lines = [
        "## 7. Market regime breakdown",
        "",
        "BTC 1h change によるレジーム別の成績。",
        "",
        TABLE_HEADER,
    ]
    for r in regimes:
        subset = _filter(closed, lambda t, r=r: t.market_regime == r)
        lines.append(_row(r, _compute_stats(subset)))
    lines.append("")
    return "\n".join(lines)


def _section_combined(closed: list[ClosedTrade]) -> str:
    """RSI × 4h × volume の組み合わせ。"""
    combos = [
        ("STRICT (RSI≥75 & 4h<70 & ¬RISING)",
         lambda t: (t.rsi is not None and t.rsi >= 75)
                   and (t.rsi_4h is None or t.rsi_4h < 70)
                   and t.volume_trend != "RISING"),
        ("RSI≥70 & 4h<70 & ¬RISING",
         lambda t: (t.rsi is not None and t.rsi >= 70)
                   and (t.rsi_4h is None or t.rsi_4h < 70)
                   and t.volume_trend != "RISING"),
        ("RSI≥70 & 4h<75 & ¬RISING",
         lambda t: (t.rsi is not None and t.rsi >= 70)
                   and (t.rsi_4h is None or t.rsi_4h < 75)
                   and t.volume_trend != "RISING"),
        ("RSI≥70 & ¬RISING (no 4h)",
         lambda t: (t.rsi is not None and t.rsi >= 70)
                   and t.volume_trend != "RISING"),
        ("RSI≥65 & 4h<70 & DECLINING",
         lambda t: (t.rsi is not None and t.rsi >= 65)
                   and (t.rsi_4h is None or t.rsi_4h < 70)
                   and t.volume_trend == "DECLINING"),
    ]
    lines = [
        "## 8. Combined filters",
        "",
        "代表的なフィルターの組み合わせの仮想成績。",
        "",
        TABLE_HEADER,
    ]
    for label, pred in combos:
        subset = _filter(closed, pred)
        lines.append(_row(label, _compute_stats(subset)))
    lines.append("")
    return "\n".join(lines)


def _section_distribution(closed: list[ClosedTrade]) -> str:
    """勝者 / 敗者 の指標平均値を比較する。"""
    wins   = _filter(closed, lambda t: t.outcome == OUTCOME_TP_HIT)
    losses = _filter(closed, lambda t: t.outcome == OUTCOME_SL_HIT)

    def _avg(items: list[ClosedTrade], attr: str) -> str:
        vals = [getattr(t, attr) for t in items if getattr(t, attr) is not None]
        return f"{statistics.mean(vals):+.2f}" if vals else "–"

    rows = [
        ("RSI(1h)",          "rsi"),
        ("RSI(4h)",          "rsi_4h"),
        ("price/BB upper",   "price_vs_bb"),
        ("volume ratio",     "volume_ratio"),
        ("ATR%",             "atr_pct"),
        ("change_1h",        "change_1h"),
        ("rel strength",     "relative_strength"),
        ("btc 1h change",    "btc_change_1h"),
    ]
    lines = [
        "## 9. Indicator distribution: winners vs losers",
        "",
        "TP_HIT と SL_HIT の指標平均。乖離が大きい指標が予測力を持つ可能性あり。",
        "",
        "| indicator | wins (avg) | losses (avg) | delta |",
        "|-----------|------------|--------------|-------|",
    ]
    for label, attr in rows:
        w_str = _avg(wins, attr)
        l_str = _avg(losses, attr)
        try:
            delta = float(w_str) - float(l_str)
            d_str = f"{delta:+.2f}"
        except ValueError:
            d_str = "–"
        lines.append(f"| {label} | {w_str} | {l_str} | {d_str} |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Top-level report builder
# ---------------------------------------------------------------------------

def generate_report(
    input_path: Path = DEFAULT_INPUT,
    output_path: Path = DEFAULT_OUTPUT,
) -> Path:
    """experiments.json を読み込み Markdown レポートを書き出す。

    Returns:
        書き出した Markdown ファイルのパス。
    """
    closed = _load_closed(input_path)

    header = [
        "# Filter Granularity Experiment Report",
        "",
        f"- source: `{input_path}`",
        f"- closed shadow trades: **{len(closed)}**",
        "",
        "シャドウトレードは『現行 STRICT フィルターを通ったか否かに関わらず』",
        "全ての急騰候補を仮想エントリーとして追跡している。各レコードは",
        "検出時のフィルター値スナップショットを持つため、後から任意の閾値で",
        "再評価できる。Claude (次回セッション) は本レポートと",
        "`data/experiments.json` を読み、フィルターの粒度をチューニングできる。",
        "",
        "---",
        "",
    ]

    if not closed:
        body = [
            "## No data yet",
            "",
            "シャドウトレードがまだクローズしていません。",
            "数サイクル動かしてから再生成してください。",
        ]
        text = "\n".join(header + body) + "\n"
    else:
        sections = [
            _section_baseline(closed),
            _section_rsi_sweep(closed),
            _section_rsi_4h_sweep(closed),
            _section_bb(closed),
            _section_volume(closed),
            _section_relative_strength(closed),
            _section_regime(closed),
            _section_combined(closed),
            _section_distribution(closed),
        ]
        body = [
            "**凡例**: W/L/E = TP_HIT / SL_HIT / EXPIRED. ",
            "expectancy = 1トレードあたりの平均 PnL (%)。",
            "ショート視点なので **+ が利益**, **- が損失** であることに注意。",
            "",
            "---",
            "",
            "\n\n---\n\n".join(sections),
        ]
        text = "\n".join(header + body) + "\n"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    logger.info(
        "Experiment report written: %s (%d closed trades)",
        output_path, len(closed),
    )
    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate filter-granularity PnL report from shadow trades."
    )
    p.add_argument("--in",  dest="input",  default=str(DEFAULT_INPUT),
                   help="path to experiments.json")
    p.add_argument("--out", dest="output", default=str(DEFAULT_OUTPUT),
                   help="path to write the markdown report")
    return p.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = _parse_args()
    path = generate_report(Path(args.input), Path(args.output))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
