# Decision Report

- generated_at: 2026-07-13T04:21:10.752110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8621**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.57% / filled 20/20。**
- 全期間 MARKET基準: n=8621, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.57% | **+1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.30% | **+1.17%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.30% | **+1.04%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.24% | **+0.44%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.53% | **+0.45%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.43% | **+0.35%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.25% | **+0.25%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.10% | **+0.08%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.04% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$101.20** / 初期 $100.00 (+1.20%)
- 確定トレード: 91件 (TP 30 / SL 59 / EXP 2)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.39** / 初期 $100.00 (+221.39%)
- 確定: 2793件 (Win 876 / Loss 923 / Flat 994) / skip 2389件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $321.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1387件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 3件 / skip 62件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000475 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-13T04:21:04.557675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=62861.6
- Funnel: target 863 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +35.88% | $5,509,514.59 |
| BLAST/USDT:USDT | +15.84% | $2,340,657.08 |
| ANSEM/USDT:USDT | +9.89% | $4,723,878.37 |
| BILL/USDT:USDT | +5.32% | $11,727,357.44 |
| SYN/USDT:USDT | +5.04% | $2,748,061.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.76% | +4.63% |
| US/USDT:USDT | below_1h_threshold | +3.84% | +3.71% |
| CAP/USDT:USDT | below_1h_threshold | +2.82% | +2.69% |
| EDGE/USDT:USDT | below_1h_threshold | +2.65% | +2.52% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.43% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
