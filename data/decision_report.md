# Decision Report

- generated_at: 2026-07-01T04:30:57.531061+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7949**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7949, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.28% | **+0.13%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.19% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.28% | **+0.14%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$256.55** / 初期 $100.00 (+156.55%)
- 確定: 2356件 (Win 714 / Loss 787 / Flat 855) / skip 2154件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIGENSYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $256.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.84** / 初期 $100.00 (+6.84%)
- 確定: 491件 (Win 127 / Loss 121 / Flat 243) / skip 869件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0419 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DYDX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.84

## 5. Latest Market Context

- 更新: 2026-07-01T04:30:51.286873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=59242.0
- Funnel: target 818 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1, 4h RSI 65.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYDX/USDT:USDT | +35.78% | $5,402,640.92 |
| TAIKO/USDT:USDT | +20.85% | $1,576,572.63 |
| BTW/USDT:USDT | +18.19% | $11,524,685.12 |
| BEAT/USDT:USDT | +17.40% | $22,369,479.50 |
| M/USDT:USDT | +17.12% | $4,415,861.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +2.71% | +2.59% |
| TRIA/USDT:USDT | below_1h_threshold | +2.54% | +2.42% |
| SPX/USDT:USDT | below_1h_threshold | +2.34% | +2.21% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.96% | +1.84% |
| ADA/USDT:USDT | below_1h_threshold | +1.81% | +1.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
