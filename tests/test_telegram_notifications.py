from __future__ import annotations

import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch

from tools.check_live_api_health import run_monitor
from utils.notifier import Notifier


class TelegramNotifierTest(unittest.TestCase):
    def test_live_fill_message_uses_bot_api_without_exposing_secrets(self) -> None:
        response = Mock(status_code=200)
        response.json.return_value = {"ok": True, "result": {}}
        with (
            patch.dict(
                os.environ,
                {
                    "DISCORD_WEBHOOK_URL": "",
                    "TELEGRAM_BOT_TOKEN": "123:secret-token",
                    "TELEGRAM_CHAT_ID": "987654",
                },
                clear=False,
            ),
            patch("utils.notifier.requests.post", return_value=response) as post,
        ):
            sent = Notifier().notify_live_trade_opened(
                symbol="BTC/USDT:USDT",
                direction="short",
                order_id="order-7",
                filled_amount=0.01,
                average_fill_price=65_000.0,
                notional_usdt=650.0,
                sl_price=67_600.0,
                tp_price=59_800.0,
                risk_usdt=26.0,
                leverage=2.0,
                protection_verified=True,
            )

        self.assertTrue(sent)
        payload = post.call_args.kwargs["json"]
        self.assertEqual(payload["chat_id"], "987654")
        self.assertIn("BTC/USDT:USDT", payload["text"])
        self.assertIn("方向: ショート", payload["text"])
        self.assertIn("取引所側SL/TP: 確認済み", payload["text"])
        self.assertNotIn("secret-token", payload["text"])

    def test_missing_credentials_disables_telegram(self) -> None:
        with (
            patch.dict(
                os.environ,
                {
                    "TELEGRAM_BOT_TOKEN": "",
                    "TELEGRAM_CHAT_ID": "",
                },
                clear=False,
            ),
            patch("utils.notifier.requests.post") as post,
        ):
            notifier = Notifier()
            self.assertFalse(notifier.telegram_enabled)
            self.assertFalse(notifier.send_telegram_message("test"))
        post.assert_not_called()

    def test_live_guard_message_is_japanese_and_actionable(self) -> None:
        response = Mock(status_code=200)
        response.json.return_value = {"ok": True, "result": {}}
        with (
            patch.dict(
                os.environ,
                {
                    "TELEGRAM_BOT_TOKEN": "123:secret-token",
                    "TELEGRAM_CHAT_ID": "987654",
                },
                clear=False,
            ),
            patch("utils.notifier.requests.post", return_value=response) as post,
        ):
            sent = Notifier().notify_live_guard_status(
                guard_name="サーキットブレーカー",
                active=True,
                reason="直近10件中8件が損切り",
                impact="新規の実弾注文は送信されません。",
            )

        self.assertTrue(sent)
        message = post.call_args.kwargs["json"]["text"]
        self.assertIn("MEXC実弾売買を安全停止", message)
        self.assertIn("サーキットブレーカー", message)
        self.assertIn("新規の実弾注文は送信されません", message)
        self.assertNotIn("secret-token", message)


class _HealthyExchange:
    def load_markets(self):
        return {"BTC/USDT:USDT": {}}

    def fetch_position_mode(self):
        return {"hedged": True}

    def fetch_positions(self):
        return [{"contracts": 0}]


class _HealthyClient:
    def __init__(self) -> None:
        self.exchange = _HealthyExchange()

    def fetch_balance(self):
        return {"USDT": {"free": 25.42, "total": 25.42}}


class _RecordingNotifier:
    telegram_enabled = True

    def __init__(self) -> None:
        self.events: list[dict] = []
        self.expiry_events: list[dict] = []

    def notify_api_health(self, **kwargs):
        self.events.append(kwargs)
        return True

    def notify_api_expiry(self, **kwargs):
        self.expiry_events.append(kwargs)
        return True


class ApiHealthTransitionTest(unittest.TestCase):
    def test_notifies_only_on_initial_state_failure_and_recovery(self) -> None:
        notifier = _RecordingNotifier()
        with tempfile.TemporaryDirectory() as directory:
            state_file = Path(directory) / "health.json"
            with patch.dict(
                os.environ,
                {
                    "MEXC_API_KEY": "key",
                    "MEXC_SECRET_KEY": "secret",
                    "LIVE_POSITION_MODE": "hedged",
                    "MEXC_LIVE_API_EXPIRES_AT": "",
                },
                clear=False,
            ):
                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                    ),
                    0,
                )
                self.assertEqual(len(notifier.events), 1)
                self.assertTrue(notifier.events[-1]["healthy"])
                self.assertTrue(notifier.events[-1]["initial"])

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                    ),
                    0,
                )
                self.assertEqual(len(notifier.events), 1)

                def unavailable():
                    raise RuntimeError("API unavailable")

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=unavailable,
                    ),
                    1,
                )
                self.assertEqual(len(notifier.events), 2)
                self.assertFalse(notifier.events[-1]["healthy"])

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=unavailable,
                    ),
                    1,
                )
                self.assertEqual(len(notifier.events), 2)

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                    ),
                    0,
                )
                self.assertEqual(len(notifier.events), 3)
                self.assertTrue(notifier.events[-1]["healthy"])
                self.assertFalse(notifier.events[-1]["initial"])

    def test_expiry_alerts_only_at_five_one_and_zero_day_thresholds(self) -> None:
        notifier = _RecordingNotifier()
        with tempfile.TemporaryDirectory() as directory:
            state_file = Path(directory) / "health.json"
            environment = {
                "MEXC_API_KEY": "key",
                "MEXC_SECRET_KEY": "secret",
                "LIVE_POSITION_MODE": "hedged",
                "MEXC_LIVE_API_EXPIRES_AT": "2026-08-10T00:00:00Z",
            }
            with patch.dict(os.environ, environment, clear=False):
                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                        now=datetime(
                            2026,
                            8,
                            4,
                            23,
                            0,
                            tzinfo=timezone.utc,
                        ),
                    ),
                    0,
                )
                self.assertEqual(notifier.expiry_events, [])

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                        now=datetime(
                            2026,
                            8,
                            5,
                            1,
                            0,
                            tzinfo=timezone.utc,
                        ),
                    ),
                    0,
                )
                self.assertEqual(
                    [
                        event["threshold_days"]
                        for event in notifier.expiry_events
                    ],
                    [5],
                )

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                        now=datetime(
                            2026,
                            8,
                            5,
                            2,
                            0,
                            tzinfo=timezone.utc,
                        ),
                    ),
                    0,
                )
                self.assertEqual(len(notifier.expiry_events), 1)

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                        now=datetime(
                            2026,
                            8,
                            9,
                            1,
                            0,
                            tzinfo=timezone.utc,
                        ),
                    ),
                    0,
                )
                self.assertEqual(
                    [
                        event["threshold_days"]
                        for event in notifier.expiry_events
                    ],
                    [5, 1],
                )

                self.assertEqual(
                    run_monitor(
                        state_file=state_file,
                        notifier=notifier,
                        client_factory=_HealthyClient,
                        now=datetime(
                            2026,
                            8,
                            10,
                            0,
                            1,
                            tzinfo=timezone.utc,
                        ),
                    ),
                    0,
                )
                self.assertEqual(
                    [
                        event["threshold_days"]
                        for event in notifier.expiry_events
                    ],
                    [5, 1, 0],
                )

                state = state_file.read_text(encoding="utf-8")
                self.assertIn(
                    '"notified_threshold_days": [\n      0,\n      1,\n      5',
                    state,
                )

    def test_expiry_timestamp_requires_timezone(self) -> None:
        notifier = _RecordingNotifier()
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(
                os.environ,
                {
                    "MEXC_LIVE_API_EXPIRES_AT": "2026-08-10T00:00:00",
                },
                clear=False,
            ):
                self.assertEqual(
                    run_monitor(
                        state_file=Path(directory) / "health.json",
                        notifier=notifier,
                        client_factory=_HealthyClient,
                    ),
                    2,
                )
        self.assertEqual(notifier.events, [])
        self.assertEqual(notifier.expiry_events, [])


if __name__ == "__main__":
    unittest.main()
