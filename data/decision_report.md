# Decision Report

- generated_at: 2026-10-31T07:51:13.962744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17896**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.79% / filled 20/20。**
- 全期間 MARKET基準: n=17896, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.85% | **+0.51%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.85% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.27% | **-0.13%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6820件 (Win 1976 / Loss 2188 / Flat 2656) / skip 7637件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAMX/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$367.95** / 初期 $100.00 (+267.95%)
- 確定: 4396件 (Win 1181 / Loss 983 / Flat 2232) / skip 6911件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0530 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $367.95

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6054件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T07:51:03.562640+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77298.8
- Funnel: target 1090 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +57.27% | $13,030,499.17 |
| IDOL/USDT:USDT | +11.54% | $15,274,902.37 |
| MAGMA/USDT:USDT | +10.22% | $1,693,802.61 |
| PYTH/USDT:USDT | +5.94% | $3,689,706.22 |
| PENDLE/USDT:USDT | +5.79% | $1,515,398.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAMX/USDT:USDT | below_1h_threshold | +2.24% | +2.31% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.54% | +0.61% |
| ZEC/USDT:USDT | below_1h_threshold | +0.50% | +0.57% |
| ASTER/USDT:USDT | below_1h_threshold | +0.44% | +0.50% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.35% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
