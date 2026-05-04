# Decision Report

- generated_at: 2026-05-04T07:02:23.334025+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3167**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=3167, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| ASK | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.26% | **+1.13%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.60% | **+1.04%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.41% | **+0.99%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.45% | **+0.22%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.07% | **+0.05%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.05% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T07:02:21.418463+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79853.7
- Funnel: target 758 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +53.59% | $47,867,623.83 |
| BSB/USDT:USDT | +52.72% | $23,861,008.40 |
| TAG/USDT:USDT | +43.80% | $10,362,584.22 |
| LAB/USDT:USDT | +43.23% | $213,046,766.69 |
| TST/USDT:USDT | +37.14% | $6,692,473.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.87% | +2.84% |
| BSB/USDT:USDT | below_1h_threshold | +1.89% | +1.85% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.74% | +1.70% |
| ORDI/USDT:USDT | below_1h_threshold | +1.23% | +1.20% |
| TST/USDT:USDT | below_1h_threshold | +1.05% | +1.01% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
