# Decision Report

- generated_at: 2026-05-03T05:22:15.231811+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3034**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.66% / filled 20/20。**
- 全期間 MARKET基準: n=3034, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.69% | **+1.69%** |
| MARKET | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.34% | **+1.01%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.21% | **+0.97%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.93% | **+0.65%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.41%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.26% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T05:22:10.353931+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78194.1
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +23.23% | $2,573,733.39 |
| BR/USDT:USDT | +21.44% | $2,274,970.06 |
| B/USDT:USDT | +17.16% | $39,879,320.05 |
| AKT/USDT:USDT | +13.65% | $1,204,261.04 |
| FHE/USDT:USDT | +12.90% | $2,511,502.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.95% | +2.87% |
| BB/USDT:USDT | below_1h_threshold | +2.74% | +2.66% |
| BR/USDT:USDT | below_1h_threshold | +2.28% | +2.20% |
| AKT/USDT:USDT | below_1h_threshold | +1.80% | +1.72% |
| H/USDT:USDT | below_1h_threshold | +1.22% | +1.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
