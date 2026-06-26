# Decision Report

- generated_at: 2026-06-26T13:42:39.459599+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7631**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=7631, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_BB3S | 3/14 | 21.4% | +1.33% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$226.81** / 初期 $100.00 (+126.81%)
- 確定: 2157件 (Win 636 / Loss 715 / Flat 806) / skip 2035件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $226.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 660件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T13:42:33.913029+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=59208.4
- Funnel: target 806 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +60.50% | $4,501,975.10 |
| ICNT/USDT:USDT | +45.51% | $2,896,270.38 |
| VELVET/USDT:USDT | +35.74% | $7,328,287.33 |
| HEI/USDT:USDT | +28.53% | $9,557,232.24 |
| IDOL/USDT:USDT | +19.83% | $1,469,010.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_relative_strength | +5.00% | +4.93% |
| PAYPSTOCK/USDT:USDT | below_1h_threshold | +3.81% | +3.73% |
| IDOL/USDT:USDT | below_1h_threshold | +3.18% | +3.11% |
| UB/USDT:USDT | below_1h_threshold | +3.11% | +3.03% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +3.03% | +2.96% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
