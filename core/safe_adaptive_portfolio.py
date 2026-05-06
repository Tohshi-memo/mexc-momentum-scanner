"""
Safety-first adaptive DryRun portfolio.

This module runs beside data/live_portfolio.json. It does not place orders and
does not change the current live virtual portfolio. Instead, it forward-tests a
new $100 paper account using closed shadow experiment variants.

Selection rules are intentionally conservative:
  - only use data that was already closed before the simulated signal time
  - rank by average log return, not only arithmetic expectancy
  - require enough filled samples in both recent and all-time windows
  - enforce portfolio-level daily loss, drawdown, and loss-streak brakes
"""
from __future__ import annotations

import json
import logging
import math
import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from core.experiment_archive import load_all_archived

logger = logging.getLogger(__name__)

SAFE_ADAPTIVE_FILE = Path("data/safe_adaptive_portfolio.json")
EXPERIMENT_FILE = Path("data/experiments.json")


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}


def _env_float(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, str(default)))
    except (TypeError, ValueError):
        return default


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except (TypeError, ValueError):
        return default


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_dt(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        text = str(value)
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        dt = datetime.fromisoformat(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def _as_float(value: Any, default: float | None = None) -> float | None:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def _trade_key(trade: dict[str, Any]) -> str:
    return f"{trade.get('symbol', '?')}|{trade.get('detected_at', '')}"


def _is_long(strategy: str) -> bool:
    return strategy.endswith("_LONG")


def _direction(strategy: str) -> str:
    return "long" if _is_long(strategy) else "short"


def _variant_sl_pct(variant: dict[str, Any]) -> float | None:
    entry = _as_float(variant.get("entry_price"))
    sl = _as_float(variant.get("sl_price"))
    if entry is None or sl is None or entry <= 0:
        return None
    return abs(sl - entry) / entry * 100


def _variant_return(variant: dict[str, Any], risk_pct: float) -> float | None:
    """Return account-level fractional return for one variant opportunity."""
    if not variant.get("filled"):
        return 0.0
    pnl_pct = _as_float(variant.get("pnl_pct"))
    sl_pct = _variant_sl_pct(variant)
    if pnl_pct is None or sl_pct is None or sl_pct <= 0:
        return None
    account_return = (risk_pct / 100) * (pnl_pct / sl_pct)
    return max(account_return, -(risk_pct / 100))


def _max_drawdown_pct(returns: list[float]) -> float:
    equity = 1.0
    peak = 1.0
    max_dd = 0.0
    for ret in returns:
        equity *= max(0.0, 1.0 + ret)
        peak = max(peak, equity)
        if peak > 0:
            max_dd = max(max_dd, (peak - equity) / peak * 100)
    return max_dd


def _max_loss_streak(returns: list[float]) -> int:
    streak = 0
    best = 0
    for ret in returns:
        if ret < 0:
            streak += 1
            best = max(best, streak)
        elif ret > 0:
            streak = 0
    return best


def _load_hot_closed(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        logger.warning("Failed to read %s: %s", path, exc)
        return []
    closed = data.get("closed", [])
    return closed if isinstance(closed, list) else []


def _load_closed_records(path: Path = EXPERIMENT_FILE) -> list[dict[str, Any]]:
    raw = list(load_all_archived()) + _load_hot_closed(path)
    sortable: list[tuple[datetime, dict[str, Any]]] = []
    for rec in raw:
        if not isinstance(rec, dict):
            continue
        if not isinstance(rec.get("entry_variants"), list):
            continue
        if rec.get("pnl_pct") is None:
            continue
        detected = _parse_dt(rec.get("detected_at"))
        if detected is None:
            continue
        sortable.append((detected, rec))

    sortable.sort(key=lambda item: item[0])
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for _, rec in sortable:
        key = _trade_key(rec)
        if key in seen:
            continue
        seen.add(key)
        out.append(rec)
    return out


@dataclass
class StrategyGrowthStat:
    strategy: str
    total: int
    filled: int
    fill_rate: float
    avg_pnl_pct: float | None
    effective_ev_pct: float | None
    avg_log_return: float
    geometric_return_pct: float
    avg_account_return_pct: float
    max_drawdown_pct: float
    max_loss_streak: int

    def as_dict(self) -> dict[str, Any]:
        return {
            "strategy": self.strategy,
            "direction": _direction(self.strategy),
            "total": self.total,
            "filled": self.filled,
            "fill_rate": self.fill_rate,
            "avg_pnl_pct": self.avg_pnl_pct,
            "effective_ev_pct": self.effective_ev_pct,
            "avg_log_return": self.avg_log_return,
            "geometric_return_pct": self.geometric_return_pct,
            "avg_account_return_pct": self.avg_account_return_pct,
            "max_drawdown_pct": self.max_drawdown_pct,
            "max_loss_streak": self.max_loss_streak,
        }


class SafeAdaptivePortfolio:
    """Forward-test a separate adaptive paper portfolio."""

    def __init__(
        self,
        file_path: Path = SAFE_ADAPTIVE_FILE,
        experiment_path: Path = EXPERIMENT_FILE,
    ) -> None:
        self._file = file_path
        self._experiment_path = experiment_path
        self._config = self._read_config()
        self._state = self._load()

    @property
    def state(self) -> dict[str, Any]:
        return dict(self._state)

    def update(self) -> dict[str, Any]:
        if not self._config["enabled"]:
            self._state["enabled"] = False
            self._state["updated_at"] = _now_iso()
            self._state["config"] = self._config
            self.save()
            return {"enabled": False, "applied": 0, "skipped": 0}

        closed = _load_closed_records(self._experiment_path)
        start_dt = _parse_dt(self._state.get("started_at")) or datetime.now(timezone.utc)
        applied_keys = self._applied_keys()

        applied = 0
        skipped = 0
        for idx, trade in enumerate(closed):
            key = _trade_key(trade)
            if key in applied_keys:
                continue
            detected = _parse_dt(trade.get("detected_at"))
            if detected is None or detected < start_dt:
                continue

            history = closed[:idx]
            decision = self._select_strategy(history)
            if not decision.get("strategy"):
                self._record_skip(trade, key, decision.get("reason", "no_strategy"), decision)
                applied_keys.add(key)
                skipped += 1
                continue

            ok, reason = self._safety_gate(trade)
            if not ok:
                self._record_skip(trade, key, reason, decision)
                applied_keys.add(key)
                skipped += 1
                continue

            variant = self._find_variant(trade, str(decision["strategy"]))
            if variant is None:
                self._record_skip(trade, key, "variant_missing", decision)
                applied_keys.add(key)
                skipped += 1
                continue

            self._apply_trade(trade, key, variant, decision)
            applied_keys.add(key)
            applied += 1

        self._state["applied_keys"] = sorted(applied_keys)
        self._state["last_decision"] = self._select_strategy(closed)
        self._state["updated_at"] = _now_iso()
        self._state["config"] = self._config
        self._refresh_summary()
        self.save()
        return {"enabled": True, "applied": applied, "skipped": skipped}

    def save(self) -> None:
        self._file.parent.mkdir(parents=True, exist_ok=True)
        self._file.write_text(
            json.dumps(self._state, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def _read_config(self) -> dict[str, Any]:
        return {
            "enabled": _env_bool("SAFE_ADAPTIVE_ENABLED", True),
            "initial_capital": _env_float("SAFE_ADAPTIVE_CAPITAL", 100.0),
            "risk_pct": _env_float("SAFE_ADAPTIVE_RISK_PCT", 0.5),
            "recent_n": _env_int("SAFE_ADAPTIVE_RECENT_N", 50),
            "min_recent_filled": _env_int("SAFE_ADAPTIVE_MIN_RECENT_FILLED", 10),
            "min_all_filled": _env_int("SAFE_ADAPTIVE_MIN_ALL_FILLED", 30),
            "min_ev_pct": _env_float("SAFE_ADAPTIVE_MIN_EV_PCT", 0.20),
            "min_avg_log_return": _env_float("SAFE_ADAPTIVE_MIN_AVG_LOG_RETURN", 0.0),
            "max_strategy_dd_pct": _env_float("SAFE_ADAPTIVE_MAX_STRATEGY_DD_PCT", 15.0),
            "max_portfolio_dd_pct": _env_float("SAFE_ADAPTIVE_MAX_PORTFOLIO_DD_PCT", 10.0),
            "daily_loss_stop_pct": _env_float("SAFE_ADAPTIVE_DAILY_LOSS_STOP_PCT", 2.0),
            "max_loss_streak": _env_int("SAFE_ADAPTIVE_MAX_LOSS_STREAK", 6),
            "loss_streak_cooldown_hours": _env_int(
                "SAFE_ADAPTIVE_LOSS_STREAK_COOLDOWN_HOURS", 6
            ),
            "allow_long": _env_bool("SAFE_ADAPTIVE_ALLOW_LONG", True),
            "allow_short": _env_bool("SAFE_ADAPTIVE_ALLOW_SHORT", True),
            "allow_limit": _env_bool("SAFE_ADAPTIVE_ALLOW_LIMIT", True),
        }

    def _default_state(self) -> dict[str, Any]:
        initial = float(self._config["initial_capital"])
        return {
            "mode": "safe_adaptive_dry_run",
            "enabled": bool(self._config["enabled"]),
            "initial_capital": initial,
            "balance": initial,
            "started_at": _now_iso(),
            "updated_at": _now_iso(),
            "high_watermark": initial,
            "max_drawdown_pct": 0.0,
            "loss_streak": 0,
            "cooldown_until": None,
            "daily_pnl_usdt": {},
            "trades": [],
            "skipped": [],
            "skipped_count": 0,
            "applied_keys": [],
            "last_decision": {},
            "summary": {},
            "config": self._config,
        }

    def _load(self) -> dict[str, Any]:
        if not self._file.exists():
            return self._default_state()
        try:
            data = json.loads(self._file.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                return self._default_state()
        except Exception as exc:
            logger.warning("Failed to load safe adaptive portfolio: %s", exc)
            return self._default_state()

        initial = float(data.get("initial_capital") or self._config["initial_capital"])
        data.setdefault("mode", "safe_adaptive_dry_run")
        data.setdefault("enabled", bool(self._config["enabled"]))
        data.setdefault("initial_capital", initial)
        data.setdefault("balance", initial)
        data.setdefault("started_at", _now_iso())
        data.setdefault("updated_at", _now_iso())
        data.setdefault("high_watermark", max(initial, float(data.get("balance") or initial)))
        data.setdefault("max_drawdown_pct", 0.0)
        data.setdefault("loss_streak", 0)
        data.setdefault("cooldown_until", None)
        data.setdefault("daily_pnl_usdt", {})
        data.setdefault("trades", [])
        data.setdefault("skipped", [])
        data.setdefault("skipped_count", len(data.get("skipped") or []))
        data.setdefault("applied_keys", [])
        data.setdefault("last_decision", {})
        data.setdefault("summary", {})
        data["config"] = self._config
        return data

    def _applied_keys(self) -> set[str]:
        keys = set(str(k) for k in self._state.get("applied_keys", []) if k)
        for item in self._state.get("trades", []):
            if isinstance(item, dict) and item.get("key"):
                keys.add(str(item["key"]))
        for item in self._state.get("skipped", []):
            if isinstance(item, dict) and item.get("key"):
                keys.add(str(item["key"]))
        return keys

    def _strategy_allowed(self, strategy: str) -> bool:
        if _is_long(strategy) and not self._config["allow_long"]:
            return False
        if not _is_long(strategy) and not self._config["allow_short"]:
            return False
        if strategy.startswith("LIMIT") and not self._config["allow_limit"]:
            return False
        return True

    def _compute_growth_stats(
        self,
        trades: list[dict[str, Any]],
    ) -> dict[str, StrategyGrowthStat]:
        raw: dict[str, dict[str, Any]] = {}
        risk_pct = float(self._config["risk_pct"])

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
                ret = _variant_return(variant, risk_pct)
                if ret is None:
                    continue
                row["returns"].append(ret)
                if variant.get("filled"):
                    row["filled"] += 1
                    pnl = _as_float(variant.get("pnl_pct"))
                    if pnl is not None:
                        row["pnls"].append(pnl)

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
        recent = history[-recent_n:] if recent_n > 0 else history
        recent_stats = self._compute_growth_stats(recent)
        all_stats = self._compute_growth_stats(history)

        candidates: list[tuple[StrategyGrowthStat, StrategyGrowthStat]] = []
        rejects: list[dict[str, Any]] = []
        for strategy, recent_stat in recent_stats.items():
            all_stat = all_stats.get(strategy)
            if all_stat is None:
                continue
            reason = self._reject_reason(recent_stat, all_stat)
            if reason:
                rejects.append({
                    "strategy": strategy,
                    "reason": reason,
                    "recent": recent_stat.as_dict(),
                    "all": all_stat.as_dict(),
                })
                continue
            candidates.append((recent_stat, all_stat))

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
                "reason": "no_strategy_passed_safety_filters",
                "top_rejected": top_rejects,
                "history_count": len(history),
                "recent_count": len(recent),
            }

        candidates.sort(
            key=lambda pair: (
                pair[0].avg_log_return,
                pair[0].effective_ev_pct or -999,
                -pair[0].max_drawdown_pct,
                pair[0].filled,
            ),
            reverse=True,
        )
        recent_stat, all_stat = candidates[0]
        return {
            "strategy": recent_stat.strategy,
            "direction": _direction(recent_stat.strategy),
            "reason": "selected_by_recent_avg_log_return",
            "history_count": len(history),
            "recent_count": len(recent),
            "recent": recent_stat.as_dict(),
            "all": all_stat.as_dict(),
            "alternatives": [
                {
                    "strategy": r.strategy,
                    "direction": _direction(r.strategy),
                    "recent": r.as_dict(),
                    "all": a.as_dict(),
                }
                for r, a in candidates[1:5]
            ],
        }

    def _reject_reason(
        self,
        recent: StrategyGrowthStat,
        all_time: StrategyGrowthStat,
    ) -> str | None:
        if recent.filled < int(self._config["min_recent_filled"]):
            return "recent_filled_too_low"
        if all_time.filled < int(self._config["min_all_filled"]):
            return "all_filled_too_low"
        ev = recent.effective_ev_pct
        if ev is None or ev < float(self._config["min_ev_pct"]):
            return "recent_ev_too_low"
        min_log = float(self._config["min_avg_log_return"])
        if recent.avg_log_return <= min_log:
            return "recent_log_return_too_low"
        if all_time.avg_log_return <= min_log:
            return "all_log_return_too_low"
        if recent.max_drawdown_pct > float(self._config["max_strategy_dd_pct"]):
            return "strategy_drawdown_too_high"
        if recent.max_loss_streak >= int(self._config["max_loss_streak"]):
            return "strategy_loss_streak_too_high"
        return None

    def _find_variant(
        self,
        trade: dict[str, Any],
        strategy: str,
    ) -> dict[str, Any] | None:
        variants = trade.get("entry_variants")
        if not isinstance(variants, list):
            return None
        for variant in variants:
            if isinstance(variant, dict) and variant.get("strategy") == strategy:
                return variant
        return None

    def _safety_gate(self, trade: dict[str, Any]) -> tuple[bool, str]:
        balance = float(self._state.get("balance") or 0.0)
        if balance <= 0:
            return False, "balance_zero"

        high = float(self._state.get("high_watermark") or balance)
        current_dd = (high - balance) / high * 100 if high > 0 else 0.0
        if current_dd >= float(self._config["max_portfolio_dd_pct"]):
            return False, "portfolio_drawdown_stop"

        detected = _parse_dt(trade.get("detected_at")) or datetime.now(timezone.utc)
        cooldown_until = _parse_dt(self._state.get("cooldown_until"))
        if cooldown_until and detected < cooldown_until:
            return False, "loss_streak_cooldown"

        day = detected.date().isoformat()
        daily_pnl = float((self._state.get("daily_pnl_usdt") or {}).get(day, 0.0))
        daily_limit = balance * float(self._config["daily_loss_stop_pct"]) / 100
        if daily_pnl <= -daily_limit:
            return False, "daily_loss_stop"

        return True, "ok"

    def _apply_trade(
        self,
        trade: dict[str, Any],
        key: str,
        variant: dict[str, Any],
        decision: dict[str, Any],
    ) -> None:
        balance_before = float(self._state.get("balance") or 0.0)
        risk_pct = float(self._config["risk_pct"])
        account_return = _variant_return(variant, risk_pct)
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
        record = {
            "key": key,
            "symbol": trade.get("symbol"),
            "detected_at": trade.get("detected_at"),
            "closed_at": trade.get("outcome_at"),
            "strategy": variant.get("strategy"),
            "direction": _direction(str(variant.get("strategy") or "")),
            "outcome": variant.get("outcome") or trade.get("outcome"),
            "filled": bool(variant.get("filled")),
            "pnl_pct": _as_float(variant.get("pnl_pct"), 0.0),
            "sl_pct": _variant_sl_pct(variant),
            "risk_pct": risk_pct,
            "account_return_pct": account_return * 100,
            "log_return": log_return,
            "pnl_usdt": pnl_usdt,
            "balance_before": balance_before,
            "balance_after": balance_after,
            "drawdown_after_pct": drawdown,
            "selector_reason": decision.get("reason"),
            "selector_recent": decision.get("recent"),
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

    def _record_skip(
        self,
        trade: dict[str, Any],
        key: str,
        reason: str,
        decision: dict[str, Any],
    ) -> None:
        skipped = list(self._state.get("skipped") or [])
        skipped.append({
            "key": key,
            "symbol": trade.get("symbol"),
            "detected_at": trade.get("detected_at"),
            "reason": reason,
            "decision": decision,
        })
        self._state["skipped"] = skipped[-500:]
        self._state["skipped_count"] = int(self._state.get("skipped_count") or 0) + 1

    def _refresh_summary(self) -> None:
        trades = [t for t in self._state.get("trades", []) if isinstance(t, dict)]
        logs = [
            float(t["log_return"])
            for t in trades
            if t.get("log_return") is not None
        ]
        avg_log = sum(logs) / len(logs) if logs else 0.0
        wins = sum(1 for t in trades if float(t.get("pnl_usdt") or 0.0) > 0)
        losses = sum(1 for t in trades if float(t.get("pnl_usdt") or 0.0) < 0)
        flat = len(trades) - wins - losses
        self._state["summary"] = {
            "trade_count": len(trades),
            "wins": wins,
            "losses": losses,
            "flat": flat,
            "avg_log_return": avg_log,
            "geometric_return_pct": (math.exp(avg_log) - 1.0) * 100,
            "return_pct": (
                (float(self._state.get("balance") or 0.0) - float(self._state["initial_capital"]))
                / float(self._state["initial_capital"])
                * 100
                if float(self._state["initial_capital"]) > 0
                else 0.0
            ),
        }


def update_safe_adaptive_portfolio() -> dict[str, Any]:
    portfolio = SafeAdaptivePortfolio()
    return portfolio.update()
