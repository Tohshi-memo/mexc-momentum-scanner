# Decision Report

- generated_at: 2026-06-24T00:21:04.478737+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7448**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.85% / filled 20/20。**
- 全期間 MARKET基準: n=7448, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.36% | **-0.20%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | -2.04% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.71% | **+0.63%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.60% | **+0.45%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.15% | **+0.17%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.19% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 31件 (TP 12 / SL 19 / EXP 0)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1928件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 328件 (Win 92 / Loss 88 / Flat 148) / skip 531件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-24T00:20:58.958058+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=62833.7
- Funnel: target 802 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +54.47% | $7,841,469.24 |
| BEAT/USDT:USDT | +22.94% | $59,575,413.06 |
| SAHARA/USDT:USDT | +10.15% | $1,240,529.95 |
| DYDX/USDT:USDT | +10.10% | $3,830,736.91 |
| ALLO/USDT:USDT | +7.20% | $5,148,166.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +4.09% | +3.87% |
| SOXL/USDT:USDT | below_1h_threshold | +4.02% | +3.80% |
| HEI/USDT:USDT | below_1h_threshold | +3.73% | +3.51% |
| DRAM/USDT:USDT | below_1h_threshold | +2.76% | +2.55% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
