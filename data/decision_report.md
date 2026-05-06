# Decision Report

- generated_at: 2026-05-06T06:52:26.585564+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3424**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=3424, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +6.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.09% | **+0.73%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +1.45% | **+1.27%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.17% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T06:52:24.404787+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=81432.9
- Funnel: target 765 → liquid 197 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +56.88% | $1,646,631.36 |
| STORJ/USDT:USDT | +30.41% | $2,245,528.24 |
| ZEC/USDT:USDT | +26.99% | $644,784,763.90 |
| MAVIA/USDT:USDT | +24.99% | $1,874,103.94 |
| B3/USDT:USDT | +22.43% | $1,416,078.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.87% | +3.68% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.56% | +2.37% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.87% | +1.68% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.63% | +1.44% |
| MAVIA/USDT:USDT | below_1h_threshold | +1.53% | +1.34% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
