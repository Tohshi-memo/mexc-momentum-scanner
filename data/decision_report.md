# Decision Report

- generated_at: 2026-05-04T06:02:24.165852+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3162**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=3162, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.74% | **+0.48%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.45% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.07% | **+1.14%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.85% | **+0.34%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T06:02:22.364319+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79959.1
- Funnel: target 758 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +62.33% | $23,197,058.36 |
| TAG/USDT:USDT | +58.84% | $7,787,042.00 |
| SKYAI/USDT:USDT | +56.58% | $46,405,163.74 |
| LAB/USDT:USDT | +40.50% | $213,562,363.77 |
| TST/USDT:USDT | +37.07% | $6,527,915.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.48% | +1.51% |
| MEGA/USDT:USDT | below_1h_threshold | +0.91% | +0.94% |
| BANANAS31/USDT:USDT | below_1h_threshold | +0.52% | +0.55% |
| QUBIC/USDT:USDT | below_1h_threshold | +0.48% | +0.51% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.35% | +0.38% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
