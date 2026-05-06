# Decision Report

- generated_at: 2026-05-06T04:47:37.564828+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3416**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.09% / filled 20/20。**
- 全期間 MARKET基準: n=3416, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.15% | **+2.15%** |
| MARKET | 20/20 | 100.0% | +2.09% | **+2.09%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_BB3S | 6/14 | 42.9% | +3.30% | **+1.41%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.28% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.32% | **+0.26%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | -0.67% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T04:47:34.832524+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=81357.1
- Funnel: target 764 → liquid 191 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 95.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +39.76% | $1,316,926.78 |
| B3/USDT:USDT | +24.78% | $1,407,807.17 |
| ZEC/USDT:USDT | +23.22% | $607,316,559.21 |
| MAVIA/USDT:USDT | +22.43% | $1,825,188.49 |
| TONCOIN/USDT:USDT | +21.26% | $191,704,058.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.09% | +4.31% |
| TRIA/USDT:USDT | below_1h_threshold | +2.90% | +3.12% |
| M/USDT:USDT | below_1h_threshold | +2.89% | +3.11% |
| ICP/USDT:USDT | below_1h_threshold | +2.37% | +2.59% |
| BCH/USDT:USDT | below_1h_threshold | +2.34% | +2.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
