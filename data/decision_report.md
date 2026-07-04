# Decision Report

- generated_at: 2026-07-04T19:26:32.816903+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8289**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8289, expectancy=-0.03%
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
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.09** / 初期 $100.00 (+2.09%)
- 確定トレード: 60件 (TP 21 / SL 38 / EXP 1)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.80** / 初期 $100.00 (+231.80%)
- 確定: 2606件 (Win 828 / Loss 874 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $331.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1063件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T19:26:26.801500+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=63294.3
- Funnel: target 834 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +17.84% | $2,445,958.43 |
| RPL/USDT:USDT | +15.81% | $1,414,317.15 |
| O/USDT:USDT | +9.39% | $2,092,024.78 |
| H/USDT:USDT | +8.38% | $2,697,183.21 |
| CAP/USDT:USDT | +7.82% | $1,463,345.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RPL/USDT:USDT | below_1h_threshold | +2.25% | +2.01% |
| EPIC/USDT:USDT | below_1h_threshold | +1.55% | +1.30% |
| LAB/USDT:USDT | below_1h_threshold | +1.50% | +1.25% |
| RE/USDT:USDT | below_1h_threshold | +1.46% | +1.21% |
| HEI/USDT:USDT | below_1h_threshold | +0.96% | +0.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
