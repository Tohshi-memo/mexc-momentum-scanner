# Decision Report

- generated_at: 2026-05-05T19:57:26.241369+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3376**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=3376, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.80% | **+0.72%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.59% | **+0.72%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.47% | **+1.10%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| ASK_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.94% | **+0.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T19:57:23.795806+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=81570.1
- Funnel: target 760 → liquid 185 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1, 4h RSI 82.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +32.06% | $13,578,834.44 |
| SWARMS/USDT:USDT | +14.25% | $2,202,071.54 |
| STX/USDT:USDT | +13.63% | $2,652,369.42 |
| H/USDT:USDT | +5.57% | $10,455,931.75 |
| TONCOIN/USDT:USDT | +5.55% | $169,503,124.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.99% | +3.86% |
| TONCOIN/USDT:USDT | below_1h_threshold | +3.25% | +3.12% |
| H/USDT:USDT | below_1h_threshold | +2.55% | +2.42% |
| TST/USDT:USDT | below_1h_threshold | +2.32% | +2.19% |
| ZEN/USDT:USDT | below_1h_threshold | +2.21% | +2.08% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
