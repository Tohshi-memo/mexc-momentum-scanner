# Decision Report

- generated_at: 2026-05-13T22:38:03.126991+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4256**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4256, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.01% | **+0.01%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.28% | **-0.16%** |
| LIMIT_1PCT | 17/20 | 85.0% | -0.25% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.42% | **+1.06%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.13% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$97.70** / 初期 $100.00 (-2.30%)
- 確定トレード: 40件 (TP 10 / SL 27 / EXP 3)
- 最新: IRYS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 475件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T22:37:59.932040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=79237.2
- Funnel: target 759 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +24.30% | $1,604,801.28 |
| CSCOSTOCK/USDT:USDT | +19.21% | $3,866,302.01 |
| UP/USDT:USDT | +16.47% | $4,795,358.32 |
| AIN/USDT:USDT | +12.86% | $2,275,379.61 |
| IRYS/USDT:USDT | +12.42% | $5,691,107.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.90% | +4.06% |
| SAGA/USDT:USDT | below_1h_threshold | +2.33% | +2.49% |
| JCT/USDT:USDT | below_1h_threshold | +1.99% | +2.15% |
| ROSE/USDT:USDT | below_1h_threshold | +1.81% | +1.97% |
| BB/USDT:USDT | below_1h_threshold | +1.73% | +1.89% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
