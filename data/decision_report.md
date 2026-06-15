# Decision Report

- generated_at: 2026-06-15T14:43:58.294104+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6789**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6789, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.44% | **+1.44%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.03% | **-0.02%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | -0.12% | **-0.04%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -1.51% | **-0.38%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$174.47** / 初期 $100.00 (+74.47%)
- 確定: 1662件 (Win 432 / Loss 516 / Flat 714) / skip 1688件
- 成長率目線: 平均log +0.000335 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $174.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.16** / 初期 $100.00 (-1.84%)
- 確定: 150件 (Win 28 / Loss 28 / Flat 94) / skip 50件
- 成長率目線: 平均log -0.000124 / 幾何平均 -0.012% per trade / maxDD +2.48%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $98.16

## 5. Latest Market Context

- 更新: 2026-06-15T14:43:53.567016+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=66499.9
- Funnel: target 772 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1, 4h RSI 86.9 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +91.13% | $37,786,096.88 |
| ASTEROID/USDT:USDT | +67.83% | $5,743,021.68 |
| CLO/USDT:USDT | +42.76% | $2,329,287.03 |
| JTO/USDT:USDT | +41.28% | $3,448,729.95 |
| UAI/USDT:USDT | +31.63% | $3,915,118.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +3.03% | +2.89% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.00% | +2.87% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.30% | +2.17% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.30% | +2.16% |
| CLO/USDT:USDT | below_1h_threshold | +2.11% | +1.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
