# Decision Report

- generated_at: 2026-10-29T17:16:44.132956+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17792**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=17792, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_BB3S | 6/12 | 50.0% | +1.70% | **+0.85%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.25% | **+0.68%** |
| LIMIT_4PCT | 9/20 | 45.0% | +1.02% | **+0.46%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.61% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.31% | **+0.85%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.05% | **+0.68%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.22** / 初期 $100.00 (+1431.22%)
- 確定: 6803件 (Win 1975 / Loss 2180 / Flat 2648) / skip 7550件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HYPE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $1,531.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.70** / 初期 $100.00 (+264.70%)
- 確定: 4313件 (Win 1165 / Loss 978 / Flat 2170) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0072 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $364.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5955件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000362 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T17:16:29.003183+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=80974.3
- Funnel: target 1086 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +20.19% | $9,414,556.35 |
| BULLA/USDT:USDT | +6.99% | $1,524,194.05 |
| LSK/USDT:USDT | +5.48% | $3,376,242.91 |
| UAI/USDT:USDT | +5.14% | $2,707,407.44 |
| SOXS/USDT:USDT | +3.36% | $77,334,005.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +4.20% | +4.52% |
| SOXS/USDT:USDT | below_1h_threshold | +1.82% | +2.13% |
| XPIN/USDT:USDT | below_1h_threshold | +1.07% | +1.39% |
| BULLA/USDT:USDT | below_1h_threshold | +0.92% | +1.24% |
| UAI/USDT:USDT | below_1h_threshold | +0.69% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
