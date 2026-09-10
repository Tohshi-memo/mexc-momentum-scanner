# Decision Report

- generated_at: 2026-09-10T17:26:24.989755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14172**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=14172, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/17 | 17.6% | +6.33% | **+1.12%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.47% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.66% | **+4.66%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.22% | **+0.19%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 207件 (TP 78 / SL 124 / EXP 5)
- 最新: HEMI/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,071.40** / 初期 $100.00 (+971.40%)
- 確定: 5352件 (Win 1610 / Loss 1728 / Flat 2014) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,071.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.86** / 初期 $100.00 (+107.86%)
- 確定: 2766件 (Win 764 / Loss 649 / Flat 1353) / skip 4817件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1121 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $207.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.58** / 初期 $100.00 (+22.58%)
- 確定: 2677件 (Win 790 / Loss 1022 / Flat 865) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000421 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $122.58

## 6. Latest Market Context

- 更新: 2026-09-10T17:26:14.572865+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=77221.1
- Funnel: target 1067 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +10.27% | $2,668,044.16 |
| NIULAI/USDT:USDT | +6.70% | $1,365,756.26 |
| BTW/USDT:USDT | +6.63% | $1,600,663.97 |
| 4STOCK/USDT:USDT | +6.37% | $2,427,500.48 |
| NES/USDT:USDT | +5.77% | $1,811,439.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4STOCK/USDT:USDT | below_1h_threshold | +4.76% | +4.70% |
| VVV/USDT:USDT | below_1h_threshold | +4.39% | +4.33% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.33% | +3.27% |
| SOPH/USDT:USDT | below_1h_threshold | +2.90% | +2.84% |
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +2.52% | +2.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
