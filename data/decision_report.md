# Decision Report

- generated_at: 2026-05-01T02:31:03.865435+00:00
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

- 更新: 2026-05-01T02:31:02.566728+00:00 / 保存件数 169/288
- BTC: STAGNANT 1h -0.07% price=76591.1
- Funnel: target 760 → liquid 209 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +34.05% | $8,740,782.73 |
| BR/USDT:USDT | +25.90% | $16,528,349.32 |
| ASTEROID/USDT:USDT | +16.72% | $4,001,482.38 |
| GENIUS/USDT:USDT | +15.75% | $1,411,889.85 |
| RDDTSTOCK/USDT:USDT | +14.21% | $3,939,736.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +2.63% | +2.70% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.36% | +2.43% |
| PLAY/USDT:USDT | below_1h_threshold | +2.30% | +2.37% |
| ENSO/USDT:USDT | below_1h_threshold | +2.08% | +2.15% |
| BR/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
