"""Stable identity for the frozen live-selection policy.

The human-readable version is useful in operations.  The fingerprint prevents
accidental reuse of old outcomes when relevant code or environment thresholds
change without a manual version bump.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_POLICY_SOURCES = (
    "core/analyzer.py",
    "core/executor.py",  # ProposalBuilder defines measured SL/TP outcomes.
    "core/experiment.py",
    "core/fundamental.py",
    "core/live_filter.py",
    "core/live_policy.py",
    "core/live_strategy.py",
    "core/scanner.py",
    "core/strategy_ranker.py",
    "main.py",
    "requirements.txt",
    "utils/mexc_client.py",
)

# Explicit defaults make the identity identical when one workflow relies on a
# code default and another spells the same value out.
_POLICY_ENV_DEFAULTS = {
    "LIVE_POLICY_VERSION": "",
    "LIVE_DATA_DRIVEN_MARKET_SHORT_V2": "true",
    "LIVE_RSI_MIN": "0",
    "LIVE_RSI_4H_MAX": "65",
    "LIVE_ATR_HIGH": "9.0",
    "LIVE_REL_STRENGTH_MIN": "5.0",
    "LIVE_REQUIRE_COMPLETE_TECHNICAL_DATA": "true",
    "LIVE_REQUIRE_FUNDING_DATA": "true",
    "LIVE_MIN_FUNDING_RATE_PCT": "-0.05",
    "LIVE_REQUIRE_FUND_NON_AVOID": "true",
    "LIVE_ALLOWED_FUNDAMENTAL_CONVICTIONS": "HIGH,MEDIUM,UNKNOWN",
    "LIVE_BLOCK_UPPER_WICK": "false",
    "BLOCK_CONSEC_GREEN_1H": "8",
    "BLOCK_BBW_LO": "15.0",
    "BLOCK_BBW_HI": "20.0",
    "BLOCK_MA_DEV_LO": "5.0",
    "BLOCK_MA_DEV_HI": "10.0",
    "BLOCK_ATR_LO": "5.0",
    "BLOCK_ATR_HI": "7.0",
    "BLOCK_WICK_RATIO": "0.6",
    "LIVE_USE_RANKER": "true",
    "LIVE_MIN_EV_PCT": "0.20",
    "LIVE_MIN_RANKER_FILLED": "10",
    "LIVE_SHORT_ONLY": "true",
    "LIVE_GATE_WINDOWS": "20,50,100,200",
    "LIVE_GATE_FEE_PCT": "0.16",
    "LIVE_GATE_SLIPPAGE_PCT": "0.20",
    "LIVE_GATE_FUNDING_PCT": "0.15",
    "LIVE_GATE_MIN_NET_EV_PCT": "0.20",
    "LIVE_GATE_MIN_FILLED": "20",
    "LIVE_GATE_MIN_FILL_RATE": "0.80",
    "LIVE_GATE_MAX_DATA_AGE_HOURS": "24",
    "LIVE_GATE_MIN_DISTINCT_DAYS": "30",
    "LIVE_GATE_MIN_CI_PCT": "0.0",
    "LIVE_MARKET_DATA_MAX_AGE_SECONDS": "10",
    "LIVE_MAX_ENTRY_DRIFT_PCT": "0.5",
    "LIVE_MAX_SPREAD_PCT": "0.10",
    "LIVE_MAX_SLIPPAGE_PCT": "0.10",
    "LIVE_MIN_DEPTH_MULTIPLE": "1.0",
    "LIVE_MAX_ACTUAL_RISK_MULTIPLIER": "1.05",
    "USE_ATR_SL": "true",
    "ATR_SL_MULT": "1.5",
    "ATR_SL_MIN": "1.0",
    "ATR_SL_MAX": "4.0",
    "STOP_LOSS_PCT": "2.0",
    "TAKE_PROFIT_PCT": "4.0",
    "RISK_REWARD_RATIO": "2.0",
    "EXPERIMENT_TRACKING_HOURS": "8",
}


def live_policy_fingerprint() -> str:
    digest = hashlib.sha256()
    for name in sorted(_POLICY_ENV_DEFAULTS):
        value = os.getenv(name, _POLICY_ENV_DEFAULTS[name]).strip()
        digest.update(f"env:{name}={value}\n".encode("utf-8"))
    for name in _POLICY_SOURCES:
        path = _PROJECT_ROOT / name
        digest.update(f"source:{name}\n".encode("utf-8"))
        digest.update(path.read_bytes())
        digest.update(b"\n")
    return digest.hexdigest()
