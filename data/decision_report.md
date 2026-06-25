# Decision Report

- generated_at: 2026-06-25T16:32:10.146992+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7571**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.18% / filled 20/20。**
- 全期間 MARKET基準: n=7571, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/9 | 66.7% | +3.93% | **+2.62%** |
| ASK | 20/20 | 100.0% | +2.19% | **+2.19%** |
| MARKET | 20/20 | 100.0% | +2.18% | **+2.18%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| ASK_LONG | 20/20 | 100.0% | -0.06% | **-0.06%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.26% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2000件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定: 369件 (Win 102 / Loss 100 / Flat 167) / skip 613件
- 成長率目線: 平均log +0.000196 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.51

## 5. Latest Market Context

- 更新: 2026-06-25T16:32:01.726451+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.72% price=59600.0
- Funnel: target 807 → liquid 162 → pre 50 → checked 50 → surge 4 → strict 4
- Surge前reject: below_1h_threshold=44, below_relative_strength=2, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AERO/USDT:USDT | +14.26% | $1,942,945.02 |
| DYDX/USDT:USDT | +9.37% | $2,179,965.07 |
| VVV/USDT:USDT | +9.25% | $2,876,169.87 |
| RESOLV/USDT:USDT | +7.32% | $4,889,801.95 |
| ETH/USDT:USDT | +5.26% | $1,966,231,922.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETH/USDT:USDT | below_relative_strength | +5.27% | +4.55% |
| HEI/USDT:USDT | below_relative_strength | +5.23% | +4.51% |
| UB/USDT:USDT | below_1h_threshold | +4.34% | +3.62% |
| H/USDT:USDT | below_1h_threshold | +3.51% | +2.79% |
| ARX/USDT:USDT | below_1h_threshold | +1.99% | +1.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
