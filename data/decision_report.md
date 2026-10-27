# Decision Report

- generated_at: 2026-10-27T23:46:36.623078+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17648**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17648, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_5PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.45% | **+1.03%** |
| LIMIT_3PCT | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.99% | **+0.64%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.26% | **+0.63%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.86% | **+0.43%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.54% | **+0.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,556.14** / 初期 $100.00 (+1456.14%)
- 確定: 6756件 (Win 1968 / Loss 2167 / Flat 2621) / skip 7453件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,556.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$351.13** / 初期 $100.00 (+251.13%)
- 確定: 4177件 (Win 1141 / Loss 965 / Flat 2071) / skip 6882件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1406 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` TP_HIT account +0.69% 残高後 $351.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5812件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000352 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T23:46:17.994664+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=80926.7
- Funnel: target 1083 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.0 >= 65=1, 4h RSI 66.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +60.29% | $3,267,378.98 |
| SI/USDT:USDT | +38.89% | $1,018,867.48 |
| BULLA/USDT:USDT | +24.27% | $10,080,447.94 |
| APR/USDT:USDT | +16.75% | $4,756,832.05 |
| BTW/USDT:USDT | +13.63% | $14,981,483.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +3.08% | +3.02% |
| AIN/USDT:USDT | below_1h_threshold | +2.17% | +2.11% |
| IRYS/USDT:USDT | below_1h_threshold | +1.43% | +1.36% |
| US/USDT:USDT | below_1h_threshold | +1.16% | +1.09% |
| LAB/USDT:USDT | below_1h_threshold | +1.04% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
