# Decision Report

- generated_at: 2026-09-15T05:56:26.983009+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14566**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14566, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.09% | **+0.77%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.64% | **+0.35%** |
| LIMIT_BB3S | 4/19 | 21.1% | +1.65% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.58% | **+0.87%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.45% | **+0.86%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.11% | **+0.56%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 213件 (TP 79 / SL 129 / EXP 5)
- 最新: STORJ/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,083.58** / 初期 $100.00 (+983.58%)
- 確定: 5468件 (Win 1641 / Loss 1772 / Flat 2055) / skip 5659件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,083.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.53** / 初期 $100.00 (+129.53%)
- 確定: 3007件 (Win 833 / Loss 717 / Flat 1457) / skip 4970件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0602 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $229.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.20** / 初期 $100.00 (+24.20%)
- 確定: 2907件 (Win 862 / Loss 1132 / Flat 913) / pending 2件 / skip 3133件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000205 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.20

## 6. Latest Market Context

- 更新: 2026-09-15T05:56:14.184452+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77556.5
- Funnel: target 1073 → liquid 161 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.1 >= 65=1, 4h RSI 91.8 >= 65=1, 4h RSI 66.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +61.36% | $1,541,386.57 |
| POWER/USDT:USDT | +59.39% | $9,162,570.87 |
| AIN/USDT:USDT | +48.67% | $8,963,519.64 |
| FF/USDT:USDT | +29.30% | $1,033,879.84 |
| ASTR/USDT:USDT | +17.44% | $1,059,041.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNI/USDT:USDT | below_1h_threshold | +1.80% | +1.77% |
| CYS/USDT:USDT | below_1h_threshold | +1.63% | +1.61% |
| EGLD/USDT:USDT | below_1h_threshold | +1.57% | +1.55% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.35% | +1.33% |
| RAY/USDT:USDT | below_1h_threshold | +1.31% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
