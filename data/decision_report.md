# Decision Report

- generated_at: 2026-11-18T00:51:22.688972+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19101, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/19 | 31.6% | +1.81% | **+0.57%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.08% | **+0.05%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.07% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.03% | **+1.06%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.93% | **+0.61%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +2.67% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.76** / 初期 $100.00 (+20.76%)
- 確定トレード: 280件 (TP 100 / SL 172 / EXP 8)
- 最新: MVLL/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7352件 (Win 2109 / Loss 2358 / Flat 2885) / skip 8310件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.00** / 初期 $100.00 (+329.00%)
- 確定: 4996件 (Win 1332 / Loss 1084 / Flat 2580) / skip 7516件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INTW/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $429.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7266件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T00:51:09.857453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=64793.7
- Funnel: target 1073 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUU/USDT:USDT | +18.69% | $36,867,225.64 |
| CSOPSKHYNIX2L/USDT:USDT | +18.58% | $1,246,229.03 |
| SNXX/USDT:USDT | +18.51% | $46,861,651.91 |
| MVLL/USDT:USDT | +18.17% | $5,270,929.82 |
| SOXL/USDT:USDT | +17.96% | $1,199,524,823.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.21% | +2.40% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.51% | +1.71% |
| INIT/USDT:USDT | below_1h_threshold | +1.14% | +1.33% |
| INTW/USDT:USDT | below_1h_threshold | +1.09% | +1.29% |
| SOXL/USDT:USDT | below_1h_threshold | +1.01% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
