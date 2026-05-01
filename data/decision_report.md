# Decision Report

- generated_at: 2026-05-01T21:07:20.835885+00:00
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

- 更新: 2026-05-01T21:07:19.151869+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=77888.1
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +28.23% | $6,203,146.80 |
| ZEN/USDT:USDT | +10.92% | $7,842,992.84 |
| TAG/USDT:USDT | +9.14% | $3,448,082.77 |
| FIGHT/USDT:USDT | +8.90% | $1,211,802.72 |
| SQD/USDT:USDT | +8.04% | $2,132,931.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.28% | +1.22% |
| GUA/USDT:USDT | below_1h_threshold | +0.85% | +0.79% |
| RAVE/USDT:USDT | below_1h_threshold | +0.75% | +0.69% |
| ORCA/USDT:USDT | below_1h_threshold | +0.55% | +0.49% |
| TRADOOR/USDT:USDT | below_1h_threshold | +0.46% | +0.40% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
