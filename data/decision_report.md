# Decision Report

- generated_at: 2026-09-22T04:46:29.652668+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15295**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=15295, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.84% | **+1.66%** |
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.28% | **+0.89%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.43% | **+0.29%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.53% | **+0.24%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.23% | **+0.10%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.01% | **-0.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.02% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,177.42** / 初期 $100.00 (+1077.42%)
- 確定: 5786件 (Win 1721 / Loss 1862 / Flat 2203) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,177.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.71** / 初期 $100.00 (+148.71%)
- 確定: 3334件 (Win 921 / Loss 773 / Flat 1640) / skip 5372件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $248.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.76** / 初期 $100.00 (+22.76%)
- 確定: 3067件 (Win 902 / Loss 1200 / Flat 965) / pending 4件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000186 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MUBARAK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.76

## 6. Latest Market Context

- 更新: 2026-09-22T04:46:13.788126+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=85460.9
- Funnel: target 1057 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +36.35% | $3,105,877.96 |
| MUBARAK/USDT:USDT | +19.03% | $1,690,562.72 |
| ALCH/USDT:USDT | +18.74% | $2,489,420.49 |
| GRASS/USDT:USDT | +15.94% | $2,574,892.30 |
| FORM/USDT:USDT | +12.84% | $9,665,866.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000BONK/USDT:USDT | below_1h_threshold | +3.38% | +3.62% |
| SAGA/USDT:USDT | below_1h_threshold | +2.67% | +2.91% |
| H/USDT:USDT | below_1h_threshold | +2.47% | +2.70% |
| GRASS/USDT:USDT | below_1h_threshold | +1.92% | +2.16% |
| BEAT/USDT:USDT | below_1h_threshold | +1.69% | +1.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
