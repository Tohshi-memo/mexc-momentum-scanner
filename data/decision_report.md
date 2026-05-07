# Decision Report

- generated_at: 2026-05-07T20:37:54.231070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3695**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=3695, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/16 | 18.8% | +2.63% | **+0.49%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.29% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.21% | **+1.66%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.44% | **+0.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 67件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T20:37:47.823817+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80026.3
- Funnel: target 766 → liquid 189 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.7 >= 65=1, 4h RSI 96.3 >= 65=1, 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +35.51% | $4,964,165.24 |
| NIL/USDT:USDT | +26.80% | $11,184,362.06 |
| IRENSTOCK/USDT:USDT | +25.16% | $1,600,907.35 |
| SATO/USDT:USDT | +22.51% | $6,256,998.45 |
| DYDX/USDT:USDT | +19.31% | $8,448,560.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYDX/USDT:USDT | below_1h_threshold | +3.22% | +3.30% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +3.07% | +3.15% |
| SATO/USDT:USDT | below_1h_threshold | +2.77% | +2.85% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.58% | +2.66% |
| NOT/USDT:USDT | below_1h_threshold | +2.17% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
