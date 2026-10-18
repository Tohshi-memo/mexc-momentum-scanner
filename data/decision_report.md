# Decision Report

- generated_at: 2026-10-18T00:46:24.671308+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16928**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.75% / filled 20/20。**
- 全期間 MARKET基準: n=16928, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_BB3S | 7/17 | 41.2% | +2.07% | **+0.85%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.00% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +6.13% | **+4.09%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.41% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,288.79** / 初期 $100.00 (+1188.79%)
- 確定: 6394件 (Win 1863 / Loss 2046 / Flat 2485) / skip 7095件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,288.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.93** / 初期 $100.00 (+175.93%)
- 確定: 3693件 (Win 1028 / Loss 878 / Flat 1787) / skip 6646件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0441 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5087件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T00:46:12.376284+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81463.9
- Funnel: target 1084 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +30.40% | $1,844,295.40 |
| BR/USDT:USDT | +23.61% | $10,355,356.43 |
| Q/USDT:USDT | +23.31% | $7,188,035.82 |
| AGT/USDT:USDT | +17.39% | $16,932,283.75 |
| AVA/USDT:USDT | +15.72% | $2,146,435.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVA/USDT:USDT | below_1h_threshold | +4.63% | +4.62% |
| BR/USDT:USDT | below_1h_threshold | +3.04% | +3.03% |
| XMR/USDT:USDT | below_1h_threshold | +1.94% | +1.93% |
| Q/USDT:USDT | below_1h_threshold | +1.90% | +1.89% |
| AGT/USDT:USDT | below_1h_threshold | +1.27% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
