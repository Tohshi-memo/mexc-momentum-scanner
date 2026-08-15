# Decision Report

- generated_at: 2026-08-15T18:46:29.536739+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11690**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11690, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.41% | **-1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.21% | **+0.36%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.89% | **+0.32%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.21% | **+0.18%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.01% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.32% | **+0.93%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.02% | **+0.91%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.75% | **+0.88%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4158件 (Win 1290 / Loss 1355 / Flat 1513) / skip 4093件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1753件 (Win 492 / Loss 413 / Flat 848) / skip 3348件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.67** / 初期 $100.00 (+18.67%)
- 確定: 1621件 (Win 493 / Loss 617 / Flat 511) / pending 5件 / skip 1543件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIL/USDT:USDT `MARKET` EXPIRED account -0.03% 残高後 $118.67

## 6. Latest Market Context

- 更新: 2026-08-15T18:46:18.808423+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63017.9
- Funnel: target 985 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +9.46% | $2,699,835.35 |
| BTW/USDT:USDT | +8.40% | $11,234,032.13 |
| AIO/USDT:USDT | +7.27% | $2,403,236.45 |
| ROBO/USDT:USDT | +6.80% | $8,753,242.51 |
| AKE/USDT:USDT | +6.37% | $46,994,068.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +3.76% | +3.79% |
| CAP/USDT:USDT | below_1h_threshold | +2.59% | +2.63% |
| AVNT/USDT:USDT | below_1h_threshold | +2.15% | +2.18% |
| AIO/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |
| XMR/USDT:USDT | below_1h_threshold | +0.96% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
