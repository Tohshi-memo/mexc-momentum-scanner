# Decision Report

- generated_at: 2026-11-21T06:01:23.890462+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19280**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=19280, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +1.74% | **+1.39%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.28% | **+1.15%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.71% | **+0.43%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.88% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.70% | **+0.49%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.97% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,658.72** / 初期 $100.00 (+1558.72%)
- 確定: 7423件 (Win 2133 / Loss 2395 / Flat 2895) / skip 8418件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +8.71%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $1,658.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$441.55** / 初期 $100.00 (+341.55%)
- 確定: 5088件 (Win 1355 / Loss 1088 / Flat 2645) / skip 7603件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BARD/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.49% 残高後 $441.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7439件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000137 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T06:01:14.045644+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=55775.9
- Funnel: target 1086 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +16.13% | $23,840,613.05 |
| PIEVERSE/USDT:USDT | +13.30% | $3,968,621.01 |
| UVXY/USDT:USDT | +11.29% | $6,242,183.87 |
| SQQQ/USDT:USDT | +6.73% | $5,351,520.44 |
| RARE/USDT:USDT | +6.72% | $5,545,997.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UVXY/USDT:USDT | below_1h_threshold | +1.42% | +1.41% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.45% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.42% | +0.41% |
| USOIL/USDT:USDT | below_1h_threshold | +0.42% | +0.40% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +0.39% | +0.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
