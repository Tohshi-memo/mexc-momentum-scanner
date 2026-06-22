# Decision Report

- generated_at: 2026-06-22T02:05:21.727806+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7344**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7344, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.10% | **+0.04%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_2PCT | 18/20 | 90.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |
| ASK_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.73% | **+1.30%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.29% | **+0.12%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.60** / 初期 $100.00 (+130.60%)
- 確定: 2032件 (Win 599 / Loss 668 / Flat 765) / skip 1873件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $230.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 311件 (Win 89 / Loss 87 / Flat 135) / skip 444件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SLX/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T02:05:16.264880+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64544.1
- Funnel: target 796 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +41.64% | $3,415,840.95 |
| NAORIS/USDT:USDT | +27.50% | $4,095,080.77 |
| BEL/USDT:USDT | +15.99% | $1,037,414.53 |
| CLO/USDT:USDT | +14.39% | $4,042,101.98 |
| UB/USDT:USDT | +14.25% | $7,468,305.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.08% | +4.13% |
| SYN/USDT:USDT | below_1h_threshold | +1.92% | +1.97% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.87% | +1.92% |
| BILL/USDT:USDT | below_1h_threshold | +0.79% | +0.84% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.76% | +0.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
