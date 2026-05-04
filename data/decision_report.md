# Decision Report

- generated_at: 2026-05-04T07:12:59.563973+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3168**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3168, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| ASK | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.51% | **+1.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.86% | **+1.12%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.67% | **+1.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.15% | **-0.08%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.20% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T07:12:57.704719+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79779.9
- Funnel: target 759 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +55.63% | $24,305,815.47 |
| SKYAI/USDT:USDT | +54.56% | $48,095,122.94 |
| TAG/USDT:USDT | +46.14% | $10,708,438.07 |
| TST/USDT:USDT | +37.07% | $6,712,423.30 |
| LAB/USDT:USDT | +36.32% | $213,939,767.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.76% | +3.82% |
| GIGA/USDT:USDT | below_1h_threshold | +3.38% | +3.43% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.34% | +2.40% |
| TST/USDT:USDT | below_1h_threshold | +1.47% | +1.53% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.44% | +1.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
