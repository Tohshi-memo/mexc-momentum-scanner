# Decision Report

- generated_at: 2026-07-30T00:26:33.624774+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9845**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.79% / filled 20/20。**
- 全期間 MARKET基準: n=9845, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.79% | **+3.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.79% | **+3.79%** |
| LIMIT_1PCT | 15/20 | 75.0% | +2.75% | **+2.06%** |
| LIMIT_2PCT | 11/20 | 55.0% | +1.58% | **+0.87%** |
| LIMIT_ATR | 6/20 | 30.0% | +1.60% | **+0.48%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.98% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -1.19% | **-0.78%** |
| LIMIT_FIB1618_LONG | 9/20 | 45.0% | -2.44% | **-1.10%** |

## 2. $100 Live Portfolio

- 残高: **$121.66** / 初期 $100.00 (+21.66%)
- 確定トレード: 167件 (TP 66 / SL 96 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.66
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2887件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.91** / 初期 $100.00 (+36.91%)
- 確定: 1242件 (Win 344 / Loss 283 / Flat 615) / skip 2014件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 554件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000360 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-30T00:26:25.233702+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63964.5
- Funnel: target 911 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1, 4h RSI 79.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +15.31% | $13,254,079.93 |
| MSFU/USDT:USDT | +14.68% | $4,767,639.91 |
| ADVANTESTSTOCK/USDT:USDT | +13.76% | $1,457,218.10 |
| RE/USDT:USDT | +13.21% | $7,665,322.49 |
| LAB/USDT:USDT | +10.03% | $2,618,545.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +2.65% | +2.64% |
| ACH/USDT:USDT | below_1h_threshold | +2.55% | +2.54% |
| MSFU/USDT:USDT | below_1h_threshold | +2.19% | +2.18% |
| ADVANTESTSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.62% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
