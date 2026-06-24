# Decision Report

- generated_at: 2026-06-24T22:47:47.922093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7507**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7507, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.54% | **-1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.07% | **+0.02%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.08% | **-0.07%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.21% | **-0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.14% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.04% | **+1.82%** |
| ASK_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.71%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.92% | **+1.61%** |

## 2. $100 Live Portfolio

- 残高: **$102.43** / 初期 $100.00 (+2.43%)
- 確定トレード: 37件 (TP 14 / SL 23 / EXP 0)
- 最新: KORU/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1947件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 569件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T22:47:41.079023+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=60829.8
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KORU/USDT:USDT | +22.98% | $4,912,752.62 |
| O/USDT:USDT | +17.37% | $8,862,656.34 |
| DRAM/USDT:USDT | +15.55% | $8,023,269.46 |
| MUSTOCK/USDT:USDT | +14.66% | $91,310,394.44 |
| MVLL/USDT:USDT | +14.25% | $2,409,318.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.43% | +3.83% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.46% | +2.86% |
| MVLL/USDT:USDT | below_1h_threshold | +1.66% | +2.06% |
| DRAM/USDT:USDT | below_1h_threshold | +1.48% | +1.88% |
| DYDX/USDT:USDT | below_1h_threshold | +1.29% | +1.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
