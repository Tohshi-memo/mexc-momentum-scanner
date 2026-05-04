# Decision Report

- generated_at: 2026-05-04T21:17:19.651190+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3261**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=3261, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.40% | **+1.26%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.92% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.67% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.49% | **+1.26%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.15% | **+0.63%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.57% | **+0.63%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.81% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T21:17:17.619299+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=80069.0
- Funnel: target 759 → liquid 196 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +35.55% | $45,269,448.67 |
| FHE/USDT:USDT | +11.47% | $2,618,066.48 |
| SKYAI/USDT:USDT | +9.81% | $103,347,715.55 |
| LUNC/USDT:USDT | +8.51% | $74,096,212.80 |
| TST/USDT:USDT | +8.31% | $22,715,028.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +2.66% | +2.45% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.28% | +2.07% |
| 4/USDT:USDT | below_1h_threshold | +2.28% | +2.06% |
| ZEC/USDT:USDT | below_1h_threshold | +1.46% | +1.25% |
| QUBIC/USDT:USDT | below_1h_threshold | +1.32% | +1.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
