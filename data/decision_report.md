# Decision Report

- generated_at: 2026-05-01T06:16:01.487641+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2756**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=2756, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.34% | **+0.70%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| ASK | 20/20 | 100.0% | +0.48% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.41% | **+0.63%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.58% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T06:15:59.627557+00:00 / 保存件数 215/288
- BTC: STAGNANT 1h -0.02% price=77120.0
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +34.62% | $2,324,750.21 |
| ORCA/USDT:USDT | +30.61% | $9,915,511.70 |
| BR/USDT:USDT | +28.47% | $18,551,852.50 |
| GENIUS/USDT:USDT | +17.75% | $1,484,885.30 |
| AIOT/USDT:USDT | +17.61% | $18,030,187.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +2.24% | +2.26% |
| ZBT/USDT:USDT | below_1h_threshold | +2.14% | +2.16% |
| ZBCN/USDT:USDT | below_1h_threshold | +2.01% | +2.03% |
| BIO/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |
| BRETT/USDT:USDT | below_1h_threshold | +0.70% | +0.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
