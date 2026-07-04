# Decision Report

- generated_at: 2026-07-04T20:44:35.486785+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8292**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=8292, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.31% | **+1.31%** |
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.78% | **+0.31%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.56% | **-0.22%** |
| ASK_LONG | 20/20 | 100.0% | -0.27% | **-0.27%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | -0.50% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$102.09** / 初期 $100.00 (+2.09%)
- 確定トレード: 60件 (TP 21 / SL 38 / EXP 1)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.13** / 初期 $100.00 (+230.13%)
- 確定: 2609件 (Win 829 / Loss 876 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $330.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1066件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T20:44:28.220165+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63243.4
- Funnel: target 834 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RPL/USDT:USDT | +19.75% | $2,207,113.65 |
| O/USDT:USDT | +14.89% | $2,375,189.34 |
| HEI/USDT:USDT | +12.32% | $2,708,135.88 |
| ANSEM/USDT:USDT | +11.84% | $6,154,822.98 |
| H/USDT:USDT | +11.83% | $2,979,992.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_1h_threshold | +4.59% | +4.63% |
| H/USDT:USDT | below_1h_threshold | +3.74% | +3.78% |
| LAB/USDT:USDT | below_1h_threshold | +3.28% | +3.32% |
| VELVET/USDT:USDT | below_1h_threshold | +2.50% | +2.54% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.42% | +2.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
