# Decision Report

- generated_at: 2026-09-15T04:01:24.757382+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14558**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.64% / filled 20/20。**
- 全期間 MARKET基準: n=14558, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +4.33% | **+1.30%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| MARKET | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_BB3S | 5/17 | 29.4% | +1.81% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,087.84** / 初期 $100.00 (+987.84%)
- 確定: 5460件 (Win 1641 / Loss 1770 / Flat 2049) / skip 5659件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CVC/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,087.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.67** / 初期 $100.00 (+129.67%)
- 確定: 3000件 (Win 832 / Loss 716 / Flat 1452) / skip 4969件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0531 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CVC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $229.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.63** / 初期 $100.00 (+24.63%)
- 確定: 2903件 (Win 862 / Loss 1130 / Flat 911) / pending 6件 / skip 3124件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SHROOM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.63

## 6. Latest Market Context

- 更新: 2026-09-15T04:01:12.549070+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77680.6
- Funnel: target 1073 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +64.77% | $1,375,352.23 |
| POWER/USDT:USDT | +53.32% | $6,905,562.76 |
| AIN/USDT:USDT | +23.74% | $7,941,025.70 |
| CNPY/USDT:USDT | +15.21% | $1,838,175.12 |
| CYS/USDT:USDT | +13.04% | $1,582,787.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +0.92% | +0.89% |
| POWER/USDT:USDT | below_1h_threshold | +0.88% | +0.85% |
| CATE/USDT:USDT | below_1h_threshold | +0.83% | +0.80% |
| PONS/USDT:USDT | below_1h_threshold | +0.47% | +0.44% |
| CNPY/USDT:USDT | below_1h_threshold | +0.43% | +0.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
