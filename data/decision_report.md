# Decision Report

- generated_at: 2026-06-22T19:59:07.543218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7394**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=7394, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.44% | **+0.94%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.47% | **+0.38%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.72** / 初期 $100.00 (+132.72%)
- 確定: 2050件 (Win 607 / Loss 675 / Flat 768) / skip 1905件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.07% 残高後 $232.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 493件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T19:58:59.720101+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=64449.4
- Funnel: target 808 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +15.52% | $27,388,111.78 |
| BLESS/USDT:USDT | +15.40% | $6,950,696.37 |
| VELVET/USDT:USDT | +15.03% | $12,046,395.31 |
| SYN/USDT:USDT | +12.76% | $27,805,104.91 |
| LAB/USDT:USDT | +12.39% | $40,116,314.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +3.32% | +3.11% |
| LRCXSTOCK/USDT:USDT | below_1h_threshold | +3.07% | +2.86% |
| SOXL/USDT:USDT | below_1h_threshold | +3.05% | +2.84% |
| LAB/USDT:USDT | below_1h_threshold | +3.03% | +2.82% |
| BLESS/USDT:USDT | below_1h_threshold | +2.99% | +2.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
