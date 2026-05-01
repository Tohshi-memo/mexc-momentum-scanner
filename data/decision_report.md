# Decision Report

- generated_at: 2026-05-01T06:40:57.897205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2758**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=2758, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.91% | **+0.73%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| ASK | 20/20 | 100.0% | +0.51% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.41% | **+0.63%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.58% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T06:40:56.042296+00:00 / 保存件数 220/288
- BTC: STAGNANT 1h -0.17% price=77002.5
- Funnel: target 760 → liquid 205 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +41.86% | $2,972,222.26 |
| ORCA/USDT:USDT | +28.72% | $10,017,311.75 |
| BR/USDT:USDT | +27.98% | $18,767,761.02 |
| GENIUS/USDT:USDT | +17.97% | $1,506,017.27 |
| AIOT/USDT:USDT | +15.87% | $18,169,500.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +3.48% | +3.65% |
| LUNANEW/USDT:USDT | below_1h_threshold | +2.77% | +2.94% |
| EDU/USDT:USDT | below_1h_threshold | +1.91% | +2.08% |
| ZBCN/USDT:USDT | below_1h_threshold | +1.87% | +2.04% |
| APE/USDT:USDT | below_1h_threshold | +1.33% | +1.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
