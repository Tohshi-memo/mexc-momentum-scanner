# Decision Report

- generated_at: 2026-05-05T05:52:51.850795+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3316**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3316, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.07% | **+0.32%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.95% | **+0.20%** |
| LIMIT_BB3S | 4/12 | 33.3% | +0.57% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/8 | 25.0% | +6.30% | **+1.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| ASK_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T05:52:49.504329+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=80966.1
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +70.23% | $7,897,054.16 |
| HIVE/USDT:USDT | +44.78% | $1,889,798.53 |
| FHE/USDT:USDT | +30.76% | $3,783,966.73 |
| TONCOIN/USDT:USDT | +19.68% | $66,332,527.85 |
| M/USDT:USDT | +18.88% | $2,266,466.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.79% | +3.65% |
| FHE/USDT:USDT | below_1h_threshold | +2.74% | +2.60% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.01% | +1.87% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.88% | +1.74% |
| ALGO/USDT:USDT | below_1h_threshold | +1.88% | +1.73% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
