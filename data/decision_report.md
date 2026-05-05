# Decision Report

- generated_at: 2026-05-05T03:27:27.718598+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3300**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=3300, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.44% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_BB3S | 4/11 | 36.4% | +0.95% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.76% | **+0.42%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.55% | **+0.41%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.17% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T03:27:25.389073+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80708.2
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +84.74% | $4,597,427.35 |
| TONCOIN/USDT:USDT | +21.16% | $61,434,079.42 |
| FHE/USDT:USDT | +18.77% | $3,387,750.12 |
| 4/USDT:USDT | +18.53% | $1,865,988.84 |
| NOT/USDT:USDT | +17.71% | $1,710,563.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.79% | +4.55% |
| NOT/USDT:USDT | below_1h_threshold | +1.57% | +1.33% |
| ZRO/USDT:USDT | below_1h_threshold | +1.31% | +1.07% |
| ONDO/USDT:USDT | below_1h_threshold | +1.21% | +0.97% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.20% | +0.96% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
