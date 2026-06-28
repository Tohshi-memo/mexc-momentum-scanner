# Decision Report

- generated_at: 2026-06-28T07:02:36.007428+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7733**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7733, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.04% | **+0.76%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.48% | **-0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| ASK_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +0.35% | **+0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$245.55** / 初期 $100.00 (+145.55%)
- 確定: 2241件 (Win 678 / Loss 748 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $245.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 689件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T07:02:30.349255+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=60157.2
- Funnel: target 805 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +39.50% | $5,087,065.01 |
| BAS/USDT:USDT | +30.01% | $3,816,421.74 |
| LAB/USDT:USDT | +18.29% | $37,908,803.51 |
| S/USDT:USDT | +18.15% | $5,493,654.97 |
| POWR/USDT:USDT | +18.06% | $2,235,049.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +2.39% | +2.08% |
| O/USDT:USDT | below_1h_threshold | +1.91% | +1.60% |
| VELVET/USDT:USDT | below_1h_threshold | +1.76% | +1.45% |
| S/USDT:USDT | below_1h_threshold | +1.04% | +0.73% |
| BASED/USDT:USDT | below_1h_threshold | +0.75% | +0.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
