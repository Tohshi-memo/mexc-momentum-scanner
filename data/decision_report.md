# Decision Report

- generated_at: 2026-09-12T14:06:22.223957+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14310**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14310, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.64% | **+0.22%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.22% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.04% | **+1.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.70% | **+1.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.89% | **+0.75%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.36% | **+0.75%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5428件 (Win 1635 / Loss 1760 / Flat 2033) / skip 5443件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2834件 (Win 780 / Loss 656 / Flat 1398) / skip 4887件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0498 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.33** / 初期 $100.00 (+23.33%)
- 確定: 2767件 (Win 818 / Loss 1064 / Flat 885) / pending 0件 / skip 3013件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000351 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.33

## 6. Latest Market Context

- 更新: 2026-09-12T14:06:13.472563+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77339.9
- Funnel: target 1068 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +142.59% | $6,909,019.94 |
| LSK/USDT:USDT | +90.62% | $24,788,067.65 |
| STORJ/USDT:USDT | +47.88% | $24,893,176.43 |
| VTHO/USDT:USDT | +21.90% | $2,538,055.93 |
| LAB/USDT:USDT | +19.48% | $18,044,546.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +1.61% | +1.59% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.11% | +1.09% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +1.06% | +1.04% |
| UNI/USDT:USDT | below_1h_threshold | +0.93% | +0.91% |
| STORJ/USDT:USDT | below_1h_threshold | +0.63% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
