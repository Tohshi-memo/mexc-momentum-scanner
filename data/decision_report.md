# Decision Report

- generated_at: 2026-08-15T19:06:26.505374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11694**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11694, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.26% | **-1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.46% | **+0.39%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.56% | **+0.39%** |
| LIMIT_BB3S | 7/19 | 36.8% | +0.63% | **+0.23%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.20% | **+0.17%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.01% | **+0.91%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.17% | **+0.82%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.42% | **+0.78%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.68% | **+0.76%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.79% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.15** / 初期 $100.00 (+543.15%)
- 確定: 4162件 (Win 1291 / Loss 1355 / Flat 1516) / skip 4093件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $643.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.38** / 初期 $100.00 (+55.38%)
- 確定: 1757件 (Win 493 / Loss 413 / Flat 851) / skip 3348件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.49** / 初期 $100.00 (+19.49%)
- 確定: 1624件 (Win 495 / Loss 617 / Flat 512) / pending 2件 / skip 1543件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AEON1/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $119.49

## 6. Latest Market Context

- 更新: 2026-08-15T19:06:16.455331+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63033.6
- Funnel: target 985 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +10.27% | $2,793,683.46 |
| BTW/USDT:USDT | +10.09% | $11,026,942.16 |
| AIO/USDT:USDT | +9.38% | $2,362,641.67 |
| AKE/USDT:USDT | +7.90% | $33,479,800.32 |
| ROBO/USDT:USDT | +6.65% | $8,789,258.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIO/USDT:USDT | below_1h_threshold | +1.93% | +1.92% |
| H/USDT:USDT | below_1h_threshold | +1.43% | +1.42% |
| AKE/USDT:USDT | below_1h_threshold | +1.21% | +1.20% |
| BTW/USDT:USDT | below_1h_threshold | +1.19% | +1.18% |
| DOS/USDT:USDT | below_1h_threshold | +0.51% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
