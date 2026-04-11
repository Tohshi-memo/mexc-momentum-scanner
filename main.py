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
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

# .env を最優先でロード
# ※ logging.warning() はここでは呼ばない（setup_logging() より先に呼ぶと
#   root logger が WARNING レベルで初期化され後続の INFO ログが抑制される）
_env_path = Path(__file__).parent / ".env"
_env_example_path = Path(__file__).parent / ".env.example"
_env_fallback_warning: str = ""
if _env_path.exists():
    load_dotenv(_env_path)
elif _env_example_path.exists():
    load_dotenv(_env_example_path)
    _env_fallback_warning = (
        ".env not found. Loaded .env.example as fallback. "
        "Create .env with your actual credentials."
    )

from core.analyzer import TechnicalAnalyzer
from core.executor import ExecutorFactory, ProposalBuilder
from core.fundamental import FundamentalAnalyzer
from core.scanner import MarketScanner
from utils.display import (
    console,
    print_analysis_result,
    print_btc_status,
    print_confirmed_signal,
    print_cycle_footer,
    print_header,
    print_no_candidates,
    print_scan_result,
)
from utils.mexc_client import MEXCClient


def setup_logging() -> None:
    """ロギングをファイル専用に設定する。

    コンソール出力は rich (display.py) が担当するため、
    logging は artifact ログファイルへの記録のみ行う。
    WARNING 以上のみ rich コンソールにも出力する。
    """
    from rich.logging import RichHandler

    log_level_str: str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level: int = getattr(logging, log_level_str, logging.INFO)
    log_file: str = os.getenv("LOG_FILE", "logs/scanner.log")

    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    handlers: list[logging.Handler] = [
        # WARNING 以上のみ rich コンソールに出力（エラーを見逃さないため）
        RichHandler(
            console=console,
            level=logging.WARNING,
            rich_tracebacks=True,
            show_path=False,
        ),
        # INFO 以上はすべてファイルに記録
        logging.FileHandler(log_file, encoding="utf-8"),
    ]

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
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
    dry_run: bool,
) -> None:
    """スキャン → テクニカル分析 → ファンダ考察 → 実行の1サイクル。"""
    logger = logging.getLogger(__name__)

    # ── ヘッダー ────────────────────────────────────────────────
    print_header(cycle, dry_run)

    # ── Step 1: BTC ステータス確認 ──────────────────────────────
    btc_status, surge_candidates = scanner.run_scan()

    print_btc_status(
        price=btc_status.price,
        change_1h=btc_status.change_1h_pct,
        is_bearish=btc_status.is_bearish,
        is_stagnant=btc_status.is_stagnant,
        is_signal=btc_status.is_signal_active,
    )

    if not btc_status.is_signal_active:
        logger.info("BTC signal not active. Skipping alt scan.")
        print_no_candidates()
        return

    # ── Step 2: 急騰銘柄リスト ──────────────────────────────────
    print_scan_result(surge_candidates)

    if not surge_candidates:
        logger.info("No surge candidates found.")
        return

    # ── Step 3: テクニカル分析 ──────────────────────────────────
    console.print(
        "\n  [dim]TECHNICAL ANALYSIS ─────────────────────────────────[/dim]"
    )
    analysis_results = analyzer.analyze_candidates(surge_candidates)
    for r in analysis_results:
        print_analysis_result(
            symbol=r.symbol,
            rsi=r.rsi,
            bb_upper=r.bb_upper,
            price=r.price,
            is_confirmed=r.is_confirmed_signal,
        )

    confirmed = [r for r in analysis_results if r.is_confirmed_signal]
    if not confirmed:
        logger.info("No confirmed signals after technical analysis.")
        console.print(
            "\n  [dim]▸ No confirmed signals (RSI < 75 or price below BB upper).[/dim]\n"
        )
        return

    # ── Step 4: ファンダ考察 + 擬似注文出力 ────────────────────
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
        except Exception as e:
            logger.error("Failed to process %s: %s", result.symbol, e)


def main() -> None:
    """メインループ。SCAN_INTERVAL_SECONDS ごとにスキャンサイクルを実行する。"""
    setup_logging()
    logger = logging.getLogger(__name__)

    run_once_mode: bool = os.getenv("RUN_ONCE", "false").lower() == "true"
    scan_interval: int = int(os.getenv("SCAN_INTERVAL_SECONDS", "300"))
    dry_run: bool = os.getenv("DRY_RUN", "true").lower() != "false"

    logger.info(
        "MEXC Momentum Scanner starting | mode=%s dry_run=%s",
        "RUN_ONCE" if run_once_mode else f"LOOP/{scan_interval}s",
        dry_run,
    )

    client              = MEXCClient()
    scanner             = MarketScanner(client)
    analyzer            = TechnicalAnalyzer(client)
    fundamental_analyzer = FundamentalAnalyzer()
    builder             = ProposalBuilder()
    executor            = ExecutorFactory.create(client)

    cycle: int = 0

    while True:
        cycle += 1
        try:
            run_once(
                cycle, scanner, analyzer,
                fundamental_analyzer, builder, executor, dry_run,
            )
        except KeyboardInterrupt:
            console.print("\n  [dim]Interrupted. Shutting down.[/dim]")
            break
        except Exception as e:
            logger.error("Unhandled error in cycle #%d: %s", cycle, e, exc_info=True)

        if run_once_mode:
            print_cycle_footer(cycle)
            logger.info("RUN_ONCE: exiting after cycle #%d.", cycle)
            break

        print_cycle_footer(cycle, next_in=scan_interval)
        try:
            time.sleep(scan_interval)
        except KeyboardInterrupt:
            console.print("\n  [dim]Interrupted during sleep. Shutting down.[/dim]")
            break


if __name__ == "__main__":
    main()
