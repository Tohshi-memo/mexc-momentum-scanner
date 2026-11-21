# Decision Report

- generated_at: 2026-11-21T06:26:36.654060+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19281**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.68% / filled 20/20。**
- 全期間 MARKET基準: n=19281, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.74% | **+1.39%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.99% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.71% | **+0.43%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.88% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.26% | **+0.95%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.63% | **+0.44%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.24% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,661.00** / 初期 $100.00 (+1561.00%)
- 確定: 7424件 (Win 2134 / Loss 2395 / Flat 2895) / skip 8418件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +8.71%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $1,661.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$441.55** / 初期 $100.00 (+341.55%)
- 確定: 5088件 (Win 1355 / Loss 1088 / Flat 2645) / skip 7604件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.49% 残高後 $441.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7440件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T06:26:20.523055+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=55930.0
- Funnel: target 1086 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +19.87% | $24,499,772.75 |
| PIEVERSE/USDT:USDT | +13.61% | $4,032,486.02 |
| UVXY/USDT:USDT | +10.92% | $6,246,221.79 |
| BTW/USDT:USDT | +8.43% | $3,976,282.65 |
| RARE/USDT:USDT | +7.34% | $5,610,937.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.34% | +3.04% |
| UVXY/USDT:USDT | below_1h_threshold | +1.42% | +1.13% |
| BLESS/USDT:USDT | below_1h_threshold | +1.08% | +0.79% |
| JCT/USDT:USDT | below_1h_threshold | +0.90% | +0.61% |
| RARE/USDT:USDT | below_1h_threshold | +0.73% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
