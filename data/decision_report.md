# Decision Report

- generated_at: 2026-09-28T09:06:16.571923+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15704**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.01% / filled 20/20。**
- 全期間 MARKET基準: n=15704, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.01% | **+2.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.63% | **+1.38%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.90% | **+0.50%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_BB3S | 3/15 | 20.0% | +2.05% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.44% | **+0.52%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.90% | **+0.41%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.20% | **+0.05%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.38% | **-0.17%** |
| MARKET_LONG | 20/20 | 100.0% | -0.34% | **-0.34%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6283件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5581件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.87** / 初期 $100.00 (+18.87%)
- 確定: 3273件 (Win 952 / Loss 1287 / Flat 1034) / pending 3件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000118 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HBAR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.87

## 6. Latest Market Context

- 更新: 2026-09-28T09:06:07.602445+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=82713.3
- Funnel: target 1059 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +26.36% | $294,278,888.09 |
| BTW/USDT:USDT | +18.07% | $11,338,608.24 |
| MARSCOIN/USDT:USDT | +17.62% | $2,360,732.44 |
| HBAR/USDT:USDT | +17.00% | $26,374,817.81 |
| BATON/USDT:USDT | +16.10% | $1,468,031.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +2.86% | +3.12% |
| BTW/USDT:USDT | below_1h_threshold | +1.63% | +1.90% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.62% | +1.89% |
| HBAR/USDT:USDT | below_1h_threshold | +1.42% | +1.68% |
| USOIL/USDT:USDT | below_1h_threshold | +1.31% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
