# Decision Report

- generated_at: 2026-07-07T05:28:23.094037+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8420**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.17% / filled 20/20。**
- 全期間 MARKET基準: n=8420, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |
| ASK | 20/20 | 100.0% | +2.12% | **+2.12%** |
| LIMIT_BB3S | 3/12 | 25.0% | +1.26% | **+0.32%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.04% | **+0.65%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.04% | **-0.10%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$315.51** / 初期 $100.00 (+215.51%)
- 確定: 2632件 (Win 835 / Loss 892 / Flat 905) / skip 2349件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $315.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1192件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T05:28:18.012678+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=62867.5
- Funnel: target 842 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +30.16% | $2,422,007.35 |
| EPIC/USDT:USDT | +24.53% | $3,074,392.77 |
| BLUR/USDT:USDT | +22.90% | $7,202,216.78 |
| EDGE/USDT:USDT | +17.91% | $4,041,606.91 |
| EVAA/USDT:USDT | +15.92% | $1,162,067.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUR/USDT:USDT | below_1h_threshold | +3.89% | +4.21% |
| OPG/USDT:USDT | below_1h_threshold | +2.33% | +2.65% |
| EDGE/USDT:USDT | below_1h_threshold | +2.10% | +2.42% |
| EVAA/USDT:USDT | below_1h_threshold | +1.45% | +1.77% |
| BTW/USDT:USDT | below_1h_threshold | +1.14% | +1.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
