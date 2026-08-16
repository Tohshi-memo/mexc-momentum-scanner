# Decision Report

- generated_at: 2026-08-16T23:46:22.522699+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11778**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=11778, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_BB3S | 3/16 | 18.8% | +4.55% | **+0.85%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.22% | **-0.19%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.49% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 185件 (TP 71 / SL 109 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4156件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.46** / 初期 $100.00 (+54.46%)
- 確定: 1787件 (Win 496 / Loss 418 / Flat 873) / skip 3402件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $154.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.37** / 初期 $100.00 (+18.37%)
- 確定: 1672件 (Win 503 / Loss 635 / Flat 534) / pending 0件 / skip 1578件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $118.37

## 6. Latest Market Context

- 更新: 2026-08-16T23:46:11.839279+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62866.0
- Funnel: target 986 → liquid 144 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +32.05% | $13,197,136.15 |
| HFT/USDT:USDT | +21.13% | $2,544,062.73 |
| BTW/USDT:USDT | +17.73% | $26,242,112.87 |
| APR/USDT:USDT | +12.35% | $6,098,655.20 |
| CYS/USDT:USDT | +10.06% | $36,841,659.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.60% | +3.63% |
| H/USDT:USDT | below_1h_threshold | +3.51% | +3.54% |
| APR/USDT:USDT | below_1h_threshold | +2.77% | +2.81% |
| CYS/USDT:USDT | below_1h_threshold | +1.87% | +1.90% |
| US/USDT:USDT | below_1h_threshold | +1.85% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
