# Decision Report

- generated_at: 2026-04-30T16:05:55.603329+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2713**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2713, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.32% | **+1.26%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.28% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +7.03% | **+4.69%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.32% | **+1.49%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.70% | **+1.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T16:05:54.097227+00:00 / 保存件数 39/288
- BTC: STAGNANT 1h -0.02% price=76411.9
- Funnel: target 761 → liquid 224 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APE/USDT:USDT | +2.39% | $5,824,349.83 |
| ZBT/USDT:USDT | +2.19% | $2,899,564.69 |
| BLEND/USDT:USDT | +1.62% | $12,040,702.38 |
| TAC/USDT:USDT | +1.61% | $4,042,646.16 |
| ENSO/USDT:USDT | +1.57% | $1,723,595.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APE/USDT:USDT | below_1h_threshold | +2.26% | +2.28% |
| ZBT/USDT:USDT | below_1h_threshold | +2.19% | +2.21% |
| BLEND/USDT:USDT | below_1h_threshold | +1.62% | +1.64% |
| TAC/USDT:USDT | below_1h_threshold | +1.61% | +1.63% |
| ENSO/USDT:USDT | below_1h_threshold | +1.58% | +1.60% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
