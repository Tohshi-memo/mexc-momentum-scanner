# Decision Report

- generated_at: 2026-08-10T07:16:16.584002+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11132**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=11132, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.25% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.64% | **+0.54%** |
| LIMIT_BB3S | 3/19 | 15.8% | +3.08% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.26% | **+0.90%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.39% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.97** / 初期 $100.00 (+524.97%)
- 確定: 3933件 (Win 1230 / Loss 1282 / Flat 1421) / skip 3760件
- 成長率目線: 平均log +0.000466 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $624.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3030件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.50** / 初期 $100.00 (+17.50%)
- 確定: 1285件 (Win 398 / Loss 494 / Flat 393) / pending 2件 / skip 1315件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000387 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.50

## 6. Latest Market Context

- 更新: 2026-08-10T07:16:08.617882+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=65225.9
- Funnel: target 958 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +47.10% | $20,980,751.32 |
| CAP/USDT:USDT | +28.10% | $4,440,617.10 |
| GRVT/USDT:USDT | +25.31% | $1,649,826.71 |
| CASHCAT/USDT:USDT | +22.34% | $1,409,232.53 |
| TUT/USDT:USDT | +13.53% | $78,105,390.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +2.88% | +2.95% |
| COOKIE/USDT:USDT | below_1h_threshold | +1.60% | +1.67% |
| RE/USDT:USDT | below_1h_threshold | +0.71% | +0.78% |
| NGAS/USDT:USDT | below_1h_threshold | +0.69% | +0.76% |
| ARB/USDT:USDT | below_1h_threshold | +0.68% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
