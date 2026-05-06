# Decision Report

- generated_at: 2026-05-06T04:37:16.346573+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3414**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=3414, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +3.30% | **+1.52%** |
| ASK | 20/20 | 100.0% | +1.33% | **+1.33%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.62% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +2.52% | **+2.10%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.32% | **+0.26%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.16% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T04:37:14.395924+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=81336.6
- Funnel: target 764 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +40.55% | $1,249,597.47 |
| B3/USDT:USDT | +26.33% | $1,395,216.33 |
| ZEC/USDT:USDT | +22.46% | $604,718,733.31 |
| NOT/USDT:USDT | +22.35% | $6,806,274.28 |
| MAVIA/USDT:USDT | +21.69% | $1,819,976.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +3.96% | +4.20% |
| CTC/USDT:USDT | below_1h_threshold | +3.69% | +3.94% |
| M/USDT:USDT | below_1h_threshold | +2.06% | +2.30% |
| JTO/USDT:USDT | below_1h_threshold | +1.53% | +1.77% |
| ZBT/USDT:USDT | below_1h_threshold | +1.46% | +1.70% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
