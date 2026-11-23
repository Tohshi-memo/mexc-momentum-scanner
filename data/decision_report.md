# Decision Report

- generated_at: 2026-11-23T09:21:30.534970+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19434**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19434, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.84% | **+0.65%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.19% | **+1.44%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.66% | **+1.06%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,862.59** / 初期 $100.00 (+1762.59%)
- 確定: 7532件 (Win 2164 / Loss 2424 / Flat 2944) / skip 8463件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,862.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$466.74** / 初期 $100.00 (+366.74%)
- 確定: 5196件 (Win 1385 / Loss 1117 / Flat 2694) / skip 7649件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0059 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $466.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7597件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000147 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T09:21:14.908579+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=61759.8
- Funnel: target 1086 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +94.53% | $2,003,910.47 |
| BULLA/USDT:USDT | +33.79% | $2,929,665.69 |
| ARIA/USDT:USDT | +26.82% | $2,682,857.52 |
| ELSA/USDT:USDT | +25.54% | $2,436,914.15 |
| EVAA/USDT:USDT | +21.66% | $46,342,926.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +4.94% | +4.49% |
| VELVET/USDT:USDT | below_1h_threshold | +2.50% | +2.06% |
| SNXX/USDT:USDT | below_1h_threshold | +2.39% | +1.94% |
| BULLA/USDT:USDT | below_1h_threshold | +2.32% | +1.87% |
| SOXL/USDT:USDT | below_1h_threshold | +2.02% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
