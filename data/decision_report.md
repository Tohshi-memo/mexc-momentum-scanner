# Decision Report

- generated_at: 2026-05-01T08:42:09.302679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2777**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2777, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.93% | **+1.91%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.37% | **+1.69%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.33% | **+1.52%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.47% | **+1.40%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +3.39% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:42:07.035320+00:00 / 保存件数 244/288
- BTC: BULLISH 1h +0.36% price=77380.1
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1, 4h RSI 71.6 >= 65=1, 4h RSI 73.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +61.02% | $5,335,847.63 |
| ZEREBRO/USDT:USDT | +53.17% | $5,728,157.27 |
| BR/USDT:USDT | +43.43% | $21,602,053.39 |
| ORCA/USDT:USDT | +27.37% | $10,263,501.43 |
| UB/USDT:USDT | +23.93% | $10,371,014.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +3.00% | +2.64% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.91% | +2.55% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +2.82% | +2.45% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +2.47% | +2.11% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.23% | +1.87% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
