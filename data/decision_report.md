# Decision Report

- generated_at: 2026-05-03T04:56:54.949567+00:00
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

- 更新: 2026-05-03T04:56:50.768045+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=78109.0
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.6 >= 65=1, 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +21.09% | $2,175,047.25 |
| BR/USDT:USDT | +16.80% | $2,151,085.37 |
| FHE/USDT:USDT | +13.10% | $2,505,469.35 |
| FIGHT/USDT:USDT | +12.99% | $1,002,316.35 |
| NAORIS/USDT:USDT | +11.13% | $4,795,190.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.80% | +3.86% |
| AKT/USDT:USDT | below_1h_threshold | +3.65% | +3.71% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.58% | +2.65% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.11% | +2.18% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.95% | +2.02% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
