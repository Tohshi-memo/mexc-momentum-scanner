# Decision Report

- generated_at: 2026-09-20T15:11:19.172611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15189**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=15189, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.94% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +6.37% | **+1.27%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.02% | **+0.81%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.88% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,179.53** / 初期 $100.00 (+1079.53%)
- 確定: 5715件 (Win 1705 / Loss 1844 / Flat 2166) / skip 6035件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CELR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,179.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.68** / 初期 $100.00 (+147.68%)
- 確定: 3290件 (Win 911 / Loss 764 / Flat 1615) / skip 5310件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $247.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.42** / 初期 $100.00 (+21.42%)
- 確定: 2979件 (Win 881 / Loss 1179 / Flat 919) / pending 1件 / skip 3677件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000141 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CELR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.04% 残高後 $121.42

## 6. Latest Market Context

- 更新: 2026-09-20T15:11:08.400494+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=80793.4
- Funnel: target 1050 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +62.32% | $8,807,279.73 |
| OFC/USDT:USDT | +22.75% | $2,579,939.56 |
| SAGA/USDT:USDT | +21.84% | $2,068,514.56 |
| BTW/USDT:USDT | +20.76% | $2,871,727.63 |
| ONE/USDT:USDT | +19.25% | $56,214,408.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.93% | +4.75% |
| AVAX/USDT:USDT | below_1h_threshold | +3.63% | +3.45% |
| HBAR/USDT:USDT | below_1h_threshold | +2.65% | +2.47% |
| ALGO/USDT:USDT | below_1h_threshold | +2.64% | +2.46% |
| EVAA/USDT:USDT | below_1h_threshold | +2.62% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
