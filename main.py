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

# .env を最優先でロード（存在しない場合は .env.example の値を参照）
# ※ logging.warning() はここでは呼ばない（setup_logging() より先に呼ぶと
#   root logger が WARNING レベルで初期化され、後続の INFO ログが全て抑制される）
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
from utils.mexc_client import MEXCClient


def setup_logging() -> None:
    """ロギングをファイルとコンソールの両方に設定する。"""
    log_level_str: str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level: int = getattr(logging, log_level_str, logging.INFO)
    log_file: str = os.getenv("LOG_FILE", "logs/scanner.log")

    # logs/ ディレクトリを作成
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    log_format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    handlers: list[logging.Handler] = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_file, encoding="utf-8"),
    ]

    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=date_format,
        handlers=handlers,
        force=True,  # 既存ハンドラを強制的に置き換え（モジュール初期化時の先行設定を上書き）
    )

    # ccxt の内部ログをWARN以上のみ表示（ノイズ抑制）
    logging.getLogger("ccxt").setLevel(logging.WARNING)

    # dotenv フォールバック警告をロギング設定後に出力
    if _env_fallback_warning:
        logging.getLogger(__name__).warning(_env_fallback_warning)


def run_once(
    scanner: MarketScanner,
    analyzer: TechnicalAnalyzer,
    fundamental_analyzer: FundamentalAnalyzer,
    builder: ProposalBuilder,
    executor,
) -> None:
    """スキャン → テクニカル分析 → ファンダ考察 → 実行の1サイクル。

    Args:
        scanner: MarketScanner インスタンス
        analyzer: TechnicalAnalyzer インスタンス
        fundamental_analyzer: FundamentalAnalyzer インスタンス
        builder: ProposalBuilder インスタンス
        executor: BaseExecutor の具体実装 (DryRun or Live)
    """
    logger = logging.getLogger(__name__)

    # Step 1: スキャン
    btc_status, surge_candidates = scanner.run_scan()

    if not surge_candidates:
        logger.info("No surge candidates found. Waiting for next cycle.")
        return

    logger.info(
        "Found %d surge candidate(s). Starting technical analysis...",
        len(surge_candidates),
    )
    for c in surge_candidates:
        logger.info(
            "  Candidate: %s +%.2f%% vol=$%.0f",
            c.symbol, c.change_1h_pct, c.volume_24h_usdt,
        )

    # Step 2: テクニカル分析
    analysis_results = analyzer.analyze_candidates(surge_candidates)
    confirmed_signals = [r for r in analysis_results if r.is_confirmed_signal]

    if not confirmed_signals:
        logger.info("No confirmed signals after technical analysis.")
        return

    logger.info(
        "%d confirmed signal(s). Starting fundamental analysis...",
        len(confirmed_signals),
    )

    # Step 3: ファンダ考察（テクニカル確認済み銘柄のみ）
    for result in confirmed_signals:
        try:
            fundamental = fundamental_analyzer.analyze(result.symbol)
            proposal = builder.build(result, fundamental)
            executor.execute(proposal)
        except Exception as e:
            logger.error("Failed to process %s: %s", result.symbol, e)


def main() -> None:
    """メインループ。SCAN_INTERVAL_SECONDS ごとにスキャンサイクルを実行する。

    RUN_ONCE=true の場合は1サイクルのみ実行して終了する（GitHub Actions 向け）。
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    run_once_mode: bool = os.getenv("RUN_ONCE", "false").lower() == "true"
    scan_interval: int = int(os.getenv("SCAN_INTERVAL_SECONDS", "300"))

    logger.info("=" * 60)
    logger.info("MEXC Momentum Scanner starting up")
    logger.info(
        "Mode: %s | DRY_RUN=%s",
        "RUN_ONCE" if run_once_mode else f"LOOP every {scan_interval}s",
        os.getenv("DRY_RUN", "true"),
    )
    logger.info("=" * 60)

    # 依存オブジェクトの初期化
    client = MEXCClient()
    scanner = MarketScanner(client)
    analyzer = TechnicalAnalyzer(client)
    fundamental_analyzer = FundamentalAnalyzer()
    builder = ProposalBuilder()
    executor = ExecutorFactory.create(client)

    cycle: int = 0

    while True:
        cycle += 1
        logger.info("--- Cycle #%d ---", cycle)

        try:
            run_once(scanner, analyzer, fundamental_analyzer, builder, executor)
        except KeyboardInterrupt:
            logger.info("Interrupted by user. Shutting down.")
            break
        except Exception as e:
            logger.error("Unhandled error in scan cycle #%d: %s", cycle, e, exc_info=True)

        # RUN_ONCE モードは1サイクルで終了
        if run_once_mode:
            logger.info("RUN_ONCE mode: exiting after cycle #%d.", cycle)
            break

        logger.info("Cycle #%d done. Next scan in %ds...", cycle, scan_interval)
        try:
            time.sleep(scan_interval)
        except KeyboardInterrupt:
            logger.info("Interrupted during sleep. Shutting down.")
            break


if __name__ == "__main__":
    main()
