# Decision Report

- generated_at: 2026-08-01T10:41:13.290127+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10084**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=10084, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +2.24% | **+2.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.50% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.42% | **+0.78%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.96% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.85% | **+0.43%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.16% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$573.69** / 初期 $100.00 (+473.69%)
- 確定: 3629件 (Win 1158 / Loss 1190 / Flat 1281) / skip 3016件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $573.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2216件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.11** / 初期 $100.00 (+11.11%)
- 確定: 895件 (Win 285 / Loss 353 / Flat 257) / pending 4件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000076 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $111.11

## 6. Latest Market Context

- 更新: 2026-08-01T10:41:04.724692+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63000.3
- Funnel: target 921 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +42.03% | $6,749,144.16 |
| JIMOTHY/USDT:USDT | +36.11% | $1,414,148.91 |
| TAKE/USDT:USDT | +31.74% | $1,082,299.25 |
| KOMA/USDT:USDT | +29.81% | $17,216,295.78 |
| ICNT/USDT:USDT | +20.92% | $1,061,080.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.73% | +4.77% |
| SATS/USDT:USDT | below_1h_threshold | +4.57% | +4.61% |
| EVAA/USDT:USDT | below_1h_threshold | +2.57% | +2.61% |
| BTW/USDT:USDT | below_1h_threshold | +2.51% | +2.54% |
| TAKE/USDT:USDT | below_1h_threshold | +2.11% | +2.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
