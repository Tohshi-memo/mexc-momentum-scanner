# Decision Report

- generated_at: 2026-05-06T06:47:21.243877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3423**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=3423, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +4.22% | **+1.62%** |
| ASK | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.65% | **+0.55%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.53% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.25% | **+0.22%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.05% | **+0.04%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.09% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T06:47:19.049979+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=81446.0
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +50.51% | $1,290,827.42 |
| STORJ/USDT:USDT | +30.91% | $2,226,258.20 |
| ZEC/USDT:USDT | +26.79% | $641,751,311.52 |
| MAVIA/USDT:USDT | +24.28% | $1,868,763.89 |
| B3/USDT:USDT | +22.63% | $1,414,966.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +3.49% | +3.28% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.96% | +2.76% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.50% | +2.30% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.28% | +2.08% |
| TRIA/USDT:USDT | below_1h_threshold | +2.27% | +2.07% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
