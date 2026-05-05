# Decision Report

- generated_at: 2026-05-05T12:37:28.185348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3350**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3350, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.01% | **+0.45%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| ASK | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.95%** |
| ASK_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.03% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T12:37:23.691742+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=81220.0
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +99.65% | $21,442,318.51 |
| LAB/USDT:USDT | +46.63% | $100,099,030.15 |
| HIVE/USDT:USDT | +41.66% | $7,492,771.13 |
| TONCOIN/USDT:USDT | +29.97% | $106,365,322.83 |
| FHE/USDT:USDT | +26.62% | $5,446,908.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_relative_strength | +5.03% | +4.73% |
| NOT/USDT:USDT | below_1h_threshold | +2.88% | +2.57% |
| MORPHO/USDT:USDT | below_1h_threshold | +2.69% | +2.38% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.33% | +2.02% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.25% | +1.94% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
