# Decision Report

- generated_at: 2026-04-30T20:25:56.411006+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2733**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2733, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.67% | **+2.27%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.03% | **+1.81%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.96% | **+1.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T20:25:54.915141+00:00 / 保存件数 94/288
- BTC: STAGNANT 1h +0.04% price=76404.1
- Funnel: target 757 → liquid 224 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +19.88% | $10,623,855.30 |
| DRIFT/USDT:USDT | +13.11% | $1,180,790.75 |
| ORCA/USDT:USDT | +8.09% | $2,767,637.50 |
| NAORIS/USDT:USDT | +7.97% | $11,226,196.00 |
| BIO/USDT:USDT | +6.85% | $3,877,682.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.03% | +3.99% |
| MEGA/USDT:USDT | below_1h_threshold | +3.85% | +3.81% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +3.23% | +3.19% |
| ZBCN/USDT:USDT | below_1h_threshold | +2.00% | +1.96% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.69% | +1.65% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
