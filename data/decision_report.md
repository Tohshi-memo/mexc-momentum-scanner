# Decision Report

- generated_at: 2026-05-04T19:37:18.647440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3253**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=3253, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.17% | **+1.11%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.14% | **+0.92%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.83% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.76% | **+1.14%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.93% | **+0.68%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T19:37:16.703452+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=79962.3
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +29.73% | $20,221,236.26 |
| TST/USDT:USDT | +11.76% | $22,252,369.35 |
| LUNC/USDT:USDT | +8.87% | $69,648,524.12 |
| USTC/USDT:USDT | +8.66% | $1,388,805.58 |
| BB/USDT:USDT | +7.51% | $1,027,420.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.78% | +4.92% |
| TST/USDT:USDT | below_1h_threshold | +3.42% | +3.57% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.44% | +2.59% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.32% | +2.47% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.05% | +2.19% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
