# Decision Report

- generated_at: 2026-09-23T02:56:43.356757+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15385**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=15385, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.48% | **+0.41%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.34% | **+0.24%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.05% | **+0.73%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.84% | **+0.71%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.33% | **+0.30%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.33% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.35** / 初期 $100.00 (+1067.35%)
- 確定: 5862件 (Win 1731 / Loss 1881 / Flat 2250) / skip 6084件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4STOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,167.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5443件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.35** / 初期 $100.00 (+22.35%)
- 確定: 3124件 (Win 919 / Loss 1226 / Flat 979) / pending 5件 / skip 3734件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.35

## 6. Latest Market Context

- 更新: 2026-09-23T02:56:25.363052+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=86420.0
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.6 >= 65=1, 4h RSI 71.4 >= 65=1, 4h RSI 87.0 >= 65=1, 4h RSI 75.4 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +78.83% | $1,111,600.11 |
| FOLKS/USDT:USDT | +19.52% | $6,279,421.29 |
| PONS/USDT:USDT | +18.02% | $5,756,193.07 |
| MARSCOIN/USDT:USDT | +17.66% | $3,609,178.14 |
| ALLO/USDT:USDT | +17.19% | $2,491,101.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OP/USDT:USDT | below_1h_threshold | +2.77% | +2.65% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.48% | +2.37% |
| FORM/USDT:USDT | below_1h_threshold | +2.18% | +2.07% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.16% | +2.05% |
| ARB/USDT:USDT | below_1h_threshold | +2.06% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
