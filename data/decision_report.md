# Decision Report

- generated_at: 2026-04-30T17:05:54.941386+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2720**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2720, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +4.98% | **+2.49%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +4.15% | **+2.28%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.84% | **+1.42%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T17:05:53.432341+00:00 / 保存件数 52/288
- BTC: STAGNANT 1h -0.01% price=76209.7
- Funnel: target 761 → liquid 227 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +8.85% | $4,309,491.76 |
| ASTEROID/USDT:USDT | +6.86% | $3,593,336.40 |
| TAC/USDT:USDT | +6.55% | $5,868,006.75 |
| AIOT/USDT:USDT | +5.40% | $11,739,243.41 |
| BIO/USDT:USDT | +5.35% | $3,625,429.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.53% | +1.54% |
| CVNASTOCK/USDT:USDT | below_1h_threshold | +0.86% | +0.88% |
| PENGU/USDT:USDT | below_1h_threshold | +0.83% | +0.84% |
| BIO/USDT:USDT | below_1h_threshold | +0.75% | +0.77% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +0.69% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
