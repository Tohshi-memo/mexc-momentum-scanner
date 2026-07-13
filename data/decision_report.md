# Decision Report

- generated_at: 2026-07-13T13:31:07.927485+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8634**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=8634, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.73% | **+1.56%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.95% | **+0.71%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.67% | **+0.53%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.30% | **-0.23%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.69** / 初期 $100.00 (+0.69%)
- 確定トレード: 92件 (TP 30 / SL 60 / EXP 2)
- 最新: TRIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$322.16** / 初期 $100.00 (+222.16%)
- 確定: 2802件 (Win 878 / Loss 923 / Flat 1001) / skip 2393件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $322.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1400件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.14** / 初期 $100.00 (-0.86%)
- 確定: 38件 (Win 13 / Loss 25 / Flat 0) / pending 1件 / skip 63件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000499 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.14

## 6. Latest Market Context

- 更新: 2026-07-13T13:31:01.752065+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62534.9
- Funnel: target 867 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +36.25% | $11,676,261.46 |
| JCT/USDT:USDT | +29.33% | $1,966,100.69 |
| XEC/USDT:USDT | +26.67% | $5,587,353.50 |
| KITE/USDT:USDT | +17.38% | $4,316,145.40 |
| CAP/USDT:USDT | +10.63% | $1,673,800.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +4.12% | +4.22% |
| BILL/USDT:USDT | below_1h_threshold | +0.80% | +0.90% |
| COPSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.75% |
| AVAX/USDT:USDT | below_1h_threshold | +0.62% | +0.72% |
| COPPER/USDT:USDT | below_1h_threshold | +0.59% | +0.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
