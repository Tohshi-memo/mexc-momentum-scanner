# Decision Report

- generated_at: 2026-09-11T11:31:57.760139+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14214**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=14214, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.51% | **+0.38%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.30% | **-0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.61% | **-0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.52% | **+0.45%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.81% | **+0.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.44% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,067.54** / 初期 $100.00 (+967.54%)
- 確定: 5379件 (Win 1619 / Loss 1739 / Flat 2021) / skip 5396件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.83% 残高後 $1,067.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2804件 (Win 770 / Loss 650 / Flat 1384) / skip 4821件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.86** / 初期 $100.00 (+22.86%)
- 確定: 2717件 (Win 802 / Loss 1040 / Flat 875) / pending 4件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000182 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.86

## 6. Latest Market Context

- 更新: 2026-09-11T11:31:45.310435+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=76812.5
- Funnel: target 1068 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +58.30% | $1,144,944.62 |
| NIULAI/USDT:USDT | +50.47% | $18,225,326.37 |
| RAY/USDT:USDT | +19.21% | $19,984,474.82 |
| LSK/USDT:USDT | +18.27% | $2,267,793.12 |
| CNPY/USDT:USDT | +16.43% | $2,788,443.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.57% | +1.76% |
| UAI/USDT:USDT | below_1h_threshold | +1.22% | +1.41% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.86% | +1.06% |
| BTR/USDT:USDT | below_1h_threshold | +0.81% | +1.01% |
| VVV/USDT:USDT | below_1h_threshold | +0.70% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
