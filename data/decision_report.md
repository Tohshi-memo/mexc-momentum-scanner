# Decision Report

- generated_at: 2026-09-12T21:16:22.383189+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14323**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14323, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.62% | **+0.56%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.43% | **+0.50%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_BB3S | 3/20 | 15.0% | +2.06% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.37% | **+1.16%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.84% | **+0.80%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.27% | **-0.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.47% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5455件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$210.51** / 初期 $100.00 (+110.51%)
- 確定: 2841件 (Win 782 / Loss 659 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1304 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $210.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2774件 (Win 820 / Loss 1067 / Flat 887) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000447 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIVER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-12T21:16:12.043710+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=77128.3
- Funnel: target 1068 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +24.25% | $23,532,188.07 |
| LONGXIA/USDT:USDT | +17.59% | $9,499,822.48 |
| REZ/USDT:USDT | +13.29% | $1,586,837.81 |
| ILV/USDT:USDT | +10.65% | $1,086,747.70 |
| RIVER/USDT:USDT | +9.92% | $14,599,408.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALCH/USDT:USDT | below_1h_threshold | +2.46% | +2.46% |
| GRIFFAIN/USDT:USDT | below_1h_threshold | +2.24% | +2.25% |
| STORJ/USDT:USDT | below_1h_threshold | +1.31% | +1.31% |
| UAI/USDT:USDT | below_1h_threshold | +1.08% | +1.08% |
| BTW/USDT:USDT | below_1h_threshold | +0.81% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
