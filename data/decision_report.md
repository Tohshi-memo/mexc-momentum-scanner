# Decision Report

- generated_at: 2026-07-17T07:36:23.202733+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8829**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=8829, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.64% | **+1.05%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.31% | **+0.99%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.62% | **+0.53%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.93% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.59% | **+0.78%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.79% | **+0.42%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.82% | **+0.12%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$110.71** / 初期 $100.00 (+10.71%)
- 確定トレード: 110件 (TP 41 / SL 65 / EXP 4)
- 最新: AERO/USDT:USDT SL_HIT PnL -3.73% 残高後 $110.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.01** / 初期 $100.00 (+242.01%)
- 確定: 2944件 (Win 916 / Loss 947 / Flat 1081) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AERO/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $342.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.87** / 初期 $100.00 (+7.87%)
- 確定: 791件 (Win 183 / Loss 171 / Flat 437) / skip 1449件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0214 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AERO/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $107.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.65** / 初期 $100.00 (-1.35%)
- 確定: 96件 (Win 30 / Loss 62 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AERO/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.65

## 6. Latest Market Context

- 更新: 2026-07-17T07:36:14.349155+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=62864.8
- Funnel: target 885 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +29.21% | $1,958,653.12 |
| TAC/USDT:USDT | +18.16% | $3,349,748.03 |
| KAITO/USDT:USDT | +13.68% | $3,930,603.70 |
| SOXS/USDT:USDT | +12.48% | $1,597,894.39 |
| T/USDT:USDT | +11.25% | $1,991,851.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.58% | +3.65% |
| LUMIA/USDT:USDT | below_1h_threshold | +3.27% | +3.35% |
| APDSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.88% |
| ENS/USDT:USDT | below_1h_threshold | +2.71% | +2.79% |
| CAP/USDT:USDT | below_1h_threshold | +2.05% | +2.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
