# Decision Report

- generated_at: 2026-06-14T21:32:23.765890+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6700**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=6700, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.61% | **+0.97%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_BB3S | 6/20 | 30.0% | +1.01% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.46% | **+0.30%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.23% | **+0.15%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.37% | **+0.15%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.93** / 初期 $100.00 (+71.93%)
- 確定: 1573件 (Win 418 / Loss 498 / Flat 657) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $171.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 74件 (Win 20 / Loss 15 / Flat 39) / skip 37件
- 成長率目線: 平均log -0.000177 / 幾何平均 -0.018% per trade / maxDD +2.07%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T21:32:19.380741+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.14% price=64707.1
- Funnel: target 770 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +38.95% | $10,797,470.01 |
| OPG/USDT:USDT | +16.40% | $2,284,024.16 |
| EDEN/USDT:USDT | +14.53% | $1,043,838.86 |
| BABY/USDT:USDT | +12.19% | $1,789,860.67 |
| BP/USDT:USDT | +11.81% | $1,051,923.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BP/USDT:USDT | below_1h_threshold | +4.40% | +3.26% |
| TRADOOR/USDT:USDT | below_1h_threshold | +4.03% | +2.89% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +4.02% | +2.88% |
| LIT/USDT:USDT | below_1h_threshold | +3.87% | +2.73% |
| EDEN/USDT:USDT | below_1h_threshold | +3.65% | +2.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
