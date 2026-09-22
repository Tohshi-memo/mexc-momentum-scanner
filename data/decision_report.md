# Decision Report

- generated_at: 2026-09-22T12:36:20.885284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15326**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15326, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/16 | 50.0% | +2.45% | **+1.23%** |
| LIMIT_2PCT | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.80% | **+0.76%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.02% | **+0.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,174.97** / 初期 $100.00 (+1074.97%)
- 確定: 5817件 (Win 1726 / Loss 1872 / Flat 2219) / skip 6070件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,174.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5384件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.36** / 初期 $100.00 (+22.36%)
- 確定: 3096件 (Win 908 / Loss 1211 / Flat 977) / pending 3件 / skip 3697件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000156 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.36

## 6. Latest Market Context

- 更新: 2026-09-22T12:36:07.951324+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=85979.3
- Funnel: target 1058 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +60.04% | $3,489,279.57 |
| MUBARAK/USDT:USDT | +53.41% | $5,058,663.31 |
| NIL/USDT:USDT | +27.37% | $3,642,375.52 |
| KERNEL/USDT:USDT | +26.91% | $5,319,557.75 |
| AGT/USDT:USDT | +25.50% | $1,889,045.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +5.00% | +4.96% |
| MUBARAK/USDT:USDT | below_1h_threshold | +3.82% | +3.78% |
| WIF/USDT:USDT | below_1h_threshold | +3.17% | +3.13% |
| BCH/USDT:USDT | below_1h_threshold | +2.10% | +2.07% |
| NEAR/USDT:USDT | below_1h_threshold | +1.78% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
