# Decision Report

- generated_at: 2026-04-30T18:18:32.769294+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2727**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2727, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.34% | **+0.67%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.85% | **+0.56%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.86% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +6.55% | **+2.29%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.51% | **+2.13%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T18:18:31.298254+00:00 / 保存件数 67/288
- BTC: BULLISH 1h +0.26% price=76409.1
- Funnel: target 757 → liquid 229 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +19.23% | $6,163,208.74 |
| AIOT/USDT:USDT | +18.63% | $14,086,726.36 |
| ASTEROID/USDT:USDT | +5.55% | $3,813,462.58 |
| ZEREBRO/USDT:USDT | +5.46% | $3,406,604.66 |
| BIO/USDT:USDT | +4.82% | $3,738,169.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +2.36% | +2.10% |
| PENGU/USDT:USDT | below_1h_threshold | +1.86% | +1.60% |
| LUNANEW/USDT:USDT | below_1h_threshold | +1.39% | +1.13% |
| ZEC/USDT:USDT | below_1h_threshold | +1.21% | +0.94% |
| DASH/USDT:USDT | below_1h_threshold | +1.00% | +0.74% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
