# Decision Report

- generated_at: 2026-09-10T18:02:01.871022+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14176**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14176, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.84% | **+0.96%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_BB3S | 2/14 | 14.3% | +5.50% | **+0.79%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.42% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +4.76% | **+4.76%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.11% | **+1.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.87%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.08% | **+0.48%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,074.20** / 初期 $100.00 (+974.20%)
- 確定: 5356件 (Win 1611 / Loss 1729 / Flat 2016) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,074.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.50** / 初期 $100.00 (+108.50%)
- 確定: 2770件 (Win 766 / Loss 649 / Flat 1355) / skip 4817件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1095 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $208.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.69** / 初期 $100.00 (+22.69%)
- 確定: 2681件 (Win 791 / Loss 1023 / Flat 867) / pending 5件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000475 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.69

## 6. Latest Market Context

- 更新: 2026-09-10T18:01:49.942123+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=77299.7
- Funnel: target 1067 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +24.13% | $1,144,921.49 |
| NIULAI/USDT:USDT | +14.38% | $1,457,053.18 |
| PONS/USDT:USDT | +10.88% | $8,816,810.11 |
| 4STOCK/USDT:USDT | +9.86% | $2,449,611.20 |
| EIGEN/USDT:USDT | +8.52% | $1,429,642.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +2.08% | +2.08% |
| CATE/USDT:USDT | below_1h_threshold | +1.41% | +1.41% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +0.92% |
| NGAS/USDT:USDT | below_1h_threshold | +0.52% | +0.52% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +0.52% | +0.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
