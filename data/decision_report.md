# Decision Report

- generated_at: 2026-08-16T22:01:23.790218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11772**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=11772, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_BB3S | 5/17 | 29.4% | +3.07% | **+0.90%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.09% | **+0.49%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.09% | **+0.06%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 184件 (TP 71 / SL 108 / EXP 5)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4150件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.46** / 初期 $100.00 (+54.46%)
- 確定: 1787件 (Win 496 / Loss 418 / Flat 873) / skip 3396件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $154.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.46** / 初期 $100.00 (+18.46%)
- 確定: 1668件 (Win 502 / Loss 632 / Flat 534) / pending 3件 / skip 1573件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.46

## 6. Latest Market Context

- 更新: 2026-08-16T22:01:15.342416+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=62844.8
- Funnel: target 986 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +29.36% | $11,357,988.60 |
| HFT/USDT:USDT | +22.92% | $2,396,980.50 |
| BTW/USDT:USDT | +14.32% | $21,876,879.64 |
| BEAT/USDT:USDT | +13.04% | $41,397,015.20 |
| APR/USDT:USDT | +10.00% | $6,102,608.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MASTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.35% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.76% | +0.85% |
| BEAT/USDT:USDT | below_1h_threshold | +0.73% | +0.81% |
| CYS/USDT:USDT | below_1h_threshold | +0.65% | +0.74% |
| SILVER/USDT:USDT | below_1h_threshold | +0.34% | +0.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
