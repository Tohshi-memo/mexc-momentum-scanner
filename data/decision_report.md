# Decision Report

- generated_at: 2026-09-23T00:46:21.700447+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15376**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.22% / filled 20/20。**
- 全期間 MARKET基準: n=15376, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.22% | **+1.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.17% | **+1.85%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.06% | **+1.34%** |
| MARKET | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_BB3S | 7/13 | 53.8% | +2.02% | **+1.09%** |
| LIMIT_3PCT | 10/20 | 50.0% | +2.08% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.91% | **+1.31%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.96% | **+0.86%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.31% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.21** / 初期 $100.00 (+1073.21%)
- 確定: 5854件 (Win 1731 / Loss 1880 / Flat 2243) / skip 6083件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,173.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5434件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.78** / 初期 $100.00 (+22.78%)
- 確定: 3122件 (Win 919 / Loss 1224 / Flat 979) / pending 5件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000068 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FOLKS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $122.78

## 6. Latest Market Context

- 更新: 2026-09-23T00:46:10.523967+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=86432.0
- Funnel: target 1058 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FOLKS/USDT:USDT | +29.20% | $4,678,076.26 |
| DRIFT/USDT:USDT | +21.64% | $1,731,193.66 |
| ALLO/USDT:USDT | +17.38% | $2,112,969.69 |
| ZAMA/USDT:USDT | +16.35% | $2,280,022.45 |
| TIA/USDT:USDT | +14.68% | $29,683,127.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +3.25% | +2.93% |
| EVAA/USDT:USDT | below_1h_threshold | +2.86% | +2.54% |
| INJ/USDT:USDT | below_1h_threshold | +2.24% | +1.92% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.88% | +1.57% |
| ARB/USDT:USDT | below_1h_threshold | +1.78% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
