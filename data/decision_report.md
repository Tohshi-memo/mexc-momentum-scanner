# Decision Report

- generated_at: 2026-05-05T19:52:28.347872+00:00
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

- 更新: 2026-05-05T19:52:26.212522+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81473.7
- Funnel: target 760 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +30.23% | $13,178,380.27 |
| STX/USDT:USDT | +15.33% | $2,261,234.10 |
| SWARMS/USDT:USDT | +14.60% | $2,199,615.97 |
| TONCOIN/USDT:USDT | +5.40% | $169,200,691.62 |
| TAG/USDT:USDT | +5.12% | $12,269,051.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.91% | +4.90% |
| ZEC/USDT:USDT | below_1h_threshold | +4.07% | +4.05% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.97% | +2.96% |
| ZEN/USDT:USDT | below_1h_threshold | +2.44% | +2.43% |
| H/USDT:USDT | below_1h_threshold | +1.96% | +1.95% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
