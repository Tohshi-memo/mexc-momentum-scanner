# Decision Report

- generated_at: 2026-10-29T17:51:39.144135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17796**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=17796, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.07% | **+0.72%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.92% | **+0.46%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_BB3S | 5/10 | 50.0% | +0.31% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +1.96% | **+1.37%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6804件 (Win 1975 / Loss 2180 / Flat 2649) / skip 7553件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.70** / 初期 $100.00 (+264.70%)
- 確定: 4317件 (Win 1165 / Loss 978 / Flat 2174) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0070 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PARTI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $364.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5959件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T17:51:23.779475+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=80788.3
- Funnel: target 1086 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.1 >= 65=1, 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +47.45% | $1,411,725.20 |
| BLESS/USDT:USDT | +12.43% | $10,492,950.89 |
| BULLA/USDT:USDT | +7.41% | $1,568,153.37 |
| UAI/USDT:USDT | +4.68% | $2,757,280.71 |
| EVAA/USDT:USDT | +3.58% | $13,463,807.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +3.41% | +3.96% |
| SOXS/USDT:USDT | below_1h_threshold | +1.82% | +2.36% |
| INIT/USDT:USDT | below_1h_threshold | +1.45% | +2.00% |
| BULLA/USDT:USDT | below_1h_threshold | +1.18% | +1.73% |
| EVAA/USDT:USDT | below_1h_threshold | +0.80% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
