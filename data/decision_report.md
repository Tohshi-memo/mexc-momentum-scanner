# Decision Report

- generated_at: 2026-07-17T22:56:21.126602+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8890**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=8890, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.04% | **+0.80%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.97% | **+0.45%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.70% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.04% | **-0.03%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.42% | **-0.27%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.67% | **-0.44%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$362.05** / 初期 $100.00 (+262.05%)
- 確定: 3005件 (Win 934 / Loss 955 / Flat 1116) / skip 2446件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $362.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.15** / 初期 $100.00 (+11.15%)
- 確定: 852件 (Win 201 / Loss 174 / Flat 477) / skip 1449件
- 成長率目線: 平均log +0.000124 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0615 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $111.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.25** / 初期 $100.00 (-0.75%)
- 確定: 149件 (Win 47 / Loss 81 / Flat 21) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.25

## 6. Latest Market Context

- 更新: 2026-07-17T22:56:13.302923+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=63955.2
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +18.14% | $1,174,779.29 |
| ESPORTS/USDT:USDT | +17.70% | $9,305,711.37 |
| AKE/USDT:USDT | +14.51% | $48,630,850.63 |
| XEC/USDT:USDT | +6.92% | $3,324,861.40 |
| VVV/USDT:USDT | +6.70% | $2,595,236.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.05% | +3.23% |
| SLX/USDT:USDT | below_1h_threshold | +1.68% | +1.86% |
| UB/USDT:USDT | below_1h_threshold | +1.35% | +1.53% |
| GALA/USDT:USDT | below_1h_threshold | +1.15% | +1.33% |
| CRO/USDT:USDT | below_1h_threshold | +1.13% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
