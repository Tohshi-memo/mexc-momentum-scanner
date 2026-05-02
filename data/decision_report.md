# Decision Report

- generated_at: 2026-05-02T23:57:06.872707+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3000**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=3000, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.23% | **+1.11%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.76%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.99% | **+0.65%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.76% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T23:57:05.026346+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=78623.2
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +19.52% | $1,403,128.73 |
| LUNC/USDT:USDT | +15.96% | $28,959,759.66 |
| BIANRENSHENG/USDT:USDT | +14.45% | $1,643,804.16 |
| XNY/USDT:USDT | +12.77% | $2,272,433.42 |
| NAORIS/USDT:USDT | +12.59% | $4,558,071.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +2.72% | +2.94% |
| BSB/USDT:USDT | below_1h_threshold | +2.44% | +2.65% |
| BABY/USDT:USDT | below_1h_threshold | +2.33% | +2.55% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.65% | +1.87% |
| LUNC/USDT:USDT | below_1h_threshold | +1.50% | +1.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
