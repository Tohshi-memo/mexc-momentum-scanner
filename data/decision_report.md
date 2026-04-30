# Decision Report

- generated_at: 2026-04-30T21:31:03.815663+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2736, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.68% | **+1.07%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.42% | **+0.64%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.09% | **+2.47%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.23% | **+2.12%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.86% | **+1.74%** |
| ASK_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T21:31:02.235367+00:00 / 保存件数 107/288
- BTC: STAGNANT 1h -0.17% price=76322.3
- Funnel: target 756 → liquid 223 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +17.19% | $12,659,320.59 |
| ORCA/USDT:USDT | +13.55% | $2,992,688.06 |
| AIOT/USDT:USDT | +12.06% | $16,779,004.08 |
| DRIFT/USDT:USDT | +11.33% | $1,246,270.02 |
| GENIUS/USDT:USDT | +11.04% | $1,091,625.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +4.60% | +4.76% |
| BR/USDT:USDT | below_1h_threshold | +2.60% | +2.77% |
| ENSO/USDT:USDT | below_1h_threshold | +2.29% | +2.46% |
| AIOT/USDT:USDT | below_1h_threshold | +2.13% | +2.30% |
| BLEND/USDT:USDT | below_1h_threshold | +1.93% | +2.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
