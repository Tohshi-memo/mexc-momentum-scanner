# Decision Report

- generated_at: 2026-05-01T06:55:57.115590+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2759**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.03% / filled 20/20。**
- 全期間 MARKET基準: n=2759, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.91% | **+0.73%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.31% | **+0.17%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.08% | **+0.05%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.07% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T06:55:55.262916+00:00 / 保存件数 223/288
- BTC: STAGNANT 1h -0.17% price=77007.0
- Funnel: target 760 → liquid 206 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEREBRO/USDT:USDT | +41.07% | $3,273,389.33 |
| ORCA/USDT:USDT | +28.38% | $10,093,715.26 |
| BR/USDT:USDT | +28.11% | $18,892,010.94 |
| GENIUS/USDT:USDT | +21.72% | $1,532,598.63 |
| RDDTSTOCK/USDT:USDT | +14.72% | $3,909,893.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNANEW/USDT:USDT | below_1h_threshold | +3.93% | +4.10% |
| GENIUS/USDT:USDT | below_1h_threshold | +3.71% | +3.88% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.09% | +3.26% |
| EDU/USDT:USDT | below_1h_threshold | +2.63% | +2.79% |
| ZBCN/USDT:USDT | below_1h_threshold | +1.92% | +2.08% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
