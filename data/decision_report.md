# Decision Report

- generated_at: 2026-06-22T00:34:30.297093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7336**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7336, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 18/20 | 90.0% | +0.55% | **+0.50%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.75% | **+1.75%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.00% | **+1.70%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.24% | **+0.74%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.55% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2031件 (Win 599 / Loss 668 / Flat 764) / skip 1866件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 436件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T00:32:03.299374+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.78% price=63780.0
- Funnel: target 796 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NAORIS/USDT:USDT | +30.19% | $3,530,055.25 |
| LAB/USDT:USDT | +23.03% | $43,730,201.10 |
| SYN/USDT:USDT | +15.02% | $2,850,532.09 |
| UB/USDT:USDT | +14.90% | $7,101,045.91 |
| BEL/USDT:USDT | +14.40% | $1,034,691.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_relative_strength | +5.40% | +4.62% |
| EIGEN/USDT:USDT | below_1h_threshold | +4.22% | +3.44% |
| BSB/USDT:USDT | below_1h_threshold | +3.70% | +2.92% |
| BEL/USDT:USDT | below_1h_threshold | +3.24% | +2.46% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +2.71% | +1.93% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
