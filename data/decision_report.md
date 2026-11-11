# Decision Report

- generated_at: 2026-11-11T05:06:17.343880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18642**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.58% / filled 20/20。**
- 全期間 MARKET基準: n=18642, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 16/20 | 80.0% | +2.13% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.78% | **+0.89%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.08% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.83% | **+0.58%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.94% | **+0.49%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.27% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7210件 (Win 2073 / Loss 2305 / Flat 2832) / skip 7993件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4777件 (Win 1283 / Loss 1056 / Flat 2438) / skip 7276件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0107 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6803件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000719 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T05:06:09.256074+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=73791.8
- Funnel: target 1099 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +19.50% | $17,317,388.86 |
| FLOAT/USDT:USDT | +17.15% | $1,096,376.11 |
| INIT/USDT:USDT | +15.51% | $63,006,831.25 |
| CRWVSTOCK/USDT:USDT | +14.53% | $5,868,198.55 |
| MUU/USDT:USDT | +14.51% | $14,169,871.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +2.06% | +1.94% |
| SNXX/USDT:USDT | below_1h_threshold | +0.80% | +0.68% |
| SPX/USDT:USDT | below_1h_threshold | +0.62% | +0.50% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.34% |
| PYTH/USDT:USDT | below_1h_threshold | +0.46% | +0.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
