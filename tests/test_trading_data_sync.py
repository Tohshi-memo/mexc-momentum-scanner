from __future__ import annotations

import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from types import SimpleNamespace

from core.trading_data_events import (
    record_analysis_event,
    record_live_decision_event,
)
from tools.sync_trading_data import (
    build_outcome_event,
    build_policy_events,
    build_shadow_signal_event,
    runtime_path,
    sync_outbox,
    sync_stream,
)


class FakeClient:
    def __init__(self, *, fail_on_call: int | None = None) -> None:
        self.calls: list[dict] = []
        self.fail_on_call = fail_on_call

    def ingest_events(
        self,
        events,
        *,
        schema_version: str,
        idempotency_key: str | None = None,
    ):
        call_number = len(self.calls) + 1
        if self.fail_on_call == call_number:
            raise RuntimeError("simulated outage")
        self.calls.append(
            {
                "events": list(events),
                "schema_version": schema_version,
                "idempotency_key": idempotency_key,
            }
        )
        return {"accepted": len(self.calls[-1]["events"])}


def _analysis() -> SimpleNamespace:
    return SimpleNamespace(
        symbol="AAA/USDT:USDT",
        signal_candle_at="2026-07-29T06:00:00+00:00",
        price=100.0,
        change_1h_pct=7.5,
        relative_strength_pct=6.0,
        volume_24h_usdt=2_000_000.0,
        rsi=72.0,
        rsi_4h=61.0,
        rsi_15m=78.0,
        bb_upper=98.0,
        bb_middle=90.0,
        bb_lower=82.0,
        bb_width_pct=17.8,
        volume_trend_ratio=1.4,
        volume_trend="RISING",
        atr_pct=9.5,
        funding_rate=0.02,
        obv_divergence="NONE",
        open_interest_usd=100_000.0,
        oi_change_pct=4.0,
        long_short_ratio=1.2,
        upper_wick_ratio_1h=0.3,
        consecutive_green_1h=3,
        consecutive_green_4h=1,
        ma20_deviation_pct=11.1,
        candle_body_ratio=0.7,
        daily_direction="GREEN",
        is_confirmed_signal=False,
        reject_reasons=["4h RSI gate"],
    )


def _proposal() -> SimpleNamespace:
    return SimpleNamespace(
        entry_price=100.0,
        stop_loss=104.0,
        take_profit=92.0,
        sl_pct=4.0,
        tp_pct=8.0,
    )


def _historical_record() -> dict:
    return {
        "symbol": "AAA/USDT:USDT",
        "signal_candle_at": "2026-07-29T06:00:00+00:00",
        "detected_at": "2026-07-29T06:05:00+00:00",
        "expires_at": "2026-07-29T14:05:00+00:00",
        "entry_price": 100.0,
        "sl_price": 104.0,
        "tp_price": 92.0,
        "sl_pct": 4.0,
        "tp_pct": 8.0,
        "market_regime": "STAGNANT",
        "confirmed_strict": False,
        "strict_reject_reasons": ["4h RSI gate"],
        "policy_version": "test-v1",
        "policy_fingerprint": "f" * 64,
        "filters": {
            "rsi": 72.0,
            "rsi_4h": 61.0,
            "bb_upper": 98.0,
            "price_vs_bb": 100.0 / 98.0,
            "volume_ratio": 1.4,
            "volume_trend": "RISING",
            "atr_pct": 9.5,
            "change_1h": 7.5,
            "relative_strength": 6.0,
            "btc_change_1h": 0.1,
            "funding_rate": 0.02,
            "obv_divergence": "NONE",
            "open_interest_usd": 100_000.0,
            "oi_change_pct": 4.0,
            "long_short_ratio": 1.2,
            "upper_wick_ratio_1h": 0.3,
            "consecutive_green_1h": 3,
            "consecutive_green_4h": 1,
            "bb_width_pct": 17.8,
            "ma20_deviation_pct": 11.1,
            "candle_body_ratio": 0.7,
            "rsi_15m": 78.0,
            "daily_direction": "GREEN",
        },
        "ask_price": 100.1,
        "bid_price": 99.9,
        "spread_pct": (100.1 - 99.9) / ((100.1 + 99.9) / 2) * 100,
        "outcome": "TP_HIT",
        "outcome_at": "2026-07-29T08:00:00+00:00",
        "outcome_price": 92.0,
        "pnl_pct": 8.0,
        "hours_held": 1.92,
        "max_favorable_pct": 8.5,
        "max_adverse_pct": -1.0,
        "last_price": 92.0,
        "entry_variants": [
            {
                "strategy": "MARKET",
                "entry_price": 100.0,
                "sl_price": 104.0,
                "tp_price": 92.0,
                "filled": True,
                "outcome": "TP_HIT",
                "pnl_pct": 8.0,
            }
        ],
    }


class EventCaptureTest(unittest.TestCase):
    def test_direct_and_historical_signal_share_event_identity(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            outbox = Path(directory) / "events.jsonl"
            with patch.dict(
                "os.environ",
                {"TD_OUTBOX_FILE": str(outbox)},
                clear=False,
            ):
                direct = record_analysis_event(
                    _analysis(),
                    regime="STAGNANT",
                    proposal=_proposal(),
                    policy_version="test-v1",
                    policy_fingerprint="f" * 64,
                    btc_change_1h=0.1,
                    ask_price=100.1,
                    bid_price=99.9,
                    recorded_at="2026-07-29T06:05:00+00:00",
                )

            historical = build_shadow_signal_event(_historical_record())
            self.assertEqual(direct["event_id"], historical["event_id"])
            self.assertEqual(direct, historical)
            self.assertFalse(direct["payload"]["confirmed_strict"])
            self.assertEqual(
                ["4h RSI gate"],
                direct["payload"]["strict_reject_reasons"],
            )
            stored = json.loads(outbox.read_text(encoding="utf-8"))
            self.assertEqual(direct["event_id"], stored["event_id"])

    def test_live_reject_references_signal_and_keeps_decision_time(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            outbox = Path(directory) / "events.jsonl"
            with patch.dict(
                "os.environ",
                {"TD_OUTBOX_FILE": str(outbox)},
                clear=False,
            ):
                event = record_live_decision_event(
                    _analysis(),
                    accepted=False,
                    stage="cooldown",
                    reasons=["SL within last 48h"],
                    policy_version="test-v1",
                    policy_fingerprint="f" * 64,
                    dry_run=False,
                    decided_at="2026-07-29T06:06:00+00:00",
                )

            self.assertEqual("mexc.live_reject", event["event_type"])
            self.assertEqual(
                "2026-07-29T06:06:00+00:00",
                event["payload"]["decision_at"],
            )
            self.assertEqual("live", event["payload"]["mode"])

    def test_outcome_keeps_variants_without_repeating_signal_features(self) -> None:
        event = build_outcome_event(_historical_record())
        self.assertIsNotNone(event)
        assert event is not None
        self.assertEqual("mexc.outcome", event["event_type"])
        self.assertEqual(
            "MARKET",
            event["payload"]["entry_variants"][0]["strategy"],
        )
        self.assertNotIn("features", event["payload"])
        self.assertEqual(
            "SL_FIRST",
            event["payload"]["label_method"]["same_candle_tie_break"],
        )


class IncrementalSyncTest(unittest.TestCase):
    def test_runtime_outbox_path_honors_environment(self) -> None:
        with patch.dict(
            "os.environ",
            {"TD_OUTBOX_FILE": "data/trading_data_outbox.jsonl"},
            clear=False,
        ):
            resolved = runtime_path(
                "TD_OUTBOX_FILE",
                Path("logs/trading-data-events.jsonl"),
            )

        self.assertEqual(
            resolved,
            Path(__file__).resolve().parents[1]
            / "data"
            / "trading_data_outbox.jsonl",
        )

    def test_current_policy_event_is_immutable_when_history_arrives(self) -> None:
        fingerprint = "f" * 64
        kwargs = {
            "current_policy_version": "test-v1",
            "current_policy_fingerprint": fingerprint,
            "current_effective_at": "2026-07-29T00:00:00+00:00",
            "current_policy_config": {"LIVE_MAX_ORDERS_PER_RUN": "1"},
        }
        initial = build_policy_events([], **kwargs)
        later = build_policy_events(
            [
                {
                    "policy_version": "test-v1",
                    "policy_fingerprint": fingerprint,
                    "detected_at": "2026-07-30T06:05:00+00:00",
                }
            ],
            **kwargs,
        )

        self.assertEqual(initial, later)
        self.assertEqual(
            "2026-07-29T00:00:00+00:00",
            initial[0]["payload"]["effective_at"],
        )

    def test_stream_cursor_advances_only_after_acknowledged_batches(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            state_path = Path(directory) / "state.json"
            state = {"schema_version": 1, "streams": {}}
            records = [_historical_record(), {**_historical_record()}]
            records[1]["symbol"] = "BBB/USDT:USDT"
            events = [build_shadow_signal_event(record) for record in records]
            client = FakeClient()

            sent = sync_stream(
                client,
                stream="mexc.shadow_signal",
                events=events,
                state=state,
                state_path=state_path,
                batch_size=1,
            )
            repeated = sync_stream(
                client,
                stream="mexc.shadow_signal",
                events=events,
                state=state,
                state_path=state_path,
                batch_size=1,
            )

            self.assertEqual(2, sent)
            self.assertEqual(0, repeated)
            self.assertEqual(2, len(client.calls))
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertIn("mexc.shadow_signal", saved["streams"])

    def test_outbox_preserves_unacknowledged_suffix(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            outbox = Path(directory) / "events.jsonl"
            records = [_historical_record(), {**_historical_record()}]
            records[1]["symbol"] = "BBB/USDT:USDT"
            events = [build_shadow_signal_event(record) for record in records]
            outbox.write_text(
                "".join(json.dumps(event) + "\n" for event in events),
                encoding="utf-8",
            )
            client = FakeClient(fail_on_call=2)

            with self.assertRaises(RuntimeError):
                sync_outbox(client, outbox_path=outbox, batch_size=1)

            remaining = [
                json.loads(line)
                for line in outbox.read_text(encoding="utf-8").splitlines()
                if line
            ]
            self.assertEqual(1, len(remaining))
            self.assertEqual(events[1]["event_id"], remaining[0]["event_id"])


if __name__ == "__main__":
    unittest.main()
