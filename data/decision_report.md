# Decision Report

- generated_at: 2026-08-10T17:06:31.311570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11179**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=11179, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.80% | **+0.56%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.35% | **+0.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.54% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$619.87** / 初期 $100.00 (+519.87%)
- 確定: 3935件 (Win 1230 / Loss 1284 / Flat 1421) / skip 3805件
- 成長率目線: 平均log +0.000464 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $619.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 3077件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.05** / 初期 $100.00 (+17.05%)
- 確定: 1302件 (Win 403 / Loss 506 / Flat 393) / pending 1件 / skip 1351件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000051 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $117.05

## 6. Latest Market Context

- 更新: 2026-08-10T17:06:21.827760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=63814.9
- Funnel: target 962 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +10.05% | $7,572,197.13 |
| MUBARAK/USDT:USDT | +5.79% | $7,697,814.77 |
| CASHCAT/USDT:USDT | +5.61% | $1,461,955.48 |
| B/USDT:USDT | +4.94% | $1,024,349.11 |
| UB/USDT:USDT | +4.61% | $1,242,459.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +3.44% | +3.55% |
| CYS/USDT:USDT | below_1h_threshold | +2.52% | +2.64% |
| BTW/USDT:USDT | below_1h_threshold | +2.50% | +2.61% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.90% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.54% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
