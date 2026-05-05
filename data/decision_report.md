# Decision Report

- generated_at: 2026-05-05T13:07:12.892418+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3352**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=3352, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.55% | **+0.52%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.63% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.35%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| ASK_LONG | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T13:07:10.907173+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=81431.5
- Funnel: target 765 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +100.79% | $22,187,782.23 |
| LAB/USDT:USDT | +53.84% | $98,963,986.84 |
| HIVE/USDT:USDT | +40.98% | $7,730,276.76 |
| FHE/USDT:USDT | +30.11% | $5,514,687.30 |
| TONCOIN/USDT:USDT | +30.02% | $109,393,320.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +2.21% | +1.95% |
| LIT/USDT:USDT | below_1h_threshold | +1.72% | +1.46% |
| LAB/USDT:USDT | below_1h_threshold | +1.45% | +1.19% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.07% | +0.81% |
| FHE/USDT:USDT | below_1h_threshold | +0.97% | +0.72% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
