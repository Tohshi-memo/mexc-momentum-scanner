# Decision Report

- generated_at: 2026-10-27T18:56:29.955539+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17638**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17638, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +3.97% | **+1.79%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_5PCT | 13/20 | 65.0% | +1.22% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.39% | **+1.32%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.59% | **+1.30%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.19% | **+1.10%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.94% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 254件 (TP 94 / SL 152 / EXP 8)
- 最新: APR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,555.81** / 初期 $100.00 (+1455.81%)
- 確定: 6746件 (Win 1966 / Loss 2164 / Flat 2616) / skip 7453件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HAEDAL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,555.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$347.57** / 初期 $100.00 (+247.57%)
- 確定: 4167件 (Win 1139 / Loss 964 / Flat 2064) / skip 6882件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1215 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HAEDAL/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $347.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5800件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000421 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T18:56:14.758055+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80598.0
- Funnel: target 1083 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +14.20% | $3,985,649.09 |
| BULLA/USDT:USDT | +13.02% | $11,659,645.13 |
| AKE/USDT:USDT | +9.19% | $5,234,547.28 |
| LAB/USDT:USDT | +8.22% | $1,311,581.86 |
| CBRSSTOCK/USDT:USDT | +6.73% | $2,027,443.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +2.86% | +2.71% |
| US/USDT:USDT | below_1h_threshold | +2.46% | +2.31% |
| LAB/USDT:USDT | below_1h_threshold | +2.00% | +1.85% |
| BAT/USDT:USDT | below_1h_threshold | +1.52% | +1.37% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.46% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
