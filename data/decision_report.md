# Decision Report

- generated_at: 2026-05-05T06:42:17.638900+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3321**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=3321, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_BB3S | 3/14 | 21.4% | +1.68% | **+0.36%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.36% | **+0.29%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.30% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.42% | **+0.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T06:42:15.057869+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=80778.7
- Funnel: target 765 → liquid 205 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +69.69% | $8,537,073.62 |
| HIVE/USDT:USDT | +36.14% | $3,020,752.70 |
| FHE/USDT:USDT | +26.53% | $3,872,440.49 |
| M/USDT:USDT | +25.81% | $3,414,996.88 |
| 4/USDT:USDT | +21.62% | $2,431,807.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.74% | +4.92% |
| QUBIC/USDT:USDT | below_1h_threshold | +3.56% | +3.74% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.43% | +2.61% |
| LUNC/USDT:USDT | below_1h_threshold | +1.85% | +2.03% |
| M/USDT:USDT | below_1h_threshold | +1.44% | +1.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
