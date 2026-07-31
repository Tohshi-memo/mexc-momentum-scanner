"""Stateful Telegram alerts for live-trading safety guards."""
from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Protocol


logger = logging.getLogger(__name__)


class GuardNotifier(Protocol):
    def notify_live_guard_status(
        self,
        *,
        guard_name: str,
        active: bool,
        reason: str,
        impact: str,
    ) -> bool: ...


def notify_guard_transition(
    notifier: GuardNotifier,
    *,
    guard_key: str,
    guard_name: str,
    active: bool,
    reason: str,
    impact: str,
    state_file: Path | None = None,
) -> bool:
    """Notify once when a live guard activates or recovers.

    An active transition is persisted only after Telegram accepts the message,
    so a temporary Telegram failure is retried on the next live run.  An
    initially inactive guard is recorded silently as the baseline.
    """
    path = state_file or Path(
        os.getenv("LIVE_ALERT_STATE_FILE", "data/live_alert_state.json")
    )
    state = _load_state(path)
    guards = state.setdefault("guards", {})
    previous = guards.get(guard_key)
    previous_active = (
        previous.get("active") if isinstance(previous, dict) else None
    )

    if previous_active is active:
        return False

    if previous_active is None and not active:
        _store_guard_state(
            path,
            state,
            guard_key=guard_key,
            active=False,
            reason=reason,
        )
        return False

    try:
        sent = notifier.notify_live_guard_status(
            guard_name=guard_name,
            active=active,
            reason=reason,
            impact=impact,
        )
    except Exception as error:
        logger.warning(
            "Telegram live-guard notification failed for %s (%s).",
            guard_key,
            type(error).__name__,
        )
        return False

    if not sent:
        logger.warning(
            "Telegram live-guard notification was not delivered for %s.",
            guard_key,
        )
        return False

    _store_guard_state(
        path,
        state,
        guard_key=guard_key,
        active=active,
        reason=reason,
    )
    return True


def _load_state(path: Path) -> dict:
    if not path.exists():
        return {"guards": {}}
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        logger.warning(
            "Live alert state could not be read (%s); rebuilding it.",
            type(error).__name__,
        )
        return {"guards": {}}
    if not isinstance(loaded, dict):
        return {"guards": {}}
    if not isinstance(loaded.get("guards"), dict):
        loaded["guards"] = {}
    return loaded


def _store_guard_state(
    path: Path,
    state: dict,
    *,
    guard_key: str,
    active: bool,
    reason: str,
) -> None:
    state.setdefault("guards", {})[guard_key] = {
        "active": active,
        "reason": reason,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)
