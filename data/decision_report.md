# Decision Report

- generated_at: 2026-09-11T23:11:14.506877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14261**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14261, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.85% | **+0.68%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.86% | **+1.16%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.34% | **+1.01%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.84% | **+0.29%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.38% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,113.42** / 初期 $100.00 (+1013.42%)
- 確定: 5418件 (Win 1635 / Loss 1754 / Flat 2029) / skip 5404件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,113.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$210.58** / 初期 $100.00 (+110.58%)
- 確定: 2831件 (Win 780 / Loss 655 / Flat 1396) / skip 4841件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1174 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $210.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.65** / 初期 $100.00 (+24.65%)
- 確定: 2752件 (Win 816 / Loss 1054 / Flat 882) / pending 2件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000376 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $124.65

## 6. Latest Market Context

- 更新: 2026-09-11T23:11:06.272218+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77166.0
- Funnel: target 1067 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +40.81% | $14,357,862.25 |
| LAB/USDT:USDT | +27.59% | $11,692,269.85 |
| CYS/USDT:USDT | +22.07% | $1,136,853.55 |
| LSK/USDT:USDT | +14.89% | $3,135,917.33 |
| BEAT/USDT:USDT | +14.35% | $11,162,497.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.73% | +4.65% |
| LSK/USDT:USDT | below_1h_threshold | +2.21% | +2.14% |
| 4/USDT:USDT | below_1h_threshold | +1.55% | +1.47% |
| SAGA/USDT:USDT | below_1h_threshold | +1.37% | +1.29% |
| RIVER/USDT:USDT | below_1h_threshold | +1.29% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
