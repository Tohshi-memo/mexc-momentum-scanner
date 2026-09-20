# Decision Report

- generated_at: 2026-09-20T16:41:43.041638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15193**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=15193, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +2.11% | **+1.90%** |
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_BB3S | 6/15 | 40.0% | +2.43% | **+0.97%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.89% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +6.37% | **+1.27%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.46% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.63** / 初期 $100.00 (+1073.63%)
- 確定: 5717件 (Win 1705 / Loss 1845 / Flat 2167) / skip 6037件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OFC/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,173.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.68** / 初期 $100.00 (+147.68%)
- 確定: 3290件 (Win 911 / Loss 764 / Flat 1615) / skip 5314件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $247.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.84** / 初期 $100.00 (+21.84%)
- 確定: 2983件 (Win 882 / Loss 1179 / Flat 922) / pending 6件 / skip 3680件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000145 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LUNC/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $121.84

## 6. Latest Market Context

- 更新: 2026-09-20T16:41:28.038609+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=81290.3
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 8 → strict 0
- Surge前reject: below_1h_threshold=42, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 81.9 >= 65=1, 4h RSI 75.8 >= 65=1, 4h RSI 76.6 >= 65=1, 4h RSI 77.8 >= 65=1, 4h RSI 72.0 >= 65=1, 4h RSI 70.3 >= 65=1, 4h RSI 75.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUNANEW/USDT:USDT | +28.76% | $1,090,420.89 |
| RENDER/USDT:USDT | +8.90% | $3,539,545.13 |
| NEAR/USDT:USDT | +8.79% | $102,044,414.65 |
| AR/USDT:USDT | +7.83% | $6,995,767.48 |
| ENA/USDT:USDT | +7.15% | $70,091,362.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICP/USDT:USDT | below_1h_threshold | +4.83% | +4.32% |
| RAY/USDT:USDT | below_1h_threshold | +4.33% | +3.81% |
| APT/USDT:USDT | below_1h_threshold | +3.68% | +3.16% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.51% | +2.99% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.43% | +2.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
