# Decision Report

- generated_at: 2026-07-17T23:51:11.854687+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8896**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=8896, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.04% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.76% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.80% | **+0.44%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.68% | **+0.31%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.09% | **+0.07%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$364.79** / 初期 $100.00 (+264.79%)
- 確定: 3011件 (Win 936 / Loss 957 / Flat 1118) / skip 2446件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $364.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$112.09** / 初期 $100.00 (+12.09%)
- 確定: 858件 (Win 203 / Loss 174 / Flat 481) / skip 1449件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $112.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.50** / 初期 $100.00 (-0.50%)
- 確定: 155件 (Win 49 / Loss 83 / Flat 23) / pending 5件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.50

## 6. Latest Market Context

- 更新: 2026-07-17T23:51:06.169056+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63922.9
- Funnel: target 885 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +43.60% | $9,906,588.99 |
| CASHCAT/USDT:USDT | +25.06% | $1,231,744.33 |
| AKE/USDT:USDT | +14.69% | $49,348,486.46 |
| XEC/USDT:USDT | +7.80% | $3,396,414.51 |
| CRO/USDT:USDT | +7.32% | $2,258,400.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +2.42% | +2.47% |
| UNI/USDT:USDT | below_1h_threshold | +1.71% | +1.76% |
| PI/USDT:USDT | below_1h_threshold | +1.28% | +1.33% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.16% | +1.21% |
| TAG/USDT:USDT | below_1h_threshold | +1.10% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
