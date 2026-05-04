# Decision Report

- generated_at: 2026-05-04T09:02:34.724394+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3173**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=3173, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| ASK | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.44% | **+0.87%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.48% | **+0.81%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.69% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.46% | **-0.25%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:02:32.761572+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79682.0
- Funnel: target 760 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +54.82% | $7,105,454.28 |
| SKYAI/USDT:USDT | +52.49% | $48,390,233.63 |
| TAG/USDT:USDT | +47.12% | $13,089,740.40 |
| BSB/USDT:USDT | +38.05% | $24,961,705.76 |
| 4/USDT:USDT | +33.86% | $1,208,673.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +2.10% | +2.08% |
| LAB/USDT:USDT | below_1h_threshold | +1.48% | +1.47% |
| UB/USDT:USDT | below_1h_threshold | +1.46% | +1.44% |
| 4/USDT:USDT | below_1h_threshold | +1.07% | +1.05% |
| LUNC/USDT:USDT | below_1h_threshold | +0.72% | +0.70% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
