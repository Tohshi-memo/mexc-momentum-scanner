# Decision Report

- generated_at: 2026-09-22T06:51:20.079554+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15301**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=15301, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.91% | **+1.62%** |
| LIMIT_BB3S | 5/16 | 31.2% | +3.41% | **+1.06%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.80% | **+0.54%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.39% | **+0.35%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,172.17** / 初期 $100.00 (+1072.17%)
- 確定: 5792件 (Win 1722 / Loss 1865 / Flat 2205) / skip 6070件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,172.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.87** / 初期 $100.00 (+147.87%)
- 確定: 3340件 (Win 922 / Loss 776 / Flat 1642) / skip 5372件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $247.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.56** / 初期 $100.00 (+22.56%)
- 確定: 3073件 (Win 903 / Loss 1203 / Flat 967) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000169 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.56

## 6. Latest Market Context

- 更新: 2026-09-22T06:51:10.160223+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=85429.8
- Funnel: target 1056 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUBARAK/USDT:USDT | +32.88% | $2,345,351.34 |
| KERNEL/USDT:USDT | +30.16% | $3,182,758.12 |
| ALCH/USDT:USDT | +21.53% | $2,568,566.78 |
| GRASS/USDT:USDT | +18.63% | $2,851,568.11 |
| NIL/USDT:USDT | +15.39% | $3,786,539.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.26% | +3.20% |
| WIF/USDT:USDT | below_1h_threshold | +2.37% | +2.31% |
| SEI/USDT:USDT | below_1h_threshold | +2.30% | +2.23% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.25% | +2.18% |
| CHIP/USDT:USDT | below_1h_threshold | +1.92% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
