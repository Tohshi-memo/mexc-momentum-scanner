# Decision Report

- generated_at: 2026-05-05T07:22:19.958809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3326**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3326, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +1.86% | **+0.57%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.93% | **+0.29%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.09% | **+0.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.11% | **-0.05%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.13% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +6.14% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| ASK_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T07:22:17.539344+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80961.3
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +86.46% | $9,432,736.58 |
| HIVE/USDT:USDT | +39.44% | $3,370,317.23 |
| FHE/USDT:USDT | +28.25% | $3,955,802.99 |
| M/USDT:USDT | +27.54% | $4,882,627.16 |
| LAB/USDT:USDT | +25.18% | $77,758,036.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PRL/USDT:USDT | below_1h_threshold | +1.93% | +1.90% |
| LUNC/USDT:USDT | below_1h_threshold | +1.77% | +1.74% |
| TURBO/USDT:USDT | below_1h_threshold | +1.75% | +1.72% |
| HIVE/USDT:USDT | below_1h_threshold | +1.74% | +1.71% |
| RAVE/USDT:USDT | below_1h_threshold | +1.30% | +1.26% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
