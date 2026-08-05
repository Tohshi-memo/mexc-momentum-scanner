# Decision Report

- generated_at: 2026-08-05T17:41:33.851020+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10432**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10432, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-2.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.96% | **-2.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.75% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.98% | **+2.39%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.43% | **+2.19%** |
| MARKET_LONG | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.11% | **+1.23%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.84% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3223件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.75** / 初期 $100.00 (+41.75%)
- 確定: 1336件 (Win 376 / Loss 314 / Flat 646) / skip 2507件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0945 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $141.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.94** / 初期 $100.00 (+17.94%)
- 確定: 1141件 (Win 365 / Loss 443 / Flat 333) / pending 1件 / skip 772件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000293 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.94

## 6. Latest Market Context

- 更新: 2026-08-05T17:41:23.088895+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64689.1
- Funnel: target 948 → liquid 182 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.8 >= 65=1, 4h RSI 83.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +19.41% | $34,928,527.67 |
| ESPORTS/USDT:USDT | +17.60% | $4,510,199.19 |
| BLESS/USDT:USDT | +15.96% | $79,188,666.43 |
| UB/USDT:USDT | +14.99% | $24,085,442.91 |
| BICO/USDT:USDT | +7.36% | $14,443,886.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.71% | +3.62% |
| SOXL/USDT:USDT | below_1h_threshold | +2.98% | +2.89% |
| SNXX/USDT:USDT | below_1h_threshold | +2.60% | +2.51% |
| GRVT/USDT:USDT | below_1h_threshold | +2.58% | +2.50% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.39% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
