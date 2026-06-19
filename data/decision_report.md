# Decision Report

- generated_at: 2026-06-19T13:56:34.136513+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7144**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7144, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.32% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.06% | **+1.65%** |
| MARKET_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| ASK_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.29% | **+0.16%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.16% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.71** / 初期 $100.00 (+131.71%)
- 確定: 1964件 (Win 571 / Loss 635 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $231.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 246件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T13:56:29.529976+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.65% price=63208.4
- Funnel: target 795 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +82.70% | $8,912,166.22 |
| HEI/USDT:USDT | +51.26% | $11,723,281.70 |
| RE/USDT:USDT | +50.88% | $44,853,166.26 |
| BTW/USDT:USDT | +44.26% | $4,184,713.11 |
| ZEREBRO/USDT:USDT | +39.80% | $4,960,903.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_relative_strength | +5.60% | +4.95% |
| ORDI/USDT:USDT | below_relative_strength | +5.49% | +4.84% |
| BLESS/USDT:USDT | below_1h_threshold | +3.87% | +3.22% |
| AERO/USDT:USDT | below_1h_threshold | +3.55% | +2.90% |
| ENJ/USDT:USDT | below_1h_threshold | +3.13% | +2.48% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
