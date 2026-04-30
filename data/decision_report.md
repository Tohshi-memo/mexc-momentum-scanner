# Decision Report

- generated_at: 2026-04-30T18:36:20.691544+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2728**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2728, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.23% | **+1.06%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.28% | **+0.58%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.85% | **+0.56%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +6.70% | **+2.35%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +5.47% | **+2.19%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T18:36:19.000069+00:00 / 保存件数 71/288
- BTC: STAGNANT 1h +0.06% price=76256.2
- Funnel: target 757 → liquid 229 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +18.58% | $6,606,320.06 |
| AIOT/USDT:USDT | +12.98% | $15,088,467.14 |
| ASTEROID/USDT:USDT | +6.34% | $3,846,052.60 |
| ZEREBRO/USDT:USDT | +5.69% | $3,423,150.97 |
| BIO/USDT:USDT | +5.58% | $3,764,864.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IONQSTOCK/USDT:USDT | below_1h_threshold | +2.50% | +2.43% |
| LUNANEW/USDT:USDT | below_1h_threshold | +1.88% | +1.82% |
| PENGU/USDT:USDT | below_1h_threshold | +1.75% | +1.69% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.70% | +1.63% |
| USOIL/USDT:USDT | below_1h_threshold | +1.50% | +1.44% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
