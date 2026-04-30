"""
tools/decision_report.py
Human-readable decision report for the live scanner.

This is intentionally shorter than experiment_report.md. It combines:
  - strategy EV from shadow experiments
  - live virtual portfolio status
  - latest market context / scan funnel

Output: data/decision_report.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_root = Path(__file__).parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from tools.analyze_experiments import (  # noqa: E402
    DEFAULT_INPUT,
    _compute_stats,
    _compute_strategy_ev,
    _load_closed_with_archives,
)


DEFAULT_OUTPUT = Path("data/decision_report.md")
LIVE_PORTFOLIO_FILE = Path("data/live_portfolio.json")
MARKET_CONTEXT_FILE = Path("data/market_context.json")


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _fmt_pct(value: float | None, digits: int = 2) -> str:
    if value is None:
        return "n/a"
    return f"{value:+.{digits}f}%"


def _fmt_usd(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"${value:,.2f}"


def _is_long(strategy: str) -> bool:
    return strategy.endswith("_LONG")


def _rank_strategies(
    stats: dict[str, dict[str, Any]],
    *,
    is_long: bool | None = None,
    min_filled: int = 0,
    allow: set[str] | None = None,
    top: int = 5,
) -> list[tuple[str, dict[str, Any]]]:
    rows: list[tuple[str, dict[str, Any]]] = []
    for strategy, data in stats.items():
        ev = data.get("effective_ev")
        if ev is None:
            continue
        if data.get("filled", 0) < min_filled:
            continue
        if is_long is not None and _is_long(strategy) != is_long:
            continue
        if allow is not None and strategy not in allow:
            continue
        rows.append((strategy, data))
    rows.sort(key=lambda item: item[1]["effective_ev"], reverse=True)
    return rows[:top]


def _strategy_table(rows: list[tuple[str, dict[str, Any]]]) -> list[str]:
    if not rows:
        return ["該当なし"]

    lines = [
        "| strategy | filled/total | fill率 | avg PnL | 実質EV |",
        "|---|---:|---:|---:|---:|",
    ]
    for strategy, data in rows:
        total = int(data.get("total") or 0)
        filled = int(data.get("filled") or 0)
        fill_rate = float(data.get("fill_rate") or 0.0) * 100
        lines.append(
            f"| {strategy} | {filled}/{total} | {fill_rate:.1f}% | "
            f"{_fmt_pct(data.get('avg_pnl'))} | **{_fmt_pct(data.get('effective_ev'))}** |"
        )
    return lines


def _portfolio_section(path: Path) -> list[str]:
    data = _load_json(path)
    if not data:
        return [
            "## 2. $100 Live Portfolio",
            "",
            "- 状態: `data/live_portfolio.json` がまだありません。",
            "",
        ]

    initial = float(data.get("initial_capital") or 0.0)
    balance = float(data.get("balance") or 0.0)
    trades = data.get("trades") or []
    if not isinstance(trades, list):
        trades = []
    ret = (balance - initial) / initial * 100 if initial > 0 else 0.0
    wins = sum(1 for t in trades if t.get("outcome") == "TP_HIT")
    losses = sum(1 for t in trades if t.get("outcome") == "SL_HIT")
    expired = sum(1 for t in trades if t.get("outcome") == "EXPIRED")
    latest = trades[-1] if trades else None

    lines = [
        "## 2. $100 Live Portfolio",
        "",
        f"- 残高: **{_fmt_usd(balance)}** / 初期 {_fmt_usd(initial)} ({_fmt_pct(ret)})",
        f"- 確定トレード: {len(trades)}件 (TP {wins} / SL {losses} / EXP {expired})",
    ]
    if latest:
        lines.append(
            "- 最新: "
            f"{latest.get('symbol', '?')} {latest.get('outcome', '?')} "
            f"PnL {_fmt_pct(float(latest.get('pnl_pct') or 0.0))} "
            f"残高後 {_fmt_usd(float(latest.get('balance_after') or 0.0))}"
        )
        strategy = latest.get("strategy_entry_style") or "未記録"
        direction = latest.get("strategy_direction") or "未記録"
        tier = latest.get("strategy_tier") or "未記録"
        lines.append(f"- 最新戦略メタ: tier={tier}, direction={direction}, entry={strategy}")
    lines.append("")
    return lines


def _market_context_section(path: Path) -> list[str]:
    data = _load_json(path)
    records = data.get("records") if data else None
    if not isinstance(records, list) or not records:
        return [
            "## 3. Latest Market Context",
            "",
            "- 状態: `data/market_context.json` はまだ蓄積中です。",
            "",
        ]

    latest = records[-1]
    btc = latest.get("btc") or {}
    scan = latest.get("scan") or {}
    analysis = latest.get("analysis") or {}
    counts = scan.get("symbol_counts") or {}
    reject_counts = scan.get("reject_counts") or {}
    reject_reasons = analysis.get("reject_reason_counts") or {}
    coverage = analysis.get("data_coverage") or {}
    near_misses = scan.get("near_misses") or []
    top_by_24h = scan.get("top_by_24h") or []

    lines = [
        "## 3. Latest Market Context",
        "",
        f"- 更新: {latest.get('timestamp', 'n/a')} / 保存件数 {len(records)}/{data.get('max_records', 'n/a')}",
        (
            f"- BTC: {btc.get('regime', 'UNKNOWN')} "
            f"1h {_fmt_pct(btc.get('change_1h_pct'))} "
            f"price={btc.get('price', 'n/a')}"
        ),
        (
            "- Funnel: "
            f"target {counts.get('target_symbols', 0)} → "
            f"liquid {counts.get('liquid_symbols', 0)} → "
            f"pre {counts.get('pre_candidates', 0)} → "
            f"checked {counts.get('ohlcv_checked', 0)} → "
            f"surge {counts.get('surge_candidates', 0)} → "
            f"strict {analysis.get('confirmed_strict', 0)}"
        ),
    ]

    if reject_counts:
        joined = ", ".join(f"{k}={v}" for k, v in reject_counts.items())
        lines.append(f"- Surge前reject: {joined}")
    if reject_reasons:
        joined = ", ".join(f"{k}={v}" for k, v in reject_reasons.items())
        lines.append(f"- Strict後reject: {joined}")

    total = int(coverage.get("total") or 0)
    if total > 0:
        gaps = []
        for key, value in coverage.items():
            if key == "total":
                continue
            pct = int(value) / total * 100
            if pct < 80:
                gaps.append(f"{key} {pct:.0f}%")
        lines.append(
            "- データ欠損注意: "
            + (", ".join(gaps) if gaps else "主要指標は概ね取得できています")
        )

    if top_by_24h:
        lines += ["", "### 24h上昇上位", "", "| symbol | 24h | volume |", "|---|---:|---:|"]
        for row in top_by_24h[:5]:
            lines.append(
                f"| {row.get('symbol', '?')} | {_fmt_pct(row.get('change_24h_pct'))} | "
                f"{_fmt_usd(row.get('volume_24h_usdt'))} |"
            )

    if near_misses:
        lines += ["", "### Near Miss", "", "| symbol | reason | 1h | RS |", "|---|---|---:|---:|"]
        for row in near_misses[:5]:
            lines.append(
                f"| {row.get('symbol', '?')} | {row.get('reject_reason', '?')} | "
                f"{_fmt_pct(row.get('change_1h_pct'))} | "
                f"{_fmt_pct(row.get('relative_strength_pct'))} |"
            )

    lines.append("")
    return lines


def generate_report(
    input_path: Path = DEFAULT_INPUT,
    output_path: Path = DEFAULT_OUTPUT,
    *,
    include_archives: bool = True,
) -> Path:
    closed = _load_closed_with_archives(input_path, include_archives)
    all_stats = _compute_strategy_ev(closed)
    recent_trades = closed[-20:] if len(closed) >= 20 else closed
    recent_stats = _compute_strategy_ev(recent_trades)
    all_summary = _compute_stats(closed)
    recent_summary = _compute_stats(recent_trades)

    live_min_ev = float(os.getenv("LIVE_MIN_EV_PCT", "0.20"))
    live_min_filled = int(os.getenv("LIVE_MIN_RANKER_FILLED", "10"))
    executable = _rank_strategies(
        recent_stats,
        is_long=False,
        min_filled=live_min_filled,
        allow={"MARKET"},
        top=3,
    )
    shadow_short = _rank_strategies(
        recent_stats,
        is_long=False,
        min_filled=2,
        top=5,
    )
    shadow_long = _rank_strategies(
        recent_stats,
        is_long=True,
        min_filled=2,
        top=5,
    )

    if executable and executable[0][1].get("effective_ev", 0.0) >= live_min_ev:
        action = (
            f"MARKET SHORTは実行候補。直近EV "
            f"{_fmt_pct(executable[0][1].get('effective_ev'))} / "
            f"filled {executable[0][1].get('filled')}/{executable[0][1].get('total')}。"
        )
    else:
        action = (
            "実行可能なMARKET SHORTは安全条件未達。"
            "LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。"
        )

    generated_at = datetime.now(timezone.utc).isoformat()
    lines = [
        "# Decision Report",
        "",
        f"- generated_at: {generated_at}",
        f"- source: `{input_path}` + archive={include_archives}",
        f"- closed shadow trades: **{len(closed)}**",
        "",
        "## 1. 今日の判断",
        "",
        f"- 結論: **{action}**",
        f"- 全期間 MARKET基準: n={all_summary.n}, expectancy={_fmt_pct(all_summary.expectancy)}",
        f"- 直近20件 MARKET基準: n={recent_summary.n}, expectancy={_fmt_pct(recent_summary.expectancy)}",
        f"- live採用条件: `MARKET`のみ / EV >= {_fmt_pct(live_min_ev)} / filled >= {live_min_filled}",
        "",
        "### 実行可能ランキング (現executorで正確に測れるもの)",
        "",
        *_strategy_table(executable),
        "",
        "### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)",
        "",
        *_strategy_table(shadow_short),
        "",
        "### シャドウ上位 LONG",
        "",
        *_strategy_table(shadow_long),
        "",
    ]
    lines += _portfolio_section(LIVE_PORTFOLIO_FILE)
    lines += _market_context_section(MARKET_CONTEXT_FILE)
    lines += [
        "## 4. 次に見るべき不足",
        "",
        "- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。",
        "- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。",
        "- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。",
        "",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate compact decision report.")
    parser.add_argument("--in", dest="input_path", default=str(DEFAULT_INPUT))
    parser.add_argument("--out", dest="output_path", default=str(DEFAULT_OUTPUT))
    parser.add_argument(
        "--hot-only",
        action="store_true",
        help="do not include data/archive/*.json.gz",
    )
    args = parser.parse_args()
    path = generate_report(
        input_path=Path(args.input_path),
        output_path=Path(args.output_path),
        include_archives=not args.hot_only,
    )
    print(f"Decision report written: {path}")


if __name__ == "__main__":
    main()
