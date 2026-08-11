# Decision Report

- generated_at: 2026-08-11T10:16:22.753884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11241**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11241, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.08% | **+0.87%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.14% | **+0.47%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.62% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.95% | **+1.33%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.99% | **+1.20%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.81% | **+1.18%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.03% | **+1.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 177件 (TP 68 / SL 104 / EXP 5)
- 最新: EPIC/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3937件 (Win 1230 / Loss 1285 / Flat 1422) / skip 3865件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1514件 (Win 424 / Loss 361 / Flat 729) / skip 3138件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.84** / 初期 $100.00 (+14.84%)
- 確定: 1330件 (Win 407 / Loss 524 / Flat 399) / pending 1件 / skip 1384件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000032 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.84

## 6. Latest Market Context

- 更新: 2026-08-11T10:16:14.594464+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=64218.9
- Funnel: target 963 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +90.57% | $19,272,350.19 |
| VELVET/USDT:USDT | +44.26% | $5,591,743.83 |
| BTR/USDT:USDT | +37.00% | $1,199,509.40 |
| TOAD/USDT:USDT | +29.46% | $1,457,594.00 |
| CYS/USDT:USDT | +20.22% | $26,747,747.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANANAS31/USDT:USDT | below_1h_threshold | +1.20% | +1.30% |
| PROM/USDT:USDT | below_1h_threshold | +1.14% | +1.23% |
| SQD/USDT:USDT | below_1h_threshold | +1.07% | +1.17% |
| MAV/USDT:USDT | below_1h_threshold | +0.98% | +1.08% |
| CYS/USDT:USDT | below_1h_threshold | +0.91% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
