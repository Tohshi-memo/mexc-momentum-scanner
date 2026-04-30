# Decision Report

- generated_at: 2026-04-30T22:31:03.012379+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2739**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2739, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.65% | **-1.65%** |

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
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.51% | **+1.93%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.39% | **+1.69%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T22:31:01.430348+00:00 / 保存件数 120/288
- BTC: BULLISH 1h +0.26% price=76400.0
- Funnel: target 756 → liquid 220 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +20.29% | $13,486,093.47 |
| AIOT/USDT:USDT | +19.18% | $17,676,780.87 |
| ORCA/USDT:USDT | +18.07% | $3,245,493.21 |
| DRIFT/USDT:USDT | +14.37% | $1,321,543.51 |
| RDDTSTOCK/USDT:USDT | +12.87% | $3,835,378.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +4.60% | +4.34% |
| UB/USDT:USDT | below_1h_threshold | +3.55% | +3.29% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.86% | +2.60% |
| ZBCN/USDT:USDT | below_1h_threshold | +2.59% | +2.33% |
| BR/USDT:USDT | below_1h_threshold | +2.42% | +2.16% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
