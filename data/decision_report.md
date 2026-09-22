# Decision Report

- generated_at: 2026-09-22T05:06:24.937501+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15297**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.24% / filled 20/20。**
- 全期間 MARKET基準: n=15297, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.56% | **+2.17%** |
| LIMIT_BB3S | 6/18 | 33.3% | +4.17% | **+1.39%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.65% | **+0.58%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.43% | **+0.29%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.26% | **+0.13%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.10% | **+0.05%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.11** / 初期 $100.00 (+1069.11%)
- 確定: 5788件 (Win 1721 / Loss 1864 / Flat 2203) / skip 6070件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,169.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.45** / 初期 $100.00 (+147.45%)
- 確定: 3336件 (Win 921 / Loss 775 / Flat 1640) / skip 5372件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $247.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.45** / 初期 $100.00 (+22.45%)
- 確定: 3069件 (Win 902 / Loss 1202 / Flat 965) / pending 2件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000196 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.45

## 6. Latest Market Context

- 更新: 2026-09-22T05:06:11.956047+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=85389.2
- Funnel: target 1057 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +35.12% | $3,064,472.41 |
| MUBARAK/USDT:USDT | +21.85% | $1,806,861.01 |
| ALCH/USDT:USDT | +19.76% | $2,499,943.81 |
| GRASS/USDT:USDT | +19.14% | $2,655,541.19 |
| FORM/USDT:USDT | +10.74% | $9,721,387.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +1.80% | +1.84% |
| JASMY/USDT:USDT | below_1h_threshold | +1.39% | +1.42% |
| SAGA/USDT:USDT | below_1h_threshold | +1.04% | +1.07% |
| ALCH/USDT:USDT | below_1h_threshold | +0.82% | +0.86% |
| FORM/USDT:USDT | below_1h_threshold | +0.81% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
