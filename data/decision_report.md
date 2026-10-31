# Decision Report

- generated_at: 2026-10-31T04:06:24.072704+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17887**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17887, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.15% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| MARKET_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.83% | **+1.46%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.87% | **+1.31%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,515.83** / 初期 $100.00 (+1415.83%)
- 確定: 6815件 (Win 1976 / Loss 2184 / Flat 2655) / skip 7633件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,515.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$367.39** / 初期 $100.00 (+267.39%)
- 確定: 4387件 (Win 1180 / Loss 983 / Flat 2224) / skip 6911件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0580 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $367.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6048件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T04:06:08.988832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77170.0
- Funnel: target 1090 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +57.23% | $8,772,389.16 |
| IDOL/USDT:USDT | +18.07% | $14,679,749.64 |
| SOPH/USDT:USDT | +17.19% | $1,403,806.72 |
| BEAMX/USDT:USDT | +9.60% | $2,418,093.13 |
| OP/USDT:USDT | +7.80% | $16,876,694.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOPH/USDT:USDT | below_1h_threshold | +2.22% | +2.17% |
| BLUR/USDT:USDT | below_1h_threshold | +1.72% | +1.67% |
| MUU/USDT:USDT | below_1h_threshold | +0.73% | +0.68% |
| RUNE/USDT:USDT | below_1h_threshold | +0.56% | +0.51% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.33% | +0.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
