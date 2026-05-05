# Decision Report

- generated_at: 2026-05-05T01:37:17.013983+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3286**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=3286, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.87% | **+1.68%** |
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| ASK | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.91% | **+0.49%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T01:37:11.953828+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=80238.8
- Funnel: target 765 → liquid 205 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.0 >= 65=1, 4h RSI 66.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +47.70% | $1,129,476.66 |
| RAVE/USDT:USDT | +28.99% | $60,737,132.77 |
| FHE/USDT:USDT | +22.49% | $3,323,583.34 |
| TONCOIN/USDT:USDT | +20.94% | $51,837,800.19 |
| NOT/USDT:USDT | +15.56% | $1,199,301.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TIA/USDT:USDT | below_1h_threshold | +3.22% | +3.08% |
| WLFI/USDT:USDT | below_1h_threshold | +2.53% | +2.39% |
| NOT/USDT:USDT | below_1h_threshold | +1.79% | +1.66% |
| RAVE/USDT:USDT | below_1h_threshold | +1.72% | +1.58% |
| ZRO/USDT:USDT | below_1h_threshold | +1.54% | +1.41% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
