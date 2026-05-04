# Decision Report

- generated_at: 2026-05-04T09:12:18.273424+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3174**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3174, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.99% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.27% | **+0.76%** |
| LIMIT_BB3S | 3/14 | 21.4% | +2.30% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.13% | **-0.08%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.29% | **-0.14%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:12:16.167453+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79738.0
- Funnel: target 760 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +60.44% | $7,338,299.02 |
| SKYAI/USDT:USDT | +53.55% | $48,835,576.58 |
| TAG/USDT:USDT | +45.57% | $13,238,889.63 |
| GIGA/USDT:USDT | +36.57% | $1,243,107.13 |
| 4/USDT:USDT | +36.53% | $1,218,949.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.34% | +3.25% |
| DASH/USDT:USDT | below_1h_threshold | +3.07% | +2.98% |
| 4/USDT:USDT | below_1h_threshold | +2.95% | +2.86% |
| GIGA/USDT:USDT | below_1h_threshold | +2.31% | +2.22% |
| ZBT/USDT:USDT | below_1h_threshold | +2.21% | +2.12% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
