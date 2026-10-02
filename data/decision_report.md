# Decision Report

- generated_at: 2026-10-02T14:46:40.043670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.51% / filled 20/20。**
- 全期間 MARKET基準: n=16005, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.78% | **+0.83%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.26% | **+0.68%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.78% | **+0.55%** |
| MARKET | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_BB3S | 2/10 | 20.0% | +2.09% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.32% | **+0.22%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.24% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.32** / 初期 $100.00 (+1242.32%)
- 確定: 6110件 (Win 1807 / Loss 1960 / Flat 2343) / skip 6456件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,342.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5811件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0107 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4168件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000143 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T14:46:27.170519+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.77% price=85862.0
- Funnel: target 1098 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +72.11% | $4,248,101.81 |
| MAGMA/USDT:USDT | +54.01% | $2,890,195.94 |
| SAND/USDT:USDT | +44.12% | $51,475,597.48 |
| SI/USDT:USDT | +32.71% | $3,843,160.11 |
| NIGHT/USDT:USDT | +24.57% | $7,420,596.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +4.24% | +5.00% |
| TESLA/USDT:USDT | below_1h_threshold | +3.19% | +3.95% |
| STRK/USDT:USDT | below_1h_threshold | +2.61% | +3.38% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.61% | +3.38% |
| SKY/USDT:USDT | below_1h_threshold | +2.34% | +3.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
