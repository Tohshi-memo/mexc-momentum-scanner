# Decision Report

- generated_at: 2026-07-14T03:46:16.373014+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8662**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.20% / filled 20/20。**
- 全期間 MARKET基準: n=8662, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.51% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.90% | **+1.14%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.22% | **+0.91%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.06% | **+0.58%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 96件 (TP 33 / SL 61 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.22
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.03** / 初期 $100.00 (+230.03%)
- 確定: 2830件 (Win 888 / Loss 923 / Flat 1019) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $330.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 662件 (Win 157 / Loss 159 / Flat 346) / skip 1411件
- 成長率目線: 平均log +0.000081 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0195 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.81** / 初期 $100.00 (-0.19%)
- 確定: 43件 (Win 16 / Loss 27 / Flat 0) / pending 2件 / skip 86件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000345 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.81

## 6. Latest Market Context

- 更新: 2026-07-14T03:46:08.398874+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=62440.0
- Funnel: target 867 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +26.05% | $7,161,622.33 |
| TRIA/USDT:USDT | +21.31% | $1,285,707.36 |
| EVAA/USDT:USDT | +18.27% | $22,279,634.96 |
| ZBT/USDT:USDT | +15.07% | $2,072,994.15 |
| BLAST/USDT:USDT | +7.09% | $1,695,842.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.89% | +3.02% |
| EGLD/USDT:USDT | below_1h_threshold | +1.84% | +1.96% |
| US/USDT:USDT | below_1h_threshold | +1.27% | +1.40% |
| EVAA/USDT:USDT | below_1h_threshold | +0.99% | +1.12% |
| OP/USDT:USDT | below_1h_threshold | +0.61% | +0.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
