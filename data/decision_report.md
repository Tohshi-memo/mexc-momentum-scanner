# Decision Report

- generated_at: 2026-10-22T08:16:23.031510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17128**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17128, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.78% | **+0.28%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.26% | **+1.24%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.90% | **+1.14%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.37** / 初期 $100.00 (+1242.37%)
- 確定: 6510件 (Win 1892 / Loss 2076 / Flat 2542) / skip 7179件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RUNE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,342.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.60** / 初期 $100.00 (+178.60%)
- 確定: 3838件 (Win 1055 / Loss 898 / Flat 1885) / skip 6701件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RUNE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $278.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5286件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000135 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T08:16:10.748173+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=82141.7
- Funnel: target 1090 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +39.29% | $3,086,320.21 |
| AGT/USDT:USDT | +20.85% | $5,090,446.29 |
| PTB/USDT:USDT | +17.95% | $1,311,583.47 |
| SOXS/USDT:USDT | +11.31% | $11,228,479.16 |
| XMR/USDT:USDT | +9.16% | $21,655,171.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +3.22% | +3.28% |
| PHA/USDT:USDT | below_1h_threshold | +1.86% | +1.92% |
| SOXS/USDT:USDT | below_1h_threshold | +1.09% | +1.16% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.73% | +0.80% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.70% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
