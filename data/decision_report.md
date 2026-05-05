# Decision Report

- generated_at: 2026-05-05T02:57:12.443048+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3297**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.56% / filled 20/20。**
- 全期間 MARKET基準: n=3297, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.24% | **+1.11%** |
| LIMIT_BB3S | 3/11 | 27.3% | +2.20% | **+0.60%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.96% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.01% | **+0.10%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.08% | **+0.05%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T02:57:10.129736+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=80469.9
- Funnel: target 765 → liquid 207 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.9 >= 65=1, 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +73.49% | $3,661,202.76 |
| RAVE/USDT:USDT | +20.82% | $62,532,188.28 |
| TONCOIN/USDT:USDT | +20.49% | $59,092,653.62 |
| FHE/USDT:USDT | +17.37% | $3,643,436.64 |
| NOT/USDT:USDT | +14.63% | $1,632,841.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +3.37% | +3.17% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.89% | +1.69% |
| QUBIC/USDT:USDT | below_1h_threshold | +1.63% | +1.44% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.29% | +1.09% |
| SQD/USDT:USDT | below_1h_threshold | +1.26% | +1.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
