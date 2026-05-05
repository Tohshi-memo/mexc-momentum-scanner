# Decision Report

- generated_at: 2026-05-05T03:47:14.106434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3301**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=3301, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.30% | **+0.58%** |
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.44% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.87% | **+0.83%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.60% | **+0.42%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.55% | **+0.41%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T03:47:11.926358+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=80818.3
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +75.57% | $5,049,144.96 |
| 4/USDT:USDT | +25.05% | $1,954,851.92 |
| NOT/USDT:USDT | +22.80% | $1,798,072.98 |
| TONCOIN/USDT:USDT | +21.09% | $62,026,993.80 |
| FHE/USDT:USDT | +19.09% | $3,404,423.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +1.82% | +1.44% |
| MONAD/USDT:USDT | below_1h_threshold | +1.78% | +1.40% |
| QUBIC/USDT:USDT | below_1h_threshold | +1.64% | +1.26% |
| FHE/USDT:USDT | below_1h_threshold | +1.46% | +1.09% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.16% | +0.78% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
