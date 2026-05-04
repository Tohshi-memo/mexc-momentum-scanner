# Decision Report

- generated_at: 2026-05-04T21:32:25.672324+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3263**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=3263, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.92% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.13% | **+0.83%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.39% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.36% | **+1.15%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.41% | **+1.08%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.65% | **+0.74%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.67% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T21:32:23.683151+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=80228.7
- Funnel: target 759 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +30.52% | $46,796,796.38 |
| FHE/USDT:USDT | +14.77% | $2,654,691.33 |
| LUNC/USDT:USDT | +11.95% | $75,713,392.47 |
| TST/USDT:USDT | +7.99% | $22,789,417.60 |
| USTC/USDT:USDT | +7.81% | $1,490,628.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +4.09% | +3.67% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.92% | +3.51% |
| FHE/USDT:USDT | below_1h_threshold | +3.61% | +3.19% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.66% | +2.25% |
| TIA/USDT:USDT | below_1h_threshold | +2.59% | +2.18% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
