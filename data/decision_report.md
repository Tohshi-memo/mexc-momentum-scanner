# Decision Report

- generated_at: 2026-07-04T01:18:43.049103+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8207**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8207, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.28% | **-2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.00% | **+0.30%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.40% | **+2.20%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.17% | **+1.87%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.83% | **+1.72%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$294.66** / 初期 $100.00 (+194.66%)
- 確定: 2525件 (Win 779 / Loss 842 / Flat 904) / skip 2243件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $294.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.83** / 初期 $100.00 (+5.83%)
- 確定: 612件 (Win 147 / Loss 148 / Flat 317) / skip 1006件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.20% 残高後 $105.83

## 5. Latest Market Context

- 更新: 2026-07-04T01:18:38.488097+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=62539.1
- Funnel: target 834 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +59.64% | $3,422,877.06 |
| TLM/USDT:USDT | +36.68% | $37,965,067.83 |
| MAGMA/USDT:USDT | +34.54% | $14,048,144.15 |
| BAS/USDT:USDT | +26.61% | $4,309,016.44 |
| HMSTR/USDT:USDT | +20.49% | $1,515,009.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.32% | +4.64% |
| MIRA/USDT:USDT | below_1h_threshold | +2.82% | +3.14% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.98% | +2.29% |
| TA/USDT:USDT | below_1h_threshold | +1.57% | +1.88% |
| TRB/USDT:USDT | below_1h_threshold | +0.91% | +1.22% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
