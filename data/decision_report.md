# Decision Report

- generated_at: 2026-07-17T07:46:19.423887+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8830**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.89% / filled 20/20。**
- 全期間 MARKET基準: n=8830, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.89% | **+1.89%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.64% | **+1.05%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.31% | **+0.99%** |
| LIMIT_4PCT | 9/20 | 45.0% | +1.03% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.59% | **+0.78%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.79% | **+0.42%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.82% | **+0.12%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | -0.25% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$110.71** / 初期 $100.00 (+10.71%)
- 確定トレード: 110件 (TP 41 / SL 65 / EXP 4)
- 最新: AERO/USDT:USDT SL_HIT PnL -3.73% 残高後 $110.71
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.01** / 初期 $100.00 (+242.01%)
- 確定: 2945件 (Win 916 / Loss 947 / Flat 1082) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $342.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.87** / 初期 $100.00 (+7.87%)
- 確定: 792件 (Win 183 / Loss 171 / Flat 438) / skip 1449件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0214 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: T/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.99** / 初期 $100.00 (-1.01%)
- 確定: 97件 (Win 31 / Loss 62 / Flat 4) / pending 3件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: T/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $98.99

## 6. Latest Market Context

- 更新: 2026-07-17T07:46:11.937531+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=62889.3
- Funnel: target 885 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +28.96% | $2,008,040.15 |
| TAC/USDT:USDT | +16.47% | $3,375,698.83 |
| SOXS/USDT:USDT | +13.59% | $1,618,814.40 |
| KAITO/USDT:USDT | +13.38% | $3,988,613.12 |
| T/USDT:USDT | +9.97% | $2,050,631.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.03% | +4.07% |
| ENS/USDT:USDT | below_1h_threshold | +3.06% | +3.10% |
| LUMIA/USDT:USDT | below_1h_threshold | +3.05% | +3.09% |
| APDSTOCK/USDT:USDT | below_1h_threshold | +2.80% | +2.84% |
| LRC/USDT:USDT | below_1h_threshold | +2.21% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
