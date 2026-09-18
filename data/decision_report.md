# Decision Report

- generated_at: 2026-09-18T03:26:24.364704+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14859**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=14859, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.32% | **+0.62%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.40% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.88% | **+1.58%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.46% | **+1.02%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.22% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,159.77** / 初期 $100.00 (+1059.77%)
- 確定: 5604件 (Win 1679 / Loss 1814 / Flat 2111) / skip 5816件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARB/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,159.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$243.85** / 初期 $100.00 (+143.85%)
- 確定: 3148件 (Win 876 / Loss 751 / Flat 1521) / skip 5122件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1251 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $243.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.32** / 初期 $100.00 (+23.32%)
- 確定: 2960件 (Win 878 / Loss 1166 / Flat 916) / pending 0件 / skip 3369件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.32

## 6. Latest Market Context

- 更新: 2026-09-18T03:26:14.856748+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=77268.8
- Funnel: target 1052 → liquid 151 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1, 4h RSI 76.2 >= 65=1, 4h RSI 87.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +30.42% | $3,449,579.40 |
| ARB/USDT:USDT | +26.97% | $83,788,989.00 |
| COTI/USDT:USDT | +20.43% | $6,872,327.26 |
| APT/USDT:USDT | +19.07% | $6,391,807.73 |
| NEAR/USDT:USDT | +18.75% | $124,829,634.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APT/USDT:USDT | below_1h_threshold | +4.78% | +4.36% |
| RAY/USDT:USDT | below_1h_threshold | +4.47% | +4.05% |
| CROSS/USDT:USDT | below_1h_threshold | +3.37% | +2.95% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.82% | +2.41% |
| UAI/USDT:USDT | below_1h_threshold | +2.40% | +1.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
