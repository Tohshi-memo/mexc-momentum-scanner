"""
utils/display.py
Rich ベースのレトロターミナル UI

カラースキーム: ダーク背景 + ブライトグリーン (クラシック CRT ターミナル調)
  通常情報  → bright_green
  警告/中程度 → bright_yellow
  シグナル/危険 → bright_red
  ミュート   → dim

GitHub Actions 環境でも force_terminal=True で ANSI カラーを強制出力する。
"""
from __future__ import annotations

from datetime import datetime, timezone

from rich import box
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text

# CI / GitHub Actions でも強制カラー出力
console = Console(force_terminal=True, highlight=False, width=100)

# ──────────────────────────────────────────────────────────────────────────────
# アスキーアートバナー
# ──────────────────────────────────────────────────────────────────────────────
_BANNER = """\
[bold bright_green]  ██████╗  ██████╗ ██╗  ██╗███████╗[/bold bright_green][bold white] ████████╗██████╗  █████╗ ██████╗ ███████╗[/bold white]
[bold bright_green]  ██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝[/bold bright_green][bold white] ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝[/bold white]
[bold bright_green]  ██████╔╝██║   ██║█████╔╝ ███████╗[/bold bright_green][bold white]    ██║   ██████╔╝███████║██║  ██║█████╗  [/bold white]
[bold bright_green]  ██╔══██╗██║   ██║██╔═██╗ ╚════██║[/bold bright_green][bold white]    ██║   ██╔══██╗██╔══██║██║  ██║██╔══╝  [/bold white]
[bold bright_green]  ██║  ██║╚██████╔╝██║  ██╗███████║[/bold bright_green][bold white]    ██║   ██║  ██║██║  ██║██████╔╝███████╗[/bold white]
[bold bright_green]  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝[/bold bright_green][bold white]    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝[/bold white]
[dim]  ─────────────  MEXC PERPETUAL FUTURES  //  AUTO SHORT DETECTION  ─────────────[/dim]"""


# ──────────────────────────────────────────────────────────────────────────────
# ヘルパー
# ──────────────────────────────────────────────────────────────────────────────

def _bar(value: float, max_val: float = 20.0, width: int = 12) -> str:
    """数値をブロック文字のゲージバーで表現する（rich markup 付き）。"""
    ratio = min(abs(value) / max(max_val, 0.01), 1.0)
    filled = round(ratio * width)
    return (
        "[bright_green]" + "█" * filled + "[/bright_green]"
        + "[dim]" + "░" * (width - filled) + "[/dim]"
    )


def _conviction_style(conviction: str) -> str:
    return {
        "HIGH":   "bold bright_red",
        "MEDIUM": "bold bright_yellow",
        "LOW":    "bright_green",
        "AVOID":  "dim",
        "UNKNOWN":"dim",
    }.get(conviction, "white")


# ──────────────────────────────────────────────────────────────────────────────
# Public 描画関数
# ──────────────────────────────────────────────────────────────────────────────

def print_header(cycle: int, dry_run: bool) -> None:
    """サイクル開始時のバナーとヘッダーを出力する。"""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    mode = (
        "[bold bright_yellow]◆ DRY RUN[/bold bright_yellow]"
        if dry_run
        else "[bold bright_red]◆ LIVE TRADING[/bold bright_red]"
    )
    console.print()
    console.print(Panel(
        Text.from_markup(_BANNER),
        box=box.DOUBLE,
        border_style="green",
        padding=(0, 1),
    ))
    console.print(
        f"  [dim]CYCLE[/dim] [bold white]#{cycle:03d}[/bold white]"
        f"  [dim]│[/dim]  [white]{now}[/white]"
        f"  [dim]│[/dim]  {mode}"
    )
    console.print()


def print_stats_panel(summary) -> None:
    """統計サマリーパネルを出力する (StatsSummary)。

    初めてのサイクルで記録がない場合はスキップ。
    """
    if summary.total == 0:
        console.print(Panel(
            Text.from_markup(
                "  [dim]No closed trades yet. Stats will appear after the first TP/SL hit.[/dim]"
            ),
            title="[bold]PERFORMANCE[/bold]",
            border_style="dim",
            box=box.DOUBLE,
            padding=(0, 1),
        ))
        return

    wr_style = (
        "bright_green" if summary.win_rate >= 55 else
        "bright_yellow" if summary.win_rate >= 40 else
        "bright_red"
    )
    pnl_style = "bright_green" if summary.total_pnl_pct >= 0 else "bright_red"
    exp_style = "bright_green" if summary.expectancy >= 0 else "bright_red"

    recent_warn = (
        "  [bright_red][!] CIRCUIT BREAKER RISK[/bright_red]"
        if summary.recent_losses >= summary.recent_window // 2
        else ""
    )

    content = (
        f"  [dim]TOTAL  [/dim][bold white]{summary.total:>4}[/bold white]"
        f"  [dim]W/L    [/dim][bright_green]{summary.wins:>3}[/bright_green]"
        f"/[bright_red]{summary.losses:<3}[/bright_red]"
        f"  [dim]EXPIRED[/dim] [dim]{summary.expired}[/dim]\n"
        f"  [dim]WIN RT [/dim][{wr_style}]{summary.win_rate:>5.1f}%[/{wr_style}]"
        f"  [dim]AVG W  [/dim][bright_green]{summary.avg_win:>+6.2f}%[/bright_green]"
        f"  [dim]AVG L  [/dim][bright_red]{summary.avg_loss:>+6.2f}%[/bright_red]\n"
        f"  [dim]EXPECT [/dim][{exp_style}]{summary.expectancy:>+5.2f}%[/{exp_style}]"
        f"  [dim]TOT PNL[/dim][{pnl_style}]{summary.total_pnl_pct:>+6.2f}%[/{pnl_style}]"
        f"  [dim]RECENT [/dim][bright_red]{summary.recent_losses}[/bright_red]"
        f"[dim]/{summary.recent_window} SL[/dim]"
        f"{recent_warn}"
    )
    console.print(Panel(
        Text.from_markup(content),
        title="[bold]PERFORMANCE[/bold]",
        border_style="bright_cyan",
        box=box.DOUBLE,
        padding=(0, 1),
    ))


def print_circuit_breaker() -> None:
    """サーキットブレーカー発動時の通知パネル。"""
    console.print(Panel(
        Text.from_markup(
            "  [bold bright_red]⊘  CIRCUIT BREAKER ACTIVE[/bold bright_red]\n\n"
            "  [dim]Recent loss streak exceeded threshold.[/dim]\n"
            "  [dim]All new entries are skipped this cycle.[/dim]\n"
            "  [dim]Review strategy parameters or wait for market conditions to normalize.[/dim]"
        ),
        title="[bold bright_red]RISK GUARD[/bold bright_red]",
        border_style="bright_red",
        box=box.DOUBLE,
        padding=(0, 1),
    ))


def print_cooldown_skip(symbol: str) -> None:
    """クールダウン中でエントリーをスキップしたことを1行で表示する。"""
    console.print(
        f"  [dim]⏱  [bright_yellow]{symbol}[/bright_yellow] skipped "
        "(recently stopped out, in cooldown).[/dim]"
    )


def print_btc_status(price: float, change_1h: float, is_bearish: bool,
                     is_stagnant: bool, is_signal: bool) -> None:
    """BTC ステータスパネルを出力する。"""
    if is_bearish:
        clr, label, border = "bright_red",    "▼ BEARISH",  "red"
    elif is_stagnant:
        clr, label, border = "bright_yellow", "◆ STAGNANT", "yellow"
    else:
        clr, label, border = "bright_green",  "▲ BULLISH",  "green"

    sign  = "+" if change_1h >= 0 else ""
    gauge = _bar(change_1h, max_val=2.0, width=10)
    sig   = (
        "[bold bright_green]██ ACTIVE  ──►  SCANNING ALTS[/bold bright_green]"
        if is_signal else "[dim]── INACTIVE  (BTC is moving, skip)[/dim]"
    )
    content = (
        f"  [dim]PRICE  [/dim][bold white]${price:>14,.4f}[/bold white]\n"
        f"  [dim]1H CHG [/dim][{clr}]{sign}{change_1h:.2f}%[/{clr}]"
        f"  {gauge}  [{clr}][{label}][/{clr}]\n"
        f"  [dim]SIGNAL [/dim]{sig}"
    )
    console.print(Panel(
        Text.from_markup(content),
        title="[bold]BTC / USDT[/bold]",
        border_style=border,
        box=box.DOUBLE,
        padding=(0, 1),
    ))


def print_scan_result(candidates: list) -> None:
    """スキャン結果テーブルを出力する。

    Args:
        candidates: SurgeCandidate のリスト
    """
    if not candidates:
        console.print(Panel(
            Text.from_markup("[dim]  No surge candidates in this cycle.[/dim]"),
            title="[bold]MARKET SCAN[/bold]",
            border_style="green",
            box=box.DOUBLE,
            padding=(0, 1),
        ))
        return

    table = Table(
        box=box.SIMPLE_HEAD,
        header_style="bold bright_green",
        show_edge=False,
        padding=(0, 2),
        min_width=84,
    )
    table.add_column("RNK",    style="dim",          width=4)
    table.add_column("SYMBOL", style="bright_cyan",  min_width=26)
    table.add_column("1H",     style="bright_yellow",justify="right", width=9)
    table.add_column("VOL 24H",style="white",        justify="right", width=12)
    table.add_column("CHART",  min_width=14)

    max_chg = max(c.change_1h_pct for c in candidates)
    for i, c in enumerate(candidates[:10], 1):
        vol = f"${c.volume_24h_usdt / 1_000_000:.1f}M"
        table.add_row(
            f"#{i:02d}",
            c.symbol,
            f"+{c.change_1h_pct:.2f}%",
            vol,
            _bar(c.change_1h_pct, max_val=max_chg, width=12),
        )

    n = len(candidates)
    header_txt = (
        f"  [bold bright_yellow]{n} SURGE CANDIDATE{'S' if n > 1 else ''}[/bold bright_yellow]"
        f"  [dim]detected while BTC is weak / stagnant[/dim]\n"
    )
    console.print(Panel(
        Group(Text.from_markup(header_txt), table),
        title="[bold]MARKET SCAN[/bold]",
        border_style="yellow",
        box=box.DOUBLE,
        padding=(0, 1),
    ))


def print_analysis_result(result) -> None:
    """テクニカル分析結果を1行で出力する (AnalysisResult を受け取る)。"""
    rsi_str = f"{result.rsi:.1f}" if result.rsi is not None else " N/A"
    rsi_4h_str = (
        f"{result.rsi_4h:.0f}" if result.rsi_4h is not None else "n/a"
    )

    if result.is_confirmed_signal:
        mark = "[bold bright_red]  ▶▶ SIGNAL[/bold bright_red]"
    else:
        mark = "[dim]  ── pass [/dim]"

    # 各フィルターのステータス
    bb_mark  = "[bright_red]BREAK[/bright_red]" if result.is_above_bb_upper else "[dim] ok  [/dim]"
    vol_mark = {
        "RISING":    "[bright_red]RISING[/bright_red]",
        "FLAT":      "[bright_yellow]FLAT  [/bright_yellow]",
        "DECLINING": "[bright_green]DECLIN[/bright_green]",
    }.get(result.volume_trend, "  --  ")
    rsi_4h_style = (
        "bright_red" if result.is_4h_trend_established else "bright_green"
    )

    console.print(
        f"  {mark}  [bright_cyan]{result.symbol:<24}[/bright_cyan]"
        f"  [dim]RSI[/dim] [bright_yellow]{rsi_str}[/bright_yellow]"
        f"  [dim]BB[/dim] {bb_mark}"
        f"  [dim]VOL[/dim] {vol_mark}"
        f"  [dim]4h[/dim] [{rsi_4h_style}]{rsi_4h_str}[/{rsi_4h_style}]"
        f"  [dim]@${result.price:.6g}[/dim]"
    )
    # 却下理由がある場合は dim 表示
    if result.reject_reasons and not result.is_confirmed_signal:
        console.print(
            f"              [dim]↳ {', '.join(result.reject_reasons)}[/dim]"
        )


def print_confirmed_signal(symbol: str, entry: float, sl: float, tp: float,
                            sl_pct: float, tp_pct: float, rsi: float | None,
                            bb_upper: float | None, change_1h: float,
                            volume: float, fundamental) -> None:
    """確認済みシグナルと擬似トレード提案をパネルで出力する。"""
    conviction  = fundamental.short_conviction if fundamental else "UNKNOWN"
    conv_style  = _conviction_style(conviction)
    catalyst    = fundamental.catalyst_type    if fundamental else "UNKNOWN"
    news_count  = fundamental.news_count       if fundamental else -1
    fund_reason = fundamental.reason           if fundamental else ""

    if conviction == "AVOID":
        console.print(Panel(
            Text.from_markup(
                f"  [bold bright_yellow]⊘  SIGNAL BLOCKED  —  AVOID SHORT[/bold bright_yellow]\n\n"
                f"  [dim]Fundamental catalyst detected. Shorting not recommended.[/dim]\n"
                f"  [dim]{fund_reason[:80]}[/dim]"
            ),
            title=f"[bold bright_yellow]⚠  {symbol}[/bold bright_yellow]",
            border_style="yellow",
            box=box.DOUBLE,
            padding=(0, 1),
        ))
        return

    rsi_str = f"{rsi:.1f}" if rsi is not None else "N/A"
    bb_str  = f"${bb_upper:.8g}" if bb_upper is not None else "N/A"

    # ── テクニカル列 ──────────────────────────────
    tech_lines = (
        f"  [dim]ENTRY[/dim]  [bold white]${entry:.8g}[/bold white]\n"
        f"\n"
        f"  [dim]SL   [/dim]  [bright_red]${sl:.8g}[/bright_red]"
        f"  [bright_red](+{sl_pct:.1f}%)[/bright_red]"
        f"  [dim]← SHORT SL 上方向[/dim]\n"
        f"  [dim]TP   [/dim]  [bright_green]${tp:.8g}[/bright_green]"
        f"  [bright_green](-{tp_pct:.1f}%)[/bright_green]"
        f"  [dim]← SHORT TP 下方向[/dim]\n"
        f"\n"
        f"  [dim]RSI  [/dim]  [bold bright_yellow]{rsi_str}[/bold bright_yellow]"
        f"  [bold bright_yellow][OVERBOUGHT ▲][/bold bright_yellow]\n"
        f"  [dim]BB   [/dim]  PRICE > {bb_str}"
        f"  [bold bright_yellow][BREAK ↑][/bold bright_yellow]\n"
        f"  [dim]1H   [/dim]  [bright_yellow]+{change_1h:.2f}%[/bright_yellow]\n"
        f"  [dim]VOL  [/dim]  ${volume:,.0f} USDT\n"
    )

    # ── ファンダ列 ──────────────────────────────────
    if news_count >= 0:
        fund_lines = (
            f"  [dim]CATALYST[/dim]  [{conv_style}]{catalyst}[/{conv_style}]\n"
            f"  [dim]NEWS 48H[/dim]  [white]{news_count} article(s)[/white]\n"
            f"  [dim]CONVICTION[/dim]\n"
            f"  [{conv_style}]  ▶  {conviction}[/{conv_style}]\n"
            f"\n"
            f"  [dim]{fund_reason[:55]}[/dim]\n"
        )
    else:
        fund_lines = (
            f"  [dim]FUNDAMENTAL DATA[/dim]\n"
            f"  [dim]  API key not set.[/dim]\n"
            f"  [dim]  Set CRYPTOPANIC_API_KEY[/dim]\n"
            f"  [dim]  for catalyst analysis.[/dim]\n"
        )

    # ── 2カラムレイアウト ────────────────────────────
    left  = Panel(Text.from_markup(tech_lines),  title="[dim]TECHNICAL[/dim]",
                  border_style="dim",  box=box.SIMPLE, padding=(0, 1))
    right = Panel(Text.from_markup(fund_lines),  title="[dim]FUNDAMENTAL[/dim]",
                  border_style="dim",  box=box.SIMPLE, padding=(0, 1))

    console.print(Panel(
        Group(
            Text.from_markup(
                f"  [bold bright_red]!! CONFIRMED SHORT SIGNAL[/bold bright_red]\n"
            ),
            Columns([left, right], equal=True, expand=True),
        ),
        title=f"[bold bright_red]▶  {symbol}[/bold bright_red]",
        border_style="bright_red",
        box=box.DOUBLE,
        padding=(0, 1),
    ))


def print_tracking_status(tracked: list) -> None:
    """追跡中の銘柄ステータスパネルを出力する。

    Args:
        tracked: TrackedSymbol のリスト
    """
    if not tracked:
        return

    table = Table(
        box=box.SIMPLE_HEAD,
        header_style="bold bright_green",
        show_edge=False,
        padding=(0, 2),
        min_width=84,
    )
    table.add_column("SYMBOL",   style="bright_cyan",   min_width=26)
    table.add_column("ENTRY",    style="dim",            justify="right", width=12)
    table.add_column("NOW",      style="white",          justify="right", width=12)
    table.add_column("CHANGE",   justify="right",        width=9)
    table.add_column("MIN CHG",  style="bright_green",   justify="right", width=9)
    table.add_column("TRACKED",  style="dim",            justify="right", width=7)
    table.add_column("STATUS",   width=10)

    for s in tracked:
        chg     = s.current_change_pct
        min_chg = (s.min_price - s.detection_price) / s.detection_price * 100

        chg_style = "bright_green" if chg <= 0 else "bright_red"
        chg_str   = f"[{chg_style}]{chg:+.2f}%[/{chg_style}]"

        if s.hit_tp():
            status = "[bold bright_green]✓ TP HIT[/bold bright_green]"
        elif s.hit_sl():
            status = "[bold bright_red]✗ SL HIT[/bold bright_red]"
        else:
            status = "[dim]● track[/dim]"

        table.add_row(
            s.symbol,
            f"${s.detection_price:.6g}",
            f"${s.current_price:.6g}",
            chg_str,
            f"{min_chg:.2f}%",
            f"{s.hours_tracked:.1f}h",
            status,
        )

    console.print(Panel(
        table,
        title=f"[bold]TRACKING  [{len(tracked)} active][/bold]",
        border_style="bright_cyan",
        box=box.DOUBLE,
        padding=(0, 1),
    ))


def print_no_candidates() -> None:
    """候補なし時のメッセージを出力する。"""
    console.print(
        "  [dim]▸ BTC signal active but no alts surging ≥ threshold. "
        "Waiting for next cycle...[/dim]"
    )
    console.print()


def print_cycle_footer(cycle: int, next_in: int | None = None) -> None:
    """サイクル終了フッターを出力する。"""
    if next_in:
        msg = f"[dim]CYCLE #{cycle:03d} COMPLETE  //  NEXT SCAN IN {next_in}s[/dim]"
    else:
        msg = f"[dim]CYCLE #{cycle:03d} COMPLETE[/dim]"
    console.print()
    console.rule(msg, style="dim green")
    console.print()
