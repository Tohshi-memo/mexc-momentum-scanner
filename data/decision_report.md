# Decision Report

- generated_at: 2026-05-05T14:31:01.487498+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3359**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3359, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.09% | **+2.09%** |
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.87% | **+1.77%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.44% | **+0.86%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.69% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | -0.09% | **-0.09%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.89% | **-0.40%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | -1.67% | **-0.58%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T14:30:59.451317+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=81426.9
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +74.72% | $25,935,350.94 |
| LAB/USDT:USDT | +36.92% | $103,606,933.99 |
| HIVE/USDT:USDT | +34.59% | $8,382,133.34 |
| FHE/USDT:USDT | +33.41% | $5,792,824.89 |
| TONCOIN/USDT:USDT | +24.64% | $116,651,949.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.06% | +3.88% |
| LUNC/USDT:USDT | below_1h_threshold | +3.99% | +3.81% |
| RAVE/USDT:USDT | below_1h_threshold | +3.25% | +3.07% |
| MORPHO/USDT:USDT | below_1h_threshold | +2.32% | +2.14% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.11% | +1.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
