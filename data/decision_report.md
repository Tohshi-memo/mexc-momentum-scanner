# Decision Report

- generated_at: 2026-06-13T09:01:36.579028+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6570**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6570, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +1.08% | **+0.27%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.25% | **+0.10%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_3PCT | 14/20 | 70.0% | -0.27% | **-0.19%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.30% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| ASK_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.68% | **+0.59%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.77% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1443件 (Win 389 / Loss 464 / Flat 590) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T09:01:33.318967+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63810.1
- Funnel: target 770 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +54.10% | $3,550,362.54 |
| EDGE/USDT:USDT | +23.15% | $2,887,348.29 |
| RIF/USDT:USDT | +22.02% | $2,020,748.39 |
| MEGA/USDT:USDT | +14.55% | $1,000,454.48 |
| VVV/USDT:USDT | +14.01% | $6,159,759.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.09% | +1.03% |
| MEGA/USDT:USDT | below_1h_threshold | +0.77% | +0.71% |
| TAO/USDT:USDT | below_1h_threshold | +0.57% | +0.51% |
| PYTH/USDT:USDT | below_1h_threshold | +0.45% | +0.39% |
| RENDER/USDT:USDT | below_1h_threshold | +0.40% | +0.34% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
