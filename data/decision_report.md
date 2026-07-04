# Decision Report

- generated_at: 2026-07-04T02:06:52.371636+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8210**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8210, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.63% | **+0.41%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.25% | **+1.24%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.15% | **+1.07%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.68% | **+0.54%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.94% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$293.18** / 初期 $100.00 (+193.18%)
- 確定: 2528件 (Win 780 / Loss 844 / Flat 904) / skip 2243件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $293.18

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.83** / 初期 $100.00 (+5.83%)
- 確定: 612件 (Win 147 / Loss 148 / Flat 317) / skip 1009件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.20% 残高後 $105.83

## 5. Latest Market Context

- 更新: 2026-07-04T02:06:46.466860+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=62497.1
- Funnel: target 834 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +62.26% | $3,514,873.83 |
| MAGMA/USDT:USDT | +39.90% | $14,345,015.41 |
| TLM/USDT:USDT | +38.88% | $38,631,931.49 |
| BAS/USDT:USDT | +25.00% | $4,053,812.91 |
| HMSTR/USDT:USDT | +22.43% | $1,706,139.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +3.83% | +3.76% |
| NOM/USDT:USDT | below_1h_threshold | +1.68% | +1.60% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.61% | +1.54% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.20% | +1.13% |
| TA/USDT:USDT | below_1h_threshold | +1.20% | +1.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
