# Decision Report

- generated_at: 2026-06-13T11:12:13.861152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6576**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6576, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.04% | **+0.36%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.13% | **+0.11%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_ATR | 19/20 | 95.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.50% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.50% | **+1.50%** |
| ASK_LONG | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.34% | **+1.00%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.68% | **+0.50%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.34% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1449件 (Win 389 / Loss 464 / Flat 596) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NOT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T11:12:11.036084+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63880.5
- Funnel: target 770 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +62.29% | $5,320,774.69 |
| RIF/USDT:USDT | +28.24% | $3,048,642.78 |
| VVV/USDT:USDT | +19.20% | $6,916,239.27 |
| COAI/USDT:USDT | +18.42% | $5,006,665.91 |
| NOT/USDT:USDT | +16.86% | $1,839,661.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.69% | +3.58% |
| COAI/USDT:USDT | below_1h_threshold | +2.06% | +1.95% |
| ZBT/USDT:USDT | below_1h_threshold | +1.04% | +0.93% |
| VVV/USDT:USDT | below_1h_threshold | +1.03% | +0.93% |
| SQD/USDT:USDT | below_1h_threshold | +0.90% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
