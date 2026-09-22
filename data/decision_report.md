# Decision Report

- generated_at: 2026-09-22T13:11:21.274812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15330**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=15330, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.86% | **+0.82%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.68% | **+0.58%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.70% | **+0.46%** |
| LIMIT_BB3S | 7/16 | 43.8% | +0.77% | **+0.34%** |
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.06% | **-0.03%** |
| MARKET_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.49** / 初期 $100.00 (+1069.49%)
- 確定: 5820件 (Win 1727 / Loss 1873 / Flat 2220) / skip 6071件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BCH/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.03% 残高後 $1,169.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5388件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.14** / 初期 $100.00 (+22.14%)
- 確定: 3100件 (Win 909 / Loss 1214 / Flat 977) / pending 3件 / skip 3697件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: WIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.14

## 6. Latest Market Context

- 更新: 2026-09-22T13:11:11.760648+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=86092.6
- Funnel: target 1058 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +57.20% | $3,596,513.76 |
| MUBARAK/USDT:USDT | +50.68% | $5,561,087.52 |
| AGT/USDT:USDT | +29.29% | $1,922,302.83 |
| KERNEL/USDT:USDT | +24.70% | $5,569,088.05 |
| NIL/USDT:USDT | +24.07% | $3,745,796.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4STOCK/USDT:USDT | below_1h_threshold | +3.13% | +3.01% |
| ETC/USDT:USDT | below_1h_threshold | +2.52% | +2.40% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.41% | +2.29% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.11% | +1.99% |
| BCH/USDT:USDT | below_1h_threshold | +2.11% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
