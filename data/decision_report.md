# Decision Report

- generated_at: 2026-07-03T09:16:55.494389+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8149**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8149, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.51% | **-0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.92% | **-0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| LIMIT_BB3S | 3/17 | 17.6% | -1.56% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.49% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.98% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.44** / 初期 $100.00 (+184.44%)
- 確定: 2470件 (Win 759 / Loss 823 / Flat 888) / skip 2240件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEX/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $284.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 599件 (Win 144 / Loss 142 / Flat 313) / skip 961件
- 成長率目線: 平均log +0.000098 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0003 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NEX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-07-03T09:16:50.683947+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=61686.9
- Funnel: target 834 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARPA/USDT:USDT | +41.96% | $1,035,192.81 |
| NEX/USDT:USDT | +38.29% | $1,681,719.67 |
| RIF/USDT:USDT | +36.88% | $8,021,087.67 |
| ZKP/USDT:USDT | +29.09% | $4,130,269.58 |
| MAGMA/USDT:USDT | +25.20% | $6,845,046.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARPA/USDT:USDT | below_1h_threshold | +2.88% | +2.66% |
| PENGU/USDT:USDT | below_1h_threshold | +1.84% | +1.62% |
| TIA/USDT:USDT | below_1h_threshold | +1.68% | +1.47% |
| ZKP/USDT:USDT | below_1h_threshold | +1.37% | +1.15% |
| CHZ/USDT:USDT | below_1h_threshold | +1.19% | +0.98% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
