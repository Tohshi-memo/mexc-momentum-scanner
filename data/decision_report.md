# Decision Report

- generated_at: 2026-09-24T01:01:17.220861+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15453**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=15453, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.54%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.74% | **+0.52%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.07% | **+0.59%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.79% | **+0.43%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5897件 (Win 1739 / Loss 1890 / Flat 2268) / skip 6117件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.21** / 初期 $100.00 (+152.21%)
- 確定: 3400件 (Win 937 / Loss 791 / Flat 1672) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0560 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $252.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.85** / 初期 $100.00 (+20.85%)
- 確定: 3143件 (Win 926 / Loss 1238 / Flat 979) / pending 3件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $120.85

## 6. Latest Market Context

- 更新: 2026-09-24T01:01:06.115945+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=84289.9
- Funnel: target 1061 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +52.04% | $1,339,215.94 |
| NIL/USDT:USDT | +35.29% | $13,901,841.72 |
| LSK/USDT:USDT | +16.82% | $4,489,058.41 |
| BTW/USDT:USDT | +10.68% | $3,887,378.34 |
| UAI/USDT:USDT | +7.80% | $2,417,652.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LSK/USDT:USDT | below_1h_threshold | +0.77% | +0.76% |
| ZRO/USDT:USDT | below_1h_threshold | +0.24% | +0.22% |
| UAI/USDT:USDT | below_1h_threshold | +0.18% | +0.17% |
| CAKE/USDT:USDT | below_1h_threshold | +0.18% | +0.16% |
| BTW/USDT:USDT | below_1h_threshold | +0.12% | +0.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
