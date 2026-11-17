# Decision Report

- generated_at: 2026-11-17T11:16:24.318001+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19064**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=19064, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.54% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.81% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.90% | **+1.14%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.91% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 277件 (TP 100 / SL 169 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7350件 (Win 2109 / Loss 2358 / Flat 2883) / skip 8275件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4992件 (Win 1332 / Loss 1081 / Flat 2579) / skip 7483件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7223件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000128 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-17T11:16:13.090276+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=64286.6
- Funnel: target 1069 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +57.84% | $1,098,483.72 |
| EVAA/USDT:USDT | +21.47% | $36,432,536.05 |
| LONGXIA/USDT:USDT | +21.01% | $3,787,409.21 |
| LIT/USDT:USDT | +13.72% | $18,440,626.77 |
| AGT/USDT:USDT | +11.80% | $1,365,976.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HUMA/USDT:USDT | below_1h_threshold | +2.16% | +1.86% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.53% | +1.23% |
| LUNC/USDT:USDT | below_1h_threshold | +1.48% | +1.17% |
| VVV/USDT:USDT | below_1h_threshold | +1.43% | +1.13% |
| JUP/USDT:USDT | below_1h_threshold | +1.35% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
