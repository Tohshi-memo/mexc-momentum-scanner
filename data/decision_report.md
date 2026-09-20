# Decision Report

- generated_at: 2026-09-20T00:11:27.274776+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15110**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.96% / filled 20/20。**
- 全期間 MARKET基準: n=15110, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.96% | **+1.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.96% | **+1.96%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.57% | **+1.41%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.96% | **+0.53%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.29% | **-0.26%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.89% | **-0.29%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -2.44% | **-0.49%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -1.96% | **-0.49%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.96% | **-0.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6031件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.41** / 初期 $100.00 (+144.41%)
- 確定: 3223件 (Win 892 / Loss 762 / Flat 1569) / skip 5298件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0217 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $244.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.58** / 初期 $100.00 (+21.58%)
- 確定: 2977件 (Win 880 / Loss 1178 / Flat 919) / pending 1件 / skip 3603件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.58

## 6. Latest Market Context

- 更新: 2026-09-20T00:11:14.460126+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=81217.9
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OFC/USDT:USDT | +47.59% | $1,832,731.77 |
| CELR/USDT:USDT | +33.71% | $1,366,237.32 |
| ONE/USDT:USDT | +27.98% | $46,039,690.54 |
| BANK/USDT:USDT | +18.41% | $2,619,668.31 |
| CATE/USDT:USDT | +18.03% | $1,259,083.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.18% | +4.18% |
| MYX/USDT:USDT | below_1h_threshold | +2.47% | +2.47% |
| G/USDT:USDT | below_1h_threshold | +1.97% | +1.97% |
| AVAX/USDT:USDT | below_1h_threshold | +1.46% | +1.46% |
| EVAA/USDT:USDT | below_1h_threshold | +1.34% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
