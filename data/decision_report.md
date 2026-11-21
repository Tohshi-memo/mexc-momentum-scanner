# Decision Report

- generated_at: 2026-11-21T03:41:11.515790+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19276**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19276, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.63% | **+0.66%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.45% | **+0.37%** |
| LIMIT_10PCT | 3/20 | 15.0% | +2.45% | **+0.37%** |
| LIMIT_8PCT | 3/20 | 15.0% | +0.78% | **+0.12%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.27% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.15% | **+1.18%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.51% | **+1.13%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.62% | **+0.97%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.99% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,667.06** / 初期 $100.00 (+1567.06%)
- 確定: 7422件 (Win 2133 / Loss 2394 / Flat 2895) / skip 8415件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,667.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.41** / 初期 $100.00 (+339.41%)
- 確定: 5087件 (Win 1354 / Loss 1088 / Flat 2645) / skip 7600件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UVXY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $439.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7436件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000104 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T03:41:02.666861+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -2.40% price=57167.4
- Funnel: target 1086 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +12.53% | $26,875,395.71 |
| PIEVERSE/USDT:USDT | +10.32% | $4,213,043.73 |
| BLESS/USDT:USDT | +9.91% | $22,669,463.36 |
| UVXY/USDT:USDT | +9.62% | $6,483,948.75 |
| SQQQ/USDT:USDT | +6.14% | $5,400,758.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BARD/USDT:USDT | below_1h_threshold | +0.89% | +3.29% |
| UVXY/USDT:USDT | below_1h_threshold | +0.67% | +3.07% |
| RARE/USDT:USDT | below_1h_threshold | +0.45% | +2.86% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.42% | +2.82% |
| EVAA/USDT:USDT | below_1h_threshold | +0.33% | +2.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
