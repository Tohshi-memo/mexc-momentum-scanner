"""
main.py
MEXC Momentum Scanner - エントリーポイント

実行方法:
    cp .env.example .env  # APIキーと設定値を編集
    python main.py
"""
from __future__ import annotations

import logging
import os
import time
from pathlib import Path

from dotenv import load_dotenv

_env_path = Path(__file__).parent / ".env"
_env_example_path = Path(__file__).parent / ".env.example"
_env_fallback_warning: str = ""
if _env_path.exists():
    load_dotenv(_env_path)
elif _env_example_path.exists():
    load_dotenv(_env_example_path)
    _env_fallback_warning = (
        ".env not found. Loaded .env.example as fallback."
    )

from core.analyzer import TechnicalAnalyzer
from core.executor import ExecutorFactory, ProposalBuilder
from core.fundamental import FundamentalAnalyzer
from core.scanner import MarketScanner
from core.stats import StatsManager
from core.tracker import SymbolTracker
from utils.display import (
    console,
    print_analysis_result,
    print_btc_status,
    print_circuit_breaker,
    print_confirmed_signal,
    print_cooldown_skip,
    print_cycle_footer,
    print_header,
    print_no_candidates,
    print_scan_result,
    print_stats_panel,
    print_tracking_status,
)
from utils.mexc_client import MEXCClient
from utils.notifier import Notifier


def setup_logging() -> None:
    """ロギングをファイル専用に設定する。

    コンソール出力は rich が担当。WARNING 以上のみ RichHandler でコンソールに出力。
    """
    from rich.logging import RichHandler

    log_level: int = getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO)
    log_file: str  = os.getenv("LOG_FILE", "logs/scanner.log")
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            RichHandler(console=console, level=logging.WARNING,
                        rich_tracebacks=True, show_path=False),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
        force=True,
    )
    logging.getLogger("ccxt").setLevel(logging.WARNING)
    if _env_fallback_warning:
        logging.getLogger(__name__).warning(_env_fallback_warning)


def run_once(
    cycle: int,
    scanner: MarketScanner,
    analyzer: TechnicalAnalyzer,
    fundamental_analyzer: FundamentalAnalyzer,
    builder: ProposalBuilder,
    executor,
    tracker: SymbolTracker,
    stats: StatsManager,
    notifier: Notifier,
    dry_run: bool,
    cooldown_hours: int,
    cb_window: int,
    cb_loss_threshold: int,
) -> None:
    """スキャン → テクニカル → ファンダ → 追跡更新 → 通知 の1サイクル。

    損失低減フィルターを組み込んだパイプライン:
      1. Stats を表示 (Performance panel)
      2. 追跡中の価格を更新 → TP/SL 確定したら記録 & 通知
      3. Circuit breaker 判定 (直近 N 件中 M 件以上 SL なら当サイクル全スキップ)
      4. BTC ステータス + サージ検知
      5. テクニカル分析 (RSI/BB/出来高/4h RSI)
      6. 各 confirmed シグナルごとに:
         a. Cooldown チェック (直近 SL 銘柄はスキップ)
         b. ファンダメンタル考察
         c. DRY RUN ログ出力
         d. 追跡登録
         e. Discord 通知
      7. 期限切れ追跡を EXPIRED として記録
    """
    logger = logging.getLogger(__name__)

    # ── ヘッダー ─────────────────────────────────────────────────────
    print_header(cycle, dry_run)

    # ── 実績パネル ───────────────────────────────────────────────────
    summary = stats.summary(recent_window=cb_window)
    print_stats_panel(summary)

    # ── 追跡中銘柄の価格更新 + TP/SL 到達の記録 ──────────────────────
    newly_closed = tracker.update_prices(scanner._client)
    if newly_closed:
        stats.record_many(newly_closed)
        # TP/SL 到達 Discord 通知
        for s in newly_closed:
            if s.outcome == "TP_HIT":
                notifier.notify_tp_sl_hit(
                    s.symbol, s.detection_price,
                    s.outcome_price or s.current_price,
                    s.current_change_pct, s.hours_tracked, hit_tp=True,
                )
            elif s.outcome == "SL_HIT":
                notifier.notify_tp_sl_hit(
                    s.symbol, s.detection_price,
                    s.outcome_price or s.current_price,
                    s.current_change_pct, s.hours_tracked, hit_tp=False,
                )

    active_tracked = tracker.active_symbols()
    if active_tracked:
        print_tracking_status(active_tracked)

    # ── サーキットブレーカー判定 ─────────────────────────────────────
    circuit_open = stats.circuit_breaker_active(
        window=cb_window, loss_threshold=cb_loss_threshold,
    )
    if circuit_open:
        print_circuit_breaker()
        logger.warning(
            "Circuit breaker active: recent_losses=%d/%d threshold=%d. "
            "Skipping all entries this cycle.",
            summary.recent_losses, cb_window, cb_loss_threshold,
        )

    # ── Step 1: BTC ステータス確認 ────────────────────────────────────
    btc_status, surge_candidates = scanner.run_scan()

    print_btc_status(
        price=btc_status.price,
        change_1h=btc_status.change_1h_pct,
        is_bearish=btc_status.is_bearish,
        is_stagnant=btc_status.is_stagnant,
        is_signal=btc_status.is_signal_active,
    )

    if not btc_status.is_signal_active:
        print_no_candidates()
        _finalize_expired(tracker, stats, notifier)
        return

    # ── Step 2: 急騰銘柄リスト ────────────────────────────────────────
    print_scan_result(surge_candidates)
    if not surge_candidates:
        _finalize_expired(tracker, stats, notifier)
        return

    # ── Step 3: テクニカル分析 ────────────────────────────────────────
    console.print("\n  [dim]TECHNICAL ANALYSIS ──────────────────────────────[/dim]")
    analysis_results = analyzer.analyze_candidates(surge_candidates)
    for r in analysis_results:
        print_analysis_result(r)

    confirmed = [r for r in analysis_results if r.is_confirmed_signal]
    if not confirmed:
        console.print(
            "\n  [dim]▸ No confirmed signals (filters rejected all candidates).[/dim]\n"
        )
        _finalize_expired(tracker, stats, notifier)
        return

    # サーキットブレーカー発動中ならここでエントリーをスキップ
    if circuit_open:
        console.print(
            "\n  [bright_red]▸ Circuit breaker active — all confirmed signals skipped.[/bright_red]\n"
        )
        _finalize_expired(tracker, stats, notifier)
        return

    # ── Step 4: ファンダ考察 + 追跡登録 + 通知 ───────────────────────
    console.print()
    for result in confirmed:
        try:
            # Cooldown チェック (直近 SL で食らった銘柄はスキップ)
            if stats.had_sl_within(result.symbol, hours=cooldown_hours):
                print_cooldown_skip(result.symbol)
                logger.info(
                    "Cooldown skip: %s (SL within last %dh)",
                    result.symbol, cooldown_hours,
                )
                continue

            fundamental = fundamental_analyzer.analyze(result.symbol)
            proposal    = builder.build(result, fundamental)
            executor.execute(proposal)

            print_confirmed_signal(
                symbol=result.symbol,
                entry=proposal.entry_price,
                sl=proposal.stop_loss,
                tp=proposal.take_profit,
                sl_pct=proposal.sl_pct,
                tp_pct=proposal.tp_pct,
                rsi=result.rsi,
                bb_upper=result.bb_upper,
                change_1h=result.change_1h_pct,
                volume=result.volume_24h_usdt,
                fundamental=fundamental,
            )

            conviction = fundamental.short_conviction if fundamental else "MEDIUM"

            # AVOID なら追跡もしない
            if conviction == "AVOID":
                continue

            # 追跡登録
            is_new = tracker.add_if_new(
                symbol=result.symbol,
                detection_price=result.price,
                rsi=result.rsi,
                change_1h=result.change_1h_pct,
                sl_price=proposal.stop_loss,
                tp_price=proposal.take_profit,
                conviction=conviction,
                catalyst_type=fundamental.catalyst_type if fundamental else "UNKNOWN",
            )

            if is_new:
                notifier.notify_new_signal(
                    symbol=result.symbol,
                    entry=proposal.entry_price,
                    sl=proposal.stop_loss,
                    tp=proposal.take_profit,
                    sl_pct=proposal.sl_pct,
                    tp_pct=proposal.tp_pct,
                    rsi=result.rsi,
                    change_1h=result.change_1h_pct,
                    conviction=conviction,
                    catalyst=fundamental.catalyst_type if fundamental else "UNKNOWN",
                    news_count=fundamental.news_count if fundamental else -1,
                )

        except Exception as e:
            logger.error("Failed to process %s: %s", result.symbol, e)

    # ── 期限切れ追跡の処理 ──────────────────────────────────────────
    _finalize_expired(tracker, stats, notifier)


def _finalize_expired(
    tracker: SymbolTracker,
    stats: StatsManager,
    notifier: Notifier,
) -> None:
    """期限切れの追跡エントリを EXPIRED として記録し通知する。

    TP/SL 確定済みは update_prices() で既に stats へ記録されているので、
    ここでは outcome=EXPIRED のものだけ記録する。
    """
    closed = tracker.clean_expired()
    expired_only = [s for s in closed if s.outcome == "EXPIRED"]
    if not expired_only:
        return

    stats.record_many(expired_only)
    for s in expired_only:
        notifier.notify_tracking_expired(
            symbol=s.symbol,
            entry=s.detection_price,
            final_price=s.current_price,
            final_change_pct=s.current_change_pct,
            min_price=s.min_price,
            max_price=s.max_price,
            hours_tracked=s.hours_tracked,
            hit_tp=False,
            hit_sl=False,
        )


def main() -> None:
    """メインループ。RUN_ONCE=true の場合は1サイクルで終了。"""
    setup_logging()
    logger = logging.getLogger(__name__)

    run_once_mode: bool = os.getenv("RUN_ONCE",   "false").lower() == "true"
    scan_interval: int  = int(os.getenv("SCAN_INTERVAL_SECONDS", "300"))
    dry_run:       bool = os.getenv("DRY_RUN",    "true").lower()  != "false"

    # 損失低減用パラメーター
    cooldown_hours:    int = int(os.getenv("COOLDOWN_HOURS", "48"))
    cb_window:         int = int(os.getenv("CIRCUIT_BREAKER_WINDOW", "10"))
    cb_loss_threshold: int = int(os.getenv("CIRCUIT_BREAKER_LOSSES", "5"))

    logger.info(
        "MEXC Scanner starting | mode=%s dry_run=%s cooldown=%dh cb=%d/%d",
        "RUN_ONCE" if run_once_mode else f"LOOP/{scan_interval}s",
        dry_run, cooldown_hours, cb_loss_threshold, cb_window,
    )

    client               = MEXCClient()
    scanner              = MarketScanner(client)
    analyzer             = TechnicalAnalyzer(client)
    fundamental_analyzer = FundamentalAnalyzer()
    builder              = ProposalBuilder()
    executor             = ExecutorFactory.create(client)
    tracker              = SymbolTracker()
    stats                = StatsManager()
    notifier             = Notifier()

    cycle: int = 0

    while True:
        cycle += 1
        try:
            run_once(
                cycle, scanner, analyzer, fundamental_analyzer,
                builder, executor, tracker, stats, notifier, dry_run,
                cooldown_hours, cb_window, cb_loss_threshold,
            )
        except KeyboardInterrupt:
            console.print("\n  [dim]Interrupted. Shutting down.[/dim]")
            break
        except Exception as e:
            logger.error("Unhandled error in cycle #%d: %s", cycle, e, exc_info=True)
        finally:
            try:
                tracker.save()
                stats.save()
            except Exception as e:
                logger.error("Failed to save data: %s", e)

        if run_once_mode:
            print_cycle_footer(cycle)
            break

        print_cycle_footer(cycle, next_in=scan_interval)
        try:
            time.sleep(scan_interval)
        except KeyboardInterrupt:
            console.print("\n  [dim]Interrupted. Shutting down.[/dim]")
            break


if __name__ == "__main__":
    main()
