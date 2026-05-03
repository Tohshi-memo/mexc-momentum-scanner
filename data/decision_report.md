# Decision Report

- generated_at: 2026-05-03T16:27:24.729226+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3084**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3084, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/15 | 53.3% | +2.32% | **+1.24%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.52% | **+1.39%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.61% | **+1.31%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.47% | **+1.11%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.67% | **+0.92%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.58% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T16:27:18.100860+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78619.3
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +8.81% | $327,239,602.66 |
| SKYAI/USDT:USDT | +5.33% | $23,542,629.94 |
| BB/USDT:USDT | +5.22% | $1,265,275.20 |
| TST/USDT:USDT | +3.55% | $5,010,301.19 |
| TAG/USDT:USDT | +2.42% | $10,278,232.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +3.55% | +3.56% |
| TAG/USDT:USDT | below_1h_threshold | +2.43% | +2.44% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.29% | +2.30% |
| AIOT/USDT:USDT | below_1h_threshold | +1.62% | +1.63% |
| JTO/USDT:USDT | below_1h_threshold | +1.57% | +1.57% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
