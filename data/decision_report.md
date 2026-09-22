# Decision Report

- generated_at: 2026-09-22T07:46:29.262690+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15306**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15306, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/16 | 43.8% | +3.28% | **+1.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.24% | **+0.90%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.94% | **+0.85%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,181.05** / 初期 $100.00 (+1081.05%)
- 確定: 5797件 (Win 1724 / Loss 1867 / Flat 2206) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,181.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.12** / 初期 $100.00 (+149.12%)
- 確定: 3345件 (Win 924 / Loss 778 / Flat 1643) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $249.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.87** / 初期 $100.00 (+22.87%)
- 確定: 3078件 (Win 905 / Loss 1205 / Flat 968) / pending 4件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.87

## 6. Latest Market Context

- 更新: 2026-09-22T07:46:16.938638+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=85292.6
- Funnel: target 1056 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1, 4h RSI 77.8 >= 65=1, 4h RSI 92.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +51.90% | $1,046,298.10 |
| 4STOCK/USDT:USDT | +39.95% | $1,586,891.79 |
| KERNEL/USDT:USDT | +39.47% | $3,322,747.81 |
| GRASS/USDT:USDT | +19.43% | $2,975,377.26 |
| ALCH/USDT:USDT | +19.32% | $2,612,984.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WIF/USDT:USDT | below_1h_threshold | +3.00% | +3.07% |
| AKT/USDT:USDT | below_1h_threshold | +2.47% | +2.54% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.30% | +2.37% |
| SEI/USDT:USDT | below_1h_threshold | +2.27% | +2.34% |
| HBAR/USDT:USDT | below_1h_threshold | +2.17% | +2.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
