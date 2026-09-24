# Decision Report

- generated_at: 2026-09-24T00:56:18.848099+00:00
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

- 更新: 2026-09-24T00:56:07.609835+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=84229.7
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +49.55% | $1,270,881.12 |
| NIL/USDT:USDT | +33.59% | $13,854,034.03 |
| LSK/USDT:USDT | +16.51% | $4,532,515.67 |
| BTW/USDT:USDT | +10.22% | $3,947,757.99 |
| MARSCOIN/USDT:USDT | +9.37% | $3,389,126.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KERNEL/USDT:USDT | below_1h_threshold | +4.62% | +4.77% |
| COMP/USDT:USDT | below_1h_threshold | +2.29% | +2.44% |
| GRASS/USDT:USDT | below_1h_threshold | +1.60% | +1.75% |
| CAKE/USDT:USDT | below_1h_threshold | +1.42% | +1.57% |
| NIL/USDT:USDT | below_1h_threshold | +1.31% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
