"""
tools/dispatch_signals.py
scanner 完了後に実行: 今サイクルで confirmed(STRICT 通過) となった銘柄のうち
『現行チャンピオン戦略と合致する』ものだけを bot へ dispatch 用に書き出す。

出力: data/latest_signal.json
    {
        "dispatched_at": "2026-04-17T06:05:00+00:00",
        "leaders": { ... strategy_selector の出力 ... },
        "signals": [
            {
                "symbol": "...",
                "direction": "long" | "short",
                "strategy": "LIMIT_3PCT_LONG",
                "detection_price": 1.234,
                "entry_price": 1.197,
                "sl_price":    1.149,
                "tp_price":    1.293,
                "sl_pct":      4.0,
                "tp_pct":      8.0,
                "detected_at": "...",
                "expires_at":  "...",
                "market_regime": "BEARISH" | "STAGNANT" | "BULLISH",
                "rel_strength_pct": 7.3,
                "rsi": 78.1,
                "change_1h_pct": 11.2,
                "conviction": "MEDIUM",
                "catalyst_type": "UNKNOWN"
            }
        ]
    }
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools.strategy_selector import select_leaders

TRACKING_FILE = Path("data/tracking.json")
OUTPUT_FILE   = Path("data/latest_signal.json")


def _load_tracking() -> dict[str, dict[str, Any]]:
    if not TRACKING_FILE.exists():
        return {}
    try:
        with TRACKING_FILE.open(encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}


def _is_new_active(entry: dict[str, Any]) -> bool:
    """今サイクルで登録されたばかり (price 履歴が空) の ACTIVE のみ対象。"""
    if entry.get("outcome", "ACTIVE") != "ACTIVE":
        return False
    return len(entry.get("prices") or []) == 0


def _build_signal(
    symbol: str,
    entry: dict[str, Any],
    direction: str,
    strategy: str,
) -> dict[str, Any] | None:
    det = entry.get("detection_price")
    sl  = entry.get("sl_price")
    tp  = entry.get("tp_price")
    if not det or det <= 0 or sl is None or tp is None:
        return None

    sl_pct = (sl - det) / det * 100.0
    tp_pct = (det - tp) / det * 100.0
    if sl_pct <= 0 or tp_pct <= 0:
        return None

    offset_pct  = _strategy_offset_pct(strategy)
    entry_price = det * (1 + offset_pct / 100.0)
    is_long     = direction == "long"

    if is_long:
        sl_price = entry_price * (1 - sl_pct / 100.0)
        tp_price = entry_price * (1 + tp_pct / 100.0)
    else:
        sl_price = entry_price * (1 + sl_pct / 100.0)
        tp_price = entry_price * (1 - tp_pct / 100.0)

    return {
        "symbol":           symbol,
        "direction":        direction,
        "strategy":         strategy,
        "detection_price":  det,
        "entry_price":      entry_price,
        "sl_price":         sl_price,
        "tp_price":         tp_price,
        "sl_pct":           round(sl_pct, 4),
        "tp_pct":           round(tp_pct, 4),
        "detected_at":      entry.get("detected_at"),
        "expires_at":       entry.get("expires_at"),
        "market_regime":    entry.get("market_regime", "UNKNOWN"),
        "rel_strength_pct": entry.get("detection_rel_strength", 0.0),
        "rsi":              entry.get("detection_rsi"),
        "change_1h_pct":    entry.get("detection_1h_change"),
        "conviction":       entry.get("conviction", "UNKNOWN"),
        "catalyst_type":    entry.get("catalyst_type", "UNKNOWN"),
    }


def _strategy_offset_pct(strategy: str) -> float:
    if strategy in ("MARKET", "ASK", "MARKET_LONG", "ASK_LONG"):
        return 0.0
    if strategy.startswith("LIMIT_") and strategy.endswith("PCT_LONG"):
        n = strategy.removeprefix("LIMIT_").removesuffix("PCT_LONG")
        try:
            return -float(n)
        except ValueError:
            return 0.0
    if strategy.startswith("LIMIT_") and strategy.endswith("PCT"):
        n = strategy.removeprefix("LIMIT_").removesuffix("PCT")
        try:
            return float(n)
        except ValueError:
            return 0.0
    return 0.0


def main() -> int:
    leaders      = select_leaders()
    short_leader = leaders["short"]
    long_leader  = leaders["long"]
    short_alive  = short_leader.get("alive") and short_leader.get("strategy")
    long_alive   = long_leader.get("alive")  and long_leader.get("strategy")

    if not short_alive and not long_alive:
        _write_empty(leaders, reason="both_kill_switch_active")
        return 0

    tracking   = _load_tracking()
    new_active = {sym: e for sym, e in tracking.items() if _is_new_active(e)}

    signals: list[dict[str, Any]] = []
    for symbol, entry in new_active.items():
        if short_alive and long_alive:
            if long_leader["recent_expectancy"] >= short_leader["recent_expectancy"]:
                direction, strategy = "long",  long_leader["strategy"]
            else:
                direction, strategy = "short", short_leader["strategy"]
        elif long_alive:
            direction, strategy = "long",  long_leader["strategy"]
        else:
            direction, strategy = "short", short_leader["strategy"]

        sig = _build_signal(symbol, entry, direction, strategy)
        if sig:
            signals.append(sig)

    payload = {
        "dispatched_at": datetime.now(timezone.utc).isoformat(),
        "leaders":       leaders,
        "signals":       signals,
    }
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    _set_output("signal_count", str(len(signals)))
    print(f"dispatch_signals: wrote {len(signals)} signal(s) to {OUTPUT_FILE}")
    return 0


def _write_empty(leaders: dict[str, Any], reason: str) -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump({
            "dispatched_at": datetime.now(timezone.utc).isoformat(),
            "leaders":       leaders,
            "signals":       [],
            "skip_reason":   reason,
        }, f, indent=2, ensure_ascii=False)
    _set_output("signal_count", "0")
    print(f"dispatch_signals: no signals ({reason})")


def _set_output(key: str, value: str) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{key}={value}\n")


if __name__ == "__main__":
    sys.exit(main())
