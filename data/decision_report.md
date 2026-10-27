# Decision Report

- generated_at: 2026-10-27T10:36:28.066128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17590**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17590, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.57% | **+0.77%** |
| LIMIT_9PCT | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_BB3S | 2/16 | 12.5% | +4.07% | **+0.51%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.63% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.49% | **+0.52%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6723件 (Win 1956 / Loss 2152 / Flat 2615) / skip 7428件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$332.87** / 初期 $100.00 (+232.87%)
- 確定: 4119件 (Win 1129 / Loss 959 / Flat 2031) / skip 6882件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1147 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAG/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $332.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5750件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000269 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T10:36:12.774011+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=79634.4
- Funnel: target 1078 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +176.90% | $5,915,684.23 |
| TAG/USDT:USDT | +35.07% | $1,825,903.00 |
| SYN/USDT:USDT | +18.49% | $4,490,650.88 |
| BTW/USDT:USDT | +14.76% | $22,274,058.42 |
| Q/USDT:USDT | +10.83% | $51,217,571.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +1.38% | +1.52% |
| MUU/USDT:USDT | below_1h_threshold | +1.18% | +1.32% |
| SNXX/USDT:USDT | below_1h_threshold | +0.82% | +0.96% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.89% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
