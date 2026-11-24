# Decision Report

- generated_at: 2026-11-24T08:21:13.300295+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19560**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=19560, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.38% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.99% | **+1.09%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.05% | **+0.31%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.15% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,010.02** / 初期 $100.00 (+1910.02%)
- 確定: 7597件 (Win 2188 / Loss 2441 / Flat 2968) / skip 8524件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KIMCHI/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $2,010.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7752件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7718件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000064 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T08:21:02.404564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=60339.7
- Funnel: target 1089 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +40.39% | $1,356,093.46 |
| MMT/USDT:USDT | +35.84% | $5,567,051.35 |
| ARIA/USDT:USDT | +28.45% | $9,867,931.43 |
| NVD/USDT:USDT | +23.12% | $2,539,117.07 |
| LISTA/USDT:USDT | +20.76% | $2,212,216.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVD/USDT:USDT | below_1h_threshold | +3.61% | +3.71% |
| KIMCHI/USDT:USDT | below_1h_threshold | +3.14% | +3.24% |
| CYS/USDT:USDT | below_1h_threshold | +2.36% | +2.46% |
| ARIA/USDT:USDT | below_1h_threshold | +1.84% | +1.94% |
| SOXS/USDT:USDT | below_1h_threshold | +1.71% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
