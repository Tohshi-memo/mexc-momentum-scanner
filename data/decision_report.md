# Decision Report

- generated_at: 2026-05-04T20:57:23.546861+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3259**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=3259, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.17% | **+1.11%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.92% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.13% | **+0.83%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.84% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.54% | **+1.16%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.61% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T20:57:21.407759+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=79910.8
- Funnel: target 760 → liquid 203 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +46.86% | $41,141,269.25 |
| SKYAI/USDT:USDT | +11.07% | $103,095,499.81 |
| FHE/USDT:USDT | +10.40% | $2,666,323.44 |
| LUNC/USDT:USDT | +8.77% | $74,190,771.05 |
| TST/USDT:USDT | +8.59% | $22,713,603.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.23% | +3.37% |
| FHE/USDT:USDT | below_1h_threshold | +3.17% | +3.30% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.79% | +2.92% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.03% | +2.16% |
| AIOZ/USDT:USDT | below_1h_threshold | +2.00% | +2.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
