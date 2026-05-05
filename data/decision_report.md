# Decision Report

- generated_at: 2026-05-05T13:57:31.835004+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3357**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.97% / filled 20/20。**
- 全期間 MARKET基準: n=3357, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +2.07% | **+2.07%** |
| ASK | 20/20 | 100.0% | +1.99% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.70% | **+1.02%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| ASK_LONG | 20/20 | 100.0% | -0.27% | **-0.27%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.48% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T13:57:29.188073+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=81209.9
- Funnel: target 765 → liquid 198 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.5 >= 65=1, 4h RSI 71.4 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +76.86% | $24,443,400.60 |
| LAB/USDT:USDT | +41.72% | $104,898,924.18 |
| HIVE/USDT:USDT | +35.26% | $8,204,327.36 |
| FHE/USDT:USDT | +32.10% | $5,706,627.28 |
| TONCOIN/USDT:USDT | +28.11% | $113,839,639.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WDCSTOCK/USDT:USDT | below_1h_threshold | +4.98% | +4.99% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.97% | +4.98% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +4.60% | +4.62% |
| UB/USDT:USDT | below_1h_threshold | +3.51% | +3.52% |
| CVNASTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.61% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
