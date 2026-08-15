# Decision Report

- generated_at: 2026-08-15T22:51:26.269675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11700**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11700, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.59% | **+1.35%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.50% | **+1.20%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.65% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.44% | **+1.10%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.68% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.15** / 初期 $100.00 (+543.15%)
- 確定: 4168件 (Win 1291 / Loss 1355 / Flat 1522) / skip 4093件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPORTFUN/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $643.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.38** / 初期 $100.00 (+55.38%)
- 確定: 1759件 (Win 493 / Loss 413 / Flat 853) / skip 3352件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.49** / 初期 $100.00 (+19.49%)
- 確定: 1625件 (Win 495 / Loss 617 / Flat 513) / pending 1件 / skip 1549件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PRL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $119.49

## 6. Latest Market Context

- 更新: 2026-08-15T22:51:17.509715+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63132.7
- Funnel: target 985 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPORTFUN/USDT:USDT | +52.42% | $2,568,897.90 |
| AIO/USDT:USDT | +12.98% | $2,812,170.34 |
| BULLA/USDT:USDT | +12.83% | $2,426,779.45 |
| BTW/USDT:USDT | +8.40% | $11,473,335.25 |
| ANSEM/USDT:USDT | +8.39% | $2,005,672.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +3.46% | +3.45% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.16% | +2.14% |
| SPX/USDT:USDT | below_1h_threshold | +1.68% | +1.67% |
| H/USDT:USDT | below_1h_threshold | +1.19% | +1.17% |
| CHIP/USDT:USDT | below_1h_threshold | +1.14% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
