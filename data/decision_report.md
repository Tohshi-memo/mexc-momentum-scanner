# Decision Report

- generated_at: 2026-06-13T19:03:49.223275+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6605**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6605, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.44% | **+1.34%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.97% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.36** / 初期 $100.00 (+67.36%)
- 確定: 1478件 (Win 397 / Loss 470 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $167.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.68** / 初期 $100.00 (-0.32%)
- 確定: 16件 (Win 5 / Loss 6 / Flat 5) / skip 0件
- 成長率目線: 平均log -0.000201 / 幾何平均 -0.020% per trade / maxDD +1.05%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0389 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $99.68

## 5. Latest Market Context

- 更新: 2026-06-13T19:03:43.440847+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64151.6
- Funnel: target 770 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +17.33% | $61,309,296.37 |
| RIF/USDT:USDT | +12.19% | $6,882,479.58 |
| AT/USDT:USDT | +11.34% | $1,027,335.12 |
| COAI/USDT:USDT | +6.40% | $24,768,837.59 |
| BTW/USDT:USDT | +5.01% | $1,503,152.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +0.87% | +0.82% |
| AT/USDT:USDT | below_1h_threshold | +0.69% | +0.65% |
| MEGA/USDT:USDT | below_1h_threshold | +0.52% | +0.47% |
| SITMSTOCK/USDT:USDT | below_1h_threshold | +0.36% | +0.32% |
| CHZ/USDT:USDT | below_1h_threshold | +0.35% | +0.31% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
