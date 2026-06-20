# Decision Report

- generated_at: 2026-06-20T05:33:42.567100+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7207**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=7207, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_BB3S | 2/17 | 11.8% | +6.74% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.86% | **+0.78%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.73% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.06% | **-0.03%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.34% | **-0.19%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.61% | **-0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.84** / 初期 $100.00 (+124.84%)
- 確定: 1970件 (Win 571 / Loss 641 / Flat 758) / skip 1798件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $224.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 308件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T05:33:36.922663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=63672.2
- Funnel: target 795 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +43.13% | $18,092,682.82 |
| BICO/USDT:USDT | +42.61% | $20,413,384.14 |
| BLESS/USDT:USDT | +26.42% | $5,977,528.80 |
| AXS/USDT:USDT | +20.42% | $3,689,280.98 |
| EIGEN/USDT:USDT | +18.76% | $6,788,633.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +4.34% | +4.16% |
| RIF/USDT:USDT | below_1h_threshold | +4.05% | +3.86% |
| EVAA/USDT:USDT | below_1h_threshold | +1.97% | +1.79% |
| VVV/USDT:USDT | below_1h_threshold | +1.63% | +1.44% |
| BSB/USDT:USDT | below_1h_threshold | +1.29% | +1.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
