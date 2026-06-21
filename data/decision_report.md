# Decision Report

- generated_at: 2026-06-21T12:58:44.177032+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7308**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=7308, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 8/20 | 40.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.83% | **+0.58%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.54% | **+0.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.48% | **+0.36%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.16% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2030件 (Win 599 / Loss 668 / Flat 763) / skip 1839件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 408件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-21T12:58:36.668572+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64175.5
- Funnel: target 796 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TNSR/USDT:USDT | +73.66% | $11,992,502.52 |
| UB/USDT:USDT | +25.45% | $2,255,096.76 |
| BULLA/USDT:USDT | +22.55% | $1,428,839.12 |
| LAB/USDT:USDT | +21.22% | $30,392,466.87 |
| BICO/USDT:USDT | +20.72% | $52,695,624.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +3.56% | +3.52% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.50% | +3.46% |
| UB/USDT:USDT | below_1h_threshold | +3.03% | +2.99% |
| ZRO/USDT:USDT | below_1h_threshold | +2.66% | +2.62% |
| BULLA/USDT:USDT | below_1h_threshold | +2.40% | +2.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
