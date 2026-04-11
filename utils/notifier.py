"""
utils/notifier.py
Discord Webhook による通知

DISCORD_WEBHOOK_URL が未設定の場合は通知をスキップし動作を継続する。
Discord サーバーのテキストチャンネルで Webhook URL を取得してください:
  チャンネル設定 → 連携サービス → ウェブフック → 新しいウェブフック
"""
from __future__ import annotations

import logging
import os
from datetime import datetime, timezone
from typing import Any

import requests

logger = logging.getLogger(__name__)

# Discord embed カラー
_COLOR_SIGNAL  = 0xFF4444   # 赤   (新規シグナル)
_COLOR_TP      = 0x44FF88   # 緑   (TP到達)
_COLOR_SL      = 0xFF8800   # オレンジ (SL到達)
_COLOR_EXPIRE  = 0x888888   # グレー (追跡終了サマリー)


class Notifier:
    """Discord Webhook 経由でシグナル・追跡アップデートを通知する。"""

    def __init__(self) -> None:
        self._url = os.getenv("DISCORD_WEBHOOK_URL", "")
        if self._url:
            logger.info("Discord notifications enabled.")
        else:
            logger.info("DISCORD_WEBHOOK_URL not set. Notifications disabled.")

    # ------------------------------------------------------------------
    # Public
    # ------------------------------------------------------------------

    def notify_new_signal(
        self,
        symbol: str,
        entry: float,
        sl: float,
        tp: float,
        sl_pct: float,
        tp_pct: float,
        rsi: float | None,
        change_1h: float,
        conviction: str,
        catalyst: str,
        news_count: int,
        regime: str = "UNKNOWN",
        relative_strength: float = 0.0,
    ) -> None:
        """新しいシグナル検出を通知する。"""
        conv_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(conviction, "⚪")
        cat_label  = "❌ NO CATALYST" if catalyst == "NONE" else f"📰 {catalyst}"
        regime_emoji = {
            "BEARISH":  "🔻",
            "STAGNANT": "⏸️",
            "BULLISH":  "🔺",
        }.get(regime, "❔")

        embed: dict[str, Any] = {
            "title":  f"🎯  NEW SHORT SIGNAL  ─  {symbol}",
            "color":  _COLOR_SIGNAL,
            "fields": [
                {"name": "ENTRY",       "value": f"`${entry:.8g}`",                 "inline": True},
                {"name": "STOP LOSS",   "value": f"`${sl:.8g}`  (+{sl_pct:.1f}%)", "inline": True},
                {"name": "TAKE PROFIT", "value": f"`${tp:.8g}`  (-{tp_pct:.1f}%)", "inline": True},
                {"name": "RSI",         "value": f"`{rsi:.1f}` OVERBOUGHT" if rsi else "N/A", "inline": True},
                {"name": "1H CHANGE",   "value": f"`+{change_1h:.2f}%`",            "inline": True},
                {"name": "vs BTC",      "value": f"`{relative_strength:+.2f}%`",    "inline": True},
                {"name": "BTC REGIME",  "value": f"{regime_emoji}  `{regime}`",     "inline": True},
                {"name": "CONVICTION",  "value": f"{conv_emoji}  `{conviction}`",   "inline": True},
                {"name": "FUNDAMENTAL", "value": f"{cat_label}  ({news_count} news in 48h)", "inline": False},
            ],
            "footer":    {"text": "MEXC Momentum Scanner  //  DRY RUN"},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        self._send({"embeds": [embed]})
        logger.info("Discord: new signal notification sent for %s.", symbol)

    def notify_tp_sl_hit(
        self,
        symbol: str,
        entry: float,
        current: float,
        change_pct: float,
        hours_tracked: float,
        hit_tp: bool,
    ) -> None:
        """追跡中の銘柄が TP または SL に到達したことを通知する。"""
        if hit_tp:
            color = _COLOR_TP
            title = f"✅  TP HIT  ─  {symbol}"
        else:
            color = _COLOR_SL
            title = f"⚠️  SL HIT  ─  {symbol}"

        embed: dict[str, Any] = {
            "title":  title,
            "color":  color,
            "fields": [
                {"name": "ENTRY",        "value": f"`${entry:.8g}`",          "inline": True},
                {"name": "CURRENT",      "value": f"`${current:.8g}`",        "inline": True},
                {"name": "CHANGE",       "value": f"`{change_pct:+.2f}%`",    "inline": True},
                {"name": "HOURS TRACKED","value": f"`{hours_tracked:.1f}h`",  "inline": True},
            ],
            "footer":    {"text": "MEXC Momentum Scanner"},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        self._send({"embeds": [embed]})

    def notify_tracking_expired(
        self,
        symbol: str,
        entry: float,
        final_price: float,
        final_change_pct: float,
        min_price: float,
        max_price: float,
        hours_tracked: float,
        hit_tp: bool,
        hit_sl: bool,
    ) -> None:
        """追跡期間終了時のサマリーを通知する。"""
        result = "✅ TP HIT" if hit_tp else ("⚠️ SL HIT" if hit_sl else "─ EXPIRED")
        min_chg = (min_price - entry) / entry * 100
        max_chg = (max_price - entry) / entry * 100

        embed: dict[str, Any] = {
            "title":  f"📊  TRACKING COMPLETE  ─  {symbol}",
            "color":  _COLOR_EXPIRE,
            "fields": [
                {"name": "RESULT",       "value": result,                             "inline": True},
                {"name": "ENTRY",        "value": f"`${entry:.8g}`",                  "inline": True},
                {"name": "FINAL",        "value": f"`${final_price:.8g}`  ({final_change_pct:+.2f}%)", "inline": True},
                {"name": "PEAK DROP",    "value": f"`{min_chg:.2f}%`  (from entry)", "inline": True},
                {"name": "PEAK RISE",    "value": f"`{max_chg:+.2f}%`  (from entry)","inline": True},
                {"name": "TRACKED FOR",  "value": f"`{hours_tracked:.1f}h`",          "inline": True},
            ],
            "footer":    {"text": "MEXC Momentum Scanner"},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        self._send({"embeds": [embed]})

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _send(self, payload: dict[str, Any]) -> None:
        """Discord Webhook に POST を送信する。"""
        if not self._url:
            return
        try:
            resp = requests.post(self._url, json=payload, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.warning("Discord notification failed: %s", e)
