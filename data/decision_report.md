# Decision Report

- generated_at: 2026-05-03T05:07:02.566657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3029**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=3029, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.24% | **+2.24%** |
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.68% | **+0.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.35% | **+0.07%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.28% | **+0.07%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.16% | **-0.13%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.40% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T05:07:00.502023+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78200.0
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +24.76% | $2,271,115.64 |
| BR/USDT:USDT | +21.03% | $2,172,928.21 |
| FIGHT/USDT:USDT | +16.79% | $1,001,096.22 |
| FHE/USDT:USDT | +16.01% | $2,487,060.05 |
| AKT/USDT:USDT | +12.31% | $1,177,939.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +3.32% | +3.23% |
| BABY/USDT:USDT | below_1h_threshold | +2.15% | +2.07% |
| BR/USDT:USDT | below_1h_threshold | +2.11% | +2.03% |
| UB/USDT:USDT | below_1h_threshold | +1.87% | +1.78% |
| XNY/USDT:USDT | below_1h_threshold | +1.12% | +1.03% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
