# Decision Report

- generated_at: 2026-07-04T19:06:28.214649+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8288**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8288, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.55% | **+0.27%** |
| ASK | 20/20 | 100.0% | +0.24% | **+0.24%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.83% | **+0.29%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.09** / 初期 $100.00 (+2.09%)
- 確定トレード: 60件 (TP 21 / SL 38 / EXP 1)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.15** / 初期 $100.00 (+230.15%)
- 確定: 2605件 (Win 827 / Loss 874 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $330.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1062件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T19:06:20.919871+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63195.7
- Funnel: target 834 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +14.91% | $2,338,290.69 |
| RPL/USDT:USDT | +13.42% | $1,343,296.39 |
| O/USDT:USDT | +10.89% | $1,960,543.07 |
| H/USDT:USDT | +9.87% | $2,592,442.54 |
| ANSEM/USDT:USDT | +9.84% | $6,224,768.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.11% | +2.02% |
| O/USDT:USDT | below_1h_threshold | +1.43% | +1.34% |
| MYX/USDT:USDT | below_1h_threshold | +1.37% | +1.28% |
| LAB/USDT:USDT | below_1h_threshold | +1.09% | +1.00% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.71% | +0.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
