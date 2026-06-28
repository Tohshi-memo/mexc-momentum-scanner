# Decision Report

- generated_at: 2026-06-28T03:56:47.567397+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7728**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7728, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 3/16 | 18.8% | -0.00% | **-0.00%** |
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |
| ASK | 20/20 | 100.0% | -0.05% | **-0.05%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.15% | **-0.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$240.71** / 初期 $100.00 (+140.71%)
- 確定: 2236件 (Win 674 / Loss 747 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $240.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 455件 (Win 120 / Loss 119 / Flat 216) / skip 684件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-28T03:56:40.149886+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60146.0
- Funnel: target 806 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POWR/USDT:USDT | +18.20% | $1,543,987.70 |
| LAB/USDT:USDT | +16.32% | $40,760,860.24 |
| BAS/USDT:USDT | +15.75% | $3,304,526.22 |
| S/USDT:USDT | +12.41% | $4,874,866.13 |
| BASED/USDT:USDT | +12.25% | $1,314,242.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +3.71% | +3.67% |
| ALLO/USDT:USDT | below_1h_threshold | +3.07% | +3.03% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.57% | +2.53% |
| BASED/USDT:USDT | below_1h_threshold | +2.46% | +2.42% |
| S/USDT:USDT | below_1h_threshold | +2.39% | +2.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
