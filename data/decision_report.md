# Decision Report

- generated_at: 2026-05-05T13:37:30.260057+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3353**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=3353, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.13% | **+1.07%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.76% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| ASK_LONG | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.16% | **+0.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T13:37:25.787770+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=81392.6
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +85.60% | $23,303,321.64 |
| LAB/USDT:USDT | +52.36% | $101,646,531.06 |
| HIVE/USDT:USDT | +36.77% | $8,006,522.49 |
| FHE/USDT:USDT | +31.22% | $5,626,005.07 |
| TONCOIN/USDT:USDT | +27.98% | $112,430,401.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_relative_strength | +5.07% | +4.86% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +4.09% | +3.88% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.03% | +3.82% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +2.66% |
| JUP/USDT:USDT | below_1h_threshold | +2.75% | +2.54% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
