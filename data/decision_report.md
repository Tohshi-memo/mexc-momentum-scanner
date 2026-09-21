# Decision Report

- generated_at: 2026-09-21T15:26:25.844745+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15266**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15266, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.54% | **-1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.07% | **+0.85%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.66% | **+0.78%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.74% | **+2.24%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.78% | **+1.94%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.17% | **+1.90%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,189.76** / 初期 $100.00 (+1089.76%)
- 確定: 5757件 (Win 1715 / Loss 1850 / Flat 2192) / skip 6070件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEPE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,189.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3315件 (Win 915 / Loss 765 / Flat 1635) / skip 5362件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0228 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.11** / 初期 $100.00 (+23.11%)
- 確定: 3042件 (Win 895 / Loss 1189 / Flat 958) / pending 5件 / skip 3691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000182 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.11

## 6. Latest Market Context

- 更新: 2026-09-21T15:26:14.622129+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=85863.7
- Funnel: target 1055 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +62.29% | $9,796,092.09 |
| MUBARAK/USDT:USDT | +40.40% | $1,146,616.05 |
| PHA/USDT:USDT | +36.92% | $7,136,548.38 |
| NIL/USDT:USDT | +32.41% | $8,147,559.60 |
| STONK/USDT:USDT | +28.42% | $1,067,209.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.04% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.38% | +2.31% |
| SOXL/USDT:USDT | below_1h_threshold | +2.06% | +1.99% |
| USELESS/USDT:USDT | below_1h_threshold | +1.92% | +1.86% |
| MVLL/USDT:USDT | below_1h_threshold | +1.88% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
