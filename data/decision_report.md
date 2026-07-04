# Decision Report

- generated_at: 2026-07-04T19:55:37.355385+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8291**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=8291, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.84% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.54% | **+0.24%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.09% | **+0.06%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | -0.51% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$102.09** / 初期 $100.00 (+2.09%)
- 確定トレード: 60件 (TP 21 / SL 38 / EXP 1)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$331.79** / 初期 $100.00 (+231.79%)
- 確定: 2608件 (Win 829 / Loss 875 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RPL/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $331.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1065件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T19:55:30.147018+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=63259.2
- Funnel: target 834 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RPL/USDT:USDT | +26.80% | $1,814,339.49 |
| HEI/USDT:USDT | +13.70% | $2,587,071.55 |
| ANSEM/USDT:USDT | +12.77% | $6,363,101.05 |
| O/USDT:USDT | +9.66% | $2,206,631.14 |
| H/USDT:USDT | +7.39% | $2,778,719.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.47% | +3.28% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.60% | +2.41% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.43% | +2.24% |
| EPIC/USDT:USDT | below_1h_threshold | +2.42% | +2.23% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.75% | +1.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
