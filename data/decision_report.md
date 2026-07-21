# Decision Report

- generated_at: 2026-07-21T15:26:24.637681+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9186**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9186, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.62% | **+0.59%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.48% | **+0.52%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +4.12% | **+2.06%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.94% | **+1.38%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.69% | **+1.07%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$419.80** / 初期 $100.00 (+319.80%)
- 確定: 3248件 (Win 1021 / Loss 1038 / Flat 1189) / skip 2499件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $419.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.02** / 初期 $100.00 (+32.02%)
- 確定: 1147件 (Win 309 / Loss 246 / Flat 592) / skip 1450件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0433 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $132.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 343件 (Win 120 / Loss 152 / Flat 71) / pending 4件 / skip 314件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T15:26:16.745294+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=66658.7
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +119.35% | $5,112,375.67 |
| PONS/USDT:USDT | +105.16% | $1,400,252.53 |
| ERA/USDT:USDT | +61.80% | $12,494,872.42 |
| ESPORTS/USDT:USDT | +46.28% | $8,424,344.34 |
| ONE/USDT:USDT | +36.24% | $2,278,567.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.28% | +4.50% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +2.87% | +3.09% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +2.28% | +2.50% |
| KORU/USDT:USDT | below_1h_threshold | +2.22% | +2.44% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.10% | +2.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
