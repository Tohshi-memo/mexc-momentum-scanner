# Decision Report

- generated_at: 2026-11-01T04:46:54.194747+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17934**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=17934, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_BB3S | 6/20 | 30.0% | +3.01% | **+0.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.38% | **+0.33%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.27% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 257件 (TP 95 / SL 154 / EXP 8)
- 最新: JCT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.74** / 初期 $100.00 (+1385.74%)
- 確定: 6821件 (Win 1976 / Loss 2188 / Flat 2657) / skip 7674件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GANG/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,485.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$370.19** / 初期 $100.00 (+270.19%)
- 確定: 4419件 (Win 1185 / Loss 983 / Flat 2251) / skip 6926件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0396 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $370.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6098件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000451 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-01T04:46:34.953558+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77781.1
- Funnel: target 1089 → liquid 117 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +30.53% | $1,716,800.34 |
| AIN/USDT:USDT | +18.79% | $22,609,553.39 |
| GANG/USDT:USDT | +17.33% | $1,099,934.92 |
| POWR/USDT:USDT | +15.92% | $2,276,660.53 |
| ZAMA/USDT:USDT | +12.33% | $1,086,242.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.14% | +3.10% |
| EVAA/USDT:USDT | below_1h_threshold | +2.14% | +2.11% |
| USELESS/USDT:USDT | below_1h_threshold | +1.97% | +1.93% |
| AVAX/USDT:USDT | below_1h_threshold | +1.28% | +1.25% |
| ONDO/USDT:USDT | below_1h_threshold | +1.05% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
