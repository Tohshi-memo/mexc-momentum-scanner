# Decision Report

- generated_at: 2026-05-01T02:56:03.662430+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2749**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2749, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.86% | **-0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.14% | **-0.05%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.24% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.49% | **+1.62%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.73% | **+1.49%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.67% | **+1.42%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.08% | **+1.15%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T02:56:02.059324+00:00 / 保存件数 174/288
- BTC: STAGNANT 1h -0.16% price=76520.1
- Funnel: target 760 → liquid 209 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +27.30% | $9,006,135.86 |
| BR/USDT:USDT | +24.25% | $16,665,405.12 |
| GENIUS/USDT:USDT | +16.86% | $1,426,639.88 |
| ASTEROID/USDT:USDT | +16.11% | $4,098,642.75 |
| RDDTSTOCK/USDT:USDT | +14.12% | $3,959,461.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +4.59% | +4.75% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.60% | +3.76% |
| NOM/USDT:USDT | below_1h_threshold | +2.72% | +2.89% |
| MONAD/USDT:USDT | below_1h_threshold | +2.03% | +2.19% |
| ENSO/USDT:USDT | below_1h_threshold | +1.98% | +2.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
