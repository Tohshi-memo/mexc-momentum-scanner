# Decision Report

- generated_at: 2026-08-09T04:01:18.602049+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10931**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=10931, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.84% | **+1.66%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.93% | **+1.61%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.12% | **+0.84%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.20% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +4.39% | **+0.88%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.71% | **+0.36%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.45% | **+0.14%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.27% | **-0.07%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.20% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.27** / 初期 $100.00 (+531.27%)
- 確定: 3930件 (Win 1230 / Loss 1280 / Flat 1420) / skip 3562件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TST/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $631.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2831件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0012 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1159件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T04:01:10.668085+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=64758.9
- Funnel: target 961 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +97.82% | $30,350,784.24 |
| IOTX/USDT:USDT | +35.96% | $2,837,044.49 |
| BLUAI/USDT:USDT | +29.44% | $7,910,437.54 |
| SAGA/USDT:USDT | +24.59% | $1,521,501.98 |
| COOKIE/USDT:USDT | +22.68% | $4,087,532.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RBRKSTOCK/USDT:USDT | below_1h_threshold | +1.72% | +1.72% |
| TUT/USDT:USDT | below_1h_threshold | +1.12% | +1.12% |
| BEAT/USDT:USDT | below_1h_threshold | +0.89% | +0.89% |
| COOKIE/USDT:USDT | below_1h_threshold | +0.76% | +0.76% |
| UB/USDT:USDT | below_1h_threshold | +0.71% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
