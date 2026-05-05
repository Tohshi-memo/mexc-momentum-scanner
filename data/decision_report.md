# Decision Report

- generated_at: 2026-05-05T02:37:19.706968+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3295**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.13% / filled 20/20。**
- 全期間 MARKET基準: n=3295, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |
| ASK | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.77% | **+0.69%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.13% | **+0.10%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.05% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T02:37:17.548006+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80500.1
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +72.52% | $2,879,344.46 |
| TONCOIN/USDT:USDT | +27.98% | $56,901,230.51 |
| RAVE/USDT:USDT | +22.52% | $62,122,266.38 |
| NOT/USDT:USDT | +20.32% | $1,554,891.57 |
| FHE/USDT:USDT | +16.86% | $3,632,002.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TONCOIN/USDT:USDT | below_1h_threshold | +4.43% | +4.20% |
| 4/USDT:USDT | below_1h_threshold | +4.07% | +3.83% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.53% | +3.29% |
| PENGU/USDT:USDT | below_1h_threshold | +2.00% | +1.76% |
| ZRO/USDT:USDT | below_1h_threshold | +1.73% | +1.49% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
