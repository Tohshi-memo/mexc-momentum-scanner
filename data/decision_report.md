# Decision Report

- generated_at: 2026-05-04T05:42:12.165570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3160**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=3160, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.95%** |
| LIMIT_BB3S | 4/11 | 36.4% | +2.37% | **+0.86%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.63% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.48% | **+0.74%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.65% | **+0.49%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T05:42:09.802051+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=80016.3
- Funnel: target 758 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +63.37% | $23,164,522.30 |
| SKYAI/USDT:USDT | +50.76% | $46,411,502.61 |
| TAG/USDT:USDT | +49.51% | $7,428,103.98 |
| LAB/USDT:USDT | +43.00% | $217,796,829.73 |
| TST/USDT:USDT | +41.40% | $6,466,080.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +3.86% | +4.21% |
| SAPIEN/USDT:USDT | below_1h_threshold | +3.01% | +3.36% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.96% | +3.31% |
| ORDI/USDT:USDT | below_1h_threshold | +2.75% | +3.10% |
| AIOT/USDT:USDT | below_1h_threshold | +2.60% | +2.95% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
