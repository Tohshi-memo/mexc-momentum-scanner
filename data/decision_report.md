# Decision Report

- generated_at: 2026-11-24T10:56:16.320706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19562**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=19562, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.38% | **+0.21%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.90% | **+0.49%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.15% | **+0.06%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | -0.47% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,019.97** / 初期 $100.00 (+1919.97%)
- 確定: 7599件 (Win 2189 / Loss 2442 / Flat 2968) / skip 8524件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIOT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $2,019.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7754件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7723件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000064 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T10:56:06.783645+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=59636.9
- Funnel: target 1089 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NVD/USDT:USDT | +30.33% | $2,588,530.73 |
| AIOT/USDT:USDT | +29.26% | $2,111,309.71 |
| KIMCHI/USDT:USDT | +28.82% | $1,480,798.55 |
| LISTA/USDT:USDT | +23.28% | $2,853,087.63 |
| MMT/USDT:USDT | +20.72% | $6,514,327.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +3.82% | +4.37% |
| SOXS/USDT:USDT | below_1h_threshold | +3.51% | +4.06% |
| NVD/USDT:USDT | below_1h_threshold | +2.42% | +2.97% |
| UVXY/USDT:USDT | below_1h_threshold | +2.02% | +2.57% |
| SKDD/USDT:USDT | below_1h_threshold | +1.85% | +2.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
