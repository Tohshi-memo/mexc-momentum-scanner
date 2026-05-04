# Decision Report

- generated_at: 2026-05-04T23:07:11.748259+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3272**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.48% / filled 20/20。**
- 全期間 MARKET基準: n=3272, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.51% | **+1.51%** |
| MARKET | 20/20 | 100.0% | +1.48% | **+1.48%** |
| LIMIT_BB3S | 3/7 | 42.9% | +2.22% | **+0.95%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.36% | **+0.81%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T23:07:09.816680+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=79916.0
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +23.58% | $53,170,137.66 |
| FHE/USDT:USDT | +18.02% | $2,541,622.55 |
| TST/USDT:USDT | +12.93% | $23,696,937.79 |
| NAORIS/USDT:USDT | +12.80% | $3,212,610.17 |
| TONCOIN/USDT:USDT | +12.34% | $35,760,109.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +2.84% | +2.98% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.88% | +1.02% |
| B3/USDT:USDT | below_1h_threshold | +0.61% | +0.75% |
| WLFI/USDT:USDT | below_1h_threshold | +0.47% | +0.62% |
| ZEC/USDT:USDT | below_1h_threshold | +0.44% | +0.59% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
