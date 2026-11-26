# Decision Report

- generated_at: 2026-11-26T16:36:23.341571+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19705**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=19705, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.59% | **+0.56%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.84% | **+1.20%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.05% | **+0.57%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.44% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定トレード: 290件 (TP 106 / SL 176 / EXP 8)
- 最新: MONAD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,948.16** / 初期 $100.00 (+1848.16%)
- 確定: 7639件 (Win 2199 / Loss 2459 / Flat 2981) / skip 8627件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,948.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$468.19** / 初期 $100.00 (+368.19%)
- 確定: 5232件 (Win 1393 / Loss 1126 / Flat 2713) / skip 7884件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0144 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $468.19

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7868件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000377 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-26T16:36:11.983610+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=60382.3
- Funnel: target 1097 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1, 4h RSI 85.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +26.98% | $8,887,107.19 |
| INIT/USDT:USDT | +8.45% | $6,246,910.55 |
| NES/USDT:USDT | +4.74% | $1,208,392.73 |
| AIOT/USDT:USDT | +3.23% | $1,035,878.43 |
| SI/USDT:USDT | +2.87% | $1,947,202.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +4.70% | +5.06% |
| AIOT/USDT:USDT | below_1h_threshold | +3.40% | +3.76% |
| SI/USDT:USDT | below_1h_threshold | +2.88% | +3.24% |
| BLUR/USDT:USDT | below_1h_threshold | +2.51% | +2.87% |
| LISTA/USDT:USDT | below_1h_threshold | +1.74% | +2.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
