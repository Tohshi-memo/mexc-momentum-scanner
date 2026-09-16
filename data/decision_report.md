# Decision Report

- generated_at: 2026-09-16T15:01:29.908916+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14701**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14701, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.35% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +4.04% | **+3.84%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +4.36% | **+3.71%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +3.82% | **+2.39%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.79** / 初期 $100.00 (+1075.79%)
- 確定: 5578件 (Win 1673 / Loss 1803 / Flat 2102) / skip 5684件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,175.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.59** / 初期 $100.00 (+140.59%)
- 確定: 3105件 (Win 861 / Loss 734 / Flat 1510) / skip 5007件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1799 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $240.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.75** / 初期 $100.00 (+23.75%)
- 確定: 2955件 (Win 878 / Loss 1164 / Flat 913) / pending 1件 / skip 3217件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000568 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.75

## 6. Latest Market Context

- 更新: 2026-09-16T15:01:15.399198+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=75687.1
- Funnel: target 1059 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +123.28% | $25,579,866.06 |
| BR/USDT:USDT | +122.75% | $33,493,587.36 |
| LSK/USDT:USDT | +48.78% | $29,265,574.00 |
| HEI/USDT:USDT | +18.73% | $1,099,263.45 |
| 4/USDT:USDT | +17.44% | $1,649,554.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.34% |
| TESLA/USDT:USDT | below_1h_threshold | +1.24% | +1.20% |
| SNXX/USDT:USDT | below_1h_threshold | +0.98% | +0.94% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +0.84% |
| LSK/USDT:USDT | below_1h_threshold | +0.70% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
