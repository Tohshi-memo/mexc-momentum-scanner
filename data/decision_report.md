# Decision Report

- generated_at: 2026-09-23T10:01:19.761873+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15425**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=15425, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +3.06% | **+2.14%** |
| LIMIT_3PCT | 14/20 | 70.0% | +3.05% | **+2.14%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.25% | **+1.69%** |
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_5PCT | 6/20 | 30.0% | +4.83% | **+1.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.50% | **+0.42%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.51% | **+0.31%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.38% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6091件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.37** / 初期 $100.00 (+147.37%)
- 確定: 3373件 (Win 930 / Loss 789 / Flat 1654) / skip 5463件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0250 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $247.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3762件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000160 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T10:01:08.571627+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=85831.7
- Funnel: target 1061 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +200.40% | $4,519,303.46 |
| SHROOM/USDT:USDT | +64.88% | $1,353,905.71 |
| MET/USDT:USDT | +31.03% | $1,242,921.73 |
| ALLO/USDT:USDT | +27.41% | $3,459,187.95 |
| SUPER/USDT:USDT | +23.09% | $1,093,671.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +1.13% | +1.12% |
| CHR/USDT:USDT | below_1h_threshold | +0.82% | +0.81% |
| AR/USDT:USDT | below_1h_threshold | +0.54% | +0.53% |
| MYX/USDT:USDT | below_1h_threshold | +0.51% | +0.50% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.51% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
