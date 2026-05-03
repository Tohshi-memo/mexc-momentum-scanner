# Decision Report

- generated_at: 2026-05-03T04:02:21.727497+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3026**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.20% / filled 20/20。**
- 全期間 MARKET基準: n=3026, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.22% | **+2.22%** |
| MARKET | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_BB3S | 7/12 | 58.3% | +3.47% | **+2.02%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.94% | **+1.91%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.16% | **+1.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.68% | **+0.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.35% | **+0.07%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.28% | **+0.07%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.28% | **-0.18%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.60% | **-0.33%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T04:02:19.926820+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78168.6
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +14.73% | $2,002,488.37 |
| FHE/USDT:USDT | +14.50% | $2,430,390.01 |
| GENIUS/USDT:USDT | +12.79% | $1,081,085.06 |
| BIANRENSHENG/USDT:USDT | +11.90% | $2,196,445.12 |
| TAC/USDT:USDT | +9.12% | $2,667,014.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.81% | +1.80% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.46% | +1.45% |
| ALCH/USDT:USDT | below_1h_threshold | +0.68% | +0.68% |
| BABY/USDT:USDT | below_1h_threshold | +0.67% | +0.66% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.44% | +0.43% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
