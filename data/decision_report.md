# Decision Report

- generated_at: 2026-04-30T13:25:58.999943+00:00
- source: `data\experiments.json` + archive=True
- closed shadow trades: **2705**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.99% / filled 20/20。**
- 全期間 MARKET基準: n=2705, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.19% | **+2.08%** |
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |
| ASK | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.39% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.12% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$101.00** / 初期 $100.00 (+1.00%)
- 確定トレード: 1件 (TP 1 / SL 0 / EXP 0)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.00
- 最新戦略メタ: tier=未記録, direction=未記録, entry=未記録

## 3. Latest Market Context

- 更新: 2026-04-30T13:20:56.259812+00:00 / 保存件数 5/288
- BTC: STAGNANT 1h +0.02% price=76277.8
- Funnel: target 760 → liquid 220 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROLL/USDT:USDT | +44.37% | $2,775,058.42 |
| BSB/USDT:USDT | +33.14% | $43,361,138.81 |
| SKYAI/USDT:USDT | +27.73% | $23,441,305.46 |
| ASTEROID/USDT:USDT | +23.68% | $2,854,916.40 |
| BIO/USDT:USDT | +19.46% | $3,357,230.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.52% | +3.49% |
| GRIFFAIN/USDT:USDT | below_1h_threshold | +3.51% | +3.49% |
| LUNC/USDT:USDT | below_1h_threshold | +2.55% | +2.53% |
| BSB/USDT:USDT | below_1h_threshold | +2.22% | +2.20% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.09% | +2.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
