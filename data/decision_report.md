# Decision Report

- generated_at: 2026-06-26T17:26:43.345808+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7646**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7646, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.82% | **-1.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_BB3S | 5/10 | 50.0% | +1.05% | **+0.52%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.19% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.59% | **+1.12%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.86% | **+0.57%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +1.28% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.35** / 初期 $100.00 (+131.35%)
- 確定: 2171件 (Win 645 / Loss 720 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $231.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 675件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T17:26:38.708434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=60083.4
- Funnel: target 806 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +5.75% | $2,535,310.18 |
| O/USDT:USDT | +4.97% | $3,921,431.01 |
| AAVE/USDT:USDT | +4.50% | $62,868,396.52 |
| MYX/USDT:USDT | +4.50% | $2,092,821.04 |
| JTO/USDT:USDT | +4.42% | $8,147,909.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +3.98% | +3.88% |
| JTO/USDT:USDT | below_1h_threshold | +2.16% | +2.06% |
| JUP/USDT:USDT | below_1h_threshold | +1.84% | +1.74% |
| AVAX/USDT:USDT | below_1h_threshold | +1.79% | +1.68% |
| USELESS/USDT:USDT | below_1h_threshold | +1.65% | +1.54% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
