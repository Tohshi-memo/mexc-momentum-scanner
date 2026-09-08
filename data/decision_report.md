# Decision Report

- generated_at: 2026-09-08T09:21:23.876317+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13972**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.49% / filled 20/20。**
- 全期間 MARKET基準: n=13972, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.58% | **+0.20%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.11% | **+0.10%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.95% | **+0.61%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.63% | **+0.48%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.69% | **+0.41%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,015.07** / 初期 $100.00 (+915.07%)
- 確定: 5243件 (Win 1582 / Loss 1703 / Flat 1958) / skip 5290件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOFTBANKSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.01% 残高後 $1,015.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.62** / 初期 $100.00 (+89.62%)
- 確定: 2576件 (Win 719 / Loss 619 / Flat 1238) / skip 4807件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0931 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $189.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.53** / 初期 $100.00 (+22.53%)
- 確定: 2561件 (Win 753 / Loss 960 / Flat 848) / pending 4件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000271 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BNCSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.53

## 6. Latest Market Context

- 更新: 2026-09-08T09:21:11.504396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78387.6
- Funnel: target 1065 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +119.25% | $12,476,225.31 |
| BNCSTOCK/USDT:USDT | +54.39% | $1,441,146.62 |
| FORM/USDT:USDT | +41.42% | $3,328,409.02 |
| AKE/USDT:USDT | +15.95% | $12,455,893.92 |
| MEMEROBINHOOD/USDT:USDT | +14.37% | $6,358,568.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FORM/USDT:USDT | below_1h_threshold | +3.83% | +3.84% |
| SOPH/USDT:USDT | below_1h_threshold | +2.45% | +2.46% |
| XPL/USDT:USDT | below_1h_threshold | +2.35% | +2.36% |
| SOXS/USDT:USDT | below_1h_threshold | +1.93% | +1.94% |
| VVV/USDT:USDT | below_1h_threshold | +1.53% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
