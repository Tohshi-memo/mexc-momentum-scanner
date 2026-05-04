# Decision Report

- generated_at: 2026-05-04T21:02:27.461524+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3259**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=3259, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.17% | **+1.11%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.92% | **+0.88%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.13% | **+0.83%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.84% | **+0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.54% | **+1.16%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.61% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T21:02:25.532171+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79974.9
- Funnel: target 759 → liquid 194 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +45.10% | $41,418,450.62 |
| SKYAI/USDT:USDT | +12.13% | $102,241,349.05 |
| TST/USDT:USDT | +11.44% | $22,649,258.07 |
| FHE/USDT:USDT | +11.29% | $2,581,227.93 |
| LUNC/USDT:USDT | +9.90% | $73,597,586.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGGLE/USDT:USDT | below_1h_threshold | +2.09% | +1.99% |
| TST/USDT:USDT | below_1h_threshold | +1.57% | +1.48% |
| 4/USDT:USDT | below_1h_threshold | +0.94% | +0.84% |
| MYX/USDT:USDT | below_1h_threshold | +0.75% | +0.65% |
| AIOZ/USDT:USDT | below_1h_threshold | +0.62% | +0.52% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
