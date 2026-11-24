# Decision Report

- generated_at: 2026-11-24T05:51:33.294776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19556**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=19556, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.56% | **+0.51%** |
| LIMIT_BB3S | 4/16 | 25.0% | +2.00% | **+0.50%** |
| LIMIT_1PCT | 13/20 | 65.0% | +0.66% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.41% | **+0.71%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.47% | **+0.37%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.63% | **+0.32%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.63% | **+0.19%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,020.27** / 初期 $100.00 (+1920.27%)
- 確定: 7593件 (Win 2187 / Loss 2438 / Flat 2968) / skip 8524件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $2,020.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7748件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7717件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000060 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T05:51:18.928990+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=60609.9
- Funnel: target 1088 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +37.46% | $1,289,508.43 |
| MMT/USDT:USDT | +30.03% | $3,947,014.82 |
| LISTA/USDT:USDT | +28.42% | $1,547,048.83 |
| ARIA/USDT:USDT | +21.65% | $10,172,997.24 |
| NVD/USDT:USDT | +15.01% | $2,505,176.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_relative_strength | +5.16% | +4.74% |
| ARIA/USDT:USDT | below_1h_threshold | +2.33% | +1.91% |
| VET/USDT:USDT | below_1h_threshold | +1.97% | +1.54% |
| KIMCHI/USDT:USDT | below_1h_threshold | +1.84% | +1.41% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.68% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
