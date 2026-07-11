"""Causal, cost-aware adaptive paper portfolio.

The strategy decision is frozen while an experiment is still active. Historical
ranking uses only outcomes that had closed before that signal was detected.
"""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from core.robust_adaptive_portfolio import RobustAdaptivePortfolio
from core.safe_adaptive_portfolio import (
    EXPERIMENT_FILE,
    StrategyGrowthStat,
    _direction,
    _env_bool,
    _env_float,
    _env_int,
    _load_closed_records,
    _now_iso,
    _parse_dt,
    _trade_key,
)

CAUSAL_ADAPTIVE_FILE = Path("data/causal_adaptive_portfolio.json")

DEFAULT_STRATEGIES = (
    "MARKET",
    "MARKET_LONG",
    "LIMIT_2PCT_LONG",
    "LIMIT_5PCT",
    "LIMIT_7PCT",
    "LIMIT_8PCT",
    "LIMIT_9PCT",
    "LIMIT_9PCT_LONG",
    "LIMIT_10PCT",
    "LIMIT_10PCT_LONG",
)


class CausalAdaptivePortfolio(RobustAdaptivePortfolio):
    """Forward-only $100 DryRun selected by causal walk-forward statistics."""

    def __init__(
        self,
        file_path: Path = CAUSAL_ADAPTIVE_FILE,
        experiment_path: Path = EXPERIMENT_FILE,
    ) -> None:
        super().__init__(file_path=file_path, experiment_path=experiment_path)

    def _read_config(self) -> dict[str, Any]:
        return {
            "enabled": _env_bool("CAUSAL_ADAPTIVE_ENABLED", True),
            "initial_capital": _env_float("CAUSAL_ADAPTIVE_CAPITAL", 100.0),
            "risk_pct": _env_float("CAUSAL_ADAPTIVE_RISK_PCT", 0.175),
            "cost_pct": _env_float("CAUSAL_ADAPTIVE_COST_PCT", 0.15),
            "fast_n": _env_int("CAUSAL_ADAPTIVE_FAST_N", 50),
            "mid_n": _env_int("CAUSAL_ADAPTIVE_MID_N", 200),
            "long_n": _env_int("CAUSAL_ADAPTIVE_LONG_N", 1000),
            "fast_weight": _env_float("CAUSAL_ADAPTIVE_FAST_WEIGHT", 0.55),
            "mid_weight": _env_float("CAUSAL_ADAPTIVE_MID_WEIGHT", 0.30),
            "long_weight": _env_float("CAUSAL_ADAPTIVE_LONG_WEIGHT", 0.15),
            "min_fast_limit_filled": _env_int(
                "CAUSAL_ADAPTIVE_MIN_FAST_LIMIT_FILLED", 8
            ),
            "min_fast_market_filled": _env_int(
                "CAUSAL_ADAPTIVE_MIN_FAST_MARKET_FILLED", 25
            ),
            "min_mid_limit_filled": _env_int(
                "CAUSAL_ADAPTIVE_MIN_MID_LIMIT_FILLED", 20
            ),
            "min_mid_market_filled": _env_int(
                "CAUSAL_ADAPTIVE_MIN_MID_MARKET_FILLED", 80
            ),
            "min_long_filled": _env_int("CAUSAL_ADAPTIVE_MIN_LONG_FILLED", 30),
            "max_trades_per_signal_batch": _env_int(
                "CAUSAL_ADAPTIVE_MAX_TRADES_PER_BATCH", 2
            ),
            "max_open_risk_pct": _env_float(
                "CAUSAL_ADAPTIVE_MAX_OPEN_RISK_PCT", 1.05
            ),
            "max_portfolio_dd_pct": _env_float(
                "CAUSAL_ADAPTIVE_MAX_PORTFOLIO_DD_PCT", 8.0
            ),
            "daily_loss_stop_pct": _env_float(
                "CAUSAL_ADAPTIVE_DAILY_LOSS_STOP_PCT", 1.5
            ),
            "max_loss_streak": _env_int("CAUSAL_ADAPTIVE_MAX_LOSS_STREAK", 6),
            "loss_streak_cooldown_hours": _env_int(
                "CAUSAL_ADAPTIVE_LOSS_STREAK_COOLDOWN_HOURS", 12
            ),
            "allow_long": True,
            "allow_short": True,
            "allow_limit": True,
            "candidate_strategies": list(DEFAULT_STRATEGIES),
        }

    def _default_state(self) -> dict[str, Any]:
        state = super()._default_state()
        state.update(
            {
                "mode": "causal_adaptive_dry_run",
                "methodology_version": 1,
                "signals": {},
                "causal_history": True,
            }
        )
        return state

    def _load(self) -> dict[str, Any]:
        state = super()._load()
        state["mode"] = "causal_adaptive_dry_run"
        state.setdefault("methodology_version", 1)
        state.setdefault("signals", {})
        state.setdefault("causal_history", True)
        return state

    def update(self) -> dict[str, Any]:
        if not self._config["enabled"]:
            self._state["enabled"] = False
            self._state["updated_at"] = _now_iso()
            self._state["config"] = self._config
            self.save()
            return {"enabled": False, "registered": 0, "settled": 0, "skipped": 0}

        closed = _load_closed_records(self._experiment_path)
        active = self._load_active()
        applied_keys = self._applied_keys()
        signals = self._signals()

        settled = self._settle_signals(closed, signals, applied_keys)
        registered, skipped = self._register_active(
            active,
            closed,
            signals,
            applied_keys,
        )
        skipped += self._skip_unregistered_closed(closed, signals, applied_keys)

        self._state["signals"] = signals
        self._state["applied_keys"] = sorted(applied_keys)
        self._state["last_decision"] = self._select_strategy(closed)
        self._state["updated_at"] = _now_iso()
        self._state["config"] = self._config
        self._refresh_summary()
        self.save()
        return {
            "enabled": True,
            "registered": registered,
            "settled": settled,
            "skipped": skipped,
        }

    def _load_active(self) -> list[dict[str, Any]]:
        if not self._experiment_path.exists():
            return []
        try:
            payload = json.loads(self._experiment_path.read_text(encoding="utf-8"))
        except Exception:
            return []
        active = payload.get("active", []) if isinstance(payload, dict) else []
        return [trade for trade in active if isinstance(trade, dict)]

    def _signals(self) -> dict[str, dict[str, Any]]:
        raw = self._state.get("signals")
        if not isinstance(raw, dict):
            return {}
        return {str(key): value for key, value in raw.items() if isinstance(value, dict)}

    def _register_active(
        self,
        active: list[dict[str, Any]],
        closed: list[dict[str, Any]],
        signals: dict[str, dict[str, Any]],
        applied_keys: set[str],
    ) -> tuple[int, int]:
        start = _parse_dt(self._state.get("started_at")) or datetime.now(timezone.utc)
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for trade in active:
            detected = _parse_dt(trade.get("detected_at"))
            key = _trade_key(trade)
            if detected is None or detected < start or key in signals or key in applied_keys:
                continue
            grouped[self._signal_batch(detected)].append(trade)

        registered = 0
        skipped = 0
        max_per_batch = int(self._config["max_trades_per_signal_batch"])
        for batch in sorted(grouped):
            existing = sum(1 for signal in signals.values() if signal.get("signal_batch") == batch)
            slots = max(0, max_per_batch - existing)
            candidates = sorted(grouped[batch], key=self._relative_strength, reverse=True)
            for trade in candidates:
                key = _trade_key(trade)
                if slots <= 0:
                    self._record_skip(trade, key, "signal_batch_risk_cap", {})
                    applied_keys.add(key)
                    skipped += 1
                    continue

                detected = _parse_dt(trade.get("detected_at"))
                if detected is None:
                    continue
                history = self._history_available_at(closed, detected)
                decision = self._select_strategy(history)
                if not decision.get("strategy"):
                    self._record_skip(
                        trade,
                        key,
                        decision.get("reason", "no_strategy"),
                        decision,
                    )
                    applied_keys.add(key)
                    skipped += 1
                    continue

                ok, reason = self._registration_gate(trade, signals)
                if not ok:
                    self._record_skip(trade, key, reason, decision)
                    applied_keys.add(key)
                    skipped += 1
                    continue

                signals[key] = {
                    "key": key,
                    "symbol": trade.get("symbol"),
                    "detected_at": trade.get("detected_at"),
                    "registered_at": _now_iso(),
                    "signal_batch": batch,
                    "status": "pending",
                    "strategy": decision["strategy"],
                    "direction": decision.get("direction"),
                    "risk_pct": float(self._config["risk_pct"]),
                    "relative_strength": self._relative_strength(trade),
                    "decision": decision,
                }
                slots -= 1
                registered += 1
        return registered, skipped

    def _settle_signals(
        self,
        closed: list[dict[str, Any]],
        signals: dict[str, dict[str, Any]],
        applied_keys: set[str],
    ) -> int:
        records = sorted(
            closed,
            key=lambda trade: (
                _parse_dt(trade.get("outcome_at"))
                or _parse_dt(trade.get("detected_at"))
                or datetime.max.replace(tzinfo=timezone.utc)
            ),
        )
        settled = 0
        for trade in records:
            key = _trade_key(trade)
            signal = signals.get(key)
            if not signal or signal.get("status") != "pending":
                continue
            strategy = str(signal.get("strategy") or "")
            variant = self._find_variant(trade, strategy)
            if variant is None:
                self._record_skip(trade, key, "registered_variant_missing", signal.get("decision") or {})
            else:
                self._apply_trade(trade, key, variant, signal.get("decision") or {})
                latest = self._state.get("trades", [])[-1]
                latest["signal_batch"] = signal.get("signal_batch")
                latest["registered_at"] = signal.get("registered_at")
                latest["methodology_version"] = 1
            signal["status"] = "settled"
            signal["settled_at"] = trade.get("outcome_at") or _now_iso()
            signal["outcome"] = variant.get("outcome") if variant else "VARIANT_MISSING"
            applied_keys.add(key)
            settled += 1
        return settled

    def _skip_unregistered_closed(
        self,
        closed: list[dict[str, Any]],
        signals: dict[str, dict[str, Any]],
        applied_keys: set[str],
    ) -> int:
        start = _parse_dt(self._state.get("started_at")) or datetime.now(timezone.utc)
        skipped = 0
        for trade in closed:
            key = _trade_key(trade)
            detected = _parse_dt(trade.get("detected_at"))
            if detected is None or detected < start or key in signals or key in applied_keys:
                continue
            self._record_skip(trade, key, "not_registered_at_detection", {})
            applied_keys.add(key)
            skipped += 1
        return skipped

    def _registration_gate(
        self,
        trade: dict[str, Any],
        signals: dict[str, dict[str, Any]],
    ) -> tuple[bool, str]:
        ok, reason = super()._safety_gate(trade)
        if not ok:
            return ok, reason
        open_risk = sum(
            float(signal.get("risk_pct") or 0.0)
            for signal in signals.values()
            if signal.get("status") == "pending"
        )
        if open_risk + float(self._config["risk_pct"]) > float(
            self._config["max_open_risk_pct"]
        ) + 1e-12:
            return False, "max_open_risk_cap"
        return True, "ok"

    def _strategy_allowed(self, strategy: str) -> bool:
        return (
            strategy in set(self._config["candidate_strategies"])
            and super()._strategy_allowed(strategy)
        )

    def _select_strategy(self, history: list[dict[str, Any]]) -> dict[str, Any]:
        if not history:
            return {"strategy": None, "reason": "no_causal_history"}
        ordered = sorted(
            history,
            key=lambda trade: (
                _parse_dt(trade.get("outcome_at"))
                or _parse_dt(trade.get("detected_at"))
                or datetime.min.replace(tzinfo=timezone.utc)
            ),
        )
        fast_n = int(self._config["fast_n"])
        mid_n = int(self._config["mid_n"])
        long_n = int(self._config["long_n"])
        fast_stats = self._compute_growth_stats(ordered[-fast_n:])
        mid_stats = self._compute_growth_stats(ordered[-mid_n:])
        long_stats = self._compute_growth_stats(ordered[-long_n:])

        candidates: list[
            tuple[float, StrategyGrowthStat, StrategyGrowthStat, StrategyGrowthStat]
        ] = []
        rejects: list[dict[str, Any]] = []
        for strategy in self._config["candidate_strategies"]:
            fast = fast_stats.get(strategy)
            mid = mid_stats.get(strategy)
            long = long_stats.get(strategy)
            if fast is None or mid is None or long is None:
                continue
            reason = self._causal_reject_reason(fast, mid, long)
            if reason:
                rejects.append(
                    {
                        "strategy": strategy,
                        "reason": reason,
                        "fast": fast.as_dict(),
                        "mid": mid.as_dict(),
                        "long": long.as_dict(),
                    }
                )
                continue
            score = self._causal_score(fast, mid, long)
            if score > 0:
                candidates.append((score, fast, mid, long))

        if not candidates:
            return {
                "strategy": None,
                "reason": "no_strategy_passed_causal_filters",
                "causal_history_count": len(ordered),
                "top_rejected": sorted(
                    rejects,
                    key=lambda item: item["fast"].get("avg_log_return", -999),
                    reverse=True,
                )[:5],
            }

        candidates.sort(key=lambda item: item[0], reverse=True)
        score, fast, mid, long = candidates[0]
        return {
            "strategy": fast.strategy,
            "direction": _direction(fast.strategy),
            "reason": "selected_by_causal_log_growth",
            "causal_score": score,
            "robust_score": score,
            "causal_history_count": len(ordered),
            "fast": fast.as_dict(),
            "recent": fast.as_dict(),
            "mid": mid.as_dict(),
            "long": long.as_dict(),
            "all": long.as_dict(),
            "alternatives": [
                {
                    "strategy": alt_fast.strategy,
                    "direction": _direction(alt_fast.strategy),
                    "causal_score": alt_score,
                }
                for alt_score, alt_fast, _, _ in candidates[1:5]
            ],
        }

    def _causal_reject_reason(
        self,
        fast: StrategyGrowthStat,
        mid: StrategyGrowthStat,
        long: StrategyGrowthStat,
    ) -> str | None:
        is_limit = fast.strategy.startswith("LIMIT")
        min_fast = int(
            self._config[
                "min_fast_limit_filled" if is_limit else "min_fast_market_filled"
            ]
        )
        min_mid = int(
            self._config[
                "min_mid_limit_filled" if is_limit else "min_mid_market_filled"
            ]
        )
        if fast.filled < min_fast:
            return "fast_filled_too_low"
        if mid.filled < min_mid:
            return "mid_filled_too_low"
        if long.filled < int(self._config["min_long_filled"]):
            return "long_filled_too_low"
        if fast.avg_log_return <= 0:
            return "fast_log_return_not_positive"
        if mid.avg_log_return <= 0:
            return "mid_log_return_not_positive"
        if fast.effective_ev_pct is None or fast.effective_ev_pct <= 0:
            return "fast_ev_not_positive_after_cost"
        return None

    def _causal_score(
        self,
        fast: StrategyGrowthStat,
        mid: StrategyGrowthStat,
        long: StrategyGrowthStat,
    ) -> float:
        score = (
            float(self._config["fast_weight"]) * fast.avg_log_return
            + float(self._config["mid_weight"]) * mid.avg_log_return
            + float(self._config["long_weight"]) * long.avg_log_return
        )
        if fast.strategy.startswith("LIMIT"):
            reliability = min(1.0, fast.filled / 20)
            score *= 0.5 + 0.5 * reliability
        return score

    @staticmethod
    def _relative_strength(trade: dict[str, Any]) -> float:
        try:
            return float((trade.get("filters") or {}).get("relative_strength") or -999.0)
        except (TypeError, ValueError):
            return -999.0

    @staticmethod
    def _signal_batch(detected: datetime) -> str:
        return detected.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def update_causal_adaptive_portfolio() -> dict[str, Any]:
    portfolio = CausalAdaptivePortfolio()
    return portfolio.update()
