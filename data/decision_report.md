# Decision Report

- generated_at: 2026-05-04T19:22:18.355759+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3251**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=3251, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.17% | **+1.11%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.14% | **+0.92%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.09% | **+0.71%** |
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.69% | **+1.08%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.62% | **+1.05%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T19:22:16.362513+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=79950.0
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +21.42% | $18,412,824.66 |
| LUNC/USDT:USDT | +9.19% | $68,831,748.17 |
| TST/USDT:USDT | +9.03% | $22,148,156.93 |
| LUNANEW/USDT:USDT | +7.19% | $1,044,378.70 |
| BB/USDT:USDT | +7.11% | $1,015,281.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +1.55% | +1.71% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.28% |
| W/USDT:USDT | below_1h_threshold | +1.02% | +1.18% |
| BIO/USDT:USDT | below_1h_threshold | +0.86% | +1.02% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.85% | +1.01% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
