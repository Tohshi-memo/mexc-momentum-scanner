# Decision Report

- generated_at: 2026-05-19T03:48:39.049531+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4459**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4459, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.17% | **-0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.25% | **+0.87%** |
| ASK | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.73% | **+0.36%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.66% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$96.70** / 初期 $100.00 (-3.30%)
- 確定トレード: 54件 (TP 14 / SL 37 / EXP 3)
- 最新: DASH/USDT:USDT TP_HIT PnL +5.37% 残高後 $96.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.48** / 初期 $100.00 (+20.48%)
- 確定: 456件 (Win 119 / Loss 157 / Flat 180) / skip 564件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $120.48

## 4. Latest Market Context

- 更新: 2026-05-19T03:48:33.857197+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=76800.0
- Funnel: target 768 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +32.98% | $8,383,088.12 |
| ONDO/USDT:USDT | +15.86% | $46,020,498.09 |
| RAVE/USDT:USDT | +13.96% | $4,193,802.56 |
| INJ/USDT:USDT | +12.25% | $27,020,608.07 |
| AKT/USDT:USDT | +12.23% | $1,348,897.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +2.22% | +1.94% |
| CHZ/USDT:USDT | below_1h_threshold | +2.00% | +1.72% |
| PENGU/USDT:USDT | below_1h_threshold | +1.59% | +1.31% |
| ONDO/USDT:USDT | below_1h_threshold | +1.33% | +1.05% |
| MONAD/USDT:USDT | below_1h_threshold | +1.32% | +1.04% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
