# Decision Report

- generated_at: 2026-05-23T21:33:56.621197+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4801**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4801, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.31% | **-0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.00% | **+1.95%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.45% | **+1.84%** |
| ASK_LONG | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 746件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-23T21:33:54.537094+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.73% price=76687.7
- Funnel: target 764 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +19.28% | $1,547,899.77 |
| GRASS/USDT:USDT | +17.03% | $5,018,673.27 |
| NIL/USDT:USDT | +10.87% | $1,314,555.76 |
| GUA/USDT:USDT | +9.78% | $1,091,469.56 |
| EIGEN/USDT:USDT | +9.56% | $2,133,015.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAN/USDT:USDT | below_1h_threshold | +1.88% | +2.60% |
| GMTTOKEN/USDT:USDT | below_1h_threshold | +1.30% | +2.03% |
| NEAR/USDT:USDT | below_1h_threshold | +0.75% | +1.48% |
| UB/USDT:USDT | below_1h_threshold | +0.64% | +1.37% |
| TAO/USDT:USDT | below_1h_threshold | +0.20% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
