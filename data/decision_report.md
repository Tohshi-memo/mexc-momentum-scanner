# Decision Report

- generated_at: 2026-09-15T08:06:13.661339+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14579**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=14579, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.45% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.32% | **+0.99%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.50% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,077.38** / 初期 $100.00 (+977.38%)
- 確定: 5481件 (Win 1642 / Loss 1774 / Flat 2065) / skip 5659件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,077.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.55** / 初期 $100.00 (+130.55%)
- 確定: 3020件 (Win 836 / Loss 718 / Flat 1466) / skip 4970件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0516 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.98** / 初期 $100.00 (+23.98%)
- 確定: 2908件 (Win 862 / Loss 1133 / Flat 913) / pending 1件 / skip 3139件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.98

## 6. Latest Market Context

- 更新: 2026-09-15T08:06:05.999716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=76833.9
- Funnel: target 1060 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +56.43% | $1,621,244.55 |
| AIN/USDT:USDT | +51.27% | $9,580,375.32 |
| POWER/USDT:USDT | +25.23% | $10,635,779.58 |
| CNPY/USDT:USDT | +16.49% | $2,023,423.76 |
| AKE/USDT:USDT | +15.12% | $4,457,073.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +4.04% | +4.13% |
| AIN/USDT:USDT | below_1h_threshold | +2.49% | +2.58% |
| POWER/USDT:USDT | below_1h_threshold | +1.50% | +1.59% |
| SOXS/USDT:USDT | below_1h_threshold | +0.54% | +0.63% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.51% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
