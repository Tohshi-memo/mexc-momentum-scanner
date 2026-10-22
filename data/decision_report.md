# Decision Report

- generated_at: 2026-10-22T17:46:17.783974+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17163**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.82% / filled 20/20。**
- 全期間 MARKET基準: n=17163, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.82% | **+1.82%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.15% | **+0.98%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.23% | **+0.86%** |
| LIMIT_BB3S | 6/19 | 31.6% | +2.01% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.04** / 初期 $100.00 (+1242.04%)
- 確定: 6529件 (Win 1897 / Loss 2083 / Flat 2549) / skip 7195件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,342.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3849件 (Win 1055 / Loss 899 / Flat 1895) / skip 6725件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5324件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T17:46:05.681106+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81309.9
- Funnel: target 1096 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DNA/USDT:USDT | +11.83% | $2,170,827.34 |
| ALT/USDT:USDT | +7.04% | $7,715,681.29 |
| BILL/USDT:USDT | +5.63% | $1,470,223.79 |
| EDGE/USDT:USDT | +2.67% | $1,247,934.03 |
| BAT/USDT:USDT | +2.37% | $4,953,811.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +2.58% | +2.50% |
| ALT/USDT:USDT | below_1h_threshold | +2.29% | +2.21% |
| KAS/USDT:USDT | below_1h_threshold | +1.81% | +1.73% |
| EDGE/USDT:USDT | below_1h_threshold | +1.79% | +1.71% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.72% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
