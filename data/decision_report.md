# Decision Report

- generated_at: 2026-05-04T11:02:33.911486+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3194**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3194, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.54% | **+0.40%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.34% | **+0.33%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.91% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.20% | **+1.02%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.87% | **+0.65%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.55%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T11:02:31.984953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78992.5
- Funnel: target 761 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +92.89% | $9,033,852.15 |
| SKYAI/USDT:USDT | +74.64% | $57,210,832.82 |
| TAG/USDT:USDT | +46.81% | $14,863,954.68 |
| GIGA/USDT:USDT | +46.49% | $1,684,610.66 |
| 4/USDT:USDT | +39.55% | $1,455,487.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.55% | +3.43% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.46% | +2.34% |
| LAB/USDT:USDT | below_1h_threshold | +1.90% | +1.78% |
| 4/USDT:USDT | below_1h_threshold | +1.62% | +1.49% |
| AIOT/USDT:USDT | below_1h_threshold | +1.29% | +1.17% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
