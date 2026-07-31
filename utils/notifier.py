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
        self._telegram_token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        self._telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
        if self._url:
            logger.info("Discord notifications enabled.")
        else:
            logger.info("DISCORD_WEBHOOK_URL not set. Notifications disabled.")
        if self.telegram_enabled:
            logger.info("Telegram notifications enabled.")
        else:
            logger.info(
                "TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID not set. "
                "Telegram notifications disabled."
            )

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

    @property
    def telegram_enabled(self) -> bool:
        """Return True only when both Telegram credentials are configured."""
        return bool(self._telegram_token and self._telegram_chat_id)

    def send_telegram_message(self, text: str) -> bool:
        """Send a plain UTF-8 Telegram message without affecting trading."""
        return self._send_telegram(text)

    def notify_live_trade_opened(
        self,
        *,
        symbol: str,
        direction: str,
        order_id: str,
        filled_amount: float,
        average_fill_price: float,
        notional_usdt: float,
        sl_price: float,
        tp_price: float,
        risk_usdt: float,
        leverage: float,
        protection_verified: bool,
    ) -> bool:
        """Notify only after a live fill and exchange-side protection are verified."""
        protected = "確認済み" if protection_verified else "未確認"
        direction_label = {
            "long": "ロング",
            "short": "ショート",
        }.get(direction.strip().lower(), direction)
        message = (
            "🟢 MEXC 実弾エントリー\n"
            f"銘柄: {symbol}\n"
            f"方向: {direction_label}\n"
            f"約定数量: {filled_amount:.8g}\n"
            f"平均約定価格: {average_fill_price:.8g}\n"
            f"建玉: {notional_usdt:.2f} USDT\n"
            f"最大想定損失: {risk_usdt:.4f} USDT\n"
            f"レバレッジ: {leverage:.2f}x\n"
            f"SL: {sl_price:.8g}\n"
            f"TP: {tp_price:.8g}\n"
            f"取引所側SL/TP: {protected}\n"
            f"注文ID: {order_id}"
        )
        return self._send_telegram(message)

    def notify_live_execution_error(
        self,
        *,
        symbol: str,
        status: str,
        reason: str,
        emergency_close: dict[str, Any] | None,
    ) -> bool:
        """Alert when a live mutation is unsafe or needs emergency recovery."""
        close_status = "未実施"
        close_order_id = ""
        if isinstance(emergency_close, dict):
            raw_close_status = str(
                emergency_close.get("status") or "不明"
            )
            close_status = {
                "ok": "成功",
                "failed": "失敗",
                "error": "エラー",
            }.get(raw_close_status.lower(), raw_close_status)
            close_order_id = str(emergency_close.get("order_id") or "")
        status_label = {
            "ok": "正常",
            "missing": "実行結果なし",
            "failed": "失敗",
            "error": "エラー",
            "dry_run": "テスト実行",
        }.get(status.strip().lower(), status or "不明")
        message = (
            "🚨 MEXC 実弾注文エラー\n"
            f"銘柄: {symbol}\n"
            f"状態: {status_label}\n"
            f"理由: {reason[:800]}\n"
            f"緊急クローズ: {close_status}"
        )
        if close_order_id:
            message += f"\nクローズ注文ID: {close_order_id}"
        message += "\nMEXC画面でポジションとSL/TPを確認してください。"
        return self._send_telegram(message)

    def notify_live_guard_status(
        self,
        *,
        guard_name: str,
        active: bool,
        reason: str,
        impact: str,
    ) -> bool:
        """Notify when an important live-trading guard changes state."""
        if active:
            title = "🚨 MEXC実弾売買を安全停止"
            state = "発動中"
        else:
            title = "✅ MEXC実弾売買の安全停止を解除"
            state = "解除"
        message = (
            f"{title}\n"
            f"安全装置: {guard_name}\n"
            f"状態: {state}\n"
            f"理由: {reason[:1000]}\n"
            f"影響: {impact[:1000]}"
        )
        return self._send_telegram(message)

    def notify_api_health(
        self,
        *,
        healthy: bool,
        detail: str,
        free_usdt: float | None = None,
        open_positions: int | None = None,
        initial: bool = False,
    ) -> bool:
        """Notify on API monitor startup, failure transition, and recovery."""
        if healthy and initial:
            title = "🟢 MEXC API監視を開始"
        elif healthy:
            title = "✅ MEXC API復旧"
        else:
            title = "🚨 MEXC API異常"
        lines = [title, f"詳細: {detail[:800]}"]
        if free_usdt is not None:
            lines.append(f"利用可能残高: {free_usdt:.2f} USDT")
        if open_positions is not None:
            lines.append(f"オープンポジション: {open_positions}")
        return self._send_telegram("\n".join(lines))

    def notify_api_expiry(
        self,
        *,
        expires_at_jst: str,
        threshold_days: int,
    ) -> bool:
        """Notify only at selected API-key expiry thresholds."""
        if threshold_days > 0:
            title = (
                f"⏳ MEXC APIキー期限: あと{threshold_days}日以内"
            )
        else:
            title = "🚨 MEXC APIキーの登録期限に到達"
        lines = [
            title,
            f"登録済み失効日時: {expires_at_jst}",
            "MEXCで更新後、GitHub変数 "
            "MEXC_LIVE_API_EXPIRES_AT も新しい日時へ更新してください。",
        ]
        return self._send_telegram("\n".join(lines))

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
        except requests.RequestException as error:
            logger.warning(
                "Discord notification failed (%s).",
                type(error).__name__,
            )

    def _send_telegram(self, text: str) -> bool:
        """POST sendMessage while keeping the bot token out of logs."""
        if not self.telegram_enabled:
            return False
        endpoint = (
            f"https://api.telegram.org/bot{self._telegram_token}/sendMessage"
        )
        payload = {
            "chat_id": self._telegram_chat_id,
            "text": str(text)[:4000],
        }
        try:
            response = requests.post(endpoint, json=payload, timeout=10)
        except requests.RequestException as error:
            logger.warning(
                "Telegram notification request failed (%s).",
                type(error).__name__,
            )
            return False
        if response.status_code < 200 or response.status_code >= 300:
            logger.warning(
                "Telegram notification failed with HTTP %d.",
                response.status_code,
            )
            return False
        try:
            body = response.json()
        except ValueError:
            logger.warning("Telegram notification returned invalid JSON.")
            return False
        if body.get("ok") is not True:
            logger.warning("Telegram Bot API rejected the notification.")
            return False
        return True
