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
    1.  ベースライン (全候補 / STRICT 通過 / STRICT 外)
    2.  RSI 1h 閾値スイープ
    3.  RSI 4h 方向分析 (旧: < X / 新: ≥ X)
    4.  BB ブレイク要否
    5.  出来高トレンドフィルター粒度
    6.  相対強度 (vs BTC) 閾値スイープ
    7.  ATR% ゾーン分析
    8.  MFE / MAE 分析
    9.  マーケットレジーム別
    10. ファンダメンタル / ニュース
    11. 組み合わせフィルター (旧 STRICT vs 新候補)
    12. エントリー戦略比較
    13. 勝敗別の指標分布
    14. フィルター推奨

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

    # fundamental
    catalyst_type: str
    short_conviction: str
    news_count: int

    # spread / entry variants
    spread_pct: float | None
    entry_variants: list[dict] | None   # raw dicts from JSON


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
                catalyst_type=entry.get("catalyst_type", "UNKNOWN"),
                short_conviction=entry.get("short_conviction", "UNKNOWN"),
                news_count=int(entry.get("news_count", -1)),
                relative_strength=float(f_dict.get("relative_strength") or 0.0),
                btc_change_1h=float(f_dict.get("btc_change_1h") or 0.0),
                spread_pct=entry.get("spread_pct"),
                entry_variants=entry.get("entry_variants"),
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
    """4h RSI 方向分析。旧方向 (< X) と新方向 (≥ X) の両方を比較。"""
    lines = [
        "## 3. RSI(4h) direction analysis",
        "",
        "> **重要発見**: 4h RSI が**高い**ほどショートの勝率・期待値が向上する。",
        "> 旧フィルター（4h RSI < 70）は「4h がまだ低い = 新鮮な急騰」を狙っていたが、",
        "> 実際には「1h も 4h も過熱 = ダブルオーバーボート」の方が反転しやすい。",
        "",
        "### 3a. 旧方向 (4h RSI < X): 低 4h のみ採用（旧 STRICT）",
        "",
        TABLE_HEADER,
    ]
    for th in [60.0, 65.0, 70.0, 75.0]:
        subset = _filter(
            closed,
            lambda t, th=th: t.rsi_4h is None or t.rsi_4h < th,
        )
        lines.append(_row(f"4h RSI < {th:.0f}", _compute_stats(subset)))
    lines.append(_row("OFF (no 4h filter)", _compute_stats(closed)))

    lines += [
        "",
        "### 3b. 新方向 (4h RSI ≥ X): 高 4h のみ採用（推奨）",
        "",
        TABLE_HEADER,
    ]
    for th in [60.0, 65.0, 70.0, 75.0, 80.0]:
        subset = _filter(
            closed,
            lambda t, th=th: t.rsi_4h is not None and t.rsi_4h >= th,
        )
        lines.append(_row(f"4h RSI ≥ {th:.0f}", _compute_stats(subset)))
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


def _section_atr_zone(closed: list[ClosedTrade]) -> str:
    """ATR% ゾーン別の成績。ボラティリティの大小による影響。"""
    zones: list[tuple[str, Callable[[ClosedTrade], bool]]] = [
        ("ATR < 5%",     lambda t: (t.atr_pct or 0) < 5),
        ("ATR 5–7%",     lambda t: 5 <= (t.atr_pct or 0) < 7),
        ("ATR 7–9%",     lambda t: 7 <= (t.atr_pct or 0) < 9),
        ("ATR 9–11%",    lambda t: 9 <= (t.atr_pct or 0) < 11),
        ("ATR ≥ 11%",    lambda t: (t.atr_pct or 0) >= 11),
    ]
    lines = [
        "## 7. ATR% zone analysis",
        "",
        "ATR% = ATR / price × 100。ボラティリティの大きさ別の成績。",
        "高すぎると SL が刈られやすく、低すぎると値動きが小さい。",
        "",
        TABLE_HEADER,
    ]
    for label, pred in zones:
        subset = _filter(closed, pred)
        lines.append(_row(label, _compute_stats(subset)))
    lines.append("")
    return "\n".join(lines)


def _section_mfe_mae(closed: list[ClosedTrade]) -> str:
    """MFE/MAE 分析。勝ちトレードと負けトレードの値動き特性。"""
    wins   = _filter(closed, lambda t: t.outcome == OUTCOME_TP_HIT)
    losses = _filter(closed, lambda t: t.outcome == OUTCOME_SL_HIT)

    def _stat(items: list[ClosedTrade], attr: str) -> str:
        vals = [getattr(t, attr) for t in items if getattr(t, attr)]
        if not vals:
            return "n/a"
        return f"avg={statistics.mean(vals):+.2f}%  max={max(vals):+.2f}%"

    lines = [
        "## 8. MFE / MAE analysis",
        "",
        "MFE (Maximum Favorable Excursion) = エントリー後の最大含み益 (%)。",
        "MAE (Maximum Adverse Excursion) = エントリー後の最大含み損 (%)。",
        "ショート視点: 価格が下がれば MFE+, 上がれば MAE-。",
        "",
        "| group | n | MFE (avg) | MFE (max) | MAE (avg) | MAE (worst) |",
        "|-------|---|-----------|-----------|-----------|-------------|",
    ]

    for label, items in [("ALL", closed), ("TP_HIT", wins), ("SL_HIT", losses)]:
        mfe = [t.max_favorable_pct for t in items if t.max_favorable_pct]
        mae = [t.max_adverse_pct for t in items if t.max_adverse_pct]
        if not mfe:
            lines.append(f"| {label} | {len(items)} | – | – | – | – |")
            continue
        lines.append(
            f"| {label} | {len(items)} "
            f"| {statistics.mean(mfe):+.2f}% | {max(mfe):+.2f}% "
            f"| {statistics.mean(mae):+.2f}% | {min(mae):+.2f}% |"
        )
    lines += [
        "",
        "**読み方**: SL_HIT の MFE が低い = ほとんど有利に動かずに SL 到達。",
        "TP_HIT の MAE が浅い = 含み損が少なく順調に TP 到達。",
    ]
    lines.append("")
    return "\n".join(lines)


def _section_regime(closed: list[ClosedTrade]) -> str:
    regimes = ["BEARISH", "STAGNANT", "BULLISH"]
    lines = [
        "## 9. Market regime breakdown",
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


def _section_fundamental(closed: list[ClosedTrade]) -> str:
    """ファンダメンタル (ニュースの有無 / conviction) 別の成績。"""
    convictions = ["HIGH", "MEDIUM", "LOW", "AVOID", "UNKNOWN"]
    catalysts   = ["NONE", "POSITIVE", "NEGATIVE", "WEAK", "UNKNOWN"]

    has_funda = _filter(closed, lambda t: t.short_conviction != "UNKNOWN")
    no_funda  = _filter(closed, lambda t: t.short_conviction == "UNKNOWN")

    lines = [
        "## 10. Fundamental / news",
        "",
        "ファンダメンタル分析は confirmed シグナルのみに実行される。",
        "UNKNOWN = ファンダ未取得 (rejected 候補)。",
        "",
        "### By short conviction",
        "",
        TABLE_HEADER,
    ]
    for c in convictions:
        subset = _filter(closed, lambda t, c=c: t.short_conviction == c)
        lines.append(_row(c, _compute_stats(subset)))

    lines += [
        "",
        "### By catalyst type",
        "",
        TABLE_HEADER,
    ]
    for c in catalysts:
        subset = _filter(closed, lambda t, c=c: t.catalyst_type == c)
        lines.append(_row(c, _compute_stats(subset)))

    lines += [
        "",
        f"ファンダ取得済み: {len(has_funda)} 件, 未取得: {len(no_funda)} 件",
        "",
    ]
    return "\n".join(lines)


def _section_combined(closed: list[ClosedTrade]) -> str:
    """旧 STRICT vs データ駆動の新フィルター候補の比較。"""
    combos: list[tuple[str, Callable[[ClosedTrade], bool]]] = [
        # --- 旧 STRICT (参考) ---
        ("旧 STRICT (RSI≥75 & 4h<70 & BB & ¬RISING)",
         lambda t: (t.rsi is not None and t.rsi >= 75)
                   and (t.rsi_4h is None or t.rsi_4h < 70)
                   and t.price_vs_bb > 1.0
                   and t.volume_trend != "RISING"),
        # --- 4h RSI 方向反転ベースの候補 ---
        ("RSI≥75 & 4h≥75",
         lambda t: (t.rsi is not None and t.rsi >= 75)
                   and (t.rsi_4h is not None and t.rsi_4h >= 75)),
        ("RSI≥75 & 4h≥75 & ¬RISING",
         lambda t: (t.rsi is not None and t.rsi >= 75)
                   and (t.rsi_4h is not None and t.rsi_4h >= 75)
                   and t.volume_trend != "RISING"),
        ("RSI≥70 & 4h≥70 & ¬RISING",
         lambda t: (t.rsi is not None and t.rsi >= 70)
                   and (t.rsi_4h is not None and t.rsi_4h >= 70)
                   and t.volume_trend != "RISING"),
        ("RSI≥65 & 4h≥75 & ¬RISING",
         lambda t: (t.rsi is not None and t.rsi >= 65)
                   and (t.rsi_4h is not None and t.rsi_4h >= 75)
                   and t.volume_trend != "RISING"),
        ("RSI≥65 & 4h≥70 & ¬RISING",
         lambda t: (t.rsi is not None and t.rsi >= 65)
                   and (t.rsi_4h is not None and t.rsi_4h >= 70)
                   and t.volume_trend != "RISING"),
        # --- ATR ゾーン追加 ---
        ("RSI≥65 & 4h≥70 & ¬RISING & ATR 5–9%",
         lambda t: (t.rsi is not None and t.rsi >= 65)
                   and (t.rsi_4h is not None and t.rsi_4h >= 70)
                   and t.volume_trend != "RISING"
                   and 5 <= (t.atr_pct or 0) < 9),
        # --- FLAT のみ ---
        ("RSI≥65 & 4h≥70 & FLAT",
         lambda t: (t.rsi is not None and t.rsi >= 65)
                   and (t.rsi_4h is not None and t.rsi_4h >= 70)
                   and t.volume_trend == "FLAT"),
    ]
    lines = [
        "## 11. Combined filters",
        "",
        "旧 STRICT と、データに基づくフィルター候補の比較。",
        "4h RSI 方向を反転（≥ を要求）した上で各種組み合わせを評価。",
        "",
        TABLE_HEADER,
    ]
    for label, pred in combos:
        subset = _filter(closed, pred)
        lines.append(_row(label, _compute_stats(subset)))
    lines.append("")
    return "\n".join(lines)


def _section_entry_strategy(closed: list[ClosedTrade]) -> str:
    """エントリー戦略バリアントの比較。データ内に存在する全戦略を自動検出。"""
    # スプレッド統計
    spreads = [t.spread_pct for t in closed if t.spread_pct is not None]
    spread_lines: list[str] = []
    if spreads:
        avg_spread = statistics.mean(spreads)
        med_spread = statistics.median(spreads)
        max_spread = max(spreads)
        spread_lines = [
            f"- 平均スプレッド: {avg_spread:.3f}%",
            f"- 中央値スプレッド: {med_spread:.3f}%",
            f"- 最大スプレッド: {max_spread:.3f}%",
            f"- スプレッドデータ有り: {len(spreads)} / {len(closed)} 件",
        ]
    else:
        spread_lines = ["- スプレッドデータなし (order book 未取得の古いレコード)"]

    # バリアント別 PnL 集計 (データ内のすべての戦略を自動検出)
    # filled=True で pnl_pct が確定しているもののみ集計
    # filled=False で EXPIRED のものは "unfilled" としてカウント
    strategy_data: dict[str, dict] = {}

    for t in closed:
        if not t.entry_variants:
            continue
        for v in t.entry_variants:
            s = v.get("strategy", "?")
            if s not in strategy_data:
                strategy_data[s] = {
                    "total": 0, "filled": 0, "unfilled": 0,
                    "pnls": [], "tp": 0, "sl": 0,
                }
            d = strategy_data[s]
            d["total"] += 1
            outcome = v.get("outcome", "")
            pnl = v.get("pnl_pct")
            if v.get("filled"):
                d["filled"] += 1
                if pnl is not None:
                    d["pnls"].append(float(pnl))
                if outcome == "TP_HIT":
                    d["tp"] += 1
                elif outcome == "SL_HIT":
                    d["sl"] += 1
            else:
                d["unfilled"] += 1

    # 表示順: MARKET / ASK / 任意 % / テクニカル の順
    order = [
        "MARKET", "ASK",
        "LIMIT_1PCT", "LIMIT_2PCT", "LIMIT_3PCT", "LIMIT_4PCT", "LIMIT_5PCT",
        "LIMIT_BB3S", "LIMIT_ATR",
        "LIMIT_FIB1272", "LIMIT_FIB1618",
    ]
    # データに存在するが order 未定義の戦略も末尾に追加
    all_strategies = order + [s for s in strategy_data if s not in order]

    var_header = (
        "| strategy | filled/total | unfilled | avg PnL | total PnL | win% | "
        "TP | SL |\n"
        "|----------|-------------|----------|---------|-----------|------|"
        "----|----|\n"
        "| *(filled のみ集計。unfilled は機会損失として別途カウント)* "
        "| | | | | | | |"
    )
    var_rows: list[str] = []
    for s in all_strategies:
        d = strategy_data.get(s)
        if d is None:
            continue
        pnls = d["pnls"]
        if not pnls:
            var_rows.append(
                f"| {s} | {d['filled']}/{d['total']} | {d['unfilled']} "
                f"| – | – | – | {d['tp']} | {d['sl']} |"
            )
            continue
        avg_pnl = statistics.mean(pnls)
        tot_pnl = sum(pnls)
        wins = sum(1 for p in pnls if p > 0)
        wr = wins / len(pnls) * 100
        var_rows.append(
            f"| {s} | {d['filled']}/{d['total']} | {d['unfilled']} "
            f"| {avg_pnl:+.2f}% | {tot_pnl:+.1f}% | {wr:.0f}% "
            f"| {d['tp']} | {d['sl']} |"
        )

    lines = [
        "## 12. Entry strategy comparison",
        "",
        "各エントリー戦略の仮想成績。指値は価格到達で約定 (filled)、",
        "到達しなければ unfilled (機会損失)。",
        "",
        "| 戦略 | 考え方 |",
        "|------|--------|",
        "| MARKET | 検出時の last price で即入り |",
        "| ASK | 検出時の ask price (実際の成行コスト) |",
        "| LIMIT_1PCT〜5PCT | 任意 +1〜5% の指値 (ベースライン) |",
        "| LIMIT_BB3S | BB 中心 + 3σ (統計的極限) |",
        "| LIMIT_ATR | last + ATR×0.5 (ボラ半分だけ上) |",
        "| LIMIT_FIB1272 | フィボナッチ 1.272 エクステンション |",
        "| LIMIT_FIB1618 | フィボナッチ 1.618 エクステンション (黄金比) |",
        "",
        "### Spread statistics",
        "",
        *spread_lines,
        "",
        "### Strategy PnL",
        "",
        var_header,
        *var_rows,
        "",
        "**解釈**:",
        "- filled 率が低い戦略は「狙った水準まで上がらなかった」(機会損失)。",
        "- avg PnL が高い戦略は「より高い位置でショートを入れられた」。",
        "- MARKET と LIMIT 系の差が大きいほど、待機戦略が有利。",
        "",
    ]
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
        "## 13. Indicator distribution: winners vs losers",
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


def _section_recommendation(closed: list[ClosedTrade]) -> str:
    """データに基づくフィルター推奨。現行 vs 推奨を比較。"""
    old_strict = _filter(
        closed,
        lambda t: (t.rsi is not None and t.rsi >= 75)
                  and (t.rsi_4h is None or t.rsi_4h < 70)
                  and t.price_vs_bb > 1.0
                  and t.volume_trend != "RISING",
    )
    new_v1 = _filter(
        closed,
        lambda t: (t.rsi is not None and t.rsi >= 70)
                  and (t.rsi_4h is not None and t.rsi_4h >= 65)
                  and t.volume_trend != "RISING",
    )

    lines = [
        "## 14. Filter recommendation",
        "",
        "### 旧 STRICT (変更前)",
        "",
        "```",
        "RSI(1h) >= 75",
        "RSI(4h) <  70   ← 逆効果 (低い 4h RSI = 勝率悪化)",
        "BB upper break   ← シグナルが少なすぎる",
        "Volume != RISING",
        "```",
        "",
        TABLE_HEADER,
        _row("旧 STRICT", _compute_stats(old_strict)),
        "",
        "### 新 STRICT v1 (適用中)",
        "",
        "```",
        "RSI(1h) >= 70",
        "RSI(4h) >= 65   ← 方向反転: ダブルオーバーボートを狙う",
        "BB upper break   ← 撤廃 (効果なし)",
        "Volume != RISING  ← 据え置き",
        "```",
        "",
        TABLE_HEADER,
        _row("新 STRICT v1", _compute_stats(new_v1)),
        "",
        "### 今後の改善候補",
        "",
        "- ATR% フィルター追加 (5–9% ゾーンが安定)",
        "- Volume FLAT のみに絞る (FLAT 勝率 > DECLINING)",
        "- RSI(1h) 閾値を 75 に戻す (データ蓄積後に再評価)",
        "",
    ]
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
            _section_atr_zone(closed),
            _section_mfe_mae(closed),
            _section_regime(closed),
            _section_fundamental(closed),
            _section_combined(closed),
            _section_entry_strategy(closed),
            _section_distribution(closed),
            _section_recommendation(closed),
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
