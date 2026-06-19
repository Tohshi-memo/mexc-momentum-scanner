# Decision Report

- generated_at: 2026-06-19T09:39:28.654292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7116**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=7116, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.85% | **+0.26%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.28% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| MARKET_LONG | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.20% | **-0.07%** |
| ASK_LONG | 20/20 | 100.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.50** / 初期 $100.00 (+120.50%)
- 確定: 1936件 (Win 553 / Loss 625 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $220.50

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 218件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T09:39:24.281028+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=62395.6
- Funnel: target 795 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +74.28% | $8,077,116.34 |
| HEI/USDT:USDT | +61.17% | $6,327,729.90 |
| BTW/USDT:USDT | +27.74% | $3,245,098.08 |
| ZEREBRO/USDT:USDT | +17.48% | $3,966,448.19 |
| BASED/USDT:USDT | +15.01% | $7,362,216.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.53% | +4.81% |
| HEI/USDT:USDT | below_1h_threshold | +3.70% | +3.99% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.03% | +2.31% |
| ENJ/USDT:USDT | below_1h_threshold | +1.01% | +1.29% |
| VVV/USDT:USDT | below_1h_threshold | +0.95% | +1.23% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
