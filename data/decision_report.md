# Decision Report

- generated_at: 2026-05-05T22:02:38.518376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3394**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3394, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.99% | **-0.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.39% | **+0.85%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.54% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +2.18% | **+1.85%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.23% | **+1.22%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.94% | **+1.03%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.52% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T22:02:36.526326+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=81457.7
- Funnel: target 759 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +35.43% | $22,122,877.43 |
| MAVIA/USDT:USDT | +29.31% | $1,324,492.58 |
| SWARMS/USDT:USDT | +22.46% | $2,304,844.69 |
| ZEC/USDT:USDT | +21.19% | $566,060,245.52 |
| SMCISTOCK/USDT:USDT | +17.78% | $4,919,524.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +2.38% | +2.27% |
| 4/USDT:USDT | below_1h_threshold | +1.62% | +1.51% |
| STRK/USDT:USDT | below_1h_threshold | +1.27% | +1.15% |
| JUP/USDT:USDT | below_1h_threshold | +1.04% | +0.93% |
| SWARMS/USDT:USDT | below_1h_threshold | +0.89% | +0.78% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
