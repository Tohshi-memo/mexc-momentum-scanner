# Decision Report

- generated_at: 2026-05-05T20:27:29.411510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3381**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3381, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.98% | **+1.04%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.59% | **+0.72%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.10% | **-0.05%** |
| LIMIT_BB3S | 4/14 | 28.6% | -1.33% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.46% | **+2.30%** |
| ASK_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.61% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.56% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:27:26.748578+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=81537.9
- Funnel: target 760 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.0 >= 65=1, 4h RSI 82.7 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +39.02% | $15,376,854.48 |
| SWARMS/USDT:USDT | +18.12% | $2,196,588.05 |
| SMCISTOCK/USDT:USDT | +16.88% | $2,403,426.82 |
| STX/USDT:USDT | +15.68% | $14,647,645.90 |
| ZEC/USDT:USDT | +10.74% | $457,941,696.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.97% | +4.99% |
| ICP/USDT:USDT | below_1h_threshold | +4.55% | +4.57% |
| 4/USDT:USDT | below_1h_threshold | +3.29% | +3.31% |
| SWARMS/USDT:USDT | below_1h_threshold | +3.17% | +3.19% |
| DOGS/USDT:USDT | below_1h_threshold | +2.83% | +2.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
