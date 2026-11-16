# Decision Report

- generated_at: 2026-11-16T08:26:32.080035+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19002**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=19002, expectancy=+0.02%
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
| LIMIT_5PCT | 7/20 | 35.0% | +1.27% | **+0.45%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.43% | **+0.26%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.76% | **+1.66%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.91% | **+0.64%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.47% | **+0.35%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.03% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,719.93** / 初期 $100.00 (+1619.93%)
- 確定: 7343件 (Win 2109 / Loss 2353 / Flat 2881) / skip 8220件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,719.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4984件 (Win 1332 / Loss 1081 / Flat 2571) / skip 7429件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHELL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7160件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000083 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T08:26:19.390510+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.56% price=64592.8
- Funnel: target 1066 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +57.27% | $9,018,403.42 |
| SKR/USDT:USDT | +27.59% | $3,686,084.14 |
| JCT/USDT:USDT | +16.54% | $10,559,371.12 |
| EVAA/USDT:USDT | +9.91% | $19,395,431.44 |
| PIEVERSE/USDT:USDT | +6.85% | $1,807,418.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.59% | +5.15% |
| NVIDIA/USDT:USDT | below_1h_threshold | +1.15% | +1.70% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +1.48% |
| TQQQ/USDT:USDT | below_1h_threshold | +0.75% | +1.31% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.57% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
