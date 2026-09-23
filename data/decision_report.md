# Decision Report

- generated_at: 2026-09-23T14:21:24.739254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15436**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.79% / filled 20/20。**
- 全期間 MARKET基準: n=15436, expectancy=+0.01%
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
| LIMIT_1PCT | 17/20 | 85.0% | +3.44% | **+2.92%** |
| LIMIT_2PCT | 14/20 | 70.0% | +3.68% | **+2.57%** |
| LIMIT_ATR | 13/20 | 65.0% | +3.16% | **+2.05%** |
| LIMIT_3PCT | 12/20 | 60.0% | +3.36% | **+2.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | +0.03% | **+0.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -3.05% | **-0.76%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6102件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.96** / 初期 $100.00 (+148.96%)
- 確定: 3383件 (Win 931 / Loss 790 / Flat 1662) / skip 5464件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0343 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $248.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3768件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000312 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T14:21:13.566186+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.61% price=84365.7
- Funnel: target 1061 → liquid 196 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMISTOCK/USDT:USDT | +798.63% | $2,626,840.78 |
| TAKE/USDT:USDT | +144.79% | $8,983,611.51 |
| SHROOM/USDT:USDT | +55.29% | $1,431,831.19 |
| ALLO/USDT:USDT | +34.00% | $6,533,213.88 |
| MET/USDT:USDT | +24.54% | $2,145,718.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TESLA/USDT:USDT | below_1h_threshold | +1.86% | +3.48% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.86% | +3.48% |
| SOXS/USDT:USDT | below_1h_threshold | +1.82% | +3.44% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.85% | +2.46% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
