# Decision Report

- generated_at: 2026-08-28T20:31:21.243015+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12887**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=12887, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/17 | 47.1% | +3.04% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.06% | **+0.85%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.81% | **+0.73%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.52% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.11% | **+1.05%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +0.89% | **+0.85%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.86% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 193件 (TP 73 / SL 115 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$708.89** / 初期 $100.00 (+608.89%)
- 確定: 4677件 (Win 1414 / Loss 1534 / Flat 1729) / skip 4771件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $708.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2003件 (Win 544 / Loss 483 / Flat 976) / skip 4295件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.98** / 初期 $100.00 (+14.98%)
- 確定: 1990件 (Win 581 / Loss 763 / Flat 646) / pending 0件 / skip 2371件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $114.98

## 6. Latest Market Context

- 更新: 2026-08-28T20:31:10.217394+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77438.7
- Funnel: target 1023 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +18.45% | $13,514,805.88 |
| TURBO/USDT:USDT | +11.20% | $1,484,268.93 |
| MAGMA/USDT:USDT | +9.95% | $7,669,689.50 |
| BTW/USDT:USDT | +6.29% | $2,052,749.83 |
| DEXE/USDT:USDT | +4.55% | $4,432,811.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +1.59% | +1.71% |
| TURBO/USDT:USDT | below_1h_threshold | +1.55% | +1.68% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.54% | +1.66% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.28% | +1.41% |
| DEXE/USDT:USDT | below_1h_threshold | +1.01% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
