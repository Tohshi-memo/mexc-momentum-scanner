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
from core.executor import ExecutorFactory, ProposalBuilder, TradeProposal
from core.experiment import ExperimentTracker, FilterSnapshot
from core.fundamental import FundamentalAnalyzer
from core.live_filter import LiveTradeFilter
from core.live_portfolio import LivePortfolio
from core.live_strategy import DIR_SHORT, ENTRY_MARKET, LiveStrategyBuilder, LiveTradePlan
from core.market_context import MarketContextRecorder
from core.safe_adaptive_portfolio import SafeAdaptivePortfolio
from core.scanner import MarketScanner
from core.strategy_ranker import StrategyRanker
from core.stats import StatsManager
from core.tracker import SymbolTracker
from tools.analyze_experiments import generate_report as generate_experiment_report
from tools.decision_report import generate_report as generate_decision_report
from tools.virtual_portfolio import update_portfolio_report
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
    experiment_tracker: ExperimentTracker,
    live_portfolio: LivePortfolio,
    live_filter: LiveTradeFilter,
    live_strategy: LiveStrategyBuilder,
    market_context: MarketContextRecorder,
    experiment_max_per_cycle: int,
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

    # ── シャドウトレードの価格更新 (フィルター実験用) ────────────────
    # 実トレードと独立したパイプライン。STRICT 通過/外を問わず、
    # 全ての過去候補の outcome をここで確定させる。
    try:
        experiment_tracker.update(scanner._client)
    except Exception as e:
        logger.warning("Experiment tracker update failed: %s", e)

    # ── 追跡中銘柄の価格更新 + TP/SL 到達の記録 ──────────────────────
    newly_closed = tracker.update_prices(scanner._client)
    if newly_closed:
        new_records = stats.record_many(newly_closed)
        # ライブ戦略の仮想ポートフォリオ ($100 ベース) に反映
        live_portfolio.record_many(new_records)
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
        regime=btc_status.regime,
    )

    # BTC データが取れなかった場合のみスキップ (regime は常にスキャン)
    if not btc_status.is_signal_active:
        print_no_candidates()
        _record_market_context(
            cycle, btc_status, scanner, market_context, [], logger
        )
        _finalize_expired(tracker, stats, notifier, live_portfolio)
        return

    # ── Step 2: 急騰銘柄リスト ────────────────────────────────────────
    print_scan_result(surge_candidates, regime=btc_status.regime)
    if not surge_candidates:
        _record_market_context(
            cycle, btc_status, scanner, market_context, [], logger
        )
        _finalize_expired(tracker, stats, notifier, live_portfolio)
        return

    # ── Step 3: テクニカル分析 ────────────────────────────────────────
    console.print("\n  [dim]TECHNICAL ANALYSIS ──────────────────────────────[/dim]")
    analysis_results = analyzer.analyze_candidates(surge_candidates)
    for r in analysis_results:
        print_analysis_result(r)
    _record_market_context(
        cycle, btc_status, scanner, market_context, analysis_results, logger
    )

    # ── シャドウトレード登録 (フィルター実験用) ──────────────────────
    # confirmed/rejected を問わず、最大 N 件まで仮想エントリー。
    # ProposalBuilder で本番と同じ ATR ベース SL/TP を計算するため、
    # 後の集計で「STRICT に通っていたら何が起きていたか」を比較できる。
    _register_shadow_trades(
        analysis_results,
        client=scanner._client,
        builder=builder,
        experiment_tracker=experiment_tracker,
        btc_change_1h=btc_status.change_1h_pct,
        regime=btc_status.regime,
        max_per_cycle=experiment_max_per_cycle,
        logger=logger,
    )

    confirmed = [r for r in analysis_results if r.is_confirmed_signal]
    if not confirmed:
        console.print(
            "\n  [dim]▸ No confirmed signals (filters rejected all candidates).[/dim]\n"
        )
        _finalize_expired(tracker, stats, notifier, live_portfolio)
        return

    # サーキットブレーカー発動中ならここでエントリーをスキップ
    if circuit_open:
        console.print(
            "\n  [bright_red]▸ Circuit breaker active — all confirmed signals skipped.[/bright_red]\n"
        )
        _finalize_expired(tracker, stats, notifier, live_portfolio)
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
            fund_conviction = (
                fundamental.short_conviction if fundamental else None
            )

            # Live filter (Tier S/A/B gating) + Strategy (direction/sizing)
            live_decision = live_filter.evaluate(
                result,
                regime=btc_status.regime,
                stats=stats,
                fundamental_conviction=fund_conviction,
            )
            if not live_decision.passed:
                console.print(
                    f"  [dim]▸ [bright_yellow]{result.symbol}[/bright_yellow] "
                    f"live_filter REJECT ({live_decision.summary()})[/dim]"
                )
                logger.info(
                    "Live filter reject %s: %s",
                    result.symbol, live_decision.summary(),
                )
                continue

            live_plan = live_strategy.build(
                result,
                live_decision,
                account_balance_usdt=live_portfolio.balance,
                recent_short_edge_pct=None,
            )
            if live_plan.direction != DIR_SHORT:
                console.print(
                    f"  [dim]▸ [bright_yellow]{result.symbol}[/bright_yellow] "
                    f"live_strategy direction={live_plan.direction} — skipped "
                    f"(executor is SHORT-only).[/dim]"
                )
                logger.info(
                    "Live strategy skip %s: direction=%s reasons=%s",
                    result.symbol, live_plan.direction, live_plan.reasons,
                )
                continue

            logger.info(
                "Live plan %s: %s",
                result.symbol, LiveStrategyBuilder.describe_plan(live_plan),
            )

            proposal = _proposal_from_live_plan(result, fundamental, live_plan)
            if proposal is None:
                console.print(
                    f"  [dim]▸ [bright_yellow]{result.symbol}[/bright_yellow] "
                    f"live_strategy {live_plan.entry_style} is shadow-only for now; "
                    f"skipped live portfolio tracking.[/dim]"
                )
                logger.info(
                    "Live strategy skip %s: unsupported executable plan %s",
                    result.symbol, LiveStrategyBuilder.describe_plan(live_plan),
                )
                continue

            exec_result = executor.execute(proposal)

            # シャドウトレードにファンダ情報を後付け
            # (シャドウ登録はファンダ分析前に行われるため)
            if fundamental:
                experiment_tracker.update_fundamental(
                    symbol=result.symbol,
                    catalyst_type=fundamental.catalyst_type,
                    short_conviction=fundamental.short_conviction,
                    news_count=fundamental.news_count,
                )

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
                relative_strength=result.relative_strength_pct,
                regime=btc_status.regime,
            )

            conviction = fundamental.short_conviction if fundamental else "MEDIUM"

            # AVOID なら追跡もしない
            if conviction == "AVOID":
                continue

            # LIVE モードで発注がスキップ/失敗した場合は tracker にも入れない。
            # (DRY RUN は status="dry_run" で常に通過 → tracker 登録される)
            exec_status = (exec_result or {}).get("status", "")
            if exec_status not in ("dry_run", "ok"):
                logger.warning(
                    "Skip tracking %s: executor status=%s reason=%s",
                    result.symbol, exec_status, (exec_result or {}).get("reason"),
                )
                continue

            # 追跡登録 (どのライブ戦略で発注したかを保存しておき、決済時に
            # LivePortfolio へ転記する)
            is_new = tracker.add_if_new(
                symbol=result.symbol,
                detection_price=proposal.entry_price,
                rsi=result.rsi,
                change_1h=result.change_1h_pct,
                sl_price=proposal.stop_loss,
                tp_price=proposal.take_profit,
                conviction=conviction,
                catalyst_type=fundamental.catalyst_type if fundamental else "UNKNOWN",
                market_regime=btc_status.regime,
                detection_rel_strength=result.relative_strength_pct,
                live_tier=live_decision.tier,
                live_direction=live_plan.direction,
                live_entry_style=live_plan.entry_style,
                live_boosters=live_decision.boosters,
                live_score=live_decision.score,
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
                    regime=btc_status.regime,
                    relative_strength=result.relative_strength_pct,
                )

        except Exception as e:
            logger.error("Failed to process %s: %s", result.symbol, e)

    # ── 期限切れ追跡の処理 ──────────────────────────────────────────
    _finalize_expired(tracker, stats, notifier, live_portfolio)


def _record_market_context(
    cycle: int,
    btc_status,
    scanner: MarketScanner,
    market_context: MarketContextRecorder,
    analysis_results,
    logger: logging.Logger,
) -> None:
    """Persist a compact scan snapshot without interrupting trading flow."""
    try:
        market_context.record(
            cycle=cycle,
            btc_status=btc_status,
            scan_context=scanner.last_scan_context,
            analysis_results=analysis_results,
        )
    except Exception as e:
        logger.warning("Failed to record market context: %s", e)


def _proposal_from_live_plan(
    result,
    fundamental,
    live_plan: LiveTradePlan,
) -> TradeProposal | None:
    """Build an executable SHORT proposal only when the live plan is truly executable.

    The current executor can safely model/execute immediate MARKET shorts only.
    LIMIT/scale entries remain in the shadow experiment until pending-order
    tracking exists, otherwise the live portfolio would be mislabeled.
    """
    if live_plan.direction != DIR_SHORT:
        return None
    if live_plan.entry_style != ENTRY_MARKET:
        return None

    market_legs = [
        leg for leg in live_plan.legs
        if leg.kind == "MARKET" and leg.weight > 0
    ]
    market_weight = sum(leg.weight for leg in market_legs)
    if not market_legs or market_weight < 0.999:
        return None

    entry_price = sum(leg.price * leg.weight for leg in market_legs) / market_weight
    return TradeProposal(
        symbol=result.symbol,
        direction=DIR_SHORT,
        entry_price=entry_price,
        stop_loss=live_plan.stop_loss,
        take_profit=live_plan.take_profit,
        sl_pct=live_plan.sl_pct,
        tp_pct=live_plan.tp_pct,
        rsi_at_entry=result.rsi,
        bb_upper_at_entry=result.bb_upper,
        volume_24h_usdt=result.volume_24h_usdt,
        change_1h_pct=result.change_1h_pct,
        fundamental=fundamental,
    )


def _register_shadow_trades(
    analysis_results,
    *,
    client,
    builder: ProposalBuilder,
    experiment_tracker: ExperimentTracker,
    btc_change_1h: float,
    regime: str,
    max_per_cycle: int,
    logger: logging.Logger,
) -> None:
    """全候補をシャドウトレードとして登録する。

    ProposalBuilder で本番と同じ SL/TP を計算するため、
    後で『現行 STRICT に通っていなくても結果はどうだったか』
    『RSI 閾値を 70 に下げていたら？』のような re-eval が同じデータで可能。

    各候補について order book の best ask/bid を取得し、スプレッド情報と
    複数のエントリー戦略バリアント (MARKET / ASK / LIMIT) を記録する。
    """
    if not analysis_results or max_per_cycle <= 0:
        return

    added = 0
    for r in analysis_results:
        if added >= max_per_cycle:
            break
        try:
            proposal = builder.build(r)
            price_vs_bb = (
                r.price / r.bb_upper if r.bb_upper and r.bb_upper > 0 else 0.0
            )
            snapshot = FilterSnapshot(
                rsi=r.rsi,
                rsi_4h=r.rsi_4h,
                bb_upper=r.bb_upper,
                price_vs_bb=price_vs_bb,
                volume_ratio=r.volume_trend_ratio,
                volume_trend=r.volume_trend,
                atr_pct=r.atr_pct,
                change_1h=r.change_1h_pct,
                relative_strength=r.relative_strength_pct,
                btc_change_1h=btc_change_1h,
                funding_rate=r.funding_rate,
                obv_divergence=r.obv_divergence,
                open_interest_usd=r.open_interest_usd,
                oi_change_pct=r.oi_change_pct,
                long_short_ratio=r.long_short_ratio,
                upper_wick_ratio_1h=r.upper_wick_ratio_1h,
                consecutive_green_1h=r.consecutive_green_1h,
                consecutive_green_4h=r.consecutive_green_4h,
                bb_width_pct=r.bb_width_pct,
                ma20_deviation_pct=r.ma20_deviation_pct,
                candle_body_ratio=r.candle_body_ratio,
                rsi_15m=r.rsi_15m,
                daily_direction=r.daily_direction,
            )

            # Order book からスプレッド情報を取得
            ask_price: float | None = None
            bid_price: float | None = None
            try:
                ob = client.fetch_order_book(r.symbol, limit=5)
                asks = ob.get("asks") or []
                bids = ob.get("bids") or []
                if asks:
                    ask_price = float(asks[0][0])
                if bids:
                    bid_price = float(bids[0][0])
            except Exception as e:
                logger.debug("Order book unavailable for %s: %s", r.symbol, e)

            registered = experiment_tracker.add_candidate(
                symbol=r.symbol,
                entry_price=proposal.entry_price,
                sl_price=proposal.stop_loss,
                tp_price=proposal.take_profit,
                sl_pct=proposal.sl_pct,
                tp_pct=proposal.tp_pct,
                market_regime=regime,
                filters=snapshot,
                confirmed_strict=r.is_confirmed_signal,
                ask_price=ask_price,
                bid_price=bid_price,
                # テクニカル指値バリアント用
                bb_upper=r.bb_upper,
                bb_middle=r.bb_middle,
                atr_pct=r.atr_pct,
                swing_low_1h=r.swing_low_1h,
            )
            if registered:
                added += 1
        except Exception as e:
            logger.debug("Shadow registration failed for %s: %s", r.symbol, e)


def _finalize_expired(
    tracker: SymbolTracker,
    stats: StatsManager,
    notifier: Notifier,
    live_portfolio: LivePortfolio,
) -> None:
    """期限切れの追跡エントリを EXPIRED として記録し通知する。

    TP/SL 確定済みは update_prices() で既に stats へ記録されているので、
    ここでは outcome=EXPIRED のものだけ記録する。
    """
    closed = tracker.clean_expired()
    expired_only = [s for s in closed if s.outcome == "EXPIRED"]
    if not expired_only:
        return

    new_records = stats.record_many(expired_only)
    # EXPIRED も仮想ポートフォリオに反映 (PnL は時間切れ時点の終値ベース)
    live_portfolio.record_many(new_records)
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

    # 実験用シャドウトレード設定
    experiment_max_per_cycle: int = int(os.getenv("EXPERIMENT_MAX_PER_CYCLE", "20"))

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
    experiment_tracker   = ExperimentTracker()
    live_portfolio       = LivePortfolio()
    safe_adaptive_portfolio = SafeAdaptivePortfolio()
    live_filter          = LiveTradeFilter()
    strategy_ranker      = StrategyRanker(experiment_tracker)
    live_strategy        = LiveStrategyBuilder(
        proposal_builder=builder, ranker=strategy_ranker,
    )
    market_context       = MarketContextRecorder()

    cycle: int = 0

    while True:
        cycle += 1
        try:
            run_once(
                cycle, scanner, analyzer, fundamental_analyzer,
                builder, executor, tracker, stats, notifier,
                experiment_tracker, live_portfolio,
                live_filter, live_strategy, market_context,
                experiment_max_per_cycle,
                dry_run, cooldown_hours, cb_window, cb_loss_threshold,
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
                experiment_tracker.save()
                live_portfolio.save()
            except Exception as e:
                logger.error("Failed to save data: %s", e)
            # Existing live_portfolio remains untouched; this is a separate $100
            # adaptive DryRun account driven by closed shadow experiments.
            try:
                safe_adaptive_portfolio.update()
            except Exception as e:
                logger.warning("Failed to update safe adaptive portfolio: %s", e)
            # シャドウトレードの集計レポートを再生成
            # （Claude が次回セッションでフィルター粒度を再評価するための入力）
            try:
                generate_experiment_report()
            except Exception as e:
                logger.warning("Failed to regenerate experiment report: %s", e)
            # 人間が読むための短い判断レポートを再生成
            try:
                generate_decision_report()
            except Exception as e:
                logger.warning("Failed to regenerate decision report: %s", e)
            # バーチャルポートフォリオのサマリーをログ出力
            try:
                update_portfolio_report()
            except Exception as e:
                logger.warning("Failed to update portfolio report: %s", e)

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
