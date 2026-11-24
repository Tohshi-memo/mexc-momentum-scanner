# Decision Report

- generated_at: 2026-11-24T04:51:22.785553+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19554**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=19554, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_3PCT | 8/20 | 40.0% | +1.46% | **+0.58%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.09% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.47% | **+0.37%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.63% | **+0.19%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,040.63** / 初期 $100.00 (+1940.63%)
- 確定: 7591件 (Win 2187 / Loss 2436 / Flat 2968) / skip 8524件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KIMCHI/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $2,040.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7746件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7712件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000058 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T04:51:06.856435+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=60424.9
- Funnel: target 1088 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +35.28% | $1,259,234.72 |
| MMT/USDT:USDT | +21.03% | $3,395,991.00 |
| ARIA/USDT:USDT | +20.03% | $10,119,423.76 |
| NVD/USDT:USDT | +17.71% | $2,500,120.60 |
| LISTA/USDT:USDT | +16.61% | $1,373,035.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +2.54% | +2.34% |
| SOXL/USDT:USDT | below_1h_threshold | +1.88% | +1.68% |
| KIMCHI/USDT:USDT | below_1h_threshold | +1.75% | +1.56% |
| ARIA/USDT:USDT | below_1h_threshold | +1.60% | +1.41% |
| NVD/USDT:USDT | below_1h_threshold | +1.52% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
