# Decision Report

- generated_at: 2026-05-06T00:07:36.135554+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3400**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3400, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.84% | **+0.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +2.11% | **+1.90%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.58% | **+0.36%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.75% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T00:07:34.236443+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=81032.0
- Funnel: target 760 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAVIA/USDT:USDT | +24.96% | $1,539,960.74 |
| FHE/USDT:USDT | +23.94% | $26,492,263.74 |
| SWARMS/USDT:USDT | +21.06% | $2,354,519.41 |
| SMCISTOCK/USDT:USDT | +20.41% | $5,100,729.44 |
| ZEC/USDT:USDT | +20.29% | $586,988,853.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EGLD/USDT:USDT | below_1h_threshold | +2.59% | +2.38% |
| DASH/USDT:USDT | below_1h_threshold | +1.98% | +1.77% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.55% | +1.34% |
| LUNC/USDT:USDT | below_1h_threshold | +1.44% | +1.23% |
| AKT/USDT:USDT | below_1h_threshold | +1.33% | +1.12% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
