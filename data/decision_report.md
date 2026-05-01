# Decision Report

- generated_at: 2026-05-01T08:21:53.301001+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2770**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=2770, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.05% | **+1.00%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.18% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.96% | **+1.31%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.79% | **+0.59%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.66% | **+0.46%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.37% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:21:51.452929+00:00 / 保存件数 240/288
- BTC: BULLISH 1h +0.30% price=77335.0
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +63.67% | $3,361,705.23 |
| ZEREBRO/USDT:USDT | +53.23% | $5,228,857.18 |
| ORCA/USDT:USDT | +28.11% | $10,202,287.68 |
| BR/USDT:USDT | +19.46% | $20,607,649.34 |
| GENIUS/USDT:USDT | +17.59% | $1,602,358.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +3.83% | +3.53% |
| ST/USDT:USDT | below_1h_threshold | +3.24% | +2.93% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.48% | +2.18% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.20% | +1.90% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +2.16% | +1.86% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
