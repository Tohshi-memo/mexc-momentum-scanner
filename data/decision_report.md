# Decision Report

- generated_at: 2026-10-27T20:56:26.481411+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17640**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17640, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_6PCT | 8/20 | 40.0% | +3.47% | **+1.39%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.66% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.17% | **+1.43%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.58% | **+1.42%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.20% | **+0.96%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.99% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 254件 (TP 94 / SL 152 / EXP 8)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,567.72** / 初期 $100.00 (+1467.72%)
- 確定: 6748件 (Win 1967 / Loss 2164 / Flat 2617) / skip 7453件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,567.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$347.57** / 初期 $100.00 (+247.57%)
- 確定: 4169件 (Win 1139 / Loss 964 / Flat 2066) / skip 6882件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $347.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5802件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000380 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T20:56:10.996037+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80720.4
- Funnel: target 1083 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +34.14% | $1,738,955.56 |
| APR/USDT:USDT | +13.45% | $4,273,013.56 |
| BULLA/USDT:USDT | +12.01% | $10,783,595.16 |
| LAB/USDT:USDT | +7.17% | $2,016,706.76 |
| AKE/USDT:USDT | +6.86% | $5,278,111.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.34% | +4.41% |
| HAEDAL/USDT:USDT | below_1h_threshold | +3.03% | +3.10% |
| NGAS/USDT:USDT | below_1h_threshold | +1.96% | +2.03% |
| BTW/USDT:USDT | below_1h_threshold | +1.59% | +1.66% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
