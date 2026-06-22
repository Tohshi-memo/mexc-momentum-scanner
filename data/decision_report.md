# Decision Report

- generated_at: 2026-06-22T06:32:49.435669+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7351**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7351, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.43% | **-1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.47% | **+0.19%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| ASK_LONG | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.42% | **+1.70%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.98% | **+0.89%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2032件 (Win 599 / Loss 668 / Flat 765) / skip 1880件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 451件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T06:32:42.625288+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=64099.5
- Funnel: target 802 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +41.20% | $5,353,093.72 |
| UB/USDT:USDT | +36.91% | $10,214,959.05 |
| CLO/USDT:USDT | +26.19% | $3,818,288.55 |
| ZEST/USDT:USDT | +24.39% | $1,093,461.02 |
| NAORIS/USDT:USDT | +18.42% | $5,350,208.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.00% | +4.19% |
| MMT/USDT:USDT | below_1h_threshold | +2.99% | +3.18% |
| ALLO/USDT:USDT | below_1h_threshold | +2.83% | +3.02% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.81% | +2.99% |
| BLESS/USDT:USDT | below_1h_threshold | +2.40% | +2.59% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
