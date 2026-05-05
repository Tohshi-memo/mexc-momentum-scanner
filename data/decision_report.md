# Decision Report

- generated_at: 2026-05-05T21:32:48.454113+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3390**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3390, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.24% | **+0.50%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.42% | **+1.81%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.19% | **+1.12%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.62% | **+0.92%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.71% | **+0.86%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.01% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:32:46.050422+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=81375.5
- Funnel: target 759 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1, 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +45.44% | $19,450,619.96 |
| MAVIA/USDT:USDT | +29.75% | $1,243,746.96 |
| SWARMS/USDT:USDT | +21.53% | $2,278,865.67 |
| SMCISTOCK/USDT:USDT | +20.26% | $4,692,350.90 |
| ZEC/USDT:USDT | +19.86% | $557,081,319.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SWARMS/USDT:USDT | below_1h_threshold | +3.91% | +4.20% |
| MAVIA/USDT:USDT | below_1h_threshold | +3.91% | +4.20% |
| DASH/USDT:USDT | below_1h_threshold | +2.95% | +3.23% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.88% | +3.16% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.63% | +2.92% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
