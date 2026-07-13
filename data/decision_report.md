# Decision Report

- generated_at: 2026-07-13T16:26:21.175480+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8640**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=8640, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.59% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +0.79% | **+0.59%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.55% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.70** / 初期 $100.00 (+1.70%)
- 確定トレード: 93件 (TP 31 / SL 60 / EXP 2)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.70
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$326.15** / 初期 $100.00 (+226.15%)
- 確定: 2808件 (Win 881 / Loss 923 / Flat 1004) / skip 2393件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIOT/USDT:USDT `LIMIT_5PCT` TP_HIT account +1.00% 残高後 $326.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1406件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.48** / 初期 $100.00 (-0.52%)
- 確定: 39件 (Win 14 / Loss 25 / Flat 0) / pending 0件 / skip 72件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000448 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.48

## 6. Latest Market Context

- 更新: 2026-07-13T16:26:10.968081+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=62307.5
- Funnel: target 867 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +7.82% | $1,652,080.05 |
| ANSEM/USDT:USDT | +4.97% | $4,360,687.81 |
| EVAA/USDT:USDT | +2.78% | $19,936,965.95 |
| SLX/USDT:USDT | +2.28% | $1,820,149.80 |
| MAGMA/USDT:USDT | +1.91% | $5,417,114.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +2.91% | +3.37% |
| SLX/USDT:USDT | below_1h_threshold | +2.28% | +2.75% |
| BILL/USDT:USDT | below_1h_threshold | +1.83% | +2.29% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.83% | +2.29% |
| VELVET/USDT:USDT | below_1h_threshold | +1.75% | +2.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
