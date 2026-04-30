# Decision Report

- generated_at: 2026-04-30T21:56:08.911736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2737**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2737, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.56% | **+2.67%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.58% | **+2.32%** |
| ASK_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.49% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T21:56:04.709561+00:00 / 保存件数 112/288
- BTC: BULLISH 1h -0.27% price=76246.8
- Funnel: target 756 → liquid 223 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +18.19% | $17,350,967.08 |
| BR/USDT:USDT | +17.63% | $13,122,081.69 |
| ORCA/USDT:USDT | +14.09% | $3,147,873.56 |
| DRIFT/USDT:USDT | +11.87% | $1,275,598.52 |
| GENIUS/USDT:USDT | +11.70% | $1,114,016.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.86% | +5.13% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +4.02% | +4.29% |
| UB/USDT:USDT | below_1h_threshold | +3.89% | +4.16% |
| BR/USDT:USDT | below_1h_threshold | +3.13% | +3.40% |
| ZBCN/USDT:USDT | below_1h_threshold | +3.01% | +3.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
