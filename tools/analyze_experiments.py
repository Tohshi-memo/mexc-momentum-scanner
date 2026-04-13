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

    # ファンディングレート (記録のみ。フィルター未使用)
    funding_rate: float | None = None  # %表記

    # OBV ダイバージェンス (記録のみ。フィルター未使用)
    obv_divergence: str | None = None  # BEARISH_DIV / BULLISH_DIV / NONE

    # オープンインタレスト (記録のみ。フィルター未使用)
    open_interest_usd: float | None = None
    oi_change_pct:     float | None = None
    long_short_ratio:  float | None = None

    # 価格行動の質 (記録のみ。フィルター未使用)
    upper_wick_ratio_1h:  float | None = None
    consecutive_green_1h: int | None   = None
    consecutive_green_4h: int | None   = None

    # 追加パッシブ指標 (記録のみ。フィルター未使用)
    bb_width_pct:       float | None = None  # BBバンド幅%
    ma20_deviation_pct: float | None = None  # 20MA乖離率%
    candle_body_ratio:  float | None = None  # 実体比率
    rsi_15m:            float | None = None  # 15m RSI
    daily_direction:    str | None   = None  # GREEN / RED / DOJI


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
                funding_rate=f_dict.get("funding_rate"),
                obv_divergence=f_dict.get("obv_divergence"),
                open_interest_usd=f_dict.get("open_interest_usd"),
                oi_change_pct=f_dict.get("oi_change_pct"),
                long_short_ratio=f_dict.get("long_short_ratio"),
                upper_wick_ratio_1h=f_dict.get("upper_wick_ratio_1h"),
                consecutive_green_1h=f_dict.get("consecutive_green_1h"),
                consecutive_green_4h=f_dict.get("consecutive_green_4h"),
                bb_width_pct=f_dict.get("bb_width_pct"),
                ma20_deviation_pct=f_dict.get("ma20_deviation_pct"),
                candle_body_ratio=f_dict.get("candle_body_ratio"),
                rsi_15m=f_dict.get("rsi_15m"),
                daily_direction=f_dict.get("daily_direction"),
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
    s_strict  = _compute_stats(strict)
    s_relaxed = _compute_stats(relaxed)
    filter_ok = s_strict.expectancy > s_relaxed.expectancy

    verdict = (
        "✅ STRICT > REJECTED → 現フィルターは有効。"
        if filter_ok else
        f"⚠️ STRICT ({s_strict.win_rate:.1f}% WR, {s_strict.expectancy:+.2f}%) < "
        f"REJECTED ({s_relaxed.win_rate:.1f}% WR, {s_relaxed.expectancy:+.2f}%) → "
        "**現行フィルターが逆効果。フィルター見直しが必要。**"
    )

    lines = [
        "## 1. Baseline",
        "",
        TABLE_HEADER,
        _row("ALL candidates",      _compute_stats(closed)),
        _row("STRICT (current)",    s_strict),
        _row("REJECTED by STRICT",  s_relaxed),
        "",
        verdict,
    ]
    return "\n".join(lines)


def _section_rsi_sweep(closed: list[ClosedTrade]) -> str:
    """RSI 1h 閾値ごとに『その閾値以上を採用していたら』の集計。"""
    thresholds = [60.0, 65.0, 70.0, 75.0, 80.0]
    subsets = {th: _filter(closed, lambda t, th=th: t.rsi is not None and t.rsi >= th)
               for th in thresholds}
    best_th = max(thresholds, key=lambda th: _compute_stats(subsets[th]).expectancy)
    best = _compute_stats(subsets[best_th])
    all_negative = all(_compute_stats(subsets[th]).expectancy < 0 for th in thresholds)

    note = (
        f"RSI 閾値を変えても全て期待値マイナス。RSI 単独ではショートの判断根拠として不十分。"
        if all_negative else
        f"RSI ≥ {best_th:.0f} が最も期待値が高い ({best.expectancy:+.2f}%)。"
    )

    lines = [
        "## 2. RSI(1h) threshold sweep",
        "",
        f"現行 STRICT は RSI ≥ 70。閾値を変えた場合の仮想成績。{note}",
        "",
        TABLE_HEADER,
    ]
    for th in thresholds:
        lines.append(_row(f"RSI ≥ {th:.0f}", _compute_stats(subsets[th])))
    lines.append("")
    return "\n".join(lines)


def _section_rsi_4h_sweep(closed: list[ClosedTrade]) -> str:
    """4h RSI 方向分析。旧方向 (< X) と新方向 (≥ X) の両方を比較。"""
    # 現在のデータで旧方向(低4h)と新方向(高4h)どちらが良いか動的に判定
    old_best = max([60.0, 65.0, 70.0, 75.0],
                   key=lambda th: _compute_stats(
                       _filter(closed, lambda t, th=th: t.rsi_4h is None or t.rsi_4h < th)
                   ).expectancy)
    new_best = max([60.0, 65.0, 70.0, 75.0, 80.0],
                   key=lambda th: _compute_stats(
                       _filter(closed, lambda t, th=th: t.rsi_4h is not None and t.rsi_4h >= th)
                   ).expectancy)
    s_old = _compute_stats(_filter(closed, lambda t, th=old_best: t.rsi_4h is None or t.rsi_4h < th))
    s_new = _compute_stats(_filter(closed, lambda t, th=new_best: t.rsi_4h is not None and t.rsi_4h >= th))
    better_dir = "低4h方向 (< X)" if s_old.expectancy > s_new.expectancy else "高4h方向 (≥ X)"
    better_exp = max(s_old.expectancy, s_new.expectancy)

    lines = [
        "## 3. RSI(4h) direction analysis",
        "",
        f"> **現在の結論**: {better_dir} が有利 (最良 expectancy {better_exp:+.2f}%)。",
        "> 4h RSI が低い = まだ過熱しきっていない新鮮な急騰。",
        "> 4h RSI が高い = ダブルオーバーボート。",
        "> どちらが勝るかは相場環境によって変わるため継続的に監視する。",
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
    s_rising     = _compute_stats(rising)
    s_not_rising = _compute_stats(not_rising)

    if s_rising.n > 0 and s_not_rising.n > 0:
        if s_rising.expectancy > s_not_rising.expectancy:
            verdict = (
                f"⚠️ RISING ({s_rising.win_rate:.1f}% WR, {s_rising.expectancy:+.2f}%) > "
                f"NOT RISING ({s_not_rising.win_rate:.1f}% WR, {s_not_rising.expectancy:+.2f}%) → "
                "**現行の「RISING 除外」フィルターが逆効果。RISING の方が成績が高い。**"
            )
        else:
            verdict = (
                f"✅ NOT RISING ({s_not_rising.win_rate:.1f}% WR, {s_not_rising.expectancy:+.2f}%) > "
                f"RISING ({s_rising.win_rate:.1f}% WR, {s_rising.expectancy:+.2f}%) → "
                "現行の「RISING 除外」フィルターは有効。"
            )
    else:
        verdict = ""

    lines = [
        "## 5. Volume trend filter",
        "",
        f"現行 STRICT は『RISING を除外』(疲弊兆候のみショート)。{verdict}",
        "",
        TABLE_HEADER,
        _row("ALL volume trends",          _compute_stats(closed)),
        _row("NOT RISING (current)",       s_not_rising),
        _row("DECLINING only (strictest)", _compute_stats(declining)),
        _row("FLAT only",                  _compute_stats(flat)),
        _row("RISING only",                s_rising),
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
    zone_stats = [(label, _compute_stats(_filter(closed, pred))) for label, pred in zones]
    positive_zones = [label for label, s in zone_stats if s.n >= 5 and s.expectancy > 0]
    best_zone = max(zone_stats, key=lambda x: x[1].expectancy) if zone_stats else None

    if positive_zones:
        note = f"現在のデータでは **{', '.join(positive_zones)}** が期待値プラス。"
    else:
        note = "現在のデータでは全ATRゾーンが期待値マイナス。"

    if best_zone and best_zone[1].n >= 5:
        note += f" 最良: {best_zone[0]} ({best_zone[1].expectancy:+.2f}%)。"

    lines = [
        "## 7. ATR% zone analysis",
        "",
        f"ATR% = ATR / price × 100。ボラティリティの大きさ別の成績。{note}",
        "",
        TABLE_HEADER,
    ]
    for label, s in zone_stats:
        lines.append(_row(label, s))
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
        # --- 現行 STRICT (参考) ---
        ("現行 STRICT (RSI≥70 & 4h≥65 & ¬RISING)",
         lambda t: (t.rsi is not None and t.rsi >= 70)
                   and (t.rsi_4h is not None and t.rsi_4h >= 65)
                   and t.volume_trend != "RISING"),
        # --- データが示す有望な方向: 低4h RSI ─────────────────────────
        ("4h RSI < 65 (低4h = 新鮮な急騰)",
         lambda t: t.rsi_4h is not None and t.rsi_4h < 65),
        ("4h RSI < 65 & RISING",
         lambda t: (t.rsi_4h is not None and t.rsi_4h < 65)
                   and t.volume_trend == "RISING"),
        ("4h RSI < 65 & ATR≥11%",
         lambda t: (t.rsi_4h is not None and t.rsi_4h < 65)
                   and (t.atr_pct or 0) >= 11),
        ("4h RSI < 65 & RSI≥70",
         lambda t: (t.rsi_4h is not None and t.rsi_4h < 65)
                   and (t.rsi is not None and t.rsi >= 70)),
        ("4h RSI < 65 & RSI≥70 & RISING",
         lambda t: (t.rsi_4h is not None and t.rsi_4h < 65)
                   and (t.rsi is not None and t.rsi >= 70)
                   and t.volume_trend == "RISING"),
        # --- ATR ≥ 11% ベース ────────────────────────────────────────
        ("ATR ≥ 11%",
         lambda t: (t.atr_pct or 0) >= 11),
        ("ATR ≥ 11% & RISING",
         lambda t: (t.atr_pct or 0) >= 11
                   and t.volume_trend == "RISING"),
        # --- 旧 STRICT (参考) ─────────────────────────────────────────
        ("旧 STRICT (RSI≥75 & 4h<70 & BB & ¬RISING)",
         lambda t: (t.rsi is not None and t.rsi >= 75)
                   and (t.rsi_4h is None or t.rsi_4h < 70)
                   and t.price_vs_bb > 1.0
                   and t.volume_trend != "RISING"),
    ]

    combo_results = [(label, _filter(closed, pred)) for label, pred in combos]
    reliable = [(l, s) for l, s in combo_results if len(s) >= 5]
    if reliable:
        best_label, best_subset = max(reliable, key=lambda x: _compute_stats(x[1]).expectancy)
        best_s = _compute_stats(best_subset)
        best_note = (
            f"**現在の最良組み合わせ (n≥5)**: 「{best_label}」"
            f" (WR={best_s.win_rate:.1f}%, exp={best_s.expectancy:+.2f}%, n={best_s.n})"
        )
    else:
        best_note = "*(各組み合わせのサンプルが不足。データ蓄積中)*"

    lines = [
        "## 11. Combined filters",
        "",
        "各フィルター組み合わせの仮想成績。データが示す有望な方向を中心に評価。",
        best_note,
        "",
        TABLE_HEADER,
    ]
    for label, subset in combo_results:
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

    # 表示順: MARKET / ASK / 任意 % / テクニカル / ロング の順
    order = [
        "MARKET", "ASK",
        "LIMIT_1PCT", "LIMIT_2PCT", "LIMIT_3PCT", "LIMIT_4PCT", "LIMIT_5PCT",
        "LIMIT_6PCT", "LIMIT_7PCT", "LIMIT_8PCT", "LIMIT_9PCT", "LIMIT_10PCT",
        "LIMIT_BB3S", "LIMIT_ATR",
        "LIMIT_FIB1272", "LIMIT_FIB1618",
        "MARKET_LONG", "ASK_LONG",
        "LIMIT_1PCT_LONG", "LIMIT_2PCT_LONG", "LIMIT_3PCT_LONG",
        "LIMIT_4PCT_LONG", "LIMIT_5PCT_LONG",
        "LIMIT_6PCT_LONG", "LIMIT_7PCT_LONG", "LIMIT_8PCT_LONG",
        "LIMIT_9PCT_LONG", "LIMIT_10PCT_LONG",
        "LIMIT_BB3S_LONG", "LIMIT_ATR_LONG",
        "LIMIT_FIB1272_LONG", "LIMIT_FIB1618_LONG",
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
        "| LIMIT_1PCT〜10PCT | 任意 +1〜10% の指値 (ベースライン) |",
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
    """データに基づくフィルター推奨。現行 vs 候補を比較。"""
    # 比較対象
    current = _filter(
        closed,
        lambda t: (t.rsi is not None and t.rsi >= 70)
                  and (t.rsi_4h is not None and t.rsi_4h >= 65)
                  and t.volume_trend != "RISING",
    )
    candidate_v2 = _filter(
        closed,
        lambda t: (t.rsi_4h is not None and t.rsi_4h < 65)
                  and t.volume_trend == "RISING",
    )
    candidate_v3 = _filter(
        closed,
        lambda t: (t.rsi_4h is not None and t.rsi_4h < 65)
                  and (t.atr_pct or 0) >= 11,
    )

    s_current = _compute_stats(current)
    s_v2      = _compute_stats(candidate_v2)
    s_v3      = _compute_stats(candidate_v3)

    lines = [
        "## 14. Filter recommendation",
        "",
        "### 現行 STRICT v1 (適用中)",
        "",
        "```",
        "RSI(1h) >= 70",
        "RSI(4h) >= 65   ← データでは逆効果の可能性あり",
        "Volume != RISING ← データでは RISING が最も成績が高い",
        "```",
        "",
        TABLE_HEADER,
        _row("現行 STRICT v1", s_current),
        "",
        "### 候補 v2: データが示す有望方向",
        "",
        "```",
        "RSI(1h) >= 70",
        "RSI(4h) < 65   ← 4h 未過熱 = 新鮮な急騰",
        "Volume RISING  ← トレンド継続の勢いを活かす",
        "```",
        "",
        TABLE_HEADER,
        _row("候補 v2 (4h<65 & RISING)", s_v2),
        "",
        "### 候補 v3: 高ボラ × 新鮮な急騰",
        "",
        "```",
        "RSI(4h) < 65   ← 4h 未過熱",
        "ATR >= 11%     ← 高ボラ帯 (唯一の期待値プラスゾーン)",
        "```",
        "",
        TABLE_HEADER,
        _row("候補 v3 (4h<65 & ATR≥11%)", s_v3),
        "",
        "### 判断基準",
        "",
        "| 指標 | 現行 v1 | 候補 v2 | 候補 v3 |",
        "|------|---------|---------|---------|",
        f"| WR   | {s_current.win_rate:.1f}% | {s_v2.win_rate:.1f}% | {s_v3.win_rate:.1f}% |",
        f"| exp  | {s_current.expectancy:+.2f}% | {s_v2.expectancy:+.2f}% | {s_v3.expectancy:+.2f}% |",
        f"| n    | {s_current.n} | {s_v2.n} | {s_v3.n} |",
        "",
        "**次のアクション**: n が 30 件以上になった候補を本番 STRICT に昇格させる。",
        "候補 v2/v3 は引き続きシャドウトレードで追跡中。",
        "",
    ]
    return "\n".join(lines)


def _section_funding_rate(closed: list[ClosedTrade]) -> str:
    """ファンディングレート別の勝率比較。

    記録開始が途中のため、データがない場合はその旨を表示。
    """
    # funding_rate を持つトレードのみ
    with_fr = [
        t for t in closed
        if getattr(t, "funding_rate", None) is not None
    ]

    lines = ["## 15. Funding rate analysis", ""]

    if len(with_fr) < 5:
        lines += [
            f"ファンディングレートデータ: {len(with_fr)} / {len(closed)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    lines += [
        f"ファンディングレートデータ: {len(with_fr)} / {len(closed)} 件",
        "",
        "**考え方**: 正値(+) = ロングがショートに支払う → ロング過熱 → ショート有利。",
        "高いほど反転圧力が強い可能性。",
        "",
        TABLE_HEADER,
    ]

    # バケット定義
    buckets: list[tuple[str, float, float]] = [
        ("< 0%  (ショート過熱)", -999, 0.0),
        ("0〜0.05%", 0.0, 0.05),
        ("0.05〜0.1%", 0.05, 0.1),
        (">= 0.1% (ロング過熱)", 0.1, 999),
    ]

    for label, lo, hi in buckets:
        subset = [
            t for t in with_fr
            if t.funding_rate is not None and lo <= t.funding_rate < hi
        ]
        if not subset:
            continue
        lines.append(_row(f"FR {label}", _compute_stats(subset)))

    # 全体
    lines.append(_row("FR 全件", _compute_stats(with_fr)))
    lines.append("")

    # 平均・中央値
    rates = [t.funding_rate for t in with_fr if t.funding_rate is not None]
    avg_fr = statistics.mean(rates)
    med_fr = statistics.median(rates)
    lines += [
        f"- 平均 FR: {avg_fr:+.4f}%",
        f"- 中央値 FR: {med_fr:+.4f}%",
        f"- 最大 FR: {max(rates):+.4f}%",
        f"- 最小 FR: {min(rates):+.4f}%",
        "",
    ]
    return "\n".join(lines)


def _section_obv_divergence(closed: list[ClosedTrade]) -> str:
    """OBV ダイバージェンス別の勝率比較。"""
    with_obv = [
        t for t in closed
        if getattr(t, "obv_divergence", None) is not None
    ]

    lines = ["## 16. OBV divergence analysis", ""]

    if len(with_obv) < 5:
        lines += [
            f"OBV ダイバージェンスデータ: {len(with_obv)} / {len(closed)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    lines += [
        f"OBV ダイバージェンスデータ: {len(with_obv)} / {len(closed)} 件",
        "",
        "**考え方**: BEARISH_DIV (価格↑ OBV↓) はショートの強い根拠。",
        "BEARISH_DIV の勝率が高ければ将来フィルターとして有効化する。",
        "",
        TABLE_HEADER,
    ]

    for label in ("BEARISH_DIV", "BULLISH_DIV", "NONE"):
        subset = [t for t in with_obv if t.obv_divergence == label]
        if not subset:
            continue
        lines.append(_row(label, _compute_stats(subset)))

    lines.append(_row("全件 (OBV あり)", _compute_stats(with_obv)))
    lines.append("")
    return "\n".join(lines)


def _section_open_interest(closed: list[ClosedTrade]) -> str:
    """OI・OI変化率・ロングショート比率の分析。"""
    with_oi = [t for t in closed if getattr(t, "open_interest_usd", None) is not None]
    with_ls = [t for t in closed if getattr(t, "long_short_ratio", None) is not None]

    lines = ["## 17. Open Interest & Long/Short ratio", ""]

    if len(with_oi) < 5 and len(with_ls) < 5:
        n_oi = len(with_oi)
        n_ls = len(with_ls)
        lines += [
            f"OI データ: {n_oi} / {len(closed)} 件 　L/S 比率データ: {n_ls} / {len(closed)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    # --- OI 変化率バケット ---
    with_oic = [
        t for t in with_oi
        if getattr(t, "oi_change_pct", None) is not None
    ]
    if len(with_oic) >= 5:
        lines += [
            f"### OI 変化率 (直近1h) — {len(with_oic)} 件",
            "",
            "**考え方**: 価格↑ OI↑ = 新規ロング参入 → 過熱 → 反転リスク大。",
            "",
            TABLE_HEADER,
        ]
        oi_buckets = [
            ("OI 急減 (< -5%)",  -999, -5.0),
            ("OI 減少 (-5〜0%)", -5.0,  0.0),
            ("OI 増加 (0〜5%)",   0.0,  5.0),
            ("OI 急増 (>= 5%)",  5.0,  999),
        ]
        for label, lo, hi in oi_buckets:
            subset = [
                t for t in with_oic
                if lo <= t.oi_change_pct < hi
            ]
            if not subset:
                continue
            lines.append(_row(f"  {label}", _compute_stats(subset)))
        lines.append("")

    # --- L/S 比率バケット ---
    if len(with_ls) >= 5:
        lines += [
            f"### L/S 比率 — {len(with_ls)} 件",
            "",
            "**考え方**: L/S > 1.5 = ロング過多 → 清算リスク高 → ショート有利。",
            "",
            TABLE_HEADER,
        ]
        ls_buckets = [
            ("L/S < 1.0 (ショート優勢)", -999, 1.0),
            ("L/S 1.0〜1.5",               1.0, 1.5),
            ("L/S 1.5〜2.0",               1.5, 2.0),
            ("L/S >= 2.0 (ロング過多)",    2.0, 999),
        ]
        for label, lo, hi in ls_buckets:
            subset = [t for t in with_ls if lo <= t.long_short_ratio < hi]
            if not subset:
                continue
            lines.append(_row(f"  {label}", _compute_stats(subset)))
        lines.append("")

    return "\n".join(lines)


def _section_price_action(closed: list[ClosedTrade]) -> str:
    """上ヒゲ比率・連続陽線数の分析。"""
    with_wick = [t for t in closed if getattr(t, "upper_wick_ratio_1h", None) is not None]
    with_g1h  = [t for t in closed if getattr(t, "consecutive_green_1h", None) is not None]
    with_g4h  = [t for t in closed if getattr(t, "consecutive_green_4h", None) is not None]

    lines = ["## 18. Price action quality", ""]

    has_data = len(with_wick) >= 5 or len(with_g1h) >= 5

    if not has_data:
        lines += [
            f"上ヒゲ比率データ: {len(with_wick)} / {len(closed)} 件",
            f"連続陽線(1h)データ: {len(with_g1h)} / {len(closed)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    # --- 上ヒゲ比率バケット ---
    if len(with_wick) >= 5:
        lines += [
            f"### 上ヒゲ比率 (1h直前完成足) — {len(with_wick)} 件",
            "",
            "**考え方**: 上ヒゲが長い (比率高い) ほど売り圧力あり → ショートに有利。",
            "",
            TABLE_HEADER,
        ]
        wick_buckets = [
            ("上ヒゲ小  (0〜0.2)",  0.0, 0.2),
            ("上ヒゲ中  (0.2〜0.4)", 0.2, 0.4),
            ("上ヒゲ大  (0.4〜0.6)", 0.4, 0.6),
            ("上ヒゲ極大 (>= 0.6)",  0.6, 999),
        ]
        for label, lo, hi in wick_buckets:
            subset = [t for t in with_wick if lo <= t.upper_wick_ratio_1h < hi]
            if not subset:
                continue
            lines.append(_row(f"  {label}", _compute_stats(subset)))
        lines.append("")

    # --- 連続陽線数バケット (1h) ---
    if len(with_g1h) >= 5:
        lines += [
            f"### 連続陽線数 (1h) — {len(with_g1h)} 件",
            "",
            "**考え方**: 多いほど一方的な上昇 = 過熱感。反転確率が高い可能性。",
            "",
            TABLE_HEADER,
        ]
        green_buckets = [
            ("1〜2本",  1, 3),
            ("3〜4本",  3, 5),
            ("5〜7本",  5, 8),
            ("8本以上", 8, 999),
        ]
        for label, lo, hi in green_buckets:
            subset = [t for t in with_g1h if lo <= t.consecutive_green_1h < hi]
            if not subset:
                continue
            lines.append(_row(f"  {label}", _compute_stats(subset)))
        lines.append("")

    # --- 連続陽線数バケット (4h) ---
    if len(with_g4h) >= 5:
        lines += [
            f"### 連続陽線数 (4h) — {len(with_g4h)} 件",
            "",
            TABLE_HEADER,
        ]
        for label, lo, hi in green_buckets:
            subset = [t for t in with_g4h if lo <= t.consecutive_green_4h < hi]
            if not subset:
                continue
            lines.append(_row(f"  {label}", _compute_stats(subset)))
        lines.append("")

    return "\n".join(lines)


def _section_direction_comparison(closed: list[ClosedTrade]) -> str:
    """ロング vs ショート: 同一急騰イベントでの方向比較。

    同じ検出イベントで MARKET_LONG と MARKET(ショート) を比較し、
    「この相場では急騰後にロング/ショートどちらが有効か」を定量判断する。
    """
    long_count = sum(
        1 for t in closed
        if t.entry_variants
        and any(v.get("strategy") == "MARKET_LONG" for v in t.entry_variants)
    )

    lines = ["## 22. Long vs Short direction comparison", ""]

    if long_count < 5:
        lines += [
            f"ロング方向データ: {long_count} / {len(closed)} 件",
            "",
            "*(データ蓄積中。5件以上で自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    lines += [
        f"ロング方向データ: {long_count} / {len(closed)} 件",
        "",
        "**考え方**: 同じ急騰検出イベントでロング/ショートどちらが正解だったか。",
        "ロング優位 = 急騰継続トレンド（今はロング向き相場）。",
        "ショート優位 = 急騰は反転ポイント（ショート戦略が有効）。",
        "",
        "### 戦略別成績",
        "",
        "| 戦略 | 方向 | filled | avg PnL | win% | TP | SL |",
        "|------|------|-------:|--------:|-----:|---:|---:|",
    ]

    compare_pairs = [
        ("MARKET",       "MARKET_LONG"),
        ("ASK",          "ASK_LONG"),
        ("LIMIT_1PCT",   "LIMIT_1PCT_LONG"),
        ("LIMIT_3PCT",   "LIMIT_3PCT_LONG"),
        ("LIMIT_5PCT",   "LIMIT_5PCT_LONG"),
        ("LIMIT_10PCT",  "LIMIT_10PCT_LONG"),
        ("LIMIT_BB3S",   "LIMIT_BB3S_LONG"),
        ("LIMIT_ATR",    "LIMIT_ATR_LONG"),
        ("LIMIT_FIB1272","LIMIT_FIB1272_LONG"),
        ("LIMIT_FIB1618","LIMIT_FIB1618_LONG"),
    ]

    def _variant_stats(strategy_name: str) -> tuple[int, float | None, float | None, int, int]:
        """(filled, avg_pnl, win_rate, tp_count, sl_count)"""
        pnls: list[float] = []
        tp_n = sl_n = filled_n = 0
        for t in closed:
            if not t.entry_variants:
                continue
            for v in t.entry_variants:
                if v.get("strategy") != strategy_name:
                    continue
                if v.get("filled"):
                    filled_n += 1
                    pnl = v.get("pnl_pct")
                    if pnl is not None:
                        pnls.append(float(pnl))
                    if v.get("outcome") == OUTCOME_TP_HIT:
                        tp_n += 1
                    elif v.get("outcome") == OUTCOME_SL_HIT:
                        sl_n += 1
        avg = statistics.mean(pnls) if pnls else None
        wr  = sum(1 for p in pnls if p > 0) / len(pnls) * 100 if pnls else None
        return filled_n, avg, wr, tp_n, sl_n

    for short_s, long_s in compare_pairs:
        for name in (short_s, long_s):
            direction = "LONG 🔼" if name.endswith("_LONG") else "SHORT 🔽"
            filled, avg, wr, tp_n, sl_n = _variant_stats(name)
            if avg is None:
                lines.append(f"| {name} | {direction} | {filled} | – | – | – | – |")
            else:
                lines.append(
                    f"| {name} | {direction} | {filled} "
                    f"| {avg:+.2f}% | {wr:.0f}% | {tp_n} | {sl_n} |"
                )
        lines.append("|  |  |  |  |  |  |  |")  # separator

    # ── 同一イベントでの直接比較 ──────────────────────────────────────
    better_long = better_short = tie = 0
    for t in closed:
        if not t.entry_variants:
            continue
        short_pnl = next(
            (float(v["pnl_pct"]) for v in t.entry_variants
             if v.get("strategy") == "MARKET"
             and v.get("filled") and v.get("pnl_pct") is not None),
            None,
        )
        long_pnl = next(
            (float(v["pnl_pct"]) for v in t.entry_variants
             if v.get("strategy") == "MARKET_LONG"
             and v.get("filled") and v.get("pnl_pct") is not None),
            None,
        )
        if short_pnl is not None and long_pnl is not None:
            if long_pnl > short_pnl + 0.1:
                better_long += 1
            elif short_pnl > long_pnl + 0.1:
                better_short += 1
            else:
                tie += 1

    total = better_long + better_short + tie
    if total > 0:
        lines += [
            "",
            f"### 同一イベント直接比較 (MARKET ショート vs MARKET_LONG) — {total} 件",
            "",
            "| 判定 | 件数 | 比率 |",
            "|------|-----:|-----:|",
            f"| ロングが有利 | {better_long} | {better_long/total*100:.0f}% |",
            f"| ショートが有利 | {better_short} | {better_short/total*100:.0f}% |",
            f"| ほぼ同等 | {tie} | {tie/total*100:.0f}% |",
            "",
            "**解釈**:",
            "- ロング有利 > 60%: 急騰継続が多い → 相場はロング向き。ショート戦略の見直しを検討。",
            "- ショート有利 > 60%: 急騰反転が多い → 現行ショート戦略が環境に合っている。",
            "- 拮抗 (40〜60%): 方向選択の鍵は別のフィルター（出来高・RSI等）にある。",
            "",
        ]
    return "\n".join(lines)


def _section_bb_width(closed: list[ClosedTrade]) -> str:
    """BBバンド幅% / 20MA乖離率 / 実体比率の分析。"""
    with_bbw  = [t for t in closed if getattr(t, "bb_width_pct",       None) is not None]
    with_ma20 = [t for t in closed if getattr(t, "ma20_deviation_pct", None) is not None]
    with_body = [t for t in closed if getattr(t, "candle_body_ratio",  None) is not None]

    lines = ["## 19. BB width / MA20 deviation / candle body ratio", ""]

    has_data = any(len(x) >= 5 for x in [with_bbw, with_ma20, with_body])
    if not has_data:
        lines += [
            f"BBバンド幅データ: {len(with_bbw)} 件 / "
            f"MA20乖離率: {len(with_ma20)} 件 / "
            f"実体比率: {len(with_body)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    # --- BB バンド幅バケット ---
    if len(with_bbw) >= 5:
        lines += [
            f"### BB バンド幅% — {len(with_bbw)} 件",
            "",
            "**考え方**: バンド幅が大きいほど高ボラ。スクイーズ直後は爆発力大。",
            "",
            TABLE_HEADER,
        ]
        for label, lo, hi in [
            ("< 5%",    0,  5),
            ("5〜10%",  5, 10),
            ("10〜15%", 10, 15),
            ("15〜20%", 15, 20),
            (">= 20%",  20, 999),
        ]:
            subset = [t for t in with_bbw if lo <= (t.bb_width_pct or 0) < hi]
            if subset:
                lines.append(_row(f"  BBW {label}", _compute_stats(subset)))
        lines.append("")

    # --- 20MA 乖離率バケット ---
    if len(with_ma20) >= 5:
        lines += [
            f"### 20MA 乖離率% — {len(with_ma20)} 件",
            "",
            "**考え方**: 正値 = 上方乖離 (過熱)。大きいほど平均回帰リスク大 = ショート有利。",
            "",
            TABLE_HEADER,
        ]
        for label, lo, hi in [
            ("< 5%",    0,  5),
            ("5〜10%",  5, 10),
            ("10〜15%", 10, 15),
            (">= 15%",  15, 999),
        ]:
            subset = [t for t in with_ma20 if lo <= (t.ma20_deviation_pct or 0) < hi]
            if subset:
                lines.append(_row(f"  乖離 {label}", _compute_stats(subset)))
        lines.append("")

    # --- 実体比率バケット ---
    if len(with_body) >= 5:
        lines += [
            f"### ローソク足実体比率 — {len(with_body)} 件",
            "",
            "**考え方**: 実体が大きい = 方向性が明確。ショートの根拠として強い。",
            "",
            TABLE_HEADER,
        ]
        for label, lo, hi in [
            ("実体小 (0〜0.3)",  0.0, 0.3),
            ("実体中 (0.3〜0.6)", 0.3, 0.6),
            ("実体大 (0.6〜0.8)", 0.6, 0.8),
            ("実体極大 (>= 0.8)", 0.8, 999),
        ]:
            subset = [t for t in with_body if lo <= (t.candle_body_ratio or 0) < hi]
            if subset:
                lines.append(_row(f"  {label}", _compute_stats(subset)))
        lines.append("")

    return "\n".join(lines)


def _section_rsi_15m(closed: list[ClosedTrade]) -> str:
    """15分足 RSI 別の勝率比較。"""
    with_r15 = [t for t in closed if getattr(t, "rsi_15m", None) is not None]

    lines = ["## 20. 15-minute RSI analysis", ""]

    if len(with_r15) < 5:
        lines += [
            f"15m RSI データ: {len(with_r15)} / {len(closed)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    lines += [
        f"15m RSI データ: {len(with_r15)} / {len(closed)} 件",
        "",
        "**考え方**: 15m も過熱 (高 RSI) = 超短期でも売られすぎ警戒 → ショート有利。",
        "1h 過熱 + 15m 過熱の「ダブル過熱」がより強いシグナルになるか確認。",
        "",
        TABLE_HEADER,
    ]
    for label, lo, hi in [
        ("15m RSI < 60",  0,  60),
        ("15m RSI 60〜70", 60, 70),
        ("15m RSI 70〜80", 70, 80),
        ("15m RSI >= 80",  80, 999),
    ]:
        subset = [t for t in with_r15 if lo <= (t.rsi_15m or 0) < hi]
        if subset:
            lines.append(_row(label, _compute_stats(subset)))

    # 相関サマリー
    vals = [(t.rsi_15m, t.pnl_pct) for t in with_r15
            if t.rsi_15m is not None and t.pnl_pct is not None]
    if vals:
        import statistics as _st
        avg_rsi_win  = _st.mean(t.rsi_15m for t in with_r15
                                if t.outcome == "TP_HIT" and t.rsi_15m is not None) \
                       if any(t.outcome == "TP_HIT" for t in with_r15) else None
        avg_rsi_loss = _st.mean(t.rsi_15m for t in with_r15
                                if t.outcome == "SL_HIT" and t.rsi_15m is not None) \
                       if any(t.outcome == "SL_HIT" for t in with_r15) else None
        lines += [
            "",
            f"- 勝ちトレードの平均 15m RSI: "
            f"{avg_rsi_win:.1f}" if avg_rsi_win else "- 勝ちトレードの平均 15m RSI: n/a",
            f"- 負けトレードの平均 15m RSI: "
            f"{avg_rsi_loss:.1f}" if avg_rsi_loss else "- 負けトレードの平均 15m RSI: n/a",
        ]
    lines.append("")
    return "\n".join(lines)


def _section_daily_direction(closed: list[ClosedTrade]) -> str:
    """日足方向別の勝率比較。"""
    with_dd = [t for t in closed if getattr(t, "daily_direction", None) is not None]

    lines = ["## 21. Daily candle direction", ""]

    if len(with_dd) < 5:
        lines += [
            f"日足方向データ: {len(with_dd)} / {len(closed)} 件",
            "",
            "*(データ蓄積中。十分なサンプルが集まると自動的に分析が表示されます)*",
            "",
        ]
        return "\n".join(lines)

    lines += [
        f"日足方向データ: {len(with_dd)} / {len(closed)} 件",
        "",
        "**考え方**: 急騰が日足上昇トレンド中に起きた場合 (GREEN) は ",
        "上昇が継続しやすくショートが不利かもしれない。",
        "逆に日足が赤 (RED) なら反転信頼度が高い可能性。",
        "",
        TABLE_HEADER,
    ]
    for label in ("GREEN", "RED", "DOJI"):
        subset = [t for t in with_dd if t.daily_direction == label]
        if subset:
            lines.append(_row(f"日足 {label}", _compute_stats(subset)))
    lines.append(_row("全件 (日足あり)", _compute_stats(with_dd)))
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
            _section_atr_zone(closed),
            _section_mfe_mae(closed),
            _section_regime(closed),
            _section_fundamental(closed),
            _section_combined(closed),
            _section_entry_strategy(closed),
            _section_distribution(closed),
            _section_recommendation(closed),
            _section_funding_rate(closed),
            _section_obv_divergence(closed),
            _section_open_interest(closed),
            _section_price_action(closed),
            _section_bb_width(closed),
            _section_rsi_15m(closed),
            _section_daily_direction(closed),
            _section_direction_comparison(closed),
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
