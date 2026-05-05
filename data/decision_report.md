# Decision Report

- generated_at: 2026-05-05T14:07:19.092659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3358**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.97% / filled 20/20。**
- 全期間 MARKET基準: n=3358, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.99% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.76% | **+1.67%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.70% | **+1.02%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| ASK_LONG | 20/20 | 100.0% | -0.27% | **-0.27%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.48% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T14:07:17.044241+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81283.5
- Funnel: target 765 → liquid 190 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +78.66% | $24,867,011.19 |
| LAB/USDT:USDT | +43.14% | $101,350,268.41 |
| HIVE/USDT:USDT | +36.54% | $8,284,330.33 |
| FHE/USDT:USDT | +33.87% | $5,710,531.39 |
| TONCOIN/USDT:USDT | +27.19% | $113,387,218.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MORPHO/USDT:USDT | below_1h_threshold | +1.53% | +1.52% |
| SQD/USDT:USDT | below_1h_threshold | +1.33% | +1.33% |
| JUP/USDT:USDT | below_1h_threshold | +1.26% | +1.25% |
| RAVE/USDT:USDT | below_1h_threshold | +1.25% | +1.24% |
| HIVE/USDT:USDT | below_1h_threshold | +1.12% | +1.12% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
