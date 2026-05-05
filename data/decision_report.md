# Decision Report

- generated_at: 2026-05-05T02:27:21.747795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3293**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=3293, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.91% | **+0.49%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.58% | **+0.44%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.40% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T02:27:19.860663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=80444.7
- Funnel: target 765 → liquid 205 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +49.75% | $2,397,512.44 |
| TONCOIN/USDT:USDT | +25.06% | $55,988,538.77 |
| RAVE/USDT:USDT | +22.11% | $61,939,576.80 |
| NAORIS/USDT:USDT | +16.91% | $6,299,287.47 |
| FHE/USDT:USDT | +16.68% | $3,627,907.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENDLE/USDT:USDT | below_1h_threshold | +2.63% | +2.46% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.59% | +2.42% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.10% | +1.93% |
| PENGU/USDT:USDT | below_1h_threshold | +2.07% | +1.90% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.59% | +1.43% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
