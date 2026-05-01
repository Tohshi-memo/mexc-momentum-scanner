# Decision Report

- generated_at: 2026-05-01T08:26:56.530190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2772**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2772, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.41% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.22% | **+0.86%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.16% | **+0.75%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.01% | **+0.50%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.97% | **+0.48%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:26:54.657883+00:00 / 保存件数 241/288
- BTC: BULLISH 1h +0.40% price=77404.8
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +62.23% | $3,649,109.21 |
| ZEREBRO/USDT:USDT | +50.28% | $5,457,837.57 |
| ORCA/USDT:USDT | +27.71% | $10,213,084.10 |
| BR/USDT:USDT | +20.67% | $20,632,360.42 |
| GENIUS/USDT:USDT | +18.32% | $1,604,428.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ST/USDT:USDT | below_1h_threshold | +4.65% | +4.26% |
| DRIFT/USDT:USDT | below_1h_threshold | +3.44% | +3.05% |
| B/USDT:USDT | below_1h_threshold | +2.78% | +2.38% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +2.35% | +1.95% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +2.34% | +1.95% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
