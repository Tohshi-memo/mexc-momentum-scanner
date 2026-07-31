from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from utils.live_alerts import notify_guard_transition


class LiveGuardTransitionTest(unittest.TestCase):
    def test_notifies_only_on_activation_and_recovery(self) -> None:
        notifier = Mock()
        notifier.notify_live_guard_status.return_value = True

        with tempfile.TemporaryDirectory() as directory:
            state_file = Path(directory) / "alerts.json"
            common = {
                "notifier": notifier,
                "guard_key": "circuit_breaker",
                "guard_name": "サーキットブレーカー",
                "reason": "直近10件中8件が損切り",
                "impact": "新規注文を停止",
                "state_file": state_file,
            }

            self.assertTrue(notify_guard_transition(active=True, **common))
            self.assertFalse(notify_guard_transition(active=True, **common))
            self.assertTrue(notify_guard_transition(active=False, **common))
            self.assertFalse(notify_guard_transition(active=False, **common))

            state = json.loads(state_file.read_text(encoding="utf-8"))
            self.assertFalse(state["guards"]["circuit_breaker"]["active"])

        self.assertEqual(notifier.notify_live_guard_status.call_count, 2)
        first, second = notifier.notify_live_guard_status.call_args_list
        self.assertTrue(first.kwargs["active"])
        self.assertFalse(second.kwargs["active"])

    def test_initial_inactive_state_is_silent_baseline(self) -> None:
        notifier = Mock()
        with tempfile.TemporaryDirectory() as directory:
            state_file = Path(directory) / "alerts.json"
            sent = notify_guard_transition(
                notifier,
                guard_key="strategy_gate",
                guard_name="期待値・戦略ゲート",
                active=False,
                reason="正常",
                impact="注文可能",
                state_file=state_file,
            )
            self.assertFalse(sent)
            state = json.loads(state_file.read_text(encoding="utf-8"))
            self.assertFalse(state["guards"]["strategy_gate"]["active"])
        notifier.notify_live_guard_status.assert_not_called()

    def test_failed_delivery_is_retried(self) -> None:
        notifier = Mock()
        notifier.notify_live_guard_status.side_effect = [False, True]
        with tempfile.TemporaryDirectory() as directory:
            state_file = Path(directory) / "alerts.json"
            kwargs = {
                "guard_key": "circuit_breaker",
                "guard_name": "サーキットブレーカー",
                "active": True,
                "reason": "損失超過",
                "impact": "新規注文を停止",
                "state_file": state_file,
            }
            self.assertFalse(notify_guard_transition(notifier, **kwargs))
            self.assertFalse(state_file.exists())
            self.assertTrue(notify_guard_transition(notifier, **kwargs))
        self.assertEqual(notifier.notify_live_guard_status.call_count, 2)


if __name__ == "__main__":
    unittest.main()
