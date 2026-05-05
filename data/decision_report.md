# Decision Report

- generated_at: 2026-05-05T01:02:24.960738+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3282**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=3282, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| ASK | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_BB3S | 3/12 | 25.0% | +2.22% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.91% | **+0.49%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.56% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T01:02:23.033376+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=80036.6
- Funnel: target 761 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +25.62% | $59,514,011.13 |
| TONCOIN/USDT:USDT | +23.25% | $46,758,858.94 |
| FHE/USDT:USDT | +19.56% | $2,629,288.90 |
| PLAY/USDT:USDT | +13.48% | $2,684,361.99 |
| B3/USDT:USDT | +8.48% | $1,149,034.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.74% | +0.85% |
| VELO/USDT:USDT | below_1h_threshold | +0.71% | +0.82% |
| BR/USDT:USDT | below_1h_threshold | +0.40% | +0.52% |
| PLAY/USDT:USDT | below_1h_threshold | +0.20% | +0.31% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.15% | +0.26% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
