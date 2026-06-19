# Decision Report

- generated_at: 2026-06-19T00:26:12.471812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7087**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7087, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.29% | **-0.12%** |
| ASK | 20/20 | 100.0% | -0.28% | **-0.28%** |
| LIMIT_5PCT | 7/20 | 35.0% | -1.17% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.61% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.18% | **+0.65%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$103.51** / 初期 $100.00 (+3.51%)
- 確定トレード: 17件 (TP 8 / SL 9 / EXP 0)
- 最新: BEAT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.41** / 初期 $100.00 (+124.41%)
- 確定: 1907件 (Win 544 / Loss 611 / Flat 752) / skip 1741件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $224.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 190件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T00:26:09.086227+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=62924.6
- Funnel: target 795 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +95.67% | $4,978,164.84 |
| BASED/USDT:USDT | +24.90% | $2,892,965.67 |
| ZEREBRO/USDT:USDT | +23.09% | $2,999,461.74 |
| EDEN/USDT:USDT | +16.89% | $2,006,362.42 |
| EIGEN/USDT:USDT | +12.57% | $3,147,892.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IP/USDT:USDT | below_1h_threshold | +3.06% | +3.06% |
| BASED/USDT:USDT | below_1h_threshold | +2.93% | +2.93% |
| WLD/USDT:USDT | below_1h_threshold | +2.85% | +2.85% |
| RENDER/USDT:USDT | below_1h_threshold | +2.63% | +2.62% |
| VELVET/USDT:USDT | below_1h_threshold | +2.11% | +2.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
