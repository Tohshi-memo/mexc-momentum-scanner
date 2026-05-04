# Decision Report

- generated_at: 2026-05-04T09:47:22.302388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3178**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3178, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.93% | **+0.43%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:47:19.725464+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=79802.5
- Funnel: target 761 → liquid 182 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1, 4h RSI 80.4 >= 65=1, 4h RSI 89.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +67.89% | $8,289,773.44 |
| SKYAI/USDT:USDT | +59.78% | $51,238,696.32 |
| TAG/USDT:USDT | +49.38% | $13,825,952.23 |
| GIGA/USDT:USDT | +42.16% | $1,346,789.08 |
| 4/USDT:USDT | +36.08% | $1,263,097.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.62% | +4.45% |
| ZBT/USDT:USDT | below_1h_threshold | +4.47% | +4.30% |
| DASH/USDT:USDT | below_1h_threshold | +3.93% | +3.76% |
| MERL/USDT:USDT | below_1h_threshold | +2.94% | +2.77% |
| 4/USDT:USDT | below_1h_threshold | +2.61% | +2.44% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
