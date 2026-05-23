# Decision Report

- generated_at: 2026-05-23T18:09:16.299878+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4794**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4794, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.64% | **+0.06%** |
| LIMIT_BB3S | 3/20 | 15.0% | +0.23% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.36% | **+2.13%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.45% | **+1.84%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.76% | **+1.66%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 739件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T18:09:14.212832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=75519.6
- Funnel: target 764 → liquid 117 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ME/USDT:USDT | +10.68% | $1,248,524.42 |
| BILL/USDT:USDT | +10.61% | $18,287,588.61 |
| UB/USDT:USDT | +7.24% | $1,994,973.41 |
| WLD/USDT:USDT | +5.27% | $42,144,302.13 |
| EIGEN/USDT:USDT | +4.01% | $2,157,776.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ME/USDT:USDT | below_1h_threshold | +1.49% | +1.41% |
| WLD/USDT:USDT | below_1h_threshold | +1.23% | +1.14% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.94% | +0.86% |
| BILL/USDT:USDT | below_1h_threshold | +0.87% | +0.79% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.70% | +0.62% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
