# Decision Report

- generated_at: 2026-05-04T12:07:12.116270+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3198**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=3198, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.56% | **+0.31%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.89% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T12:07:10.131730+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78749.0
- Funnel: target 761 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +89.20% | $10,616,752.24 |
| SKYAI/USDT:USDT | +65.02% | $61,583,637.48 |
| GIGA/USDT:USDT | +60.45% | $1,980,247.79 |
| TAG/USDT:USDT | +38.77% | $15,617,340.34 |
| BSB/USDT:USDT | +27.63% | $29,185,410.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QUBIC/USDT:USDT | below_1h_threshold | +1.51% | +1.52% |
| AIOT/USDT:USDT | below_1h_threshold | +0.93% | +0.93% |
| ZEN/USDT:USDT | below_1h_threshold | +0.86% | +0.87% |
| GIGA/USDT:USDT | below_1h_threshold | +0.86% | +0.86% |
| DASH/USDT:USDT | below_1h_threshold | +0.82% | +0.83% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
