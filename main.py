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
_env_path = Path(__file__).parent / ".env"
_env_example_path = Path(__file__).parent / ".env.example"
if _env_path.exists():
    load_dotenv(_env_path)
elif _env_example_path.exists():
    load_dotenv(_env_example_path)
    logging.warning(
        ".env not found. Loaded .env.example as fallback. "
        "Create .env with your actual credentials."
    )

from core.analyzer import TechnicalAnalyzer
from core.executor import ExecutorFactory, ProposalBuilder
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
    )

    # ccxt の内部ログをWARN以上のみ表示（ノイズ抑制）
    logging.getLogger("ccxt").setLevel(logging.WARNING)


def run_once(
    scanner: MarketScanner,
    analyzer: TechnicalAnalyzer,
    builder: ProposalBuilder,
    executor,
) -> None:
    """スキャン → 分析 → 実行の1サイクルを実行する。

    Args:
        scanner: MarketScanner インスタンス
        analyzer: TechnicalAnalyzer インスタンス
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
        logger.info("  Candidate: %s +%.2f%% vol=$%.0f", c.symbol, c.change_1h_pct, c.volume_24h_usdt)

    # Step 2: テクニカル分析
    analysis_results = analyzer.analyze_candidates(surge_candidates)

    confirmed_signals = [r for r in analysis_results if r.is_confirmed_signal]

    if not confirmed_signals:
        logger.info("No confirmed signals after technical analysis.")
        return

    logger.info(
        "%d confirmed signal(s) after analysis. Generating trade proposals...",
        len(confirmed_signals),
    )

    # Step 3: 擬似/実注文実行
    for result in confirmed_signals:
        try:
            proposal = builder.build(result)
            executor.execute(proposal)
        except Exception as e:
            logger.error("Failed to execute proposal for %s: %s", result.symbol, e)


def main() -> None:
    """メインループ。SCAN_INTERVAL_SECONDS ごとにスキャンサイクルを実行する。"""
    setup_logging()
    logger = logging.getLogger(__name__)

    scan_interval: int = int(os.getenv("SCAN_INTERVAL_SECONDS", "300"))

    logger.info("=" * 60)
    logger.info("MEXC Momentum Scanner starting up")
    logger.info("Scan interval: %ds | DRY_RUN=%s", scan_interval, os.getenv("DRY_RUN", "true"))
    logger.info("=" * 60)

    # 依存オブジェクトの初期化
    client = MEXCClient()
    scanner = MarketScanner(client)
    analyzer = TechnicalAnalyzer(client)
    builder = ProposalBuilder()
    executor = ExecutorFactory.create(client)

    cycle: int = 0

    while True:
        cycle += 1
        logger.info("--- Cycle #%d ---", cycle)

        try:
            run_once(scanner, analyzer, builder, executor)
        except KeyboardInterrupt:
            logger.info("Interrupted by user. Shutting down.")
            break
        except Exception as e:
            logger.error("Unhandled error in scan cycle #%d: %s", cycle, e, exc_info=True)
            # サイクルエラーでプロセスを止めず、次のサイクルへ
        finally:
            if cycle > 0:
                logger.info(
                    "Cycle #%d done. Next scan in %ds...", cycle, scan_interval
                )
                try:
                    time.sleep(scan_interval)
                except KeyboardInterrupt:
                    logger.info("Interrupted during sleep. Shutting down.")
                    break


if __name__ == "__main__":
    main()
