# Decision Report

- generated_at: 2026-05-01T07:56:13.088599+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2765**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.98% / filled 20/20。**
- 全期間 MARKET基準: n=2765, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.29% | **+1.16%** |
| ASK | 20/20 | 100.0% | +1.03% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.72% | **+0.54%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.81% | **+0.49%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.55% | **+0.28%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +0.40% | **+0.27%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.15% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T07:56:06.297115+00:00 / 保存件数 235/288
- BTC: STAGNANT 1h +0.19% price=77099.6
- Funnel: target 760 → liquid 208 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1, 4h RSI 68.0 >= 65=1, 4h RSI 88.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +57.55% | $2,413,216.42 |
| ZEREBRO/USDT:USDT | +52.45% | $4,789,464.57 |
| ORCA/USDT:USDT | +27.71% | $10,196,941.70 |
| BR/USDT:USDT | +18.66% | $20,303,020.17 |
| GENIUS/USDT:USDT | +15.99% | $1,599,742.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +2.91% | +2.72% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.59% | +2.40% |
| MYX/USDT:USDT | below_1h_threshold | +2.23% | +2.04% |
| DRIFT/USDT:USDT | below_1h_threshold | +1.72% | +1.53% |
| COAI/USDT:USDT | below_1h_threshold | +1.65% | +1.46% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
