"""
core/market_context.py
Lightweight scan context recorder.

This keeps enough pre-detection context to audit filter decisions without
storing full OHLCV snapshots for every symbol. The file is intentionally capped
so it remains safe to commit from GitHub Actions.
"""
from __future__ import annotations

import json
import logging
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from core.analyzer import AnalysisResult
    from core.scanner import BTCStatus

logger = logging.getLogger(__name__)

MARKET_CONTEXT_FILE = Path("data/market_context.json")


class MarketContextRecorder:
    """Persist compact market context for later filter analysis."""

    def __init__(self, file_path: Path = MARKET_CONTEXT_FILE) -> None:
        self._file = file_path
        self._enabled = os.getenv("MARKET_CONTEXT_ENABLED", "true").lower() != "false"
        self._max_records = int(os.getenv("MARKET_CONTEXT_MAX_RECORDS", "288"))
        self._analysis_symbol_limit = int(
            os.getenv("MARKET_CONTEXT_ANALYSIS_SYMBOL_LIMIT", "25")
        )

    def record(
        self,
        *,
        cycle: int,
        btc_status: "BTCStatus",
        scan_context: dict[str, Any] | None,
        analysis_results: list["AnalysisResult"] | None = None,
    ) -> None:
        """Append one compact scan-context record and enforce the hot cap."""
        if not self._enabled:
            return

        now = datetime.now(timezone.utc).isoformat()
        payload = self._load()
        records = payload.get("records", [])
        if not isinstance(records, list):
            records = []

        records.append(
            {
                "timestamp": now,
                "cycle": cycle,
                "btc": {
                    "symbol": btc_status.symbol,
                    "price": self._rounded(btc_status.price),
                    "change_1h_pct": self._rounded(btc_status.change_1h_pct),
                    "regime": btc_status.regime,
                    "signal_active": btc_status.is_signal_active,
                },
                "scan": scan_context or {},
                "analysis": self._summarize_analysis(analysis_results or []),
            }
        )

        if self._max_records > 0 and len(records) > self._max_records:
            records = records[-self._max_records :]

        output = {
            "updated_at": now,
            "max_records": self._max_records,
            "record_count": len(records),
            "records": records,
        }
        self._save(output)
        logger.info("Market context recorded: records=%d", len(records))

    def _summarize_analysis(
        self, analysis_results: list["AnalysisResult"]
    ) -> dict[str, Any]:
        confirmed = [r for r in analysis_results if r.is_confirmed_signal]
        rejected = [r for r in analysis_results if not r.is_confirmed_signal]

        reason_counts: Counter[str] = Counter()
        for r in rejected:
            reasons = r.reject_reasons or ["unknown"]
            reason_counts.update(reasons)

        return {
            "analyzed": len(analysis_results),
            "confirmed_strict": len(confirmed),
            "rejected_strict": len(rejected),
            "reject_reason_counts": dict(reason_counts.most_common()),
            "data_coverage": self._coverage(analysis_results),
            "top_analyzed": [
                self._result_row(r)
                for r in sorted(
                    analysis_results,
                    key=lambda item: item.relative_strength_pct,
                    reverse=True,
                )[: self._analysis_symbol_limit]
            ],
        }

    @staticmethod
    def _coverage(analysis_results: list["AnalysisResult"]) -> dict[str, int]:
        fields = (
            "funding_rate",
            "open_interest_usd",
            "oi_change_pct",
            "long_short_ratio",
            "rsi_15m",
            "daily_direction",
        )
        coverage: dict[str, int] = {"total": len(analysis_results)}
        for field in fields:
            coverage[field] = sum(
                getattr(r, field, None) is not None for r in analysis_results
            )
        return coverage

    def _result_row(self, r: "AnalysisResult") -> dict[str, Any]:
        return {
            "symbol": r.symbol,
            "price": self._rounded(r.price),
            "change_1h_pct": self._rounded(r.change_1h_pct),
            "relative_strength_pct": self._rounded(r.relative_strength_pct),
            "volume_24h_usdt": self._rounded(r.volume_24h_usdt, 2),
            "confirmed_strict": r.is_confirmed_signal,
            "reject_reasons": list(r.reject_reasons),
            "rsi": self._rounded(r.rsi),
            "rsi_4h": self._rounded(r.rsi_4h),
            "atr_pct": self._rounded(r.atr_pct),
            "funding_rate": self._rounded(r.funding_rate),
            "oi_change_pct": self._rounded(r.oi_change_pct),
            "long_short_ratio": self._rounded(r.long_short_ratio),
            "volume_trend": r.volume_trend,
            "bb_width_pct": self._rounded(r.bb_width_pct),
            "ma20_deviation_pct": self._rounded(r.ma20_deviation_pct),
            "daily_direction": r.daily_direction,
        }

    def _load(self) -> dict[str, Any]:
        if not self._file.exists():
            return {"records": []}
        try:
            data = json.loads(self._file.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except Exception as e:
            logger.warning("Failed to load market context: %s", e)
        return {"records": []}

    def _save(self, payload: dict[str, Any]) -> None:
        self._file.parent.mkdir(parents=True, exist_ok=True)
        with self._file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

    @staticmethod
    def _rounded(value: Any, digits: int = 4) -> float | None:
        if value is None:
            return None
        try:
            return round(float(value), digits)
        except (TypeError, ValueError):
            return None
