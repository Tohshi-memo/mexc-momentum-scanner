# Decision Report

- generated_at: 2026-06-19T09:50:30.596311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7117**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=7117, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.03% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.05% | **+0.03%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.03% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.40** / 初期 $100.00 (+119.40%)
- 確定: 1937件 (Win 553 / Loss 626 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $219.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 219件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T09:50:24.808910+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=62318.6
- Funnel: target 795 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 78.7 >= 65=1, 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +74.17% | $8,107,194.58 |
| HEI/USDT:USDT | +63.36% | $6,502,254.73 |
| BTW/USDT:USDT | +27.45% | $3,260,241.09 |
| ZEREBRO/USDT:USDT | +19.07% | $3,977,481.60 |
| RE/USDT:USDT | +17.92% | $21,323,667.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.46% | +3.86% |
| RIF/USDT:USDT | below_1h_threshold | +0.91% | +1.32% |
| UNI/USDT:USDT | below_1h_threshold | +0.82% | +1.23% |
| XMR/USDT:USDT | below_1h_threshold | +0.77% | +1.18% |
| PLAY/USDT:USDT | below_1h_threshold | +0.66% | +1.06% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
