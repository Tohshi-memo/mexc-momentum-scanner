# Decision Report

- generated_at: 2026-05-05T18:27:27.494897+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3372**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=3372, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +2.01% | **+1.81%** |
| ASK | 20/20 | 100.0% | +1.50% | **+1.50%** |
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.32% | **+1.26%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.94% | **+0.19%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.12% | **+0.11%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.79% | **-0.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T18:27:25.541925+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=81408.5
- Funnel: target 761 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +21.82% | $9,827,173.81 |
| SWARMS/USDT:USDT | +12.61% | $2,112,619.67 |
| ASTEROID/USDT:USDT | +5.32% | $3,563,682.08 |
| DOGS/USDT:USDT | +5.21% | $30,276,379.75 |
| AIN/USDT:USDT | +4.09% | $1,037,575.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +3.16% | +2.93% |
| AIN/USDT:USDT | below_1h_threshold | +2.47% | +2.25% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.40% | +1.17% |
| BSB/USDT:USDT | below_1h_threshold | +1.04% | +0.81% |
| NOT/USDT:USDT | below_1h_threshold | +0.99% | +0.77% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
