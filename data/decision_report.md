# Decision Report

- generated_at: 2026-05-06T07:27:30.583070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3429**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=3429, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_BB3S | 4/10 | 40.0% | +2.40% | **+0.96%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_BB3S_LONG | 8/10 | 80.0% | +0.81% | **+0.65%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.32% | **+0.25%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.05% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T07:27:27.962153+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=81546.5
- Funnel: target 765 → liquid 193 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.2 >= 65=1, 4h RSI 82.8 >= 65=1, 4h RSI 91.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +57.56% | $4,134,170.17 |
| ZEC/USDT:USDT | +35.11% | $673,443,554.55 |
| STORJ/USDT:USDT | +26.54% | $2,400,167.33 |
| LAB/USDT:USDT | +25.09% | $129,970,820.76 |
| B3/USDT:USDT | +23.76% | $1,433,826.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEGEN/USDT:USDT | below_1h_threshold | +3.20% | +3.06% |
| FHE/USDT:USDT | below_1h_threshold | +2.61% | +2.47% |
| VVV/USDT:USDT | below_1h_threshold | +2.49% | +2.35% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.35% | +2.21% |
| DUSK/USDT:USDT | below_1h_threshold | +2.24% | +2.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
