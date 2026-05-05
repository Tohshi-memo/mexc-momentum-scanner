# Decision Report

- generated_at: 2026-05-05T06:17:30.531854+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3318**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3318, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_BB3S | 3/12 | 25.0% | +1.68% | **+0.42%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.09% | **+0.27%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.95% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/8 | 25.0% | +6.30% | **+1.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T06:17:28.429517+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80859.0
- Funnel: target 765 → liquid 205 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +68.63% | $8,202,368.66 |
| HIVE/USDT:USDT | +41.71% | $2,442,547.82 |
| FHE/USDT:USDT | +26.67% | $3,827,030.45 |
| TONCOIN/USDT:USDT | +19.45% | $64,554,659.73 |
| 4/USDT:USDT | +17.73% | $2,351,681.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.73% | +1.81% |
| B3/USDT:USDT | below_1h_threshold | +1.56% | +1.65% |
| 4/USDT:USDT | below_1h_threshold | +1.33% | +1.41% |
| LUNC/USDT:USDT | below_1h_threshold | +1.23% | +1.31% |
| JST/USDT:USDT | below_1h_threshold | +0.67% | +0.75% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
