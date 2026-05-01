# Decision Report

- generated_at: 2026-05-01T21:02:06.601992+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2831**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=2831, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.79% | **+1.79%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.94% | **+0.70%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.49% | **+0.29%** |
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +0.57% | **+0.28%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.50% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T21:02:04.885698+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77857.1
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +31.02% | $5,914,106.68 |
| ZEN/USDT:USDT | +10.94% | $7,567,566.53 |
| TAG/USDT:USDT | +9.59% | $3,432,488.98 |
| WOJAK/USDT:USDT | +8.93% | $1,010,049.13 |
| SQD/USDT:USDT | +8.85% | $2,128,274.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +1.05% | +1.03% |
| GUA/USDT:USDT | below_1h_threshold | +1.00% | +0.97% |
| LAB/USDT:USDT | below_1h_threshold | +0.78% | +0.76% |
| SQD/USDT:USDT | below_1h_threshold | +0.60% | +0.58% |
| BR/USDT:USDT | below_1h_threshold | +0.59% | +0.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
