"""
core/tracker.py
検出された銘柄の価格追跡マネージャー

シグナルが確認された銘柄を data/tracking.json に記録し、
以降のスキャンサイクルで価格推移を自動追跡する。
追跡データは GitHub Actions が自動コミットするためリポジトリに永続化される。
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)

TRACKING_FILE = Path("data/tracking.json")


@dataclass
class PricePoint:
    """単一時点の価格記録。"""
    timestamp: str
    price: float
    change_pct: float   # エントリー価格からの変化率 (%)


@dataclass
class TrackedSymbol:
    """追跡中の銘柄と価格履歴。"""
    symbol: str
    detected_at: str        # 検出時刻 (ISO 8601)
    expires_at: str         # 追跡終了時刻 (ISO 8601)
    detection_price: float
    detection_rsi: float | None
    detection_1h_change: float
    sl_price: float
    tp_price: float
    conviction: str         # HIGH / MEDIUM / LOW
    prices: list[PricePoint] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Computed properties
    # ------------------------------------------------------------------

    @property
    def current_price(self) -> float:
        return self.prices[-1].price if self.prices else self.detection_price

    @property
    def current_change_pct(self) -> float:
        return self.prices[-1].change_pct if self.prices else 0.0

    @property
    def max_price(self) -> float:
        all_prices = [p.price for p in self.prices] + [self.detection_price]
        return max(all_prices)

    @property
    def min_price(self) -> float:
        all_prices = [p.price for p in self.prices] + [self.detection_price]
        return min(all_prices)

    @property
    def is_expired(self) -> bool:
        return datetime.now(timezone.utc) >= datetime.fromisoformat(self.expires_at)

    @property
    def hours_tracked(self) -> float:
        delta = datetime.now(timezone.utc) - datetime.fromisoformat(self.detected_at)
        return delta.total_seconds() / 3600

    def hit_tp(self) -> bool:
        """TP（利確ライン）に到達したか。ショートなので min_price <= tp_price。"""
        return self.min_price <= self.tp_price

    def hit_sl(self) -> bool:
        """SL（損切りライン）に到達したか。ショートなので max_price >= sl_price。"""
        return self.max_price >= self.sl_price


class SymbolTracker:
    """シグナル銘柄の価格追跡を管理する。

    data/tracking.json を読み書きして状態を永続化する。
    GitHub Actions がサイクルごとにファイルをコミットするため
    Run をまたいでもデータが保持される。
    """

    def __init__(self) -> None:
        self._tracking_hours: int = int(os.getenv("TRACKING_HOURS", "24"))
        self._symbols: dict[str, TrackedSymbol] = {}
        self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def add_if_new(
        self,
        symbol: str,
        detection_price: float,
        rsi: float | None,
        change_1h: float,
        sl_price: float,
        tp_price: float,
        conviction: str,
    ) -> bool:
        """新しいシグナルを追跡リストに追加する。

        Returns:
            True: 新規追加  /  False: すでに追跡中
        """
        existing = self._symbols.get(symbol)
        if existing and not existing.is_expired:
            logger.info("Already tracking %s.", symbol)
            return False

        now     = datetime.now(timezone.utc)
        expires = now + timedelta(hours=self._tracking_hours)

        self._symbols[symbol] = TrackedSymbol(
            symbol=symbol,
            detected_at=now.isoformat(),
            expires_at=expires.isoformat(),
            detection_price=detection_price,
            detection_rsi=rsi,
            detection_1h_change=change_1h,
            sl_price=sl_price,
            tp_price=tp_price,
            conviction=conviction,
        )
        logger.info(
            "Started tracking %s for %dh (until %s).",
            symbol,
            self._tracking_hours,
            expires.strftime("%m/%d %H:%M UTC"),
        )
        return True

    def update_prices(self, client: MEXCClient) -> None:
        """追跡中の全銘柄の現在価格を一括更新する。"""
        active = [v for v in self._symbols.values() if not v.is_expired]
        if not active:
            return

        symbols_list = [s.symbol for s in active]
        try:
            tickers = client.fetch_tickers(symbols_list)
            now_str = datetime.now(timezone.utc).isoformat()

            for tracked in active:
                ticker = tickers.get(tracked.symbol, {})
                price  = float(ticker.get("last") or 0)
                if price <= 0:
                    continue

                change_pct = (price - tracked.detection_price) / tracked.detection_price * 100
                tracked.prices.append(PricePoint(
                    timestamp=now_str,
                    price=price,
                    change_pct=change_pct,
                ))
                # 直近 200 ポイントのみ保持
                if len(tracked.prices) > 200:
                    tracked.prices = tracked.prices[-200:]

        except Exception as e:
            logger.error("Failed to update tracking prices: %s", e)

    def clean_expired(self) -> list[TrackedSymbol]:
        """期限切れの追跡エントリを削除し、削除したものを返す。"""
        expired = [v for v in self._symbols.values() if v.is_expired]
        for s in expired:
            logger.info(
                "Tracking expired: %s | final_chg=%.2f%% | tp=%s sl=%s",
                s.symbol,
                s.current_change_pct,
                "HIT" if s.hit_tp() else "miss",
                "HIT" if s.hit_sl() else "miss",
            )
            del self._symbols[s.symbol]
        return expired

    def active_symbols(self) -> list[TrackedSymbol]:
        """アクティブな追跡銘柄リストを返す（期限切れ除く）。"""
        return [v for v in self._symbols.values() if not v.is_expired]

    def save(self) -> None:
        """追跡データを JSON ファイルに保存する。"""
        TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
        payload: dict = {}
        for k, v in self._symbols.items():
            entry = {
                f: getattr(v, f)
                for f in [
                    "symbol", "detected_at", "expires_at",
                    "detection_price", "detection_rsi", "detection_1h_change",
                    "sl_price", "tp_price", "conviction",
                ]
            }
            entry["prices"] = [asdict(p) for p in v.prices]
            payload[k] = entry

        with TRACKING_FILE.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        logger.debug("Tracking data saved: %d symbol(s).", len(payload))

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _load(self) -> None:
        """JSON ファイルから追跡データを読み込む。"""
        if not TRACKING_FILE.exists():
            logger.debug("No tracking file found. Starting fresh.")
            return
        try:
            with TRACKING_FILE.open(encoding="utf-8") as f:
                data = json.load(f)
            for symbol, entry in data.items():
                prices = [PricePoint(**p) for p in entry.pop("prices", [])]
                self._symbols[symbol] = TrackedSymbol(**entry, prices=prices)
            logger.info("Loaded %d tracked symbol(s) from file.", len(self._symbols))
        except Exception as e:
            logger.warning("Failed to load tracking file: %s", e)
