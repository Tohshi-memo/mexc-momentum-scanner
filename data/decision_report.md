# Decision Report

- generated_at: 2026-10-18T03:36:18.112090+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16938**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=16938, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.93% | **+1.73%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.59% | **+1.35%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.68% | **+0.47%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,285.71** / 初期 $100.00 (+1185.71%)
- 確定: 6404件 (Win 1865 / Loss 2049 / Flat 2490) / skip 7095件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,285.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.01** / 初期 $100.00 (+177.01%)
- 確定: 3703件 (Win 1031 / Loss 880 / Flat 1792) / skip 6646件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $277.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5096件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000142 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T03:36:04.011455+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81802.2
- Funnel: target 1084 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +26.68% | $2,261,817.80 |
| BR/USDT:USDT | +12.92% | $10,957,522.88 |
| AVA/USDT:USDT | +12.27% | $2,294,047.65 |
| XMR/USDT:USDT | +10.18% | $6,599,193.84 |
| CYS/USDT:USDT | +9.05% | $1,092,219.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +1.08% | +1.07% |
| AKE/USDT:USDT | below_1h_threshold | +0.98% | +0.96% |
| STX/USDT:USDT | below_1h_threshold | +0.65% | +0.63% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.62% | +0.61% |
| TAO/USDT:USDT | below_1h_threshold | +0.62% | +0.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
