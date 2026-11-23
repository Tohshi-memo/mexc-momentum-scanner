# Decision Report

- generated_at: 2026-11-23T05:16:28.360879+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19418**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.15% / filled 20/20。**
- 全期間 MARKET基準: n=19418, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.15% | **+3.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.15% | **+3.15%** |
| LIMIT_1PCT | 13/20 | 65.0% | +2.14% | **+1.39%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_2PCT | 11/20 | 55.0% | +0.62% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.44% | **+1.11%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.01% | **+0.60%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,809.78** / 初期 $100.00 (+1709.78%)
- 確定: 7518件 (Win 2159 / Loss 2423 / Flat 2936) / skip 8461件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,809.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$462.21** / 初期 $100.00 (+362.21%)
- 確定: 5181件 (Win 1381 / Loss 1117 / Flat 2683) / skip 7648件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $462.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7581件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T05:16:14.184580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=61209.0
- Funnel: target 1086 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +61.77% | $1,569,880.99 |
| ELSA/USDT:USDT | +19.94% | $1,795,591.87 |
| ARIA/USDT:USDT | +15.02% | $1,556,754.96 |
| BULLA/USDT:USDT | +10.52% | $2,535,790.59 |
| IDOL/USDT:USDT | +8.65% | $2,172,321.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +2.64% | +2.65% |
| MUU/USDT:USDT | below_1h_threshold | +1.51% | +1.53% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.32% | +1.33% |
| UVXY/USDT:USDT | below_1h_threshold | +1.31% | +1.32% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.15% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
