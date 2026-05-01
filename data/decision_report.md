# Decision Report

- generated_at: 2026-05-01T08:32:20.546717+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2774**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2774, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.07% | **+1.45%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +3.39% | **+1.36%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.07% | **+1.35%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.09%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.41% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:32:18.137366+00:00 / 保存件数 242/288
- BTC: BULLISH 1h +0.39% price=77403.2
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.4 >= 65=1, 4h RSI 82.6 >= 65=1, 4h RSI 73.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +53.67% | $5,540,457.62 |
| B/USDT:USDT | +52.03% | $4,499,995.83 |
| BR/USDT:USDT | +41.13% | $21,036,740.10 |
| ORCA/USDT:USDT | +28.25% | $10,233,757.59 |
| UB/USDT:USDT | +22.54% | $10,233,667.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +3.29% | +2.90% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.01% | +2.62% |
| EDGE/USDT:USDT | below_1h_threshold | +2.70% | +2.31% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +2.59% | +2.20% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.09% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
