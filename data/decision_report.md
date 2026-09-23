# Decision Report

- generated_at: 2026-09-23T15:01:24.463062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15437**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.79% / filled 20/20。**
- 全期間 MARKET基準: n=15437, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.79% | **+3.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.79% | **+3.79%** |
| LIMIT_2PCT | 14/20 | 70.0% | +3.68% | **+2.57%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.15% | **+2.52%** |
| LIMIT_ATR | 13/20 | 65.0% | +3.16% | **+2.05%** |
| LIMIT_3PCT | 12/20 | 60.0% | +3.36% | **+2.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -3.05% | **-0.76%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -1.35% | **-0.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6103件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.96** / 初期 $100.00 (+148.96%)
- 確定: 3384件 (Win 931 / Loss 790 / Flat 1663) / skip 5464件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0343 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $248.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3769件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000312 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T15:01:13.190456+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=84423.9
- Funnel: target 1061 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMISTOCK/USDT:USDT | +790.71% | $2,914,077.04 |
| TAKE/USDT:USDT | +88.58% | $10,086,955.05 |
| SHROOM/USDT:USDT | +52.09% | $1,448,424.80 |
| SAGA/USDT:USDT | +29.31% | $2,841,537.43 |
| ALLO/USDT:USDT | +25.00% | $7,151,850.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.31% |
| EGLD/USDT:USDT | below_1h_threshold | +0.83% | +0.90% |
| FOLKS/USDT:USDT | below_1h_threshold | +0.62% | +0.69% |
| UNI/USDT:USDT | below_1h_threshold | +0.50% | +0.57% |
| ON/USDT:USDT | below_1h_threshold | +0.45% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
