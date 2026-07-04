# Decision Report

- generated_at: 2026-07-04T18:27:10.382419+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8282**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8282, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.26% | **+0.44%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| ASK | 20/20 | 100.0% | +0.01% | **+0.01%** |
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.74% | **+0.44%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.47% | **+0.26%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.37% | **+0.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.61** / 初期 $100.00 (+2.61%)
- 確定トレード: 59件 (TP 21 / SL 37 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$333.49** / 初期 $100.00 (+233.49%)
- 確定: 2599件 (Win 825 / Loss 870 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000463 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $333.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1056件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T18:27:02.909060+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=63158.8
- Funnel: target 834 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +17.32% | $2,193,590.38 |
| RPL/USDT:USDT | +15.70% | $1,257,048.04 |
| VANRY/USDT:USDT | +10.63% | $2,800,912.41 |
| CAP/USDT:USDT | +7.21% | $1,358,268.01 |
| O/USDT:USDT | +6.99% | $1,901,702.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +3.11% | +3.25% |
| MYX/USDT:USDT | below_1h_threshold | +3.05% | +3.19% |
| O/USDT:USDT | below_1h_threshold | +2.98% | +3.12% |
| RPL/USDT:USDT | below_1h_threshold | +1.71% | +1.85% |
| ARPA/USDT:USDT | below_1h_threshold | +1.14% | +1.28% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
