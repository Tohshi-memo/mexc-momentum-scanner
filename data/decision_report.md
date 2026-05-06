# Decision Report

- generated_at: 2026-05-06T04:57:28.365534+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3420**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=3420, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +3.30% | **+1.52%** |
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.33% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.80% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.34% | **+0.05%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.02% | **+0.02%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T04:57:25.701788+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=81290.3
- Funnel: target 764 → liquid 191 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 78.7 >= 65=1, 4h RSI 95.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +43.63% | $1,381,468.50 |
| B3/USDT:USDT | +25.28% | $1,410,630.68 |
| MAVIA/USDT:USDT | +23.90% | $1,830,163.39 |
| ZEC/USDT:USDT | +22.99% | $610,123,524.71 |
| TONCOIN/USDT:USDT | +20.68% | $193,412,790.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.79% | +5.09% |
| FILECOIN/USDT:USDT | below_1h_threshold | +3.22% | +3.52% |
| STORJ/USDT:USDT | below_1h_threshold | +3.08% | +3.38% |
| TRIA/USDT:USDT | below_1h_threshold | +2.77% | +3.07% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.52% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
