# Decision Report

- generated_at: 2026-09-11T14:36:29.709978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14227**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=14227, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 4/13 | 30.8% | +0.88% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.31% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.62% | **+1.16%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.41% | **+1.08%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.58%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,072.94** / 初期 $100.00 (+972.94%)
- 確定: 5386件 (Win 1622 / Loss 1742 / Flat 2022) / skip 5402件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,072.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2805件 (Win 770 / Loss 650 / Flat 1385) / skip 4833件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0004 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.38** / 初期 $100.00 (+23.38%)
- 確定: 2727件 (Win 806 / Loss 1044 / Flat 877) / pending 6件 / skip 2968件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.38

## 6. Latest Market Context

- 更新: 2026-09-11T14:36:15.499998+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=78766.5
- Funnel: target 1067 → liquid 164 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1, 4h RSI 89.9 >= 65=1, 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STONK/USDT:USDT | +71.15% | $1,201,817.91 |
| NIULAI/USDT:USDT | +64.12% | $21,835,292.10 |
| STORJ/USDT:USDT | +59.95% | $4,981,743.64 |
| RAY/USDT:USDT | +25.60% | $24,838,965.03 |
| CNPY/USDT:USDT | +23.38% | $2,898,500.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.62% | +3.18% |
| LAB/USDT:USDT | below_1h_threshold | +2.04% | +2.60% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +1.87% | +2.42% |
| BTW/USDT:USDT | below_1h_threshold | +1.60% | +2.15% |
| NEAR/USDT:USDT | below_1h_threshold | +1.51% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
