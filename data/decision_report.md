# Decision Report

- generated_at: 2026-05-06T07:12:25.860245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3426**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=3426, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/11 | 27.3% | +5.33% | **+1.45%** |
| ASK | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +1.45% | **+1.13%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.92% | **+0.82%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.58% | **+0.44%** |
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T07:12:23.402992+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=81552.1
- Funnel: target 765 → liquid 191 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1, 4h RSI 91.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +60.88% | $3,050,201.15 |
| ZEC/USDT:USDT | +34.73% | $661,539,321.05 |
| STORJ/USDT:USDT | +31.21% | $2,288,553.87 |
| B3/USDT:USDT | +25.51% | $1,426,709.29 |
| MAVIA/USDT:USDT | +23.40% | $1,885,130.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +3.99% | +3.85% |
| DUSK/USDT:USDT | below_1h_threshold | +3.48% | +3.33% |
| IO/USDT:USDT | below_1h_threshold | +3.16% | +3.01% |
| DYDX/USDT:USDT | below_1h_threshold | +2.23% | +2.08% |
| ZEN/USDT:USDT | below_1h_threshold | +1.95% | +1.81% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
