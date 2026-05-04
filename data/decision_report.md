# Decision Report

- generated_at: 2026-05-04T09:57:30.175395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3180**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3180, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_BB3S | 3/18 | 16.7% | +3.36% | **+0.56%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.47% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:57:27.049449+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=79846.1
- Funnel: target 761 → liquid 184 → pre 50 → checked 50 → surge 5 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1, 4h RSI 88.8 >= 65=1, 4h RSI 80.3 >= 65=1, 4h RSI 71.9 >= 65=1, 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +62.71% | $8,570,689.11 |
| SKYAI/USDT:USDT | +61.59% | $51,809,988.78 |
| TAG/USDT:USDT | +53.04% | $14,059,633.96 |
| GIGA/USDT:USDT | +47.26% | $1,374,119.14 |
| 4/USDT:USDT | +38.75% | $1,276,761.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_relative_strength | +5.18% | +4.96% |
| 4/USDT:USDT | below_1h_threshold | +4.62% | +4.40% |
| MERL/USDT:USDT | below_1h_threshold | +3.77% | +3.55% |
| AR/USDT:USDT | below_1h_threshold | +3.55% | +3.32% |
| TAG/USDT:USDT | below_1h_threshold | +2.98% | +2.75% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
