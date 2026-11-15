# Decision Report

- generated_at: 2026-11-15T06:26:22.224877+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18931**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.17% / filled 20/20。**
- 全期間 MARKET基準: n=18931, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.12% | **+0.90%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.08% | **+0.76%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +2.10% | **+0.63%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +0.29% | **+0.23%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,711.71** / 初期 $100.00 (+1611.71%)
- 確定: 7335件 (Win 2106 / Loss 2348 / Flat 2881) / skip 8157件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,711.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$428.00** / 初期 $100.00 (+328.00%)
- 確定: 4939件 (Win 1320 / Loss 1080 / Flat 2539) / skip 7403件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $428.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7091件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000196 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T06:26:08.802893+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64449.9
- Funnel: target 1071 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARIA/USDT:USDT | +13.07% | $2,501,057.82 |
| PIEVERSE/USDT:USDT | +9.75% | $1,861,514.45 |
| SHELL/USDT:USDT | +9.63% | $2,140,006.84 |
| INIT/USDT:USDT | +9.62% | $1,875,230.99 |
| VVV/USDT:USDT | +8.44% | $2,890,675.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INIT/USDT:USDT | below_1h_threshold | +3.54% | +3.61% |
| ARIA/USDT:USDT | below_1h_threshold | +1.88% | +1.94% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.38% | +1.44% |
| JCT/USDT:USDT | below_1h_threshold | +1.27% | +1.33% |
| ONE/USDT:USDT | below_1h_threshold | +1.25% | +1.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
