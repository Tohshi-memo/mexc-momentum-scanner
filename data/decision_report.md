# Decision Report

- generated_at: 2026-05-01T07:10:54.319303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2760**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=2760, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.91% | **+0.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.74% | **+0.66%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.15% | **+0.72%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.46% | **+0.35%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.18% | **+0.13%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.08% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T07:10:52.682233+00:00 / 保存件数 226/288
- BTC: STAGNANT 1h +0.10% price=77032.5
- Funnel: target 760 → liquid 203 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +47.08% | $3,488,947.29 |
| BR/USDT:USDT | +29.45% | $18,990,881.95 |
| ORCA/USDT:USDT | +28.86% | $10,014,063.81 |
| GENIUS/USDT:USDT | +21.37% | $1,528,274.18 |
| RDDTSTOCK/USDT:USDT | +14.56% | $3,909,615.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.82% | +2.72% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.64% | +1.53% |
| DRIFT/USDT:USDT | below_1h_threshold | +1.33% | +1.23% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.03% | +0.92% |
| BRETT/USDT:USDT | below_1h_threshold | +0.87% | +0.77% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
