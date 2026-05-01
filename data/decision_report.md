# Decision Report

- generated_at: 2026-05-01T08:37:07.377798+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2776**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2776, expectancy=-0.11%
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
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.58% | **+1.55%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +3.39% | **+1.36%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.27% | **+1.14%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.86% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:37:05.020273+00:00 / 保存件数 243/288
- BTC: BULLISH 1h +0.31% price=77339.2
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.1 >= 65=1, 4h RSI 71.2 >= 65=1, 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +53.17% | $4,981,400.05 |
| ZEREBRO/USDT:USDT | +52.81% | $5,614,684.49 |
| BR/USDT:USDT | +48.10% | $21,366,473.18 |
| ORCA/USDT:USDT | +27.98% | $10,248,015.77 |
| UB/USDT:USDT | +22.19% | $10,319,995.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GENIUS/USDT:USDT | below_1h_threshold | +4.33% | +4.02% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +3.25% | +2.94% |
| DRIFT/USDT:USDT | below_1h_threshold | +3.04% | +2.73% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.64% | +2.33% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +2.47% | +2.16% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
