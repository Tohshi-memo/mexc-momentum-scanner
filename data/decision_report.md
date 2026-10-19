# Decision Report

- generated_at: 2026-10-19T23:21:23.684724+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17029**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17029, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.14% | **-0.05%** |
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.96% | **-0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +4.88% | **+4.88%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.31% | **+1.85%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.70% | **+1.62%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.27% | **+1.48%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,276.64** / 初期 $100.00 (+1176.64%)
- 確定: 6469件 (Win 1877 / Loss 2065 / Flat 2527) / skip 7121件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.63% 残高後 $1,276.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.64** / 初期 $100.00 (+177.64%)
- 確定: 3794件 (Win 1043 / Loss 886 / Flat 1865) / skip 6646件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0044 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $277.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5192件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T23:21:14.010664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81963.8
- Funnel: target 1090 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +29.10% | $10,706,495.81 |
| BR/USDT:USDT | +13.38% | $31,586,283.13 |
| APR/USDT:USDT | +12.19% | $1,516,767.58 |
| BTW/USDT:USDT | +12.15% | $28,327,955.07 |
| BAT/USDT:USDT | +7.13% | $6,409,388.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.48% | +2.54% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.51% |
| Q/USDT:USDT | below_1h_threshold | +1.29% | +1.36% |
| BAT/USDT:USDT | below_1h_threshold | +1.02% | +1.09% |
| WLD/USDT:USDT | below_1h_threshold | +0.93% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
