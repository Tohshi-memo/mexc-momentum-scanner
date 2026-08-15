# Decision Report

- generated_at: 2026-08-15T19:01:31.110053+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11691, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.86% | **-1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.21% | **+0.36%** |
| LIMIT_BB3S | 6/18 | 33.3% | +0.89% | **+0.30%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.01% | **-0.01%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.24% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.34% | **+1.51%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.93% | **+1.32%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.91% | **+1.16%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.43% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.37** / 初期 $100.00 (+541.37%)
- 確定: 4159件 (Win 1290 / Loss 1355 / Flat 1514) / skip 4093件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACU/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $641.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1754件 (Win 492 / Loss 413 / Flat 849) / skip 3348件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACU/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.67** / 初期 $100.00 (+18.67%)
- 確定: 1622件 (Win 493 / Loss 617 / Flat 512) / pending 4件 / skip 1543件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACU/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $118.67

## 6. Latest Market Context

- 更新: 2026-08-15T19:01:21.130607+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=63026.2
- Funnel: target 985 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +11.67% | $2,769,617.08 |
| BTW/USDT:USDT | +9.69% | $10,935,746.18 |
| ROBO/USDT:USDT | +7.47% | $8,752,804.31 |
| AIO/USDT:USDT | +7.36% | $2,341,974.35 |
| AKE/USDT:USDT | +6.74% | $33,108,107.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +1.03% | +1.03% |
| BTW/USDT:USDT | below_1h_threshold | +0.83% | +0.83% |
| BANK/USDT:USDT | below_1h_threshold | +0.34% | +0.34% |
| BR/USDT:USDT | below_1h_threshold | +0.32% | +0.32% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.29% | +0.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
