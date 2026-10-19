# Decision Report

- generated_at: 2026-10-19T18:26:26.149732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17020**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=17020, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.42% | **+0.34%** |
| LIMIT_5PCT | 2/20 | 10.0% | -1.52% | **-0.15%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.31% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.55% | **+0.47%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,270.86** / 初期 $100.00 (+1170.86%)
- 確定: 6465件 (Win 1876 / Loss 2063 / Flat 2526) / skip 7116件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.02% 残高後 $1,270.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.66** / 初期 $100.00 (+177.66%)
- 確定: 3785件 (Win 1041 / Loss 884 / Flat 1860) / skip 6646件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0286 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.00% 残高後 $277.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5182件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T18:26:13.493664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81801.1
- Funnel: target 1090 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +12.12% | $2,127,269.27 |
| APR/USDT:USDT | +9.79% | $1,495,479.24 |
| SOXS/USDT:USDT | +6.39% | $3,166,961.21 |
| CLAUDIA/USDT:USDT | +5.99% | $1,035,447.26 |
| BTW/USDT:USDT | +5.06% | $24,366,081.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| S/USDT:USDT | below_1h_threshold | +2.72% | +2.83% |
| APR/USDT:USDT | below_1h_threshold | +1.76% | +1.88% |
| SOXS/USDT:USDT | below_1h_threshold | +1.49% | +1.61% |
| Q/USDT:USDT | below_1h_threshold | +1.49% | +1.60% |
| ARIA/USDT:USDT | below_1h_threshold | +1.32% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
