# Decision Report

- generated_at: 2026-11-17T21:26:33.596491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19093**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=19093, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.01% | **+0.76%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.57% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.46% | **+0.28%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.56% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 278件 (TP 100 / SL 170 / EXP 8)
- 最新: ARIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7352件 (Win 2109 / Loss 2358 / Flat 2885) / skip 8302件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.72** / 初期 $100.00 (+329.72%)
- 確定: 4994件 (Win 1332 / Loss 1082 / Flat 2580) / skip 7510件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $429.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7256件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000150 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-17T21:26:15.654486+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.70% price=64419.6
- Funnel: target 1073 → liquid 139 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +18.80% | $1,743,045.59 |
| SNXX/USDT:USDT | +12.93% | $41,182,918.66 |
| MUU/USDT:USDT | +12.18% | $32,999,440.23 |
| MVLL/USDT:USDT | +10.38% | $4,682,474.59 |
| CSOPSKHYNIX2L/USDT:USDT | +10.28% | $1,141,088.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +4.58% | +3.88% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +3.08% | +2.38% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.95% | +2.25% |
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +2.58% | +1.88% |
| SNXX/USDT:USDT | below_1h_threshold | +2.58% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
