# Decision Report

- generated_at: 2026-06-04T22:08:18.898366+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5673**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5673, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/15 | 20.0% | +2.12% | **+0.42%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.32% | **+0.27%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.22% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.22% | **+1.45%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.62% | **+1.31%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.88% | **+1.15%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$98.05** / 初期 $100.00 (-1.95%)
- 確定トレード: 99件 (TP 30 / SL 66 / EXP 3)
- 最新: MONAD/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1008件 (Win 239 / Loss 312 / Flat 457) / skip 1226件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T22:08:16.405351+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63212.2
- Funnel: target 770 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +38.25% | $6,388,175.31 |
| OPN/USDT:USDT | +28.93% | $37,843,362.23 |
| AAOISTOCK/USDT:USDT | +10.68% | $1,193,175.50 |
| HOME/USDT:USDT | +9.75% | $5,234,376.10 |
| XMR/USDT:USDT | +8.19% | $9,540,915.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XMR/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |
| BEAT/USDT:USDT | below_1h_threshold | +1.46% | +1.51% |
| HOME/USDT:USDT | below_1h_threshold | +0.91% | +0.96% |
| BTW/USDT:USDT | below_1h_threshold | +0.87% | +0.93% |
| MYX/USDT:USDT | below_1h_threshold | +0.87% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
