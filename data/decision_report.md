# Decision Report

- generated_at: 2026-05-05T12:17:08.550762+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3347**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3347, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.99% | **+0.64%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.64% | **+0.48%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T12:17:07.016354+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=81060.8
- Funnel: target 765 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +94.31% | $21,059,738.22 |
| HIVE/USDT:USDT | +43.71% | $7,221,609.95 |
| LAB/USDT:USDT | +40.14% | $97,605,884.88 |
| TONCOIN/USDT:USDT | +29.42% | $103,232,043.53 |
| M/USDT:USDT | +27.30% | $7,579,171.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.73% | +2.62% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.82% | +1.71% |
| MERL/USDT:USDT | below_1h_threshold | +1.54% | +1.43% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.22% | +1.11% |
| M/USDT:USDT | below_1h_threshold | +1.10% | +0.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
