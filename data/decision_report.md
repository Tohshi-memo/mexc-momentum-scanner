# Decision Report

- generated_at: 2026-10-31T00:56:24.008828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17872**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17872, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.89% | **-0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +3.39% | **+2.71%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.39% | **+2.15%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.26% | **+1.70%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.49%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.39% | **+1.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,515.94** / 初期 $100.00 (+1415.94%)
- 確定: 6807件 (Win 1975 / Loss 2182 / Flat 2650) / skip 7626件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,515.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$365.16** / 初期 $100.00 (+265.16%)
- 確定: 4372件 (Win 1176 / Loss 983 / Flat 2213) / skip 6911件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $365.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6036件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T00:56:13.223445+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=77467.6
- Funnel: target 1090 → liquid 175 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1, 4h RSI 83.8 >= 65=1, 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +25.38% | $1,343,135.37 |
| AIN/USDT:USDT | +21.08% | $4,849,837.53 |
| IDOL/USDT:USDT | +19.59% | $13,836,647.25 |
| LSK/USDT:USDT | +14.82% | $4,375,687.09 |
| OP/USDT:USDT | +10.47% | $15,333,246.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CVX/USDT:USDT | below_1h_threshold | +2.90% | +2.70% |
| RENDER/USDT:USDT | below_1h_threshold | +1.89% | +1.69% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.84% | +1.64% |
| IMX/USDT:USDT | below_1h_threshold | +1.67% | +1.47% |
| LINK/USDT:USDT | below_1h_threshold | +1.65% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
