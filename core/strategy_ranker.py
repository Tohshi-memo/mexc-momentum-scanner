"""
core/strategy_ranker.py
直近 N サイクルの experiment_tracker データから
エントリー戦略の実質期待値ランキングを計算する。

実質期待値 (effective_ev) = fill_rate × avg_pnl
    - fill_rate: 戦略バリアントが実際に約定した割合 (未約定の機会損失を加味)
    - avg_pnl:   約定トレードの平均 PnL (%)

この値が高い戦略 = 現在の相場で最も利益を出している決定。
ライブ戦略は毎サイクル最新ランキングを参照し、
最もEVが高い実装可能戦略 (かつ EV > 0) を採用する。

出力は data/experiment_report.md セクション0「意思決定サマリー」と同じ値。
ロジックは tools/analyze_experiments._compute_strategy_ev を
ライブ側で再利用できる形に切り出したもの。
"""
from __future__ import annotations

import logging
import math
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Callable

from core.live_policy import live_policy_fingerprint

if TYPE_CHECKING:
    from core.experiment import ExperimentTracker

logger = logging.getLogger(__name__)

DEFAULT_LIVE_GATE_WINDOWS = (20, 50, 100, 200)


@dataclass
class StrategyStat:
    strategy: str           # e.g. "MARKET", "LIMIT_1PCT", "LIMIT_9PCT_LONG"
    filled: int
    total: int
    avg_pnl: float          # 約定トレードの平均 PnL (%)
    fill_rate: float        # 0.0〜1.0
    effective_ev: float     # fill_rate × avg_pnl

    @property
    def is_long(self) -> bool:
        return self.strategy.endswith("_LONG")


@dataclass(frozen=True)
class LiveGateWindowStat:
    """単一の履歴窓に対する、コスト控除後の実弾可否判定。"""

    window: int
    total: int
    observed: int
    filled: int
    required_filled: int
    missing: int
    invalid: int
    avg_pnl: float | None
    fill_rate: float | None
    gross_ev: float | None
    net_ev: float | None
    passed: bool
    reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class LiveGateDecision:
    """複数窓がすべて整合した場合だけ通過する実弾判定。"""

    strategy: str
    policy_version: str
    policy_fingerprint: str
    passed: bool
    windows: tuple[LiveGateWindowStat, ...]
    fee_pct: float
    slippage_pct: float
    funding_pct: float
    min_net_ev_pct: float
    max_data_age_hours: float
    source_total: int
    eligible_total: int
    latest_data_at: str | None
    data_age_hours: float | None
    min_distinct_days: int
    distinct_days: int
    min_ci_pct: float
    daily_mean_net_pnl: float | None
    lower95_pct: float | None
    reasons: tuple[str, ...] = field(default_factory=tuple)

    @property
    def total_cost_pct(self) -> float:
        """1約定あたりに控除する往復コスト合計 (% point)。"""
        return self.fee_pct + self.slippage_pct + self.funding_pct

    def summary(self) -> str:
        state = "PASS" if self.passed else "REJECT"
        windows = ", ".join(
            (
                f"{item.window}:net={item.net_ev:+.3f}%"
                if item.net_ev is not None
                else f"{item.window}:n/a"
            )
            for item in self.windows
        )
        details = f" ({'; '.join(self.reasons)})" if self.reasons else ""
        freshness = (
            f" age={self.data_age_hours:.2f}h"
            if self.data_age_hours is not None
            else " age=n/a"
        )
        cluster = (
            f" history={self.eligible_total}/{self.source_total}"
            f" days={self.distinct_days}"
            + (
                f" lower95={self.lower95_pct:+.3f}%"
                if self.lower95_pct is not None
                else " lower95=n/a"
            )
        )
        return (
            f"{state} policy={self.policy_version} strategy={self.strategy} "
            f"fingerprint={self.policy_fingerprint[:12]} "
            f"cost={self.total_cost_pct:.3f}% "
            f"windows=[{windows}]{freshness}{cluster}{details}"
        )


class StrategyRanker:
    """experiment_tracker._closed から戦略ランキングを計算する。

    build() ごとに compute() を再計算する設計 (サイクル中に
    新しい確定トレードが加わっても即反映)。コストは直近 N 件 ×
    1トレード 30 variants 程度なので無視できる。
    """

    def __init__(
        self,
        experiment_tracker: "ExperimentTracker",
        *,
        recent_n: int = 20,
        min_filled: int = 2,
        live_trade_predicate: Callable[[object], bool] | None = None,
    ) -> None:
        self._exp = experiment_tracker
        self._recent_n = recent_n
        self._min_filled = min_filled
        self._live_trade_predicate = live_trade_predicate

        # 実弾ゲートは、従来のランキング表示とは独立させる。compute()/top()
        # は後方互換のため gross EV のまま維持し、実発注側だけがこの設定を
        # evaluate_live_gate() 経由で使用する。
        self._live_gate_windows = self._parse_live_gate_windows(
            os.getenv(
                "LIVE_GATE_WINDOWS",
                ",".join(str(value) for value in DEFAULT_LIVE_GATE_WINDOWS),
            )
        )
        self._live_fee_pct = self._env_nonnegative_float(
            "LIVE_GATE_FEE_PCT", "0.16"
        )
        self._live_slippage_pct = self._env_nonnegative_float(
            "LIVE_GATE_SLIPPAGE_PCT", "0.20"
        )
        self._live_funding_pct = self._env_nonnegative_float(
            "LIVE_GATE_FUNDING_PCT", "0.15"
        )
        self._live_min_net_ev_pct = self._env_nonnegative_float(
            "LIVE_GATE_MIN_NET_EV_PCT", "0.20"
        )
        self._live_min_filled = self._env_positive_int(
            "LIVE_GATE_MIN_FILLED", "20"
        )
        self._live_min_fill_rate = self._env_bounded_float(
            "LIVE_GATE_MIN_FILL_RATE", "0.80", lower=0.0, upper=1.0
        )
        self._live_max_data_age_hours = self._env_positive_float(
            "LIVE_GATE_MAX_DATA_AGE_HOURS", "24"
        )
        self._live_min_distinct_days = self._env_positive_int(
            "LIVE_GATE_MIN_DISTINCT_DAYS", "30"
        )
        self._live_min_ci_pct = self._env_finite_float(
            "LIVE_GATE_MIN_CI_PCT", "0.0"
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def compute(self) -> list[StrategyStat]:
        """直近 N 件の closed shadow trades から戦略ごとの EV を計算し、
        effective_ev 降順でソートして返す。
        """
        closed = getattr(self._exp, "_closed", None) or []
        trades = closed[-self._recent_n:] if self._recent_n > 0 else closed

        totals: dict[str, int] = {}
        pnls: dict[str, list[float]] = {}

        for t in trades:
            variants = getattr(t, "entry_variants", None)
            if not variants:
                continue
            for v in variants:
                strat = getattr(v, "strategy", None)
                if not strat:
                    continue
                totals[strat] = totals.get(strat, 0) + 1
                pnl = getattr(v, "pnl_pct", None)
                if getattr(v, "filled", False) and pnl is not None:
                    pnls.setdefault(strat, []).append(float(pnl))

        stats: list[StrategyStat] = []
        for strat, total in totals.items():
            arr = pnls.get(strat, [])
            filled = len(arr)
            if filled == 0:
                continue
            avg_pnl = sum(arr) / filled
            fill_rate = filled / total
            ev = fill_rate * avg_pnl
            stats.append(StrategyStat(
                strategy=strat,
                filled=filled,
                total=total,
                avg_pnl=avg_pnl,
                fill_rate=fill_rate,
                effective_ev=ev,
            ))

        stats.sort(key=lambda s: s.effective_ev, reverse=True)
        return stats

    def top(
        self,
        *,
        is_long: bool | None = None,
        allow: set[str] | None = None,
    ) -> StrategyStat | None:
        """条件に合う戦略のうち最も effective_ev が高いものを返す。

        Args:
            is_long: None なら方向不問、True なら LONG のみ、False なら SHORT のみ
            allow:   許可する戦略名セット (None なら全戦略)
        """
        for s in self.compute():
            if s.filled < self._min_filled:
                continue
            if is_long is not None and s.is_long != is_long:
                continue
            if allow is not None and s.strategy not in allow:
                continue
            return s
        return None

    def evaluate_live_gate(self, strategy: str = "MARKET") -> LiveGateDecision:
        """実弾採用前の保守的な複数窓ゲートを評価する。

        既定では 20/50/100/200 件の全窓について、次をすべて要求する。

        - 窓を満たす closed 履歴がある
        - 各レコードに対象 strategy がちょうど1件あり、filled/PnL が有効
        - 約定数が絶対値・fill率の双方の下限を満たす
        - ``fill_rate × (avg_pnl - fee - slippage - funding)`` が
          最低 net EV 以上

        1窓でも不足・欠損・不整合・非有限値があれば fail-closed。
        """
        strategy = strategy.strip()
        if not strategy:
            return self._failed_live_gate(
                strategy=strategy,
                reason="strategy is empty",
            )
        policy_version = os.getenv("LIVE_POLICY_VERSION", "").strip()
        require_policy_version = (
            os.getenv("LIVE_REQUIRE_POLICY_VERSION", "false").strip().lower()
            in {"1", "true", "yes", "on"}
        )
        if require_policy_version and not policy_version:
            return self._failed_live_gate(
                strategy=strategy,
                reason="LIVE_POLICY_VERSION is required",
            )

        closed = getattr(self._exp, "_closed", None)
        if not isinstance(closed, (list, tuple)):
            return self._failed_live_gate(
                strategy=strategy,
                reason="closed history is missing or invalid",
            )

        eligible_closed, predicate_error = self._filter_live_history(closed)
        if predicate_error is not None:
            return self._failed_live_gate(
                strategy=strategy,
                reason=f"live trade predicate failed: {predicate_error}",
                source_total=len(closed),
            )

        latest_data_at, data_age_hours, freshness_error = (
            self._check_live_gate_freshness(
                closed=eligible_closed,
                strategy=strategy,
            )
        )
        window_stats = tuple(
            self._compute_live_gate_window(
                closed=eligible_closed,
                strategy=strategy,
                window=window,
            )
            for window in self._live_gate_windows
        )
        (
            distinct_days,
            daily_mean_net_pnl,
            lower95_pct,
            cluster_reasons,
        ) = self._compute_daily_cluster_gate(
            closed=eligible_closed,
            strategy=strategy,
            window=max(self._live_gate_windows),
        )
        window_reasons = tuple(
            f"window={item.window}: {reason}"
            for item in window_stats
            for reason in item.reasons
        )
        reasons = (
            ((f"freshness: {freshness_error}",) if freshness_error else ())
            + window_reasons
            + tuple(f"daily cluster: {reason}" for reason in cluster_reasons)
        )
        passed = (
            freshness_error is None
            and len(window_stats) == len(self._live_gate_windows)
            and all(item.passed for item in window_stats)
            and not cluster_reasons
        )

        decision = LiveGateDecision(
            strategy=strategy,
            policy_version=(
                os.getenv("LIVE_POLICY_VERSION", "").strip() or "unversioned"
            ),
            policy_fingerprint=live_policy_fingerprint(),
            passed=passed,
            windows=window_stats,
            fee_pct=self._live_fee_pct,
            slippage_pct=self._live_slippage_pct,
            funding_pct=self._live_funding_pct,
            min_net_ev_pct=self._live_min_net_ev_pct,
            max_data_age_hours=self._live_max_data_age_hours,
            source_total=len(closed),
            eligible_total=len(eligible_closed),
            latest_data_at=latest_data_at,
            data_age_hours=data_age_hours,
            min_distinct_days=self._live_min_distinct_days,
            distinct_days=distinct_days,
            min_ci_pct=self._live_min_ci_pct,
            daily_mean_net_pnl=daily_mean_net_pnl,
            lower95_pct=lower95_pct,
            reasons=reasons,
        )
        logger.info("Live ranker gate: %s", decision.summary())
        return decision

    # ------------------------------------------------------------------
    # Live gate internals
    # ------------------------------------------------------------------

    def _filter_live_history(
        self,
        closed: list | tuple,
    ) -> tuple[list[object], str | None]:
        """実弾条件と同じ母集団だけを残す。例外・非boolはfail-closed。"""
        predicate = self._live_trade_predicate
        if predicate is None:
            return list(closed), None

        eligible: list[object] = []
        for index, trade in enumerate(closed):
            try:
                selected = predicate(trade)
            except Exception as exc:
                logger.warning(
                    "Live trade predicate raised at history index %d: %s",
                    index,
                    exc,
                )
                return [], f"exception at history index {index}: {type(exc).__name__}"
            if not isinstance(selected, bool):
                return (
                    [],
                    f"non-bool result at history index {index}: "
                    f"{type(selected).__name__}",
                )
            if selected:
                eligible.append(trade)
        return eligible, None

    def _check_live_gate_freshness(
        self,
        *,
        closed: list | tuple,
        strategy: str,
    ) -> tuple[str | None, float | None, str | None]:
        """対象戦略を含む最新closedレコードの鮮度を検証する。"""
        latest_trade = None
        for trade in reversed(closed):
            variants = getattr(trade, "entry_variants", None)
            if not isinstance(variants, (list, tuple)):
                continue
            if any(
                getattr(variant, "strategy", None) == strategy
                for variant in variants
            ):
                latest_trade = trade
                break

        if latest_trade is None:
            return None, None, "no closed trade for strategy"

        raw_timestamp = (
            getattr(latest_trade, "outcome_at", None)
            or getattr(latest_trade, "detected_at", None)
        )
        if not isinstance(raw_timestamp, str) or not raw_timestamp.strip():
            return None, None, "latest trade timestamp is missing"

        timestamp_text = raw_timestamp.strip()
        normalized = (
            f"{timestamp_text[:-1]}+00:00"
            if timestamp_text.endswith(("Z", "z"))
            else timestamp_text
        )
        try:
            parsed = datetime.fromisoformat(normalized)
        except ValueError:
            return timestamp_text, None, "latest trade timestamp is unparseable"
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            return timestamp_text, None, "latest trade timestamp has no timezone"

        parsed_utc = parsed.astimezone(timezone.utc)
        now_utc = datetime.now(timezone.utc)
        age_hours = (now_utc - parsed_utc).total_seconds() / 3600
        if age_hours < 0:
            return timestamp_text, age_hours, "latest trade timestamp is in the future"
        if age_hours > self._live_max_data_age_hours:
            return (
                timestamp_text,
                age_hours,
                f"latest trade age {age_hours:.2f}h > maximum "
                f"{self._live_max_data_age_hours:.2f}h",
            )
        return timestamp_text, age_hours, None

    def _compute_daily_cluster_gate(
        self,
        *,
        closed: list | tuple,
        strategy: str,
        window: int,
    ) -> tuple[int, float | None, float | None, tuple[str, ...]]:
        """最大窓をUTC日で束ね、日次平均の保守的lower95を計算する。"""
        if len(closed) < window:
            return (
                0,
                None,
                None,
                (f"history {len(closed)} < required {window}",),
            )

        daily_returns: dict[str, list[float]] = {}
        now_utc = datetime.now(timezone.utc)
        for index, trade in enumerate(closed[-window:]):
            variants = getattr(trade, "entry_variants", None)
            if not isinstance(variants, (list, tuple)):
                return 0, None, None, (f"missing variants at index {index}",)
            matches = [
                variant
                for variant in variants
                if getattr(variant, "strategy", None) == strategy
            ]
            if len(matches) != 1:
                return (
                    0,
                    None,
                    None,
                    (f"strategy variants={len(matches)} at index {index}",),
                )

            timestamp_text, parsed, timestamp_error = self._parse_trade_timestamp(
                trade
            )
            if timestamp_error is not None or parsed is None:
                return (
                    0,
                    None,
                    None,
                    (
                        f"invalid timestamp at index {index}: "
                        f"{timestamp_error or timestamp_text}",
                    ),
                )
            if parsed > now_utc:
                return (
                    0,
                    None,
                    None,
                    (f"future timestamp at index {index}",),
                )

            variant = matches[0]
            filled_value = getattr(variant, "filled", None)
            if not isinstance(filled_value, bool):
                return (
                    0,
                    None,
                    None,
                    (f"invalid filled flag at index {index}",),
                )

            net_pnl = 0.0
            if filled_value:
                pnl = getattr(variant, "pnl_pct", None)
                try:
                    pnl_value = float(pnl)
                except (TypeError, ValueError):
                    return (
                        0,
                        None,
                        None,
                        (f"invalid PnL at index {index}",),
                    )
                if not math.isfinite(pnl_value):
                    return (
                        0,
                        None,
                        None,
                        (f"nonfinite PnL at index {index}",),
                    )
                net_pnl = pnl_value - self._live_total_cost_pct

            day = parsed.date().isoformat()
            daily_returns.setdefault(day, []).append(net_pnl)

        daily_means = [
            sum(values) / len(values)
            for values in daily_returns.values()
            if values
        ]
        distinct_days = len(daily_means)
        reasons: list[str] = []
        if distinct_days < self._live_min_distinct_days:
            reasons.append(
                f"distinct days {distinct_days} < required "
                f"{self._live_min_distinct_days}"
            )
        if distinct_days < 2:
            reasons.append("at least 2 distinct days required for sample SD")
            return distinct_days, None, None, tuple(reasons)

        daily_mean_net_pnl = sum(daily_means) / distinct_days
        variance = sum(
            (value - daily_mean_net_pnl) ** 2
            for value in daily_means
        ) / (distinct_days - 1)
        sample_sd = math.sqrt(max(0.0, variance))
        lower95_pct = (
            daily_mean_net_pnl
            - 2.0 * sample_sd / math.sqrt(distinct_days)
        )
        if not math.isfinite(lower95_pct):
            reasons.append("lower95 is not finite")
            lower95_pct = None
        elif lower95_pct <= self._live_min_ci_pct:
            reasons.append(
                f"lower95 {lower95_pct:+.4f}% <= minimum "
                f"{self._live_min_ci_pct:+.4f}%"
            )

        return (
            distinct_days,
            daily_mean_net_pnl,
            lower95_pct,
            tuple(reasons),
        )

    @staticmethod
    def _parse_trade_timestamp(
        trade: object,
    ) -> tuple[str | None, datetime | None, str | None]:
        raw_timestamp = (
            getattr(trade, "outcome_at", None)
            or getattr(trade, "detected_at", None)
        )
        if not isinstance(raw_timestamp, str) or not raw_timestamp.strip():
            return None, None, "timestamp is missing"

        timestamp_text = raw_timestamp.strip()
        normalized = (
            f"{timestamp_text[:-1]}+00:00"
            if timestamp_text.endswith(("Z", "z"))
            else timestamp_text
        )
        try:
            parsed = datetime.fromisoformat(normalized)
        except ValueError:
            return timestamp_text, None, "timestamp is unparseable"
        if parsed.tzinfo is None or parsed.utcoffset() is None:
            return timestamp_text, None, "timestamp has no timezone"
        return timestamp_text, parsed.astimezone(timezone.utc), None

    def _compute_live_gate_window(
        self,
        *,
        closed: list | tuple,
        strategy: str,
        window: int,
    ) -> LiveGateWindowStat:
        available = len(closed)
        required_filled = max(
            self._live_min_filled,
            math.ceil(window * self._live_min_fill_rate),
        )
        if available < window:
            return LiveGateWindowStat(
                window=window,
                total=available,
                observed=0,
                filled=0,
                required_filled=required_filled,
                missing=window - available,
                invalid=0,
                avg_pnl=None,
                fill_rate=None,
                gross_ev=None,
                net_ev=None,
                passed=False,
                reasons=(f"history {available} < required {window}",),
            )

        trades = closed[-window:]
        observed = 0
        filled = 0
        missing = 0
        invalid = 0
        pnls: list[float] = []

        for trade in trades:
            variants = getattr(trade, "entry_variants", None)
            if not isinstance(variants, (list, tuple)):
                missing += 1
                continue

            matches = [
                variant
                for variant in variants
                if getattr(variant, "strategy", None) == strategy
            ]
            if not matches:
                missing += 1
                continue
            if len(matches) != 1:
                invalid += 1
                continue

            variant = matches[0]
            filled_value = getattr(variant, "filled", None)
            if not isinstance(filled_value, bool):
                invalid += 1
                continue

            observed += 1
            if not filled_value:
                continue

            pnl = getattr(variant, "pnl_pct", None)
            try:
                pnl_value = float(pnl)
            except (TypeError, ValueError):
                invalid += 1
                continue
            if not math.isfinite(pnl_value):
                invalid += 1
                continue

            filled += 1
            pnls.append(pnl_value)

        reasons: list[str] = []
        if missing:
            reasons.append(f"missing strategy data={missing}")
        if invalid:
            reasons.append(f"invalid strategy data={invalid}")
        if observed != window:
            reasons.append(f"complete observations {observed}/{window}")
        if filled < required_filled:
            reasons.append(f"filled {filled} < required {required_filled}")

        avg_pnl: float | None = None
        fill_rate: float | None = None
        gross_ev: float | None = None
        net_ev: float | None = None

        # 欠損データから部分的なEVを作ると誤って実弾判定へ流用されるため、
        # 完全な窓かつ有効な約定がある場合だけ数値を公開する。
        data_complete = missing == 0 and invalid == 0 and observed == window
        if data_complete and filled > 0:
            avg_pnl = sum(pnls) / filled
            fill_rate = filled / window
            gross_ev = fill_rate * avg_pnl
            net_ev = fill_rate * (avg_pnl - self._live_total_cost_pct)
            if not math.isfinite(net_ev):
                reasons.append("net EV is not finite")
                net_ev = None
            elif net_ev < self._live_min_net_ev_pct:
                reasons.append(
                    f"net EV {net_ev:+.4f}% < minimum "
                    f"{self._live_min_net_ev_pct:+.4f}%"
                )

        passed = (
            data_complete
            and filled >= required_filled
            and net_ev is not None
            and net_ev >= self._live_min_net_ev_pct
        )
        return LiveGateWindowStat(
            window=window,
            total=window,
            observed=observed,
            filled=filled,
            required_filled=required_filled,
            missing=missing,
            invalid=invalid,
            avg_pnl=avg_pnl,
            fill_rate=fill_rate,
            gross_ev=gross_ev,
            net_ev=net_ev,
            passed=passed,
            reasons=tuple(reasons),
        )

    @property
    def _live_total_cost_pct(self) -> float:
        return (
            self._live_fee_pct
            + self._live_slippage_pct
            + self._live_funding_pct
        )

    def _failed_live_gate(
        self,
        *,
        strategy: str,
        reason: str,
        source_total: int = 0,
        eligible_total: int = 0,
    ) -> LiveGateDecision:
        decision = LiveGateDecision(
            strategy=strategy,
            policy_version=(
                os.getenv("LIVE_POLICY_VERSION", "").strip() or "unversioned"
            ),
            policy_fingerprint=live_policy_fingerprint(),
            passed=False,
            windows=(),
            fee_pct=self._live_fee_pct,
            slippage_pct=self._live_slippage_pct,
            funding_pct=self._live_funding_pct,
            min_net_ev_pct=self._live_min_net_ev_pct,
            max_data_age_hours=self._live_max_data_age_hours,
            source_total=source_total,
            eligible_total=eligible_total,
            latest_data_at=None,
            data_age_hours=None,
            min_distinct_days=self._live_min_distinct_days,
            distinct_days=0,
            min_ci_pct=self._live_min_ci_pct,
            daily_mean_net_pnl=None,
            lower95_pct=None,
            reasons=(reason,),
        )
        logger.warning("Live ranker gate: %s", decision.summary())
        return decision

    @staticmethod
    def _parse_live_gate_windows(raw: str) -> tuple[int, ...]:
        try:
            windows = tuple(int(value.strip()) for value in raw.split(","))
        except ValueError as exc:
            raise ValueError(
                "LIVE_GATE_WINDOWS must be comma-separated positive integers"
            ) from exc
        if not windows or any(value <= 0 for value in windows):
            raise ValueError("LIVE_GATE_WINDOWS values must be positive")
        if len(set(windows)) != len(windows):
            raise ValueError("LIVE_GATE_WINDOWS must not contain duplicates")
        return tuple(sorted(windows))

    @staticmethod
    def _env_nonnegative_float(name: str, default: str) -> float:
        return StrategyRanker._env_bounded_float(
            name,
            default,
            lower=0.0,
            upper=float("inf"),
        )

    @staticmethod
    def _env_positive_float(name: str, default: str) -> float:
        value = StrategyRanker._env_nonnegative_float(name, default)
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return value

    @staticmethod
    def _env_finite_float(name: str, default: str) -> float:
        raw = os.getenv(name, default)
        try:
            value = float(raw)
        except ValueError as exc:
            raise ValueError(f"{name} must be numeric") from exc
        if not math.isfinite(value):
            raise ValueError(f"{name} must be finite")
        return value

    @staticmethod
    def _env_bounded_float(
        name: str,
        default: str,
        *,
        lower: float,
        upper: float,
    ) -> float:
        raw = os.getenv(name, default)
        try:
            value = float(raw)
        except ValueError as exc:
            raise ValueError(f"{name} must be numeric") from exc
        if not math.isfinite(value) or not lower <= value <= upper:
            raise ValueError(f"{name} must be within [{lower}, {upper}]")
        return value

    @staticmethod
    def _env_positive_int(name: str, default: str) -> int:
        raw = os.getenv(name, default)
        try:
            value = int(raw)
        except ValueError as exc:
            raise ValueError(f"{name} must be an integer") from exc
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return value
