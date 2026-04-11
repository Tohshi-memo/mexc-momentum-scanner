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
from core.tracker import SymbolTracker
from utils.display import (
    console,
    print_analysis_result,
    print_btc_status,
    print_confirmed_signal,
    print_cycle_footer,
    print_header,
    print_no_candidates,
    print_scan_result,
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
    notifier: Notifier,
    dry_run: bool,
) -> None:
    """スキャン → テクニカル → ファンダ → 追跡更新 → 通知 の1サイクル。"""
    logger = logging.getLogger(__name__)

    # ── ヘッダー ─────────────────────────────────────────────────────
    print_header(cycle, dry_run)

    # ── 追跡中の銘柄の価格を更新して表示 ─────────────────────────────
    tracker.update_prices(scanner._client)
    active_tracked = tracker.active_symbols()
    if active_tracked:
        print_tracking_status(active_tracked)
        # TP / SL 到達チェック
        for s in active_tracked:
            if s.hit_tp() and len(s.prices) == 1:   # 今サイクルで初めて到達
                notifier.notify_tp_sl_hit(
                    s.symbol, s.detection_price, s.current_price,
                    s.current_change_pct, s.hours_tracked, hit_tp=True,
                )
            elif s.hit_sl() and len(s.prices) == 1:
                notifier.notify_tp_sl_hit(
                    s.symbol, s.detection_price, s.current_price,
                    s.current_change_pct, s.hours_tracked, hit_tp=False,
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
        return

    # ── Step 2: 急騰銘柄リスト ────────────────────────────────────────
    print_scan_result(surge_candidates)
    if not surge_candidates:
        return

    # ── Step 3: テクニカル分析 ────────────────────────────────────────
    console.print("\n  [dim]TECHNICAL ANALYSIS ──────────────────────────────[/dim]")
    analysis_results = analyzer.analyze_candidates(surge_candidates)
    for r in analysis_results:
        print_analysis_result(
            symbol=r.symbol, rsi=r.rsi, bb_upper=r.bb_upper,
            price=r.price, is_confirmed=r.is_confirmed_signal,
        )

    confirmed = [r for r in analysis_results if r.is_confirmed_signal]
    if not confirmed:
        console.print("\n  [dim]▸ No confirmed signals (RSI < 75 or price below BB).[/dim]\n")
        return

    # ── Step 4: ファンダ考察 + 追跡登録 + 通知 ───────────────────────
    console.print()
    for result in confirmed:
        try:
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

            # 追跡登録
            is_new = tracker.add_if_new(
                symbol=result.symbol,
                detection_price=result.price,
                rsi=result.rsi,
                change_1h=result.change_1h_pct,
                sl_price=proposal.stop_loss,
                tp_price=proposal.take_profit,
                conviction=fundamental.short_conviction if fundamental else "MEDIUM",
            )

            # 新規登録 かつ AVOID でない場合のみ Discord 通知
            conviction = fundamental.short_conviction if fundamental else "MEDIUM"
            if is_new and conviction != "AVOID":
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
    expired = tracker.clean_expired()
    for s in expired:
        notifier.notify_tracking_expired(
            symbol=s.symbol,
            entry=s.detection_price,
            final_price=s.current_price,
            final_change_pct=s.current_change_pct,
            min_price=s.min_price,
            max_price=s.max_price,
            hours_tracked=s.hours_tracked,
            hit_tp=s.hit_tp(),
            hit_sl=s.hit_sl(),
        )


def main() -> None:
    """メインループ。RUN_ONCE=true の場合は1サイクルで終了。"""
    setup_logging()
    logger = logging.getLogger(__name__)

    run_once_mode: bool = os.getenv("RUN_ONCE",   "false").lower() == "true"
    scan_interval: int  = int(os.getenv("SCAN_INTERVAL_SECONDS", "300"))
    dry_run:       bool = os.getenv("DRY_RUN",    "true").lower()  != "false"

    logger.info("MEXC Scanner starting | mode=%s dry_run=%s",
                "RUN_ONCE" if run_once_mode else f"LOOP/{scan_interval}s", dry_run)

    client               = MEXCClient()
    scanner              = MarketScanner(client)
    analyzer             = TechnicalAnalyzer(client)
    fundamental_analyzer = FundamentalAnalyzer()
    builder              = ProposalBuilder()
    executor             = ExecutorFactory.create(client)
    tracker              = SymbolTracker()
    notifier             = Notifier()

    cycle: int = 0

    while True:
        cycle += 1
        try:
            run_once(cycle, scanner, analyzer, fundamental_analyzer,
                     builder, executor, tracker, notifier, dry_run)
        except KeyboardInterrupt:
            console.print("\n  [dim]Interrupted. Shutting down.[/dim]")
            break
        except Exception as e:
            logger.error("Unhandled error in cycle #%d: %s", cycle, e, exc_info=True)
        finally:
            # 毎サイクル終了時に追跡データを保存
            try:
                tracker.save()
            except Exception as e:
                logger.error("Failed to save tracking data: %s", e)

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
