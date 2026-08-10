# Decision Report

- generated_at: 2026-08-10T08:31:48.120205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11137**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.02% / filled 20/20。**
- 全期間 MARKET基準: n=11137, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +2.88% | **+2.88%** |
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.25% | **+0.94%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.13% | **+0.74%** |
| LIMIT_BB3S | 3/20 | 15.0% | +4.60% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.68% | **+0.38%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.14% | **+0.08%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.98** / 初期 $100.00 (+522.98%)
- 確定: 3934件 (Win 1230 / Loss 1283 / Flat 1421) / skip 3764件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACT/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.32% 残高後 $622.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3035件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.51** / 初期 $100.00 (+18.51%)
- 確定: 1289件 (Win 401 / Loss 495 / Flat 393) / pending 5件 / skip 1315件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000346 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.51

## 6. Latest Market Context

- 更新: 2026-08-10T08:31:35.475904+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=65279.5
- Funnel: target 958 → liquid 164 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1, 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +40.55% | $21,276,487.97 |
| GRVT/USDT:USDT | +37.06% | $2,567,527.91 |
| TST/USDT:USDT | +23.78% | $2,495,436.60 |
| ACT/USDT:USDT | +20.03% | $1,299,413.03 |
| CASHCAT/USDT:USDT | +19.34% | $1,521,350.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +4.00% | +3.85% |
| NIL/USDT:USDT | below_1h_threshold | +2.52% | +2.37% |
| RIVER/USDT:USDT | below_1h_threshold | +2.15% | +2.01% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.57% | +1.42% |
| SOXL/USDT:USDT | below_1h_threshold | +1.11% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
