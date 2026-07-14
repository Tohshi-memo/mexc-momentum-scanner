# Decision Report

- generated_at: 2026-07-14T06:06:15.468319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8674**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=8674, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.69% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.59% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.48% | **+0.99%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.71** / 初期 $100.00 (+230.71%)
- 確定: 2842件 (Win 891 / Loss 924 / Flat 1027) / skip 2393件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $330.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.98** / 初期 $100.00 (+4.98%)
- 確定: 673件 (Win 159 / Loss 161 / Flat 353) / skip 1412件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0520 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $104.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.27** / 初期 $100.00 (-0.73%)
- 確定: 55件 (Win 19 / Loss 36 / Flat 0) / pending 3件 / skip 87件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000080 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.27

## 6. Latest Market Context

- 更新: 2026-07-14T06:06:08.036160+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62657.0
- Funnel: target 867 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +33.26% | $7,305,286.61 |
| TRIA/USDT:USDT | +31.14% | $2,100,651.70 |
| ZBT/USDT:USDT | +20.57% | $2,863,543.79 |
| VELVET/USDT:USDT | +17.85% | $33,982,888.82 |
| BSB/USDT:USDT | +11.39% | $2,029,057.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.43% | +2.50% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.77% | +1.83% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.68% | +1.75% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.52% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
