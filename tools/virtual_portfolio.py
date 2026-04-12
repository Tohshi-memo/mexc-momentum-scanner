"""
tools/virtual_portfolio.py
バーチャル資金シミュレーター

experiments.json に蓄積された確定済みシャドウトレードを時系列で再生し、
複数のレバレッジレベルで仮想的な損益を計算する。

使い方:
    python tools/virtual_portfolio.py          # 現在の損益を表示
    python tools/virtual_portfolio.py --show   # 同上 (明示的)
    python tools/virtual_portfolio.py --reset  # 資金をリセットしてタイムスタンプを更新

設計:
    - 初期資金: VIRTUAL_CAPITAL 環境変数 (デフォルト $100)
    - 1トレードあたりのマージン: 残高 × VIRTUAL_RISK_PCT% (デフォルト 10%)
    - レバレッジ: LEVERAGE_LEVELS (デフォルト [1, 2, 5, 10, 20])
    - 損失上限: マージン全額 (清算でそれ以上の損は出ない)
    - リセット: --reset フラグで reset_at タイムスタンプを更新。
                以降は reset_at 以後に検出されたトレードのみ対象。
    - 戦略別: experiments.json の各 entry_variants の pnl_pct を使用
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# プロジェクトルートを sys.path に追加 (直接実行時)
_root = Path(__file__).parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

EXPERIMENT_FILE = Path("data/experiments.json")
PORTFOLIO_FILE  = Path("data/portfolio.json")

INITIAL_CAPITAL: float = float(os.getenv("VIRTUAL_CAPITAL", "100"))
RISK_PCT:        float = float(os.getenv("VIRTUAL_RISK_PCT", "10"))
LEVERAGE_LEVELS: list[int] = [1, 2, 5, 10, 20]

# シミュレーション対象戦略 (order matters for display)
STRATEGIES = [
    "MARKET",
    "ASK",
    "LIMIT_1PCT",
    "LIMIT_2PCT",
    "LIMIT_BB3S",
    "LIMIT_ATR",
    "LIMIT_FIB1272",
    "LIMIT_FIB1618",
]


# ---------------------------------------------------------------------------
# データ構造
# ---------------------------------------------------------------------------

@dataclass
class TradeResult:
    """再生用のシンプルなトレード結果。"""
    symbol: str
    detected_at: str        # ISO 8601 (ソート用)
    strategy: str
    pnl_pct: float          # 確定 PnL (%)
    outcome: str            # TP_HIT / SL_HIT / EXPIRED


@dataclass
class LeverageStats:
    """1レバレッジレベルの累積統計。"""
    leverage: int
    balance: float          # 現在の残高
    initial: float          # 初期残高
    trades: int = 0
    wins: int = 0
    losses: int = 0
    total_pnl_usd: float = 0.0
    max_balance: float = 0.0
    min_balance: float = 0.0
    liquidated: bool = False  # 残高がゼロ以下になったか

    def __post_init__(self) -> None:
        self.max_balance = self.balance
        self.min_balance = self.balance

    @property
    def win_rate(self) -> float:
        return self.wins / self.trades * 100 if self.trades > 0 else 0.0

    @property
    def return_pct(self) -> float:
        return (self.balance - self.initial) / self.initial * 100 if self.initial > 0 else 0.0

    @property
    def max_drawdown_pct(self) -> float:
        """最大ドローダウン (最大残高からの最大下落 %)。"""
        if self.max_balance <= 0:
            return 0.0
        return (self.max_balance - self.min_balance) / self.max_balance * 100


@dataclass
class PortfolioState:
    """portfolio.json に永続化するステート。"""
    reset_at: str | None = None      # リセットタイムスタンプ (この以後のトレードのみ対象)
    initial_capital: float = INITIAL_CAPITAL
    risk_pct: float = RISK_PCT

    @classmethod
    def load(cls, path: Path) -> "PortfolioState":
        if path.exists():
            try:
                data = json.loads(path.read_text())
                return cls(
                    reset_at=data.get("reset_at"),
                    initial_capital=data.get("initial_capital", INITIAL_CAPITAL),
                    risk_pct=data.get("risk_pct", RISK_PCT),
                )
            except Exception:
                pass
        return cls()

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        data: dict[str, Any] = {
            "reset_at": self.reset_at,
            "initial_capital": self.initial_capital,
            "risk_pct": self.risk_pct,
        }
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# コア: トレード抽出
# ---------------------------------------------------------------------------

def _load_closed_trades(exp_path: Path) -> list[dict]:
    """experiments.json から closed リストを返す。"""
    if not exp_path.exists():
        return []
    try:
        data = json.loads(exp_path.read_text())
        return data.get("closed", [])
    except Exception:
        return []


def _extract_results(
    closed: list[dict],
    reset_at: str | None,
    strategy: str,
) -> list[TradeResult]:
    """指定戦略の確定済みトレードを時系列順で返す。

    - reset_at が設定されていれば、それ以後の detected_at のみ対象
    - filled=True かつ pnl_pct が数値のバリアントのみ
    """
    results: list[TradeResult] = []

    for trade in closed:
        detected = trade.get("detected_at", "")
        if reset_at and detected <= reset_at:
            continue

        variants = trade.get("entry_variants") or []
        for v in variants:
            if v.get("strategy") != strategy:
                continue
            if not v.get("filled", False):
                continue
            pnl = v.get("pnl_pct")
            if pnl is None:
                continue
            outcome = v.get("outcome", "UNKNOWN")
            if outcome not in ("TP_HIT", "SL_HIT", "EXPIRED"):
                continue
            results.append(TradeResult(
                symbol=trade.get("symbol", "?"),
                detected_at=detected,
                strategy=strategy,
                pnl_pct=float(pnl),
                outcome=outcome,
            ))
            break  # 同トレードの同戦略は1件のみ

    results.sort(key=lambda r: r.detected_at)
    return results


# ---------------------------------------------------------------------------
# コア: シミュレーション
# ---------------------------------------------------------------------------

def _simulate(
    trades: list[TradeResult],
    initial: float,
    risk_pct: float,
    leverage: int,
) -> LeverageStats:
    """トレードリストをバランス更新しながら再生する。"""
    stats = LeverageStats(
        leverage=leverage,
        balance=initial,
        initial=initial,
    )

    for trade in trades:
        if stats.balance <= 0:
            stats.liquidated = True
            break

        # マージン = 現在残高 × リスク%
        margin = stats.balance * risk_pct / 100

        # PnL 計算: ショートなので pnl_pct が正なら利益
        pnl_usd = margin * leverage * trade.pnl_pct / 100

        # 清算保護: 損失はマージン以上にはならない
        if pnl_usd < -margin:
            pnl_usd = -margin

        stats.balance += pnl_usd
        stats.total_pnl_usd += pnl_usd
        stats.trades += 1
        if pnl_usd > 0:
            stats.wins += 1
        else:
            stats.losses += 1

        # 残高トラッキング
        if stats.balance > stats.max_balance:
            stats.max_balance = stats.balance
        if stats.balance < stats.min_balance:
            stats.min_balance = stats.balance

    return stats


# ---------------------------------------------------------------------------
# メイン: run_simulation
# ---------------------------------------------------------------------------

def run_simulation(state: PortfolioState) -> dict[str, list[LeverageStats]]:
    """全戦略 × 全レバレッジの結果を返す。

    Returns:
        {"MARKET": [LeverageStats(lev=1), ...], "ASK": [...], ...}
    """
    closed = _load_closed_trades(EXPERIMENT_FILE)
    results: dict[str, list[LeverageStats]] = {}

    for strategy in STRATEGIES:
        trades = _extract_results(closed, state.reset_at, strategy)
        if not trades:
            continue
        lev_stats: list[LeverageStats] = []
        for lev in LEVERAGE_LEVELS:
            s = _simulate(trades, state.initial_capital, state.risk_pct, lev)
            lev_stats.append(s)
        results[strategy] = lev_stats

    return results


# ---------------------------------------------------------------------------
# 表示
# ---------------------------------------------------------------------------

def _fmt_usd(v: float) -> str:
    sign = "+" if v >= 0 else ""
    return f"{sign}${v:.2f}"


def _fmt_pct(v: float) -> str:
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:.1f}%"


def print_report(
    state: PortfolioState,
    results: dict[str, list[LeverageStats]],
) -> None:
    """シミュレーション結果をコンソールに表示する。"""
    sep = "=" * 80

    print(sep)
    print("  バーチャルポートフォリオ シミュレーション")
    print(sep)
    print(f"  初期資金   : ${state.initial_capital:.2f}")
    print(f"  1トレードリスク: {state.risk_pct:.0f}% of balance")
    if state.reset_at:
        print(f"  リセット日時 : {state.reset_at}")
    else:
        print("  リセット日時 : (全期間)")
    print()

    if not results:
        print("  確定済みトレードがありません。データが蓄積されるまでお待ちください。")
        print(sep)
        return

    for strategy, lev_list in results.items():
        n_trades = lev_list[0].trades if lev_list else 0
        if n_trades == 0:
            continue
        wins = lev_list[0].wins
        wr = lev_list[0].win_rate
        print(f"  ■ 戦略: {strategy}  ({n_trades}件, 勝率 {wr:.0f}%  TP:{wins} / SL/EXP:{n_trades - wins})")
        print(f"  {'Leverage':>10}  {'残高':>10}  {'損益':>12}  {'リターン':>10}  {'最大DD':>10}  {'状態':>6}")
        print("  " + "-" * 64)

        for s in lev_list:
            status = "BUST" if s.liquidated else "OK"
            print(
                f"  {s.leverage:>9}x"
                f"  {f'${s.balance:.2f}':>10}"
                f"  {_fmt_usd(s.total_pnl_usd):>12}"
                f"  {_fmt_pct(s.return_pct):>10}"
                f"  {f'-{s.max_drawdown_pct:.1f}%':>10}"
                f"  {status:>6}"
            )
        print()

    print(sep)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="バーチャルポートフォリオ シミュレーター"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="資金をリセット: 現在のUTC時刻を reset_at に書き込み、以降のトレードのみ集計対象にする",
    )
    parser.add_argument(
        "--show",
        action="store_true",
        help="現在の損益を表示 (デフォルト動作と同じ)",
    )
    parser.add_argument(
        "--capital",
        type=float,
        default=None,
        help="初期資金をオーバーライド (ドル)",
    )
    args = parser.parse_args()

    state = PortfolioState.load(PORTFOLIO_FILE)

    if args.capital is not None:
        state.initial_capital = args.capital

    if args.reset:
        state.reset_at = datetime.now(timezone.utc).isoformat()
        state.save(PORTFOLIO_FILE)
        print(f"[RESET] バーチャル資金をリセットしました。")
        print(f"        reset_at = {state.reset_at}")
        print(f"        以降は {state.initial_capital:.0f}ドル から再計測します。")
        return

    results = run_simulation(state)
    print_report(state, results)


# ---------------------------------------------------------------------------
# main.py から呼び出せる API
# ---------------------------------------------------------------------------

def update_portfolio_report() -> None:
    """main.py の finally ブロックから呼び出す。

    portfolio.json を読み込み → シミュレーション → 結果をログ出力。
    サイレントに失敗する（スキャナー動作に影響しない）。
    """
    import logging
    _log = logging.getLogger(__name__)
    try:
        state = PortfolioState.load(PORTFOLIO_FILE)
        results = run_simulation(state)
        if not results:
            return
        # MARKET 戦略の結果をサマリーログ
        market = results.get("MARKET")
        if market:
            for s in market:
                _log.info(
                    "[Portfolio] MARKET lev=%dx  balance=$%.2f (%s)  trades=%d  wr=%.0f%%",
                    s.leverage,
                    s.balance,
                    _fmt_pct(s.return_pct),
                    s.trades,
                    s.win_rate,
                )
    except Exception as exc:
        _log.warning("Failed to update portfolio report: %s", exc)


if __name__ == "__main__":
    main()
