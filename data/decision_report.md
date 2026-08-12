# Decision Report

- generated_at: 2026-08-12T01:36:32.829241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11316**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=11316, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.29% | **+1.16%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.95% | **+0.90%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.57% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.68% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.09% | **+0.63%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.69% | **+0.59%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.64% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3939件 (Win 1230 / Loss 1285 / Flat 1424) / skip 3938件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.44** / 初期 $100.00 (+43.44%)
- 確定: 1567件 (Win 437 / Loss 364 / Flat 766) / skip 3160件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.83** / 初期 $100.00 (+14.83%)
- 確定: 1336件 (Win 408 / Loss 526 / Flat 402) / pending 4件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000117 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $114.83

## 6. Latest Market Context

- 更新: 2026-08-12T01:36:18.249950+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63701.2
- Funnel: target 967 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOLO/USDT:USDT | +30.91% | $4,876,866.25 |
| JIMOTHY/USDT:USDT | +25.97% | $1,798,568.64 |
| PROM/USDT:USDT | +22.32% | $6,674,352.52 |
| CRWVSTOCK/USDT:USDT | +16.84% | $3,790,610.51 |
| LSK/USDT:USDT | +13.80% | $3,238,045.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQD/USDT:USDT | below_1h_threshold | +2.24% | +2.26% |
| NEAR/USDT:USDT | below_1h_threshold | +1.72% | +1.75% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.71% | +1.74% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +1.57% | +1.59% |
| HOLO/USDT:USDT | below_1h_threshold | +1.56% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
