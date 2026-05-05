# Decision Report

- generated_at: 2026-05-05T20:42:43.842814+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3383**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3383, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.17% | **+0.95%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.97% | **+0.63%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.11% | **-0.05%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.07% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.96% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.63% | **+0.57%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:42:39.222379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=81646.0
- Funnel: target 760 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1, 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +37.93% | $16,147,466.77 |
| MAVIA/USDT:USDT | +22.61% | $1,007,719.13 |
| SWARMS/USDT:USDT | +20.65% | $2,222,701.19 |
| SMCISTOCK/USDT:USDT | +18.32% | $3,685,097.90 |
| ZEC/USDT:USDT | +11.77% | $476,928,921.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.96% | +4.84% |
| FHE/USDT:USDT | below_1h_threshold | +4.95% | +4.84% |
| ZEN/USDT:USDT | below_1h_threshold | +4.51% | +4.40% |
| ICP/USDT:USDT | below_1h_threshold | +3.89% | +3.78% |
| NOT/USDT:USDT | below_1h_threshold | +3.63% | +3.51% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
