"""
core/stats.py
バックテスト的な勝率・損益集計マネージャー

data/stats.json にクローズしたトレード (TrackedSymbol) を追記していき、
勝率・平均損益・ドローダウンなどのサマリーをいつでも取得できる。

このファイルから得られる情報をもとに、以下の機能を構築している:
    - クールダウン: 直近 SL 銘柄を一定時間再エントリー禁止
    - サーキットブレーカー: 直近 N 件で損失が閾値超なら当サイクル全スキップ
    - ヘッダー表示: 稼働状況を一目で確認

GitHub Actions が毎サイクルで data/stats.json をコミットするため、
Run をまたいでも記録が永続化される。
"""
from __future__ import annotations

import json
import logging
import math
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from core.tracker import (
    OUTCOME_EXPIRED,
    OUTCOME_SL_HIT,
    OUTCOME_TP_HIT,
    TrackedSymbol,
)

logger = logging.getLogger(__name__)

STATS_FILE     = Path("data/stats.json")
STATS_META_FILE = Path("data/stats_meta.json")


@dataclass
class TradeRecord:
    """クローズしたトレード1件の記録。"""

    symbol: str
    detected_at: str
    closed_at: str
    outcome: str            # TP_HIT | SL_HIT | EXPIRED
    entry_price: float
    exit_price: float
    sl_price: float
    tp_price: float
    pnl_pct: float          # ショート視点の損益率 (%)
    hours_held: float
    conviction: str
    catalyst_type: str
    detection_rsi: float | None
    detection_1h_change: float
    market_regime: str = "UNKNOWN"           # BEARISH / STAGNANT / BULLISH
    detection_rel_strength: float = 0.0      # alt_1h - btc_1h (乖離度)

    # ライブ戦略のスナップショット (検出時の LiveTradeFilter / LiveStrategyBuilder 判定)
    live_tier: str = ""                      # S / A / B
    live_direction: str = ""                 # short / long
    live_entry_style: str = ""               # MARKET / LIMIT_SCALE / LIMIT_PATIENT
    live_boosters: list[str] = field(default_factory=list)
    live_score: float = 0.0

    @classmethod
    def from_tracked(cls, t: TrackedSymbol) -> "TradeRecord":
        """TrackedSymbol から TradeRecord を組み立てる。"""
        exit_price = (
            t.outcome_price
            if t.outcome_price is not None
            else t.current_price
        )
        pnl = (t.detection_price - exit_price) / t.detection_price * 100

        # 経過時間
        closed_at = t.outcome_at or datetime.now(timezone.utc).isoformat()
        detected  = datetime.fromisoformat(t.detected_at)
        closed    = datetime.fromisoformat(closed_at)
        hours_held = (closed - detected).total_seconds() / 3600

        return cls(
            symbol=t.symbol,
            detected_at=t.detected_at,
            closed_at=closed_at,
            outcome=t.outcome,
            entry_price=t.detection_price,
            exit_price=exit_price,
            sl_price=t.sl_price,
            tp_price=t.tp_price,
            pnl_pct=pnl,
            hours_held=hours_held,
            conviction=t.conviction,
            catalyst_type=t.catalyst_type,
            detection_rsi=t.detection_rsi,
            detection_1h_change=t.detection_1h_change,
            market_regime=t.market_regime,
            detection_rel_strength=t.detection_rel_strength,
            live_tier=t.live_tier,
            live_direction=t.live_direction,
            live_entry_style=t.live_entry_style,
            live_boosters=list(t.live_boosters),
            live_score=t.live_score,
        )


@dataclass
class StatsSummary:
    """集計サマリー。UI 表示やログ用。"""
    total: int          = 0
    wins: int           = 0   # TP_HIT
    losses: int         = 0   # SL_HIT
    expired: int        = 0
    win_rate: float     = 0.0   # wins / decided (TP + SL のみ)
    avg_pnl: float      = 0.0   # 全トレードの平均損益率
    avg_win: float      = 0.0   # 勝ちトレードの平均利益率
    avg_loss: float     = 0.0   # 負けトレードの平均損失率 (負の値)
    expectancy: float   = 0.0   # 期待値
    total_pnl_pct: float = 0.0  # 累積損益率（%の総和）
    recent_losses: int  = 0     # 直近ウィンドウ内の SL 数
    recent_window: int  = 10    # 直近ウィンドウサイズ


@dataclass(frozen=True)
class CircuitBreakerState:
    """損失件数とコスト控除後損益を組み合わせた停止判定。"""

    active: bool
    warning: bool
    level: str
    sample_size: int
    minimum_sample_size: int
    window: int
    losses: int
    warning_loss_threshold: int
    loss_threshold: int
    gross_pnl_pct: float
    estimated_cost_pct: float
    net_pnl_pct: float
    severe_net_loss_pct: float
    reasons: tuple[str, ...] = field(default_factory=tuple)


class StatsManager:
    """トレード記録の永続化と集計。"""

    def __init__(
        self,
        file_path: Path = STATS_FILE,
        meta_path: Path = STATS_META_FILE,
    ) -> None:
        self._file = file_path
        self._meta_file = meta_path
        self._records: list[TradeRecord] = []
        # 直近 SL 連発でサーキットブレーカーが発動したあと、リセット時刻を
        # ここに書き込むことで、以降の記録のみで再度カウントする。
        self._cb_reset_at: str | None = None
        self._load()
        self._load_meta()

    # ------------------------------------------------------------------
    # Recording
    # ------------------------------------------------------------------

    def record_closed(self, tracked: TrackedSymbol) -> TradeRecord:
        """クローズした TrackedSymbol をトレード記録に追加して保存する。"""
        record = TradeRecord.from_tracked(tracked)
        self._records.append(record)
        self.save()
        logger.info(
            "Stats: recorded %s | outcome=%s pnl=%+.2f%%",
            record.symbol, record.outcome, record.pnl_pct,
        )
        return record

    def record_many(self, tracked_list: list[TrackedSymbol]) -> list[TradeRecord]:
        """複数 TrackedSymbol を一度に記録する（保存は最後に1回）。"""
        new_records: list[TradeRecord] = []
        for t in tracked_list:
            if t.outcome in (OUTCOME_TP_HIT, OUTCOME_SL_HIT, OUTCOME_EXPIRED):
                record = TradeRecord.from_tracked(t)
                self._records.append(record)
                new_records.append(record)
                logger.info(
                    "Stats: recorded %s | outcome=%s pnl=%+.2f%%",
                    record.symbol, record.outcome, record.pnl_pct,
                )
        if new_records:
            self.save()
        return new_records

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def summary(self, recent_window: int = 10) -> StatsSummary:
        """全トレード集計サマリーを返す。"""
        if not self._records:
            return StatsSummary(recent_window=recent_window)

        wins    = [r for r in self._records if r.outcome == OUTCOME_TP_HIT]
        losses  = [r for r in self._records if r.outcome == OUTCOME_SL_HIT]
        expired = [r for r in self._records if r.outcome == OUTCOME_EXPIRED]
        decided = len(wins) + len(losses)

        win_rate = (len(wins) / decided * 100) if decided > 0 else 0.0

        avg_pnl  = sum(r.pnl_pct for r in self._records) / len(self._records)
        avg_win  = (sum(r.pnl_pct for r in wins)   / len(wins))   if wins   else 0.0
        avg_loss = (sum(r.pnl_pct for r in losses) / len(losses)) if losses else 0.0

        # 期待値 = (勝率 × 平均利益) + ((1 - 勝率) × 平均損失)
        wr = win_rate / 100
        expectancy = wr * avg_win + (1 - wr) * avg_loss if decided > 0 else 0.0

        total_pnl = sum(r.pnl_pct for r in self._records)

        # recent_losses はサーキットブレーカーと同じ基準
        # (reset 以降 かつ 直近 CIRCUIT_BREAKER_LOOKBACK_HOURS 内)
        pool = self._filter_within_lookback(self._records_since_reset())
        recent = pool[-recent_window:]
        recent_losses = sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT)

        return StatsSummary(
            total=len(self._records),
            wins=len(wins),
            losses=len(losses),
            expired=len(expired),
            win_rate=win_rate,
            avg_pnl=avg_pnl,
            avg_win=avg_win,
            avg_loss=avg_loss,
            expectancy=expectancy,
            total_pnl_pct=total_pnl,
            recent_losses=recent_losses,
            recent_window=recent_window,
        )

    def had_sl_within(self, symbol: str, hours: int) -> bool:
        """指定銘柄が `hours` 以内に SL_HIT で終わっていれば True。

        クールダウンに使う。
        """
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        for r in reversed(self._records):
            if r.symbol != symbol:
                continue
            try:
                closed_dt = datetime.fromisoformat(r.closed_at)
            except ValueError:
                continue
            if closed_dt < cutoff:
                return False
            if r.outcome == OUTCOME_SL_HIT:
                return True
        return False

    def circuit_breaker_active(
        self,
        window: int = 10,
        loss_threshold: int = 5,
    ) -> bool:
        """従来どおり、直近 window 件の SL 件数だけを真偽値で返す。"""
        pool = self._filter_within_lookback(self._records_since_reset())
        if len(pool) < window:
            return False
        recent = pool[-window:]
        recent_losses = sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT)
        return recent_losses >= loss_threshold

    def circuit_breaker_state(
        self,
        *,
        window: int = 10,
        minimum_sample_size: int = 5,
        warning_loss_threshold: int = 5,
        loss_threshold: int = 7,
        cost_pct: float = 0.51,
        severe_net_loss_pct: float = -8.0,
    ) -> CircuitBreakerState:
        """直近成績を段階評価し、警戒または新規停止を返す。

        判定対象は次の AND で絞り込む:
          1. reset_circuit_breaker() 以降の記録
          2. 直近 CIRCUIT_BREAKER_LOOKBACK_HOURS 時間内に closed したもの
             (0 または未設定で無効化 = 全期間)

        単純な損失件数だけでは、1:2 のリスクリワードで利益が残る
        5勝5敗まで止めてしまう。そこで次の二段階にする:

          - warning: 損失件数が警戒値以上、またはネット損益がマイナス
          - active:  ハード損失件数以上かつネット損益がマイナス、または
                     ネット損益が severe_net_loss_pct 以下

        コストは各記録から ``cost_pct`` を控除する。通常の損失件数判定は
        window 全件を要求するが、深いネット損失は minimum_sample_size 件から
        早期停止する。それ未満は warmup とする。
        """
        if window <= 0:
            raise ValueError("circuit breaker window must be positive")
        if not 1 <= minimum_sample_size <= window:
            raise ValueError(
                "circuit breaker minimum_sample_size must be within window"
            )
        if not 0 <= warning_loss_threshold <= loss_threshold <= window:
            raise ValueError(
                "circuit breaker thresholds must satisfy "
                "0 <= warning <= hard <= window"
            )
        if not math.isfinite(cost_pct) or cost_pct < 0:
            raise ValueError(
                "circuit breaker cost_pct must be finite and non-negative"
            )
        if not math.isfinite(severe_net_loss_pct) or severe_net_loss_pct > 0:
            raise ValueError(
                "circuit breaker severe_net_loss_pct must be finite and <= 0"
            )

        pool = self._filter_within_lookback(self._records_since_reset())
        recent = pool[-window:]
        recent_losses = sum(1 for r in recent if r.outcome == OUTCOME_SL_HIT)
        gross_pnl = sum(r.pnl_pct for r in recent)
        estimated_cost = len(recent) * cost_pct
        net_pnl = gross_pnl - estimated_cost

        if len(recent) < minimum_sample_size:
            return CircuitBreakerState(
                active=False,
                warning=False,
                level="warmup",
                sample_size=len(recent),
                minimum_sample_size=minimum_sample_size,
                window=window,
                losses=recent_losses,
                warning_loss_threshold=warning_loss_threshold,
                loss_threshold=loss_threshold,
                gross_pnl_pct=gross_pnl,
                estimated_cost_pct=estimated_cost,
                net_pnl_pct=net_pnl,
                severe_net_loss_pct=severe_net_loss_pct,
                reasons=(
                    f"sample={len(recent)}/{minimum_sample_size} minimum",
                ),
            )

        hard_loss_cluster = (
            len(recent) >= window
            and recent_losses >= loss_threshold
            and net_pnl < 0
        )
        severe_net_loss = net_pnl <= severe_net_loss_pct
        active = hard_loss_cluster or severe_net_loss
        warning = active or (
            recent_losses >= warning_loss_threshold or net_pnl < 0
        )
        reasons: list[str] = []
        if hard_loss_cluster:
            reasons.append(
                f"losses={recent_losses}/{window}>={loss_threshold} and net_pnl<0"
            )
        if severe_net_loss:
            reasons.append(
                f"net_pnl={net_pnl:+.2f}%<={severe_net_loss_pct:+.2f}%"
            )
        if not active and warning:
            if recent_losses >= warning_loss_threshold:
                reasons.append(
                    f"warning_losses={recent_losses}/{window}>="
                    f"{warning_loss_threshold}"
                )
            if net_pnl < 0:
                reasons.append(f"warning_net_pnl={net_pnl:+.2f}%")
        if not reasons:
            reasons.append("recent risk is within limits")

        return CircuitBreakerState(
            active=active,
            warning=warning,
            level="blocked" if active else "warning" if warning else "normal",
            sample_size=len(recent),
            minimum_sample_size=minimum_sample_size,
            window=window,
            losses=recent_losses,
            warning_loss_threshold=warning_loss_threshold,
            loss_threshold=loss_threshold,
            gross_pnl_pct=gross_pnl,
            estimated_cost_pct=estimated_cost,
            net_pnl_pct=net_pnl,
            severe_net_loss_pct=severe_net_loss_pct,
            reasons=tuple(reasons),
        )

    def reset_circuit_breaker(self) -> str:
        """サーキットブレーカーのカウントを現時点からやり直す。

        記録自体は消さず、meta ファイルに ``cb_reset_at`` を書き込み、
        以降の circuit_breaker_active() はこの時刻以後の記録のみで判定する。
        戻り値は書き込んだタイムスタンプ (ISO 8601)。
        """
        self._cb_reset_at = datetime.now(timezone.utc).isoformat()
        self._save_meta()
        logger.warning(
            "Circuit breaker reset. Counting from %s onwards.", self._cb_reset_at,
        )
        return self._cb_reset_at

    @property
    def cb_reset_at(self) -> str | None:
        return self._cb_reset_at

    def _records_since_reset(self) -> list[TradeRecord]:
        """リセットタイムスタンプ以降の記録のみ返す (未設定なら全件)。"""
        if not self._cb_reset_at:
            return self._records
        try:
            cutoff = datetime.fromisoformat(self._cb_reset_at)
        except ValueError:
            return self._records
        pool: list[TradeRecord] = []
        for r in self._records:
            try:
                closed = datetime.fromisoformat(r.closed_at)
            except ValueError:
                continue
            if closed >= cutoff:
                pool.append(r)
        return pool

    @staticmethod
    def _lookback_hours() -> float:
        """CIRCUIT_BREAKER_LOOKBACK_HOURS を読み出す (0 で無効)。"""
        try:
            return float(os.getenv("CIRCUIT_BREAKER_LOOKBACK_HOURS", "48"))
        except ValueError:
            return 48.0

    def _filter_within_lookback(
        self, records: list[TradeRecord],
    ) -> list[TradeRecord]:
        """直近 CIRCUIT_BREAKER_LOOKBACK_HOURS 内の closed 記録に絞る。

        0 以下 → 無効化 (全件返す)
        これにより、古い連敗履歴が延々とサーキットブレーカーを
        発動させ続ける問題を防ぐ。
        """
        hours = self._lookback_hours()
        if hours <= 0:
            return records
        cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
        pool: list[TradeRecord] = []
        for r in records:
            try:
                closed = datetime.fromisoformat(r.closed_at)
            except ValueError:
                continue
            if closed >= cutoff:
                pool.append(r)
        return pool

    def summary_by_conviction(self) -> dict[str, dict[str, Any]]:
        """conviction 別のミニサマリー（勝率分析用）。"""
        return self._grouped_summary(lambda r: r.conviction)

    def summary_by_regime(self) -> dict[str, dict[str, Any]]:
        """market_regime 別のミニサマリー。

        BEARISH / STAGNANT / BULLISH 各局面でどの程度勝てているかを見る。
        BULLISH (乖離検出) が有効に働いているかの検証に使う。
        """
        return self._grouped_summary(lambda r: r.market_regime or "UNKNOWN")

    def _grouped_summary(
        self, key_func: "Any"
    ) -> dict[str, dict[str, Any]]:
        groups: dict[str, list[TradeRecord]] = {}
        for r in self._records:
            groups.setdefault(key_func(r), []).append(r)

        out: dict[str, dict[str, Any]] = {}
        for key, records in groups.items():
            wins    = sum(1 for r in records if r.outcome == OUTCOME_TP_HIT)
            losses  = sum(1 for r in records if r.outcome == OUTCOME_SL_HIT)
            decided = wins + losses
            wr  = (wins / decided * 100) if decided > 0 else 0.0
            avg = sum(r.pnl_pct for r in records) / len(records) if records else 0.0
            out[key] = {
                "total":    len(records),
                "wins":     wins,
                "losses":   losses,
                "win_rate": wr,
                "avg_pnl":  avg,
            }
        return out

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self) -> None:
        """トレード記録を JSON ファイルに保存する。"""
        self._file.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(r) for r in self._records]
        with self._file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        logger.debug("Stats saved: %d record(s).", len(self._records))

    def _load(self) -> None:
        """JSON ファイルから記録を読み込む。

        旧形式 (market_regime / detection_rel_strength なし) も読めるよう
        setdefault で欠落フィールドを埋める。
        """
        if not self._file.exists():
            logger.debug("No stats file found. Starting fresh.")
            return
        try:
            with self._file.open(encoding="utf-8") as f:
                data = json.load(f)
            records: list[TradeRecord] = []
            for entry in data:
                entry.setdefault("market_regime", "UNKNOWN")
                entry.setdefault("detection_rel_strength", 0.0)
                entry.setdefault("live_tier", "")
                entry.setdefault("live_direction", "")
                entry.setdefault("live_entry_style", "")
                entry.setdefault("live_boosters", [])
                entry.setdefault("live_score", 0.0)
                records.append(TradeRecord(**entry))
            self._records = records
            logger.info("Loaded %d trade record(s) from stats file.", len(self._records))
        except Exception as e:
            logger.warning("Failed to load stats file: %s", e)
            self._records = []

    def _load_meta(self) -> None:
        """stats_meta.json からサーキットブレーカーのリセット時刻を読む。"""
        if not self._meta_file.exists():
            return
        try:
            with self._meta_file.open(encoding="utf-8") as f:
                data = json.load(f)
            self._cb_reset_at = data.get("cb_reset_at") or None
            if self._cb_reset_at:
                logger.info(
                    "Circuit breaker reset active since %s.", self._cb_reset_at,
                )
        except Exception as e:
            logger.warning("Failed to load stats meta file: %s", e)

    def _save_meta(self) -> None:
        self._meta_file.parent.mkdir(parents=True, exist_ok=True)
        payload = {"cb_reset_at": self._cb_reset_at}
        with self._meta_file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
