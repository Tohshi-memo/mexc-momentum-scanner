# Decision Report

- generated_at: 2026-05-04T12:17:15.794334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3199**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.22% / filled 20/20。**
- 全期間 MARKET基準: n=3199, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.22% | **+1.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.22% | **+1.22%** |
| ASK | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.56% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.17% | **+0.47%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.46% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T12:17:13.970789+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78822.6
- Funnel: target 761 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +89.84% | $10,882,550.55 |
| SKYAI/USDT:USDT | +68.51% | $62,407,413.02 |
| GIGA/USDT:USDT | +59.14% | $2,013,599.82 |
| TAG/USDT:USDT | +38.99% | $15,720,102.69 |
| 4/USDT:USDT | +27.02% | $1,606,580.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.20% | +2.11% |
| AIOT/USDT:USDT | below_1h_threshold | +2.09% | +2.00% |
| UB/USDT:USDT | below_1h_threshold | +1.72% | +1.63% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.60% | +1.51% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.39% | +1.31% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
