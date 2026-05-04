# Decision Report

- generated_at: 2026-05-04T13:17:23.292028+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3203**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=3203, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.64% | **+0.64%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.14% | **+0.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.41% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.11%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.71% | **+0.61%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.99% | **+0.54%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.33% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T13:17:21.329738+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78869.6
- Funnel: target 761 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +101.42% | $12,134,978.60 |
| SKYAI/USDT:USDT | +80.75% | $69,575,885.58 |
| GIGA/USDT:USDT | +59.20% | $2,107,576.70 |
| 4/USDT:USDT | +35.02% | $1,680,671.95 |
| TAG/USDT:USDT | +29.56% | $16,039,136.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.28% | +4.21% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.67% | +3.60% |
| TST/USDT:USDT | below_1h_threshold | +3.47% | +3.40% |
| UB/USDT:USDT | below_1h_threshold | +3.10% | +3.04% |
| LAB/USDT:USDT | below_1h_threshold | +1.57% | +1.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
