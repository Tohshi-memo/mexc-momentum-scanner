# Decision Report

- generated_at: 2026-06-29T08:51:36.812018+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7804**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7804, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +0.42% | **+0.17%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.62% | **+0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.03% | **-0.00%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.24% | **+0.68%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.14** / 初期 $100.00 (+2.14%)
- 確定トレード: 42件 (TP 15 / SL 26 / EXP 1)
- 最新: G/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$260.69** / 初期 $100.00 (+160.69%)
- 確定: 2308件 (Win 701 / Loss 768 / Flat 839) / skip 2057件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_9PCT` EXPIRED account +0.00% 残高後 $260.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 759件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T08:51:29.780479+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=59876.9
- Funnel: target 810 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +98.65% | $4,702,250.95 |
| RAVE/USDT:USDT | +58.24% | $33,471,594.82 |
| G/USDT:USDT | +17.57% | $1,991,897.89 |
| HIGH/USDT:USDT | +14.86% | $1,602,391.65 |
| UB/USDT:USDT | +14.29% | $1,454,601.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.16% | +3.37% |
| BEAT/USDT:USDT | below_1h_threshold | +2.41% | +2.62% |
| INJ/USDT:USDT | below_1h_threshold | +0.92% | +1.12% |
| WIF/USDT:USDT | below_1h_threshold | +0.88% | +1.09% |
| SOXL/USDT:USDT | below_1h_threshold | +0.83% | +1.03% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
