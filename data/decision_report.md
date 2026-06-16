# Decision Report

- generated_at: 2026-06-16T04:05:56.311463+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6836**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6836, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +5.87% | **+0.88%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.15% | **+0.40%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.37% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| ASK_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.20% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$181.96** / 初期 $100.00 (+81.96%)
- 確定: 1709件 (Win 446 / Loss 534 / Flat 729) / skip 1688件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUFFER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $181.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 92件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T04:05:52.118784+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=66248.6
- Funnel: target 772 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +39.82% | $2,858,099.18 |
| ASTEROID/USDT:USDT | +23.64% | $6,367,232.08 |
| SPACE/USDT:USDT | +20.07% | $1,589,872.72 |
| SPCXSTOCK/USDT:USDT | +19.78% | $441,156,695.71 |
| PUFFER/USDT:USDT | +18.82% | $1,438,978.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.55% | +1.36% |
| AERO/USDT:USDT | below_1h_threshold | +1.44% | +1.25% |
| SPACE/USDT:USDT | below_1h_threshold | +1.18% | +0.99% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.17% | +0.99% |
| RIF/USDT:USDT | below_1h_threshold | +0.89% | +0.70% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
