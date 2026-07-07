# Decision Report

- generated_at: 2026-07-07T07:59:43.157375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8421**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.79% / filled 20/20。**
- 全期間 MARKET基準: n=8421, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/11 | 27.3% | +1.26% | **+0.34%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_BB3S_LONG | 6/9 | 66.7% | +0.20% | **+0.13%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.04% | **-0.10%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.35% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$313.93** / 初期 $100.00 (+213.93%)
- 確定: 2633件 (Win 835 / Loss 893 / Flat 905) / skip 2349件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $313.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1193件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T07:59:37.967143+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=63070.5
- Funnel: target 846 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUR/USDT:USDT | +21.33% | $8,028,136.18 |
| EVAA/USDT:USDT | +20.80% | $1,711,814.98 |
| EDGE/USDT:USDT | +19.97% | $4,695,580.12 |
| ANSEM/USDT:USDT | +18.71% | $6,512,727.86 |
| OPG/USDT:USDT | +15.97% | $3,487,560.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.59% | +4.97% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.29% | +3.67% |
| EVAA/USDT:USDT | below_1h_threshold | +3.18% | +3.56% |
| CHIP/USDT:USDT | below_1h_threshold | +2.99% | +3.37% |
| UB/USDT:USDT | below_1h_threshold | +2.00% | +2.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
