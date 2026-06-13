"""
More conservative adaptive DryRun portfolio.

This runs in parallel with SafeAdaptivePortfolio. It keeps the same no-lookahead
forward-test structure, but adds stricter robustness checks:
  - cost haircut for filled trades
  - recent, mid-term, and all-time positive growth requirements
  - minimum fill-rate gate
  - stronger drawdown and daily-loss brakes
"""
from __future__ import annotations

import math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from core.safe_adaptive_portfolio import (
    EXPERIMENT_FILE,
    SafeAdaptivePortfolio,
    StrategyGrowthStat,
    _as_float,
    _direction,
    _env_bool,
    _env_float,
    _env_int,
    _is_long,
    _max_drawdown_pct,
    _max_loss_streak,
    _parse_dt,
    _variant_sl_pct,
)

ROBUST_ADAPTIVE_FILE = Path("data/robust_adaptive_portfolio.json")


def _robust_variant_return(
    variant: dict[str, Any],
    risk_pct: float,
    cost_pct: float,
) -> float | None:
    """Account-level return after a simple round-trip cost haircut."""
    if not variant.get("filled"):
        return 0.0
    pnl_pct = _as_float(variant.get("pnl_pct"))
    sl_pct = _variant_sl_pct(variant)
    if pnl_pct is None or sl_pct is None or sl_pct <= 0:
        return None
    adjusted_pnl_pct = pnl_pct - cost_pct
    account_return = (risk_pct / 100) * (adjusted_pnl_pct / sl_pct)
    return max(account_return, -(risk_pct / 100))


class RobustAdaptivePortfolio(SafeAdaptivePortfolio):
    """Lower-risk adaptive paper portfolio with robustness penalties."""

    def __init__(
        self,
        file_path: Path = ROBUST_ADAPTIVE_FILE,
        experiment_path: Path = EXPERIMENT_FILE,
    ) -> None:
        super().__init__(file_path=file_path, experiment_path=experiment_path)

    def _read_config(self) -> dict[str, Any]:
        return {
            "enabled": _env_bool("ROBUST_ADAPTIVE_ENABLED", True),
            "initial_capital": _env_float("ROBUST_ADAPTIVE_CAPITAL", 100.0),
            "risk_pct": _env_float("ROBUST_ADAPTIVE_RISK_PCT", 0.35),
            "cost_pct": _env_float("ROBUST_ADAPTIVE_COST_PCT", 0.15),
            "recent_n": _env_int("ROBUST_ADAPTIVE_RECENT_N", 50),
            "mid_n": _env_int("ROBUST_ADAPTIVE_MID_N", 200),
            "min_recent_filled": _env_int("ROBUST_ADAPTIVE_MIN_RECENT_FILLED", 12),
            "min_mid_filled": _env_int("ROBUST_ADAPTIVE_MIN_MID_FILLED", 30),
            "min_all_filled": _env_int("ROBUST_ADAPTIVE_MIN_ALL_FILLED", 50),
            "min_recent_fill_rate": _env_float("ROBUST_ADAPTIVE_MIN_RECENT_FILL_RATE", 0.25),
            "min_ev_pct": _env_float("ROBUST_ADAPTIVE_MIN_EV_PCT", 0.20),
            "min_avg_log_return": _env_float("ROBUST_ADAPTIVE_MIN_AVG_LOG_RETURN", 0.0),
            "max_strategy_dd_pct": _env_float("ROBUST_ADAPTIVE_MAX_STRATEGY_DD_PCT", 8.0),
            "max_all_strategy_dd_pct": _env_float(
                "ROBUST_ADAPTIVE_MAX_ALL_STRATEGY_DD_PCT", 20.0
            ),
            "max_portfolio_dd_pct": _env_float("ROBUST_ADAPTIVE_MAX_PORTFOLIO_DD_PCT", 8.0),
            "daily_loss_stop_pct": _env_float("ROBUST_ADAPTIVE_DAILY_LOSS_STOP_PCT", 1.5),
            "max_loss_streak": _env_int("ROBUST_ADAPTIVE_MAX_LOSS_STREAK", 5),
            "loss_streak_cooldown_hours": _env_int(
                "ROBUST_ADAPTIVE_LOSS_STREAK_COOLDOWN_HOURS", 12
            ),
            "allow_long": _env_bool("ROBUST_ADAPTIVE_ALLOW_LONG", True),
            "allow_short": _env_bool("ROBUST_ADAPTIVE_ALLOW_SHORT", True),
            "allow_limit": _env_bool("ROBUST_ADAPTIVE_ALLOW_LIMIT", True),
        }

    def _default_state(self) -> dict[str, Any]:
        state = super()._default_state()
        state["mode"] = "robust_adaptive_dry_run"
        return state

    def _load(self) -> dict[str, Any]:
        state = super()._load()
        state["mode"] = "robust_adaptive_dry_run"
        return state

    def _compute_growth_stats(
        self,
        trades: list[dict[str, Any]],
    ) -> dict[str, StrategyGrowthStat]:
        raw: dict[str, dict[str, Any]] = {}
        risk_pct = float(self._config["risk_pct"])
        cost_pct = float(self._config["cost_pct"])

        for trade in trades:
            variants = trade.get("entry_variants")
            if not isinstance(variants, list):
                continue
            for variant in variants:
                if not isinstance(variant, dict):
                    continue
                strategy = str(variant.get("strategy") or "")
                if not strategy or not self._strategy_allowed(strategy):
                    continue
                row = raw.setdefault(
                    strategy,
                    {"total": 0, "filled": 0, "pnls": [], "returns": []},
                )
                row["total"] += 1
                ret = _robust_variant_return(variant, risk_pct, cost_pct)
                if ret is None:
                    continue
                row["returns"].append(ret)
                if variant.get("filled"):
                    row["filled"] += 1
                    pnl = _as_float(variant.get("pnl_pct"))
                    if pnl is not None:
                        row["pnls"].append(pnl - cost_pct)

        stats: dict[str, StrategyGrowthStat] = {}
        for strategy, row in raw.items():
            returns = list(row["returns"])
            if not returns:
                continue
            pnls = list(row["pnls"])
            avg_pnl = sum(pnls) / len(pnls) if pnls else None
            fill_rate = row["filled"] / row["total"] if row["total"] else 0.0
            effective_ev = fill_rate * avg_pnl if avg_pnl is not None else None
            logs = [math.log(max(1e-12, 1.0 + ret)) for ret in returns]
            avg_log = sum(logs) / len(logs)
            stats[strategy] = StrategyGrowthStat(
                strategy=strategy,
                total=int(row["total"]),
                filled=int(row["filled"]),
                fill_rate=fill_rate,
                avg_pnl_pct=avg_pnl,
                effective_ev_pct=effective_ev,
                avg_log_return=avg_log,
                geometric_return_pct=(math.exp(avg_log) - 1.0) * 100,
                avg_account_return_pct=(sum(returns) / len(returns)) * 100,
                max_drawdown_pct=_max_drawdown_pct(returns),
                max_loss_streak=_max_loss_streak(returns),
            )
        return stats

    def _select_strategy(self, history: list[dict[str, Any]]) -> dict[str, Any]:
        if not history:
            return {"strategy": None, "reason": "no_history"}

        recent_n = int(self._config["recent_n"])
        mid_n = int(self._config["mid_n"])
        recent = history[-recent_n:] if recent_n > 0 else history
        mid = history[-mid_n:] if mid_n > 0 else history

        recent_stats = self._compute_growth_stats(recent)
        mid_stats = self._compute_growth_stats(mid)
        all_stats = self._compute_growth_stats(history)

        candidates: list[tuple[float, StrategyGrowthStat, StrategyGrowthStat, StrategyGrowthStat]] = []
        rejects: list[dict[str, Any]] = []
        for strategy, recent_stat in recent_stats.items():
            mid_stat = mid_stats.get(strategy)
            all_stat = all_stats.get(strategy)
            if mid_stat is None or all_stat is None:
                continue
            reason = self._robust_reject_reason(recent_stat, mid_stat, all_stat)
            if reason:
                rejects.append({
                    "strategy": strategy,
                    "reason": reason,
                    "recent": recent_stat.as_dict(),
                    "mid": mid_stat.as_dict(),
                    "all": all_stat.as_dict(),
                })
                continue
            score = self._robust_score(recent_stat, mid_stat, all_stat)
            candidates.append((score, recent_stat, mid_stat, all_stat))

        top_rejects = sorted(
            rejects,
            key=lambda item: (
                item["recent"].get("avg_log_return") or -999,
                item["recent"].get("effective_ev_pct") or -999,
            ),
            reverse=True,
        )[:5]

        if not candidates:
            return {
                "strategy": None,
                "reason": "no_strategy_passed_robust_filters",
                "top_rejected": top_rejects,
                "history_count": len(history),
                "recent_count": len(recent),
                "mid_count": len(mid),
            }

        candidates.sort(key=lambda item: item[0], reverse=True)
        score, recent_stat, mid_stat, all_stat = candidates[0]
        return {
            "strategy": recent_stat.strategy,
            "direction": _direction(recent_stat.strategy),
            "reason": "selected_by_robust_growth_score",
            "robust_score": score,
            "history_count": len(history),
            "recent_count": len(recent),
            "mid_count": len(mid),
            "recent": recent_stat.as_dict(),
            "mid": mid_stat.as_dict(),
            "all": all_stat.as_dict(),
            "alternatives": [
                {
                    "strategy": r.strategy,
                    "direction": _direction(r.strategy),
                    "robust_score": alt_score,
                    "recent": r.as_dict(),
                    "mid": m.as_dict(),
                    "all": a.as_dict(),
                }
                for alt_score, r, m, a in candidates[1:5]
            ],
        }

    def _robust_reject_reason(
        self,
        recent: StrategyGrowthStat,
        mid: StrategyGrowthStat,
        all_time: StrategyGrowthStat,
    ) -> str | None:
        if recent.filled < int(self._config["min_recent_filled"]):
            return "recent_filled_too_low"
        if mid.filled < int(self._config["min_mid_filled"]):
            return "mid_filled_too_low"
        if all_time.filled < int(self._config["min_all_filled"]):
            return "all_filled_too_low"
        if recent.fill_rate < float(self._config["min_recent_fill_rate"]):
            return "recent_fill_rate_too_low"
        ev = recent.effective_ev_pct
        if ev is None or ev < float(self._config["min_ev_pct"]):
            return "recent_ev_too_low_after_cost"
        min_log = float(self._config["min_avg_log_return"])
        if recent.avg_log_return <= min_log:
            return "recent_log_return_too_low"
        if mid.avg_log_return <= min_log:
            return "mid_log_return_too_low"
        if all_time.avg_log_return <= min_log:
            return "all_log_return_too_low"
        if recent.max_drawdown_pct > float(self._config["max_strategy_dd_pct"]):
            return "recent_strategy_drawdown_too_high"
        if all_time.max_drawdown_pct > float(self._config["max_all_strategy_dd_pct"]):
            return "all_strategy_drawdown_too_high"
        if recent.max_loss_streak >= int(self._config["max_loss_streak"]):
            return "strategy_loss_streak_too_high"
        return None

    @staticmethod
    def _robust_score(
        recent: StrategyGrowthStat,
        mid: StrategyGrowthStat,
        all_time: StrategyGrowthStat,
    ) -> float:
        return (
            recent.geometric_return_pct
            + 0.60 * mid.geometric_return_pct
            + 0.30 * all_time.geometric_return_pct
            + 0.05 * recent.fill_rate
            - 0.01 * recent.max_drawdown_pct
            - 0.005 * all_time.max_drawdown_pct
        )

    def _apply_trade(
        self,
        trade: dict[str, Any],
        key: str,
        variant: dict[str, Any],
        decision: dict[str, Any],
    ) -> None:
        balance_before = float(self._state.get("balance") or 0.0)
        risk_pct = float(self._config["risk_pct"])
        cost_pct = float(self._config["cost_pct"])
        account_return = _robust_variant_return(variant, risk_pct, cost_pct)
        if account_return is None:
            account_return = 0.0

        pnl_usdt = balance_before * account_return
        balance_after = max(0.0, balance_before + pnl_usdt)
        high = max(float(self._state.get("high_watermark") or balance_before), balance_after)
        drawdown = (high - balance_after) / high * 100 if high > 0 else 0.0

        detected = _parse_dt(trade.get("detected_at")) or datetime.now(timezone.utc)
        day = detected.date().isoformat()
        daily = dict(self._state.get("daily_pnl_usdt") or {})
        daily[day] = float(daily.get(day, 0.0)) + pnl_usdt

        loss_streak = int(self._state.get("loss_streak") or 0)
        if pnl_usdt < 0:
            loss_streak += 1
        elif pnl_usdt > 0:
            loss_streak = 0

        cooldown_until = self._state.get("cooldown_until")
        if loss_streak >= int(self._config["max_loss_streak"]):
            base_dt = _parse_dt(trade.get("outcome_at")) or detected
            cooldown_until = (
                base_dt + timedelta(
                    hours=int(self._config["loss_streak_cooldown_hours"])
                )
            ).isoformat()

        log_return = (
            math.log(balance_after / balance_before)
            if balance_before > 0 and balance_after > 0
            else None
        )
        strategy = str(variant.get("strategy") or "")
        record = {
            "key": key,
            "symbol": trade.get("symbol"),
            "detected_at": trade.get("detected_at"),
            "closed_at": trade.get("outcome_at"),
            "strategy": strategy,
            "direction": _direction(strategy),
            "outcome": variant.get("outcome") or trade.get("outcome"),
            "filled": bool(variant.get("filled")),
            "raw_pnl_pct": _as_float(variant.get("pnl_pct"), 0.0),
            "cost_pct": cost_pct,
            "pnl_pct": (_as_float(variant.get("pnl_pct"), 0.0) or 0.0) - cost_pct
            if variant.get("filled")
            else 0.0,
            "sl_pct": _variant_sl_pct(variant),
            "risk_pct": risk_pct,
            "account_return_pct": account_return * 100,
            "log_return": log_return,
            "pnl_usdt": pnl_usdt,
            "balance_before": balance_before,
            "balance_after": balance_after,
            "drawdown_after_pct": drawdown,
            "selector_reason": decision.get("reason"),
            "selector_score": decision.get("robust_score"),
            "selector_recent": decision.get("recent"),
            "selector_mid": decision.get("mid"),
            "selector_all": decision.get("all"),
        }

        self._state["balance"] = balance_after
        self._state["high_watermark"] = high
        self._state["max_drawdown_pct"] = max(
            float(self._state.get("max_drawdown_pct") or 0.0),
            drawdown,
        )
        self._state["daily_pnl_usdt"] = daily
        self._state["loss_streak"] = loss_streak
        self._state["cooldown_until"] = cooldown_until
        self._state.setdefault("trades", []).append(record)


def update_robust_adaptive_portfolio() -> dict[str, Any]:
    portfolio = RobustAdaptivePortfolio()
    return portfolio.update()
