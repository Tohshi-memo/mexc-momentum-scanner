# Decision Report

- generated_at: 2026-05-24T16:34:19.197915+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4829**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4829, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.02% | **+0.10%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | -0.10% | **-0.06%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.60% | **-0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.45% | **+2.45%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.57% | **+1.16%** |
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.90** / 初期 $100.00 (+22.90%)
- 確定: 635件 (Win 156 / Loss 200 / Flat 279) / skip 755件
- 成長率目線: 平均log +0.000325 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $122.90

## 4. Latest Market Context

- 更新: 2026-05-24T16:34:16.983744+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=76526.5
- Funnel: target 764 → liquid 114 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GENIUS/USDT:USDT | +2.66% | $5,966,495.18 |
| NIL/USDT:USDT | +2.60% | $7,134,658.02 |
| B2/USDT:USDT | +2.31% | $1,699,226.30 |
| MYX/USDT:USDT | +2.28% | $2,981,986.71 |
| CHIP/USDT:USDT | +1.68% | $1,224,868.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +2.61% | +2.37% |
| NIL/USDT:USDT | below_1h_threshold | +2.60% | +2.36% |
| MYX/USDT:USDT | below_1h_threshold | +2.33% | +2.09% |
| B2/USDT:USDT | below_1h_threshold | +2.32% | +2.08% |
| CHIP/USDT:USDT | below_1h_threshold | +1.69% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
