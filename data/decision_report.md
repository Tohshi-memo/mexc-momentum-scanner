# Decision Report

- generated_at: 2026-09-28T18:36:21.164416+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15742**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=15742, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.21% | **+1.88%** |
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_BB3S | 6/16 | 37.5% | +3.22% | **+1.21%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.26% | **-0.17%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.27% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5983件 (Win 1766 / Loss 1925 / Flat 2292) / skip 6320件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5619件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.79** / 初期 $100.00 (+17.79%)
- 確定: 3305件 (Win 957 / Loss 1300 / Flat 1048) / pending 3件 / skip 3908件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000126 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $117.79

## 6. Latest Market Context

- 更新: 2026-09-28T18:36:09.840505+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=83839.0
- Funnel: target 1066 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CRV/USDT:USDT | +10.70% | $6,973,440.29 |
| MARSCOIN/USDT:USDT | +8.11% | $3,879,428.32 |
| GRASS/USDT:USDT | +7.90% | $5,592,854.74 |
| QNT/USDT:USDT | +7.66% | $344,047,027.70 |
| BTW/USDT:USDT | +6.45% | $17,682,550.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +3.97% | +3.97% |
| XLM/USDT:USDT | below_1h_threshold | +3.37% | +3.37% |
| XDC/USDT:USDT | below_1h_threshold | +3.27% | +3.27% |
| BTW/USDT:USDT | below_1h_threshold | +1.93% | +1.93% |
| UAI/USDT:USDT | below_1h_threshold | +1.83% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
