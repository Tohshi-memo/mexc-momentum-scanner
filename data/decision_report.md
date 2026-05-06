# Decision Report

- generated_at: 2026-05-06T05:37:48.203294+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3421**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=3421, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +3.30% | **+1.52%** |
| ASK | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.53% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.58% | **+0.44%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.50% | **+0.42%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.19% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T05:37:45.765355+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=81067.3
- Funnel: target 765 → liquid 193 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +36.58% | $1,646,169.27 |
| ZEC/USDT:USDT | +24.98% | $617,499,191.62 |
| MAVIA/USDT:USDT | +22.75% | $1,843,695.85 |
| B3/USDT:USDT | +21.22% | $1,404,134.74 |
| TONCOIN/USDT:USDT | +20.03% | $197,260,716.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +3.41% | +3.69% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.74% | +3.02% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.94% | +2.22% |
| ZEC/USDT:USDT | below_1h_threshold | +1.75% | +2.03% |
| AKT/USDT:USDT | below_1h_threshold | +1.29% | +1.57% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
