# Decision Report

- generated_at: 2026-11-16T09:55:08.010208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19010**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19010, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.87% | **-0.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.03% | **+0.60%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.66% | **+1.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,677.36** / 初期 $100.00 (+1577.36%)
- 確定: 7348件 (Win 2109 / Loss 2358 / Flat 2881) / skip 8223件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,677.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.10** / 初期 $100.00 (+330.10%)
- 確定: 4984件 (Win 1332 / Loss 1081 / Flat 2571) / skip 7437件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHELL/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $430.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7170件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000078 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T09:54:58.627444+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=64323.1
- Funnel: target 1066 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +88.84% | $10,887,213.25 |
| EVAA/USDT:USDT | +23.15% | $21,456,764.12 |
| SKR/USDT:USDT | +22.38% | $4,291,095.73 |
| BLESS/USDT:USDT | +18.31% | $2,243,249.63 |
| JCT/USDT:USDT | +8.57% | $11,206,997.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +2.99% | +3.16% |
| SHELL/USDT:USDT | below_1h_threshold | +2.02% | +2.18% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.74% | +0.91% |
| ASTER/USDT:USDT | below_1h_threshold | +0.66% | +0.83% |
| HYPE/USDT:USDT | below_1h_threshold | +0.65% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
