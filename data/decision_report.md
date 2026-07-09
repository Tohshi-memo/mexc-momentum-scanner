# Decision Report

- generated_at: 2026-07-09T02:36:48.428218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8518**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8518, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.42% | **+1.36%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| MARKET | 20/20 | 100.0% | +0.10% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 5/20 | 25.0% | +1.63% | **+0.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.50% | **+0.33%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.57% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.06** / 初期 $100.00 (+3.06%)
- 確定トレード: 82件 (TP 29 / SL 52 / EXP 1)
- 最新: ANSEM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.06
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$318.10** / 初期 $100.00 (+218.10%)
- 確定: 2706件 (Win 854 / Loss 906 / Flat 946) / skip 2373件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $318.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1287件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-09T02:36:42.295751+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=61787.1
- Funnel: target 851 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +106.57% | $5,432,623.91 |
| CAP/USDT:USDT | +14.37% | $1,719,511.46 |
| VANRY/USDT:USDT | +14.28% | $6,982,090.13 |
| ALLO/USDT:USDT | +12.08% | $11,535,434.14 |
| OGN/USDT:USDT | +11.80% | $6,346,895.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +2.41% | +2.56% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.45% | +1.61% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +0.99% | +1.14% |
| SOXL/USDT:USDT | below_1h_threshold | +0.77% | +0.92% |
| FLNCSTOCK/USDT:USDT | below_1h_threshold | +0.59% | +0.74% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
