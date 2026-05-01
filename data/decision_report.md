# Decision Report

- generated_at: 2026-05-01T08:05:52.631456+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2766**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=2766, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.87% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.69% | **+0.55%** |
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.96% | **+1.31%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.25% | **+0.69%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.59% | **+0.45%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.39% | **+0.28%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.13% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:05:50.944886+00:00 / 保存件数 237/288
- BTC: STAGNANT 1h -0.05% price=77059.2
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +57.93% | $2,574,253.78 |
| ZEREBRO/USDT:USDT | +54.61% | $4,900,670.02 |
| ORCA/USDT:USDT | +27.84% | $10,157,559.38 |
| BR/USDT:USDT | +20.66% | $20,421,199.62 |
| GENIUS/USDT:USDT | +17.01% | $1,584,428.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.27% | +3.32% |
| ST/USDT:USDT | below_1h_threshold | +2.70% | +2.76% |
| BR/USDT:USDT | below_1h_threshold | +2.42% | +2.47% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +2.02% | +2.08% |
| LINSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +2.01% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
