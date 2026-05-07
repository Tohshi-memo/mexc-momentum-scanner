# Decision Report

- generated_at: 2026-05-07T18:42:45.609660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3684**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3684, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.60% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.81% | **+2.11%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.15% | **+2.08%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.63% | **+1.84%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.08% | **+1.39%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$110.61** / 初期 $100.00 (+10.61%)
- 確定: 178件 (Win 48 / Loss 60 / Flat 70) / skip 67件
- 成長率目線: 平均log +0.000567 / 幾何平均 +0.057% per trade / maxDD +2.62%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $110.61

## 4. Latest Market Context

- 更新: 2026-05-07T18:42:41.764030+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=80140.6
- Funnel: target 767 → liquid 183 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1, 4h RSI 74.6 >= 65=1, 4h RSI 95.3 >= 65=1, 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +42.79% | $2,423,668.98 |
| JTO/USDT:USDT | +24.29% | $14,040,012.18 |
| NOT/USDT:USDT | +18.89% | $8,123,193.79 |
| SATO/USDT:USDT | +15.08% | $6,020,963.41 |
| DYDX/USDT:USDT | +13.85% | $6,701,118.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +4.34% | +4.23% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.98% | +2.87% |
| BSB/USDT:USDT | below_1h_threshold | +2.16% | +2.06% |
| LAB/USDT:USDT | below_1h_threshold | +1.86% | +1.75% |
| DOGS/USDT:USDT | below_1h_threshold | +1.81% | +1.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
