# Decision Report

- generated_at: 2026-05-01T04:25:57.788170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2751**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2751, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.09% | **-0.09%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.66% | **+1.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.06% | **+0.90%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.24% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T04:25:56.208470+00:00 / 保存件数 193/288
- BTC: STAGNANT 1h +0.05% price=77119.4
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +28.79% | $9,554,975.91 |
| BR/USDT:USDT | +25.37% | $17,137,490.33 |
| ASTEROID/USDT:USDT | +16.75% | $4,189,272.96 |
| GENIUS/USDT:USDT | +16.44% | $1,450,281.13 |
| ZEREBRO/USDT:USDT | +16.00% | $1,777,064.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.71% | +3.66% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.88% | +2.83% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.79% | +2.75% |
| AIOT/USDT:USDT | below_1h_threshold | +2.11% | +2.06% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.05% | +2.00% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
