# Decision Report

- generated_at: 2026-09-17T22:16:32.181948+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14845**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14845, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.82% | **+0.85%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.48% | **+1.86%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.54% | **+1.78%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.47% | **+1.39%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.43% | **+1.15%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.71% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5603件 (Win 1679 / Loss 1814 / Flat 2110) / skip 5803件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GENIUS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$241.42** / 初期 $100.00 (+141.42%)
- 確定: 3139件 (Win 873 / Loss 748 / Flat 1518) / skip 5117件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1003 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $241.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2958件 (Win 878 / Loss 1165 / Flat 915) / pending 0件 / skip 3361件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000335 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T22:16:19.359985+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=76330.7
- Funnel: target 1052 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +44.90% | $2,903,765.99 |
| ONE/USDT:USDT | +37.92% | $36,406,540.48 |
| COTI/USDT:USDT | +27.32% | $4,689,149.36 |
| CROSS/USDT:USDT | +20.76% | $1,331,769.52 |
| PIEVERSE/USDT:USDT | +7.21% | $1,492,455.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +2.01% | +2.07% |
| SAGA/USDT:USDT | below_1h_threshold | +1.43% | +1.49% |
| MERL/USDT:USDT | below_1h_threshold | +0.49% | +0.55% |
| UAI/USDT:USDT | below_1h_threshold | +0.32% | +0.38% |
| SOXL/USDT:USDT | below_1h_threshold | +0.31% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
