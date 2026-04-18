"""
tools/show_balance.py
MEXC USDT-M 先物口座の残高表示ユーティリティ

実行方法:
    # 1) ローカル: .env に MEXC_API_KEY / MEXC_SECRET_KEY を書いて
    python tools/show_balance.py

    # 2) GitHub Actions: workflow_dispatch で .github/workflows/show_balance.yml
    #    を起動するとログに同じ内容が出力される

出力:
    - 総資産 (USDT 換算)
    - 利用可能残高 / 拘束中証拠金
    - 含み損益 (uPnL)
    - 保有中ポジション一覧 (シンボル / サイズ / エントリー / マーク価格 / uPnL)

注:
    - Read-only API キーで取得可能 (Trade 権限不要)
    - LiveExecutor 実装後はこの関数を起点にポジションサイズを決定する
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

_root = Path(__file__).parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from utils.mexc_client import MEXCClient


def _safe_float(v: Any, default: float = 0.0) -> float:
    try:
        return float(v) if v is not None else default
    except (TypeError, ValueError):
        return default


def fetch_account_overview() -> dict[str, Any]:
    """USDT-M 先物口座の残高情報を構造化して返す。"""
    client = MEXCClient()

    if not (os.getenv("MEXC_API_KEY") and os.getenv("MEXC_SECRET_KEY")):
        raise RuntimeError(
            "MEXC_API_KEY / MEXC_SECRET_KEY が設定されていません。"
            ".env か GitHub Actions secrets に登録してください。"
        )

    balance = client.fetch_balance()

    usdt_info = balance.get("USDT", {}) or {}
    total = _safe_float(usdt_info.get("total"))
    free  = _safe_float(usdt_info.get("free"))
    used  = _safe_float(usdt_info.get("used"))

    # 含み損益はポジションから集計 (ccxt の info に依存しない)
    positions: list[dict[str, Any]] = []
    upnl_total: float = 0.0
    try:
        raw_positions = client.exchange.fetch_positions()
        for p in raw_positions:
            contracts = _safe_float(p.get("contracts"))
            if contracts == 0:
                continue
            upnl = _safe_float(p.get("unrealizedPnl"))
            upnl_total += upnl
            positions.append({
                "symbol":   p.get("symbol"),
                "side":     p.get("side"),
                "contracts": contracts,
                "notional": _safe_float(p.get("notional")),
                "entry":    _safe_float(p.get("entryPrice")),
                "mark":     _safe_float(p.get("markPrice")),
                "leverage": _safe_float(p.get("leverage")),
                "upnl":     upnl,
                "upnl_pct": _safe_float(p.get("percentage")),
            })
    except Exception as e:
        # ポジション取得失敗 ≠ 残高取得失敗。残高だけは返す
        positions = [{"error": f"failed to fetch positions: {e}"}]

    return {
        "total_usdt":      total,
        "free_usdt":       free,
        "used_usdt":       used,
        "unrealized_pnl":  upnl_total,
        "positions":       positions,
    }


def print_overview(overview: dict[str, Any]) -> None:
    sep = "=" * 60
    print(sep)
    print("  MEXC USDT-M 先物口座サマリー")
    print(sep)
    print(f"  総資産         : ${overview['total_usdt']:>12,.2f} USDT")
    print(f"  利用可能       : ${overview['free_usdt']:>12,.2f} USDT")
    print(f"  証拠金 (拘束中): ${overview['used_usdt']:>12,.2f} USDT")
    upnl = overview["unrealized_pnl"]
    sign = "+" if upnl >= 0 else ""
    print(f"  含み損益 (uPnL): {sign}${upnl:>11,.2f} USDT")
    print()

    positions = overview["positions"]
    if not positions:
        print("  保有ポジション : なし")
        print(sep)
        return

    print(f"  保有ポジション : {len(positions)} 件")
    print(f"  {'SYMBOL':<24} {'SIDE':<6} {'SIZE':>10} {'ENTRY':>12} {'MARK':>12} {'uPnL':>10}")
    print("  " + "-" * 76)
    for p in positions:
        if "error" in p:
            print(f"  [WARN] {p['error']}")
            continue
        upnl_p = p["upnl"]
        upnl_s = f"{'+' if upnl_p >= 0 else ''}${upnl_p:.2f}"
        print(
            f"  {str(p['symbol']):<24} "
            f"{str(p['side']):<6} "
            f"{p['contracts']:>10.4f} "
            f"${p['entry']:>11.6g} "
            f"${p['mark']:>11.6g} "
            f"{upnl_s:>10}"
        )
    print(sep)


def main() -> int:
    # GitHub Actions では .env が存在しないので load_dotenv はスキップ可
    try:
        from dotenv import load_dotenv
        env_path = _root / ".env"
        if env_path.exists():
            load_dotenv(env_path)
    except ImportError:
        pass

    try:
        overview = fetch_account_overview()
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1

    print_overview(overview)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
