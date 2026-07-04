# Decision Report

- generated_at: 2026-07-04T14:41:26.735988+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8271**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8271, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.49% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.04% | **+0.36%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.19% | **+0.22%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.24% | **-0.17%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.53% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.96% | **+0.53%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.23** / 初期 $100.00 (+230.23%)
- 確定: 2588件 (Win 819 / Loss 865 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $330.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1045件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T14:41:21.847227+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=62630.0
- Funnel: target 834 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +119.05% | $84,436,818.16 |
| ANSEM/USDT:USDT | +63.39% | $6,069,218.53 |
| TLM/USDT:USDT | +61.77% | $58,504,341.05 |
| HMSTR/USDT:USDT | +56.05% | $14,273,621.29 |
| BAS/USDT:USDT | +49.33% | $4,991,944.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.22% | +2.12% |
| VELVET/USDT:USDT | below_1h_threshold | +2.16% | +2.05% |
| BASED/USDT:USDT | below_1h_threshold | +1.78% | +1.68% |
| XPL/USDT:USDT | below_1h_threshold | +1.47% | +1.36% |
| EPIC/USDT:USDT | below_1h_threshold | +1.45% | +1.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
