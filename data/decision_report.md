# Decision Report

- generated_at: 2026-05-03T04:47:09.238981+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3028**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=3028, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.24% | **+2.24%** |
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.94% | **+1.91%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.28% | **+1.71%** |
| LIMIT_BB3S | 5/11 | 45.5% | +3.64% | **+1.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.68% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.25% | **+0.14%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.35% | **+0.07%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.10% | **+0.07%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.28% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T04:47:04.734735+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78144.8
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1, 4h RSI 73.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +17.58% | $2,112,585.03 |
| BABY/USDT:USDT | +16.98% | $2,127,050.38 |
| AKT/USDT:USDT | +15.39% | $1,093,847.13 |
| AIGENSYN/USDT:USDT | +12.92% | $2,744,164.24 |
| FHE/USDT:USDT | +11.89% | $2,498,268.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +3.64% | +3.66% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.14% | +3.17% |
| BABY/USDT:USDT | below_1h_threshold | +2.59% | +2.62% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.43% | +2.45% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.10% | +2.12% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
