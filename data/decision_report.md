# Decision Report

- generated_at: 2026-04-30T15:01:22.410192+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2711**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2711, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.68% | **+0.56%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +7.03% | **+7.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T15:01:21.185715+00:00 / 保存件数 25/288
- BTC: STAGNANT 1h +0.08% price=76316.4
- Funnel: target 762 → liquid 224 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +39.96% | $1,968,430.55 |
| BSB/USDT:USDT | +39.08% | $43,865,001.97 |
| SKYAI/USDT:USDT | +32.18% | $23,110,590.03 |
| ROLL/USDT:USDT | +24.40% | $2,952,985.96 |
| BIO/USDT:USDT | +21.61% | $3,484,707.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IONQSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.20% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.99% | +0.91% |
| QCOMSTOCK/USDT:USDT | below_1h_threshold | +0.82% | +0.75% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +0.64% |
| SWARMS/USDT:USDT | below_1h_threshold | +0.60% | +0.52% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
