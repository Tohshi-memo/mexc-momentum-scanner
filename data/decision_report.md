# Decision Report

- generated_at: 2026-05-01T20:36:54.482361+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2830**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=2830, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.86% | **+1.86%** |
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +1.71% | **+0.76%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.94% | **+0.70%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.54% | **+0.41%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.36% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T20:36:52.740185+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=78081.5
- Funnel: target 755 → liquid 190 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +18.32% | $3,925,725.52 |
| ZEN/USDT:USDT | +10.48% | $7,049,390.97 |
| SQD/USDT:USDT | +10.09% | $2,122,393.98 |
| FIGHT/USDT:USDT | +9.29% | $1,243,163.56 |
| ZEC/USDT:USDT | +7.67% | $277,105,047.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +2.86% | +3.16% |
| SQD/USDT:USDT | below_1h_threshold | +2.35% | +2.65% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.06% | +2.36% |
| ZEN/USDT:USDT | below_1h_threshold | +1.63% | +1.93% |
| LINSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.84% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
