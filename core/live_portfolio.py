"""
core/live_portfolio.py
ライブ戦略用バーチャルポートフォリオ ($100 スタート)

目的:
    core/live_filter.py + core/live_strategy.py が実トレードで何をするか、
    を DRY RUN 中から $100 の仮想資金で追跡する。戦略パラメーター
    (LIVE_BASE_RISK_PCT / LIVE_MAX_LEVERAGE 等) は環境変数から毎回読み込む
    ため、AI が戦略を書き換えれば以降の仮想トレードに即反映される。

動作:
    1. サイクルごとに stats.record_many() で確定した TradeRecord 群を受け取る
    2. 各 record の SL%・PnL% から、現在残高に対して名目ポジションを算出
       risk_usdt  = balance × LIVE_BASE_RISK_PCT%
       notional   = risk_usdt / (sl_pct / 100)
       notional  ≤ balance × LIVE_MAX_LEVERAGE
       pnl_usdt   = notional × pnl_pct / 100
                   (ただし損失は risk_usdt を超えない = 清算保護)
    3. 残高を更新して data/live_portfolio.json に追記保存
    4. データは履歴として保持 (過去分析に利用)
    5. 各 trade には検出時に下した判断 (tier / direction / entry_style /
       boosters / score) も保存され、後で「どの戦略で勝った/負けた」を
       追跡できる。

trade レコード例:
    {
      "symbol": "BTC/USDT", ...
      "pnl_usdt": -0.50, "balance_after": 99.50,
      "strategy_tier":         "S",
      "strategy_direction":    "short",
      "strategy_entry_style":  "MARKET",
      "strategy_boosters":     ["FR≥0.10", "daily_RED"],
      "strategy_score":        0.45
    }

リセット:
    LivePortfolio.reset() を呼ぶか data/live_portfolio.json を削除すれば
    再度 $100 から始まる。
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from core.stats import TradeRecord
from core.tracker import OUTCOME_EXPIRED, OUTCOME_SL_HIT, OUTCOME_TP_HIT

logger = logging.getLogger(__name__)

LIVE_PORTFOLIO_FILE = Path("data/live_portfolio.json")


def _initial_capital() -> float:
    return float(os.getenv("LIVE_VIRTUAL_CAPITAL", "100"))


@dataclass
class LiveVirtualTrade:
    """仮想ポートフォリオに反映した 1 件の確定トレード。"""

    symbol: str
    detected_at: str
    closed_at: str
    outcome: str             # TP_HIT / SL_HIT / EXPIRED
    pnl_pct: float           # ショート視点の損益率
    sl_pct: float            # ポジションサイズ計算に使った SL 幅
    risk_pct: float          # 適用したリスク比率
    notional_usdt: float     # 名目ポジションサイズ
    pnl_usdt: float          # ドル建て損益
    balance_before: float
    balance_after: float
    # ライブ戦略のスナップショット (どの戦略でこのトレードが行われたか)
    strategy_tier: str = ""              # S / A / B
    strategy_direction: str = ""         # short / long
    strategy_entry_style: str = ""       # MARKET / LIMIT_SCALE / LIMIT_PATIENT
    strategy_boosters: list[str] = field(default_factory=list)
    strategy_score: float = 0.0


@dataclass
class LivePortfolioState:
    initial_capital: float = field(default_factory=_initial_capital)
    balance: float = field(default_factory=_initial_capital)
    started_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    trades: list[LiveVirtualTrade] = field(default_factory=list)


class LivePortfolio:
    """ライブ戦略の仮想損益を $100 から追跡する。"""

    def __init__(self, file_path: Path = LIVE_PORTFOLIO_FILE) -> None:
        self._file = file_path
        # パラメーターは毎回 env から (AI による戦略変更を即反映)
        self._base_risk_pct: float = float(os.getenv("LIVE_BASE_RISK_PCT", "0.5"))
        self._max_risk_pct:  float = float(os.getenv("LIVE_MAX_RISK_PCT",  "1.5"))
        self._max_leverage:  float = float(os.getenv("LIVE_MAX_LEVERAGE",  "3.0"))
        self._state = self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def balance(self) -> float:
        return self._state.balance

    @property
    def initial_capital(self) -> float:
        return self._state.initial_capital

    @property
    def return_pct(self) -> float:
        base = self._state.initial_capital
        return (self._state.balance - base) / base * 100 if base > 0 else 0.0

    @property
    def trades(self) -> list[LiveVirtualTrade]:
        return list(self._state.trades)

    def record_many(self, records: list[TradeRecord]) -> list[LiveVirtualTrade]:
        """クローズした TradeRecord を仮想残高に適用する。"""
        applied: list[LiveVirtualTrade] = []
        for r in records:
            if r.outcome not in (OUTCOME_TP_HIT, OUTCOME_SL_HIT, OUTCOME_EXPIRED):
                continue
            # 既に記録済みなら二重計上しない (closed_at + symbol で識別)
            if any(
                t.symbol == r.symbol and t.closed_at == r.closed_at
                for t in self._state.trades
            ):
                continue
            vt = self._apply(r)
            if vt is not None:
                applied.append(vt)
        if applied:
            self.save()
        return applied

    def reset(self) -> None:
        """残高と履歴を初期状態に戻す。"""
        self._state = LivePortfolioState()
        self.save()

    def save(self) -> None:
        self._file.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "initial_capital": self._state.initial_capital,
            "balance":         self._state.balance,
            "started_at":      self._state.started_at,
            "trades":          [asdict(t) for t in self._state.trades],
        }
        with self._file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        logger.debug(
            "LivePortfolio saved: balance=$%.2f trades=%d",
            self._state.balance, len(self._state.trades),
        )

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _apply(self, r: TradeRecord) -> LiveVirtualTrade | None:
        if r.entry_price <= 0 or r.sl_price <= 0:
            return None
        sl_pct = abs(r.sl_price - r.entry_price) / r.entry_price * 100
        if sl_pct <= 0:
            return None

        balance_before = self._state.balance
        if balance_before <= 0:
            # 破産後は新規トレードを記録しない
            return None

        risk_pct    = min(self._base_risk_pct, self._max_risk_pct)
        risk_usdt   = balance_before * risk_pct / 100
        notional    = risk_usdt / (sl_pct / 100)
        notional   = min(notional, balance_before * self._max_leverage)

        pnl_usdt = notional * r.pnl_pct / 100
        # 清算保護: 1 トレードの損失はマージン (risk_usdt) を超えない
        if pnl_usdt < -risk_usdt:
            pnl_usdt = -risk_usdt
        balance_after = max(0.0, balance_before + pnl_usdt)

        vt = LiveVirtualTrade(
            symbol=r.symbol,
            detected_at=r.detected_at,
            closed_at=r.closed_at,
            outcome=r.outcome,
            pnl_pct=r.pnl_pct,
            sl_pct=sl_pct,
            risk_pct=risk_pct,
            notional_usdt=notional,
            pnl_usdt=pnl_usdt,
            balance_before=balance_before,
            balance_after=balance_after,
            strategy_tier=r.live_tier,
            strategy_direction=r.live_direction,
            strategy_entry_style=r.live_entry_style,
            strategy_boosters=list(r.live_boosters),
            strategy_score=r.live_score,
        )
        self._state.balance = balance_after
        self._state.trades.append(vt)
        logger.info(
            "LivePortfolio: %s %s pnl=%+.2f%% → $%+.2f | balance=$%.2f (%.2f%%)",
            r.symbol, r.outcome, r.pnl_pct, pnl_usdt,
            balance_after, self.return_pct,
        )
        return vt

    def _load(self) -> LivePortfolioState:
        if not self._file.exists():
            return LivePortfolioState()
        try:
            data = json.loads(self._file.read_text())
            trades: list[LiveVirtualTrade] = []
            for t in data.get("trades", []):
                t.setdefault("strategy_tier", "")
                t.setdefault("strategy_direction", "")
                t.setdefault("strategy_entry_style", "")
                t.setdefault("strategy_boosters", [])
                t.setdefault("strategy_score", 0.0)
                trades.append(LiveVirtualTrade(**t))
            default = _initial_capital()
            return LivePortfolioState(
                initial_capital=data.get("initial_capital", default),
                balance=data.get("balance", default),
                started_at=data.get(
                    "started_at", datetime.now(timezone.utc).isoformat()
                ),
                trades=trades,
            )
        except Exception as e:
            logger.warning("Failed to load live portfolio: %s", e)
            return LivePortfolioState()
