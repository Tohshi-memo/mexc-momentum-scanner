"""
core/paper_portfolio.py
ライブ Paper Trading ポートフォリオ (仮想資金による実時間トレードシミュレーション)

既存の `tools/virtual_portfolio.py` が experiments.json を事後リプレイする
レトロスペクティブ型なのに対し、こちらはスキャナー実行中にリアルタイムで
ポジションを開閉し、エクイティ曲線を蓄積する。

永続化:
    paper_state/account.json     - 残高・エクイティ・期間メタ
    paper_state/positions.json   - 建玉中のポジション一覧
    paper_state/trades.jsonl     - クローズ済みトレードログ (append-only)
    paper_state/equity.jsonl     - サイクル毎のエクイティスナップショット
    paper_state/report.md        - 人間向けサマリー (サイクル毎に再生成)

運用:
    - `mark_to_market(client)` をサイクル先頭で呼び、既存ポジションの SL/TP/
      期限切れを判定する
    - `try_open(...)` を confirmed シグナルごとに呼ぶ。方向/戦略は
      tools.strategy_selector.select_leaders() 由来のチャンピオンを使う
    - `snapshot()` をサイクル終盤で呼び equity.jsonl に追記
    - `save()` で account.json / positions.json / report.md を書き出す

想定リスク管理 (env):
    PAPER_INITIAL_BALANCE (default 100)   - 初期残高 (USDT)
    PAPER_RISK_PCT        (default 1.0)   - 1 トレードあたりリスク% (残高比)
    PAPER_MAX_CONCURRENT  (default 3)     - 同時建玉上限
    PAPER_LEVERAGE        (default 5)     - レバレッジ (証拠金計算用)
    PAPER_FEE_PCT         (default 0.04)  - Taker 手数料 (片側, %)
    PAPER_SLIPPAGE_PCT    (default 0.05)  - スリッページ想定 (片側, %)
    PAPER_MIN_NOTIONAL    (default 5.0)   - 取引所最小 notional (USDT)
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from utils.mexc_client import MEXCClient

logger = logging.getLogger(__name__)

STATE_DIR     = Path("paper_state")
ACCOUNT_FILE  = STATE_DIR / "account.json"
POSITIONS_FILE = STATE_DIR / "positions.json"
TRADES_FILE   = STATE_DIR / "trades.jsonl"
EQUITY_FILE   = STATE_DIR / "equity.jsonl"
REPORT_FILE   = STATE_DIR / "report.md"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class PaperPosition:
    """建玉中のポジション。"""
    position_id: str
    symbol: str
    direction: str            # "long" | "short"
    strategy: str             # champion strategy name (e.g. "LIMIT_5PCT")
    entry_price: float        # フィル想定価格 (slippage 込み)
    sl_price: float
    tp_price: float
    qty: float                # ベース通貨数量
    notional: float           # entry_price * qty (USDT)
    margin: float             # notional / leverage (USDT)
    leverage: float
    risk_amount: float        # 想定最大損失額 (USDT)
    opened_at: str            # ISO 8601
    expires_at: str           # ISO 8601 (強制クローズ)
    detection_price: float    # シグナル発生時のマーケット価格
    market_regime: str = "UNKNOWN"
    rsi_at_entry: float | None = None
    current_price: float = 0.0
    unrealized_pnl: float = 0.0

    def mark(self, price: float) -> None:
        """現在価格で unrealized PnL を再計算する。"""
        self.current_price = price
        if self.direction == "long":
            self.unrealized_pnl = (price - self.entry_price) * self.qty
        else:
            self.unrealized_pnl = (self.entry_price - price) * self.qty


@dataclass
class ClosedTrade:
    """クローズ済みトレード記録。trades.jsonl に追記する。"""
    position_id: str
    symbol: str
    direction: str
    strategy: str
    entry_price: float
    exit_price: float
    sl_price: float
    tp_price: float
    qty: float
    notional: float
    leverage: float
    margin: float
    risk_amount: float
    realized_pnl: float       # fee 差し引き後の net PnL (USDT)
    gross_pnl: float          # fee 差し引き前
    fees: float
    pnl_pct_on_equity: float  # 残高に対する寄与 (%)
    opened_at: str
    closed_at: str
    outcome: str              # "TP" | "SL" | "EXPIRED"
    market_regime: str = "UNKNOWN"


# ---------------------------------------------------------------------------
# PaperPortfolio
# ---------------------------------------------------------------------------

class PaperPortfolio:
    """仮想資金によるライブ paper trading ポートフォリオ。"""

    def __init__(self) -> None:
        self._initial_balance: float = float(os.getenv("PAPER_INITIAL_BALANCE", "100"))
        self._risk_pct:        float = float(os.getenv("PAPER_RISK_PCT", "1.0"))
        self._max_concurrent:  int   = int(os.getenv("PAPER_MAX_CONCURRENT", "3"))
        self._leverage:        float = float(os.getenv("PAPER_LEVERAGE", "5"))
        self._fee_pct:         float = float(os.getenv("PAPER_FEE_PCT", "0.04"))
        self._slippage_pct:    float = float(os.getenv("PAPER_SLIPPAGE_PCT", "0.05"))
        self._min_notional:    float = float(os.getenv("PAPER_MIN_NOTIONAL", "5.0"))
        self._tracking_hours:  int   = int(os.getenv("TRACKING_HOURS", "24"))

        self.balance:       float = self._initial_balance
        self.started_at:    str   = datetime.now(timezone.utc).isoformat()
        self.positions:     dict[str, PaperPosition] = {}
        self.trade_count:   int   = 0
        self.win_count:     int   = 0
        self.loss_count:    int   = 0

        self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def equity(self) -> float:
        """残高 + 全建玉の含み損益。"""
        return self.balance + sum(p.unrealized_pnl for p in self.positions.values())

    @property
    def used_margin(self) -> float:
        return sum(p.margin for p in self.positions.values())

    @property
    def free_balance(self) -> float:
        return self.balance - self.used_margin

    def has_capacity(self) -> bool:
        return len(self.positions) < self._max_concurrent

    def is_open(self, symbol: str) -> bool:
        return any(p.symbol == symbol for p in self.positions.values())

    def try_open(
        self,
        *,
        symbol: str,
        direction: str,          # "long" | "short"
        strategy: str,
        detection_price: float,
        sl_pct: float,           # 常に正の値 (%)
        tp_pct: float,           # 常に正の値 (%)
        entry_offset_pct: float = 0.0,  # detection に対する指値オフセット
        market_regime: str = "UNKNOWN",
        rsi_at_entry: float | None = None,
    ) -> PaperPosition | None:
        """新規ポジションを開く (可能なら)。

        Returns:
            PaperPosition on success, None if skipped (capacity/dup/size).
        """
        if direction not in ("long", "short"):
            logger.warning("paper: invalid direction=%s for %s", direction, symbol)
            return None
        if sl_pct <= 0 or tp_pct <= 0:
            return None
        if not self.has_capacity():
            logger.info("paper: skip %s (max concurrent %d)", symbol, self._max_concurrent)
            return None
        if self.is_open(symbol):
            logger.info("paper: skip %s (already open)", symbol)
            return None

        # エントリー参考価格 (指値オフセット)
        ref_price = detection_price * (1 + entry_offset_pct / 100.0)

        # スリッページ: LONG は不利=上, SHORT は不利=下
        if direction == "long":
            fill_price = ref_price * (1 + self._slippage_pct / 100.0)
        else:
            fill_price = ref_price * (1 - self._slippage_pct / 100.0)
        if fill_price <= 0:
            return None

        # リスク額 → ノーショナル → 数量
        risk_amount = self.balance * self._risk_pct / 100.0
        if risk_amount <= 0:
            logger.warning("paper: non-positive risk amount (balance=%.4f)", self.balance)
            return None
        # sl_pct は fill 価格に対して想定 (offset 後の価格ベース)
        notional = risk_amount / (sl_pct / 100.0)

        # margin = notional / leverage (free balance 内に収まるか)
        margin = notional / self._leverage
        if margin > self.free_balance:
            # 証拠金不足 → free_balance で賄える最大ノーショナルに縮退
            notional = self.free_balance * self._leverage
            margin = notional / self._leverage
        if notional < self._min_notional:
            logger.info(
                "paper: skip %s (notional %.3f < min %.3f)",
                symbol, notional, self._min_notional,
            )
            return None

        qty = notional / fill_price
        if qty <= 0:
            return None

        # SL/TP: fill_price を基準に sl_pct/tp_pct で再計算
        if direction == "long":
            sl_price = fill_price * (1 - sl_pct / 100.0)
            tp_price = fill_price * (1 + tp_pct / 100.0)
        else:
            sl_price = fill_price * (1 + sl_pct / 100.0)
            tp_price = fill_price * (1 - tp_pct / 100.0)

        now = datetime.now(timezone.utc)
        expires = now + timedelta(hours=self._tracking_hours)
        position_id = f"{symbol}-{direction}-{int(now.timestamp())}"

        pos = PaperPosition(
            position_id=position_id,
            symbol=symbol,
            direction=direction,
            strategy=strategy,
            entry_price=fill_price,
            sl_price=sl_price,
            tp_price=tp_price,
            qty=qty,
            notional=notional,
            margin=margin,
            leverage=self._leverage,
            risk_amount=risk_amount,
            opened_at=now.isoformat(),
            expires_at=expires.isoformat(),
            detection_price=detection_price,
            market_regime=market_regime,
            rsi_at_entry=rsi_at_entry,
            current_price=fill_price,
            unrealized_pnl=0.0,
        )
        self.positions[position_id] = pos
        logger.info(
            "paper: OPEN %s %s %s | entry=%.8g sl=%.8g tp=%.8g qty=%.6f notional=%.2f margin=%.2f",
            direction.upper(), symbol, strategy,
            fill_price, sl_price, tp_price, qty, notional, margin,
        )
        return pos

    def mark_to_market(self, client: "MEXCClient") -> list[ClosedTrade]:
        """全建玉の price を 1m OHLCV で更新し、SL/TP/期限切れをクローズする。

        Returns:
            今回サイクルでクローズされたトレードのリスト。
        """
        if not self.positions:
            return []

        now = datetime.now(timezone.utc)
        now_str = now.isoformat()
        closed: list[ClosedTrade] = []

        for pos in list(self.positions.values()):
            try:
                ohlcv = client.fetch_ohlcv(pos.symbol, timeframe="1m", limit=6)
                if not ohlcv:
                    continue
                high  = max(float(c[2]) for c in ohlcv)
                low   = min(float(c[3]) for c in ohlcv)
                close = float(ohlcv[-1][4])
            except Exception as e:
                logger.debug("paper: 1m OHLCV failed for %s: %s", pos.symbol, e)
                continue

            if close <= 0:
                continue
            pos.mark(close)

            # SL/TP 判定 (direction に応じて high/low を使う)
            outcome: str | None = None
            exit_price: float | None = None
            if pos.direction == "long":
                sl_hit = low <= pos.sl_price
                tp_hit = high >= pos.tp_price
                if sl_hit and tp_hit:
                    outcome, exit_price = "SL", pos.sl_price   # 保守的
                elif tp_hit:
                    outcome, exit_price = "TP", pos.tp_price
                elif sl_hit:
                    outcome, exit_price = "SL", pos.sl_price
            else:
                sl_hit = high >= pos.sl_price
                tp_hit = low  <= pos.tp_price
                if sl_hit and tp_hit:
                    outcome, exit_price = "SL", pos.sl_price
                elif tp_hit:
                    outcome, exit_price = "TP", pos.tp_price
                elif sl_hit:
                    outcome, exit_price = "SL", pos.sl_price

            # 期限切れ
            if outcome is None:
                expires_dt = datetime.fromisoformat(pos.expires_at)
                if now >= expires_dt:
                    outcome, exit_price = "EXPIRED", close

            if outcome is None:
                continue

            closed_trade = self._close_position(pos, exit_price, outcome, now_str)
            closed.append(closed_trade)

        return closed

    def snapshot_equity(self) -> None:
        """現在のエクイティを equity.jsonl に追記する。"""
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        row = {
            "ts":             datetime.now(timezone.utc).isoformat(),
            "balance":        round(self.balance, 6),
            "equity":         round(self.equity, 6),
            "unrealized_pnl": round(self.equity - self.balance, 6),
            "open_positions": len(self.positions),
            "used_margin":    round(self.used_margin, 6),
        }
        with EQUITY_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    def save(self) -> None:
        STATE_DIR.mkdir(parents=True, exist_ok=True)

        account = {
            "started_at":      self.started_at,
            "updated_at":      datetime.now(timezone.utc).isoformat(),
            "initial_balance": self._initial_balance,
            "balance":         round(self.balance, 6),
            "equity":          round(self.equity, 6),
            "unrealized_pnl":  round(self.equity - self.balance, 6),
            "open_positions":  len(self.positions),
            "used_margin":     round(self.used_margin, 6),
            "free_balance":    round(self.free_balance, 6),
            "trade_count":     self.trade_count,
            "win_count":       self.win_count,
            "loss_count":      self.loss_count,
            "win_rate_pct":    (
                round(self.win_count / self.trade_count * 100, 2)
                if self.trade_count > 0 else 0.0
            ),
            "total_return_pct": round(
                (self.equity - self._initial_balance) / self._initial_balance * 100, 4
            ),
            "config": {
                "risk_pct":        self._risk_pct,
                "max_concurrent":  self._max_concurrent,
                "leverage":        self._leverage,
                "fee_pct":         self._fee_pct,
                "slippage_pct":    self._slippage_pct,
                "min_notional":    self._min_notional,
                "tracking_hours":  self._tracking_hours,
            },
        }
        with ACCOUNT_FILE.open("w", encoding="utf-8") as f:
            json.dump(account, f, indent=2, ensure_ascii=False)

        positions_payload = {
            pid: asdict(p) for pid, p in self.positions.items()
        }
        with POSITIONS_FILE.open("w", encoding="utf-8") as f:
            json.dump(positions_payload, f, indent=2, ensure_ascii=False)

        self._write_report(account)

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _close_position(
        self,
        pos: PaperPosition,
        exit_price: float,
        outcome: str,
        now_str: str,
    ) -> ClosedTrade:
        """SL/TP/EXPIRED でポジションをクローズし balance を更新する。"""
        # 手数料: entry + exit の両側 (taker 想定)
        fees = pos.notional * self._fee_pct / 100.0 + \
               (exit_price * pos.qty) * self._fee_pct / 100.0

        if pos.direction == "long":
            gross = (exit_price - pos.entry_price) * pos.qty
        else:
            gross = (pos.entry_price - exit_price) * pos.qty

        # 清算保護: 損失は margin を上回らない (先物の実質上限)
        if gross < 0 and abs(gross) > pos.margin:
            gross = -pos.margin

        net = gross - fees
        pnl_pct = net / self.balance * 100.0 if self.balance > 0 else 0.0

        self.balance += net
        self.trade_count += 1
        if net >= 0:
            self.win_count += 1
        else:
            self.loss_count += 1

        trade = ClosedTrade(
            position_id=pos.position_id,
            symbol=pos.symbol,
            direction=pos.direction,
            strategy=pos.strategy,
            entry_price=pos.entry_price,
            exit_price=exit_price,
            sl_price=pos.sl_price,
            tp_price=pos.tp_price,
            qty=pos.qty,
            notional=pos.notional,
            leverage=pos.leverage,
            margin=pos.margin,
            risk_amount=pos.risk_amount,
            realized_pnl=round(net, 6),
            gross_pnl=round(gross, 6),
            fees=round(fees, 6),
            pnl_pct_on_equity=round(pnl_pct, 4),
            opened_at=pos.opened_at,
            closed_at=now_str,
            market_regime=pos.market_regime,
            outcome=outcome,
        )

        STATE_DIR.mkdir(parents=True, exist_ok=True)
        with TRADES_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(trade), ensure_ascii=False) + "\n")

        logger.info(
            "paper: CLOSE %s %s %s %s | entry=%.8g exit=%.8g net=%.4f (%.3f%% of bal) bal=%.4f",
            pos.direction.upper(), outcome, pos.symbol, pos.strategy,
            pos.entry_price, exit_price, net, pnl_pct, self.balance,
        )

        del self.positions[pos.position_id]
        return trade

    def _load(self) -> None:
        if ACCOUNT_FILE.exists():
            try:
                with ACCOUNT_FILE.open(encoding="utf-8") as f:
                    data = json.load(f)
                self.balance     = float(data.get("balance", self._initial_balance))
                self.started_at  = data.get("started_at", self.started_at)
                self.trade_count = int(data.get("trade_count", 0))
                self.win_count   = int(data.get("win_count", 0))
                self.loss_count  = int(data.get("loss_count", 0))
                logger.info(
                    "paper: loaded account balance=%.4f trades=%d",
                    self.balance, self.trade_count,
                )
            except Exception as e:
                logger.warning("paper: failed to load account.json: %s", e)

        if POSITIONS_FILE.exists():
            try:
                with POSITIONS_FILE.open(encoding="utf-8") as f:
                    data = json.load(f)
                for pid, entry in data.items():
                    self.positions[pid] = PaperPosition(**entry)
                logger.info("paper: loaded %d open position(s)", len(self.positions))
            except Exception as e:
                logger.warning("paper: failed to load positions.json: %s", e)

    def _write_report(self, account: dict[str, Any]) -> None:
        recent = _tail_jsonl(TRADES_FILE, 10)
        lines: list[str] = []
        lines.append("# Paper Trading Report")
        lines.append("")
        lines.append(f"- Started: `{account['started_at']}`")
        lines.append(f"- Updated: `{account['updated_at']}`")
        lines.append(f"- Initial Balance: **${account['initial_balance']:.2f}**")
        lines.append(f"- Current Balance: **${account['balance']:.4f}**")
        lines.append(f"- Equity (incl. unrealized): **${account['equity']:.4f}**")
        lines.append(f"- Unrealized PnL: `${account['unrealized_pnl']:+.4f}`")
        lines.append(f"- Total Return: **{account['total_return_pct']:+.2f}%**")
        lines.append(
            f"- Trades: {account['trade_count']} "
            f"(W {account['win_count']} / L {account['loss_count']}, "
            f"WR {account['win_rate_pct']:.1f}%)"
        )
        lines.append(
            f"- Open Positions: {account['open_positions']} "
            f"(margin used ${account['used_margin']:.4f} / "
            f"free ${account['free_balance']:.4f})"
        )
        lines.append("")
        cfg = account["config"]
        lines.append(
            f"- Config: risk={cfg['risk_pct']}% lev={cfg['leverage']}x "
            f"max_concurrent={cfg['max_concurrent']} fee={cfg['fee_pct']}% "
            f"slippage={cfg['slippage_pct']}%"
        )
        lines.append("")

        if self.positions:
            lines.append("## Open Positions")
            lines.append("")
            lines.append("| Symbol | Dir | Strategy | Entry | SL | TP | Qty | Unreal PnL |")
            lines.append("|---|---|---|---|---|---|---|---|")
            for p in self.positions.values():
                lines.append(
                    f"| {p.symbol} | {p.direction.upper()} | {p.strategy} "
                    f"| {p.entry_price:.8g} | {p.sl_price:.8g} | {p.tp_price:.8g} "
                    f"| {p.qty:.6g} | {p.unrealized_pnl:+.4f} |"
                )
            lines.append("")

        if recent:
            lines.append("## Recent Closed Trades (last 10)")
            lines.append("")
            lines.append("| Closed | Symbol | Dir | Strategy | Outcome | Net PnL | % of bal |")
            lines.append("|---|---|---|---|---|---|---|")
            for t in recent:
                lines.append(
                    f"| {t.get('closed_at','')[:19]} | {t.get('symbol','')} "
                    f"| {t.get('direction','').upper()} | {t.get('strategy','')} "
                    f"| {t.get('outcome','')} | {t.get('realized_pnl',0):+.4f} "
                    f"| {t.get('pnl_pct_on_equity',0):+.3f}% |"
                )
            lines.append("")

        REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _tail_jsonl(path: Path, n: int) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        with path.open(encoding="utf-8") as f:
            rows = [json.loads(line) for line in f if line.strip()]
    except Exception:
        return []
    return rows[-n:][::-1]
