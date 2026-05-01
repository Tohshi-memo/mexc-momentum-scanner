# Decision Report

- generated_at: 2026-05-01T07:25:55.813537+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2762**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.58% / filled 20/20。**
- 全期間 MARKET基準: n=2762, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.63% | **+1.63%** |
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.35% | **+1.22%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.63% | **+0.73%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.84% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.40% | **+0.23%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.21% | **-0.15%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.34% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T07:25:54.004493+00:00 / 保存件数 229/288
- BTC: STAGNANT 1h +0.03% price=76974.9
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +52.94% | $1,427,917.32 |
| ZEREBRO/USDT:USDT | +49.10% | $3,835,691.63 |
| ORCA/USDT:USDT | +28.65% | $10,100,117.43 |
| BR/USDT:USDT | +21.09% | $19,221,508.81 |
| GENIUS/USDT:USDT | +17.46% | $1,560,868.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.25% | +4.22% |
| MYX/USDT:USDT | below_1h_threshold | +2.81% | +2.79% |
| EDU/USDT:USDT | below_1h_threshold | +1.31% | +1.28% |
| COAI/USDT:USDT | below_1h_threshold | +1.29% | +1.27% |
| ZAMA/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
