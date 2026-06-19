# Decision Report

- generated_at: 2026-06-19T03:03:18.155246+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7096**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7096, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.29% | **+0.26%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| ASK | 20/20 | 100.0% | -0.12% | **-0.12%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.77% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.26% | **+0.95%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.79% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.56% | **+0.51%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.55% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.16** / 初期 $100.00 (+122.16%)
- 確定: 1916件 (Win 547 / Loss 616 / Flat 753) / skip 1741件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $222.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 199件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T03:03:12.083576+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=62948.7
- Funnel: target 795 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +88.85% | $6,195,427.38 |
| BASED/USDT:USDT | +37.02% | $4,418,224.83 |
| ZEREBRO/USDT:USDT | +20.87% | $3,444,174.11 |
| EDEN/USDT:USDT | +18.09% | $2,227,831.29 |
| LAB/USDT:USDT | +15.98% | $34,643,519.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.56% | +3.60% |
| COAI/USDT:USDT | below_1h_threshold | +1.29% | +1.33% |
| WLD/USDT:USDT | below_1h_threshold | +0.48% | +0.52% |
| HEI/USDT:USDT | below_1h_threshold | +0.32% | +0.36% |
| APE/USDT:USDT | below_1h_threshold | +0.22% | +0.26% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
