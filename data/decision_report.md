# Decision Report

- generated_at: 2026-09-24T00:36:11.901206+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15450**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.50% / filled 20/20。**
- 全期間 MARKET基準: n=15450, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.50% | **+0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +1.51% | **+1.13%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.20% | **+1.02%** |
| LIMIT_5PCT | 5/20 | 25.0% | +3.77% | **+0.94%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.87% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.80% | **+0.99%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.07% | **+0.59%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5897件 (Win 1739 / Loss 1890 / Flat 2268) / skip 6114件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.92** / 初期 $100.00 (+152.92%)
- 確定: 3397件 (Win 936 / Loss 790 / Flat 1671) / skip 5464件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0654 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $252.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定: 3141件 (Win 925 / Loss 1237 / Flat 979) / pending 2件 / skip 3777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $121.01

## 6. Latest Market Context

- 更新: 2026-09-24T00:36:04.108067+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=84304.9
- Funnel: target 1061 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +33.91% | $13,333,015.70 |
| NOM/USDT:USDT | +25.72% | $1,018,227.05 |
| LSK/USDT:USDT | +12.31% | $4,426,016.04 |
| MARSCOIN/USDT:USDT | +10.02% | $3,373,363.44 |
| BTW/USDT:USDT | +9.20% | $3,883,564.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KERNEL/USDT:USDT | below_1h_threshold | +2.96% | +3.02% |
| COMP/USDT:USDT | below_1h_threshold | +2.61% | +2.67% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.80% | +1.86% |
| GRASS/USDT:USDT | below_1h_threshold | +1.80% | +1.86% |
| NIL/USDT:USDT | below_1h_threshold | +1.73% | +1.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
