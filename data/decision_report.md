# Decision Report

- generated_at: 2026-05-24T03:04:10.476780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4807**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4807, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.09% | **-0.07%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.47% | **-0.16%** |
| LIMIT_2PCT | 16/20 | 80.0% | -0.58% | **-0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.60% | **+1.36%** |
| ASK_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.78% | **+1.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.94% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.91** / 初期 $100.00 (+20.91%)
- 確定: 616件 (Win 150 / Loss 195 / Flat 271) / skip 752件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_7PCT_LONG` SL_HIT account -0.50% 残高後 $120.91

## 4. Latest Market Context

- 更新: 2026-05-24T03:04:08.354297+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=76810.4
- Funnel: target 764 → liquid 114 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +17.07% | $8,057,070.03 |
| BLUAI/USDT:USDT | +15.57% | $1,785,488.74 |
| NIL/USDT:USDT | +12.96% | $1,960,082.06 |
| IN/USDT:USDT | +10.03% | $3,473,222.75 |
| EIGEN/USDT:USDT | +9.42% | $2,760,855.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IN/USDT:USDT | below_1h_threshold | +0.87% | +0.85% |
| MYX/USDT:USDT | below_1h_threshold | +0.79% | +0.76% |
| ICP/USDT:USDT | below_1h_threshold | +0.23% | +0.20% |
| HYPE/USDT:USDT | below_1h_threshold | +0.22% | +0.20% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.22% | +0.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
