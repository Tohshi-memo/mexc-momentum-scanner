# Decision Report

- generated_at: 2026-04-30T14:01:23.569971+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2708**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.76% / filled 20/20。**
- 全期間 MARKET基準: n=2708, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.76% | **+1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.90% | **+1.81%** |
| MARKET | 20/20 | 100.0% | +1.76% | **+1.76%** |
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.95% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.40% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T14:01:22.077904+00:00 / 保存件数 13/288
- BTC: STAGNANT 1h +0.04% price=76401.8
- Funnel: target 760 → liquid 222 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROLL/USDT:USDT | +42.93% | $2,837,296.81 |
| BSB/USDT:USDT | +31.35% | $42,767,892.23 |
| SKYAI/USDT:USDT | +26.79% | $22,854,383.76 |
| ASTEROID/USDT:USDT | +25.61% | $2,959,870.08 |
| BR/USDT:USDT | +22.36% | $1,192,882.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ATH/USDT:USDT | below_1h_threshold | +1.23% | +1.19% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.10% | +1.06% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +0.64% | +0.60% |
| UB/USDT:USDT | below_1h_threshold | +0.62% | +0.58% |
| LLYSTOCK/USDT:USDT | below_1h_threshold | +0.49% | +0.45% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
