# Decision Report

- generated_at: 2026-07-20T07:51:18.511292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9093**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9093, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.39% | **+0.13%** |
| LIMIT_BB3S | 2/18 | 11.1% | -0.57% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.09% | **+1.05%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.87% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定トレード: 121件 (TP 43 / SL 73 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -3.98% 残高後 $108.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.37** / 初期 $100.00 (+299.37%)
- 確定: 3155件 (Win 986 / Loss 1001 / Flat 1168) / skip 2499件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $399.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.36** / 初期 $100.00 (+26.36%)
- 確定: 1054件 (Win 273 / Loss 218 / Flat 563) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0332 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $126.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.98** / 初期 $100.00 (+0.98%)
- 確定: 292件 (Win 96 / Loss 131 / Flat 65) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.98

## 6. Latest Market Context

- 更新: 2026-07-20T07:51:13.192289+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=64176.4
- Funnel: target 886 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +104.99% | $9,210,765.39 |
| BANK/USDT:USDT | +45.32% | $105,561,251.04 |
| EVAA/USDT:USDT | +29.61% | $4,160,584.25 |
| PUMPFUN/USDT:USDT | +20.04% | $21,237,739.29 |
| PROM/USDT:USDT | +14.50% | $2,594,731.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PI/USDT:USDT | below_1h_threshold | +4.14% | +3.70% |
| B/USDT:USDT | below_1h_threshold | +3.13% | +2.68% |
| BLESS/USDT:USDT | below_1h_threshold | +3.11% | +2.67% |
| PENGU/USDT:USDT | below_1h_threshold | +2.59% | +2.14% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.05% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
