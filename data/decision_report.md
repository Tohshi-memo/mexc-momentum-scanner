# Decision Report

- generated_at: 2026-09-11T12:26:23.085219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14216**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.99% / filled 20/20。**
- 全期間 MARKET基準: n=14216, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.14% | **+0.43%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.32% | **-0.18%** |
| LIMIT_2PCT | 13/20 | 65.0% | -0.55% | **-0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.81% | **+0.38%** |
| MARKET_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.09% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,067.75** / 初期 $100.00 (+967.75%)
- 確定: 5381件 (Win 1620 / Loss 1740 / Flat 2021) / skip 5396件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CNPY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,067.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2804件 (Win 770 / Loss 650 / Flat 1384) / skip 4823件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.64** / 初期 $100.00 (+22.64%)
- 確定: 2719件 (Win 802 / Loss 1041 / Flat 876) / pending 4件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.64

## 6. Latest Market Context

- 更新: 2026-09-11T12:26:12.568362+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=76969.6
- Funnel: target 1068 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +62.21% | $2,233,858.84 |
| NIULAI/USDT:USDT | +55.61% | $19,580,055.82 |
| STONK/USDT:USDT | +48.90% | $1,052,243.98 |
| MET/USDT:USDT | +22.91% | $1,229,201.29 |
| CNPY/USDT:USDT | +19.81% | $2,809,036.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +2.33% | +2.37% |
| LSK/USDT:USDT | below_1h_threshold | +1.91% | +1.95% |
| LAB/USDT:USDT | below_1h_threshold | +1.35% | +1.39% |
| SOXL/USDT:USDT | below_1h_threshold | +0.64% | +0.68% |
| NIULAI/USDT:USDT | below_1h_threshold | +0.54% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
