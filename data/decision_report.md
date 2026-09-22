# Decision Report

- generated_at: 2026-09-22T06:41:15.512917+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15300**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=15300, expectancy=+0.00%
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
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.43% | **+0.29%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.34% | **+0.15%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,178.06** / 初期 $100.00 (+1078.06%)
- 確定: 5791件 (Win 1722 / Loss 1864 / Flat 2205) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,178.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.74** / 初期 $100.00 (+148.74%)
- 確定: 3339件 (Win 922 / Loss 775 / Flat 1642) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $248.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.77** / 初期 $100.00 (+22.77%)
- 確定: 3072件 (Win 903 / Loss 1202 / Flat 967) / pending 3件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.77

## 6. Latest Market Context

- 更新: 2026-09-22T06:41:07.618325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=85502.3
- Funnel: target 1056 → liquid 186 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +31.39% | $3,169,194.05 |
| MUBARAK/USDT:USDT | +29.47% | $2,266,817.84 |
| ALCH/USDT:USDT | +21.21% | $2,558,932.89 |
| GRASS/USDT:USDT | +17.19% | $2,827,738.11 |
| NIL/USDT:USDT | +13.96% | $3,719,896.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +2.60% | +2.45% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.70% | +1.55% |
| BEAT/USDT:USDT | below_1h_threshold | +1.67% | +1.52% |
| MINA/USDT:USDT | below_1h_threshold | +1.57% | +1.42% |
| EGLD/USDT:USDT | below_1h_threshold | +1.46% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
