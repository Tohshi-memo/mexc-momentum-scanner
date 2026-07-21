# Decision Report

- generated_at: 2026-07-21T14:06:26.857198+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9178**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9178, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_BB3S | 9/18 | 50.0% | +0.57% | **+0.29%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.14% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.00% | **+1.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.17% | **+1.63%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.57% | **+1.49%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.24% | **+1.01%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.63% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$430.45** / 初期 $100.00 (+330.45%)
- 確定: 3240件 (Win 1021 / Loss 1033 / Flat 1186) / skip 2499件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.12% 残高後 $430.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$133.67** / 初期 $100.00 (+33.67%)
- 確定: 1139件 (Win 308 / Loss 241 / Flat 590) / skip 1450件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1095 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.07% 残高後 $133.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 312件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000296 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T14:06:18.723491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=66860.0
- Funnel: target 885 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +115.37% | $1,254,243.84 |
| JIMOTHY/USDT:USDT | +79.13% | $4,979,257.89 |
| ERA/USDT:USDT | +64.28% | $11,858,109.83 |
| ESPORTS/USDT:USDT | +37.46% | $7,416,800.92 |
| ZHIPUSTOCK/USDT:USDT | +33.95% | $3,251,435.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.46% | +4.29% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +3.47% | +3.30% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.40% | +2.23% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +2.19% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
