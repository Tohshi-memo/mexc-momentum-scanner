# Decision Report

- generated_at: 2026-04-30T13:35:58.817613+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2706**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.76% / filled 20/20。**
- 全期間 MARKET基準: n=2706, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.76% | **+1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.96% | **+1.86%** |
| MARKET | 20/20 | 100.0% | +1.76% | **+1.76%** |
| ASK | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.56% | **+1.01%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.35% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$101.00** / 初期 $100.00 (+1.00%)
- 確定トレード: 1件 (TP 1 / SL 0 / EXP 0)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.00
- 最新戦略メタ: tier=未記録, direction=未記録, entry=未記録

## 3. Latest Market Context

- 更新: 2026-04-30T13:35:57.157064+00:00 / 保存件数 8/288
- BTC: STAGNANT 1h +0.02% price=76273.9
- Funnel: target 760 → liquid 223 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROLL/USDT:USDT | +47.08% | $2,809,732.31 |
| BSB/USDT:USDT | +32.58% | $43,656,179.63 |
| SKYAI/USDT:USDT | +27.88% | $23,618,689.37 |
| ASTEROID/USDT:USDT | +25.24% | $2,913,443.62 |
| BIO/USDT:USDT | +21.22% | $3,394,176.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRIFFAIN/USDT:USDT | below_1h_threshold | +4.68% | +4.66% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.38% | +3.36% |
| LUNC/USDT:USDT | below_1h_threshold | +3.36% | +3.34% |
| FIGHT/USDT:USDT | below_1h_threshold | +3.07% | +3.05% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.95% | +1.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
