# Decision Report

- generated_at: 2026-09-11T14:56:42.092199+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14229**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=14229, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 4/14 | 28.6% | +0.88% | **+0.25%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.62% | **+1.35%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.46% | **+1.11%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.58%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.81% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.25** / 初期 $100.00 (+978.25%)
- 確定: 5388件 (Win 1623 / Loss 1743 / Flat 2022) / skip 5402件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,078.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.79** / 初期 $100.00 (+107.79%)
- 確定: 2806件 (Win 770 / Loss 651 / Flat 1385) / skip 4834件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $207.79

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.49** / 初期 $100.00 (+23.49%)
- 確定: 2729件 (Win 807 / Loss 1045 / Flat 877) / pending 6件 / skip 2969件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.49

## 6. Latest Market Context

- 更新: 2026-09-11T14:56:22.962871+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.54% price=78776.7
- Funnel: target 1067 → liquid 167 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.4 >= 65=1, 4h RSI 76.8 >= 65=1, 4h RSI 70.2 >= 65=1, 4h RSI 89.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STONK/USDT:USDT | +72.49% | $1,216,556.97 |
| NIULAI/USDT:USDT | +71.17% | $22,314,516.07 |
| STORJ/USDT:USDT | +58.66% | $5,178,420.95 |
| RAY/USDT:USDT | +26.76% | $25,312,730.56 |
| CNPY/USDT:USDT | +21.74% | $2,917,188.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.62% | +3.16% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +1.87% | +2.41% |
| JUP/USDT:USDT | below_1h_threshold | +1.81% | +2.35% |
| LIT/USDT:USDT | below_1h_threshold | +1.48% | +2.02% |
| RAY/USDT:USDT | below_1h_threshold | +1.34% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
