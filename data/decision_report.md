# Decision Report

- generated_at: 2026-06-18T18:07:47.238830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7067**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=7067, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.23% | **+2.01%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.25% | **+1.91%** |
| ASK | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_BB3S | 6/19 | 31.6% | +4.92% | **+1.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.78% | **+0.80%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.28% | **+0.16%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.22% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.47** / 初期 $100.00 (+1.47%)
- 確定トレード: 15件 (TP 6 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.47
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$217.85** / 初期 $100.00 (+117.85%)
- 確定: 1888件 (Win 533 / Loss 604 / Flat 751) / skip 1740件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $217.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 170件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T18:07:40.540986+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=62670.7
- Funnel: target 795 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +24.05% | $26,486,112.95 |
| PLAY/USDT:USDT | +9.81% | $1,556,930.63 |
| FOLKS/USDT:USDT | +6.48% | $5,965,150.65 |
| ESPORTS/USDT:USDT | +6.46% | $51,504,381.17 |
| MYX/USDT:USDT | +6.20% | $3,659,431.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +1.87% | +1.72% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.34% | +1.20% |
| RIF/USDT:USDT | below_1h_threshold | +1.09% | +0.95% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.99% | +0.84% |
| PLAY/USDT:USDT | below_1h_threshold | +0.85% | +0.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
