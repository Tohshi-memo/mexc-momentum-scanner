# Decision Report

- generated_at: 2026-11-26T16:41:53.719422+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19708**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19708, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_BB3S | 5/19 | 26.3% | +0.01% | **+0.00%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.04% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,948.16** / 初期 $100.00 (+1848.16%)
- 確定: 7639件 (Win 2199 / Loss 2459 / Flat 2981) / skip 8630件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,948.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$468.85** / 初期 $100.00 (+368.85%)
- 確定: 5235件 (Win 1395 / Loss 1126 / Flat 2714) / skip 7884件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0168 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $468.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7872件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000367 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T16:41:27.525233+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=60501.7
- Funnel: target 1097 → liquid 136 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1, 4h RSI 86.4 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +33.91% | $9,114,950.59 |
| INIT/USDT:USDT | +10.80% | $6,456,310.03 |
| SI/USDT:USDT | +8.02% | $1,961,211.20 |
| NES/USDT:USDT | +5.31% | $1,209,459.43 |
| AIOT/USDT:USDT | +3.07% | $1,065,047.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +2.49% | +2.65% |
| ARIA/USDT:USDT | below_1h_threshold | +1.90% | +2.06% |
| LISTA/USDT:USDT | below_1h_threshold | +1.88% | +2.04% |
| BLUR/USDT:USDT | below_1h_threshold | +1.67% | +1.83% |
| BLESS/USDT:USDT | below_1h_threshold | +1.48% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
