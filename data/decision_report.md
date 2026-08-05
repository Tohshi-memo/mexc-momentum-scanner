# Decision Report

- generated_at: 2026-08-05T17:06:29.738740+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10426**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10426, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.33% | **-2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.29% | **+0.25%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.08% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.16% | **+2.05%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.50% | **+1.43%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.95% | **+1.03%** |
| MARKET_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3217件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.75** / 初期 $100.00 (+42.75%)
- 確定: 1333件 (Win 376 / Loss 312 / Flat 645) / skip 2504件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0729 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $142.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.94** / 初期 $100.00 (+17.94%)
- 確定: 1141件 (Win 365 / Loss 443 / Flat 333) / pending 1件 / skip 765件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000264 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.94

## 6. Latest Market Context

- 更新: 2026-08-05T17:06:22.229645+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64613.9
- Funnel: target 948 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +14.61% | $4,004,632.43 |
| BLESS/USDT:USDT | +12.57% | $76,171,134.61 |
| BICO/USDT:USDT | +6.53% | $14,257,250.82 |
| UB/USDT:USDT | +5.60% | $23,466,527.70 |
| VELVET/USDT:USDT | +3.27% | $4,421,505.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.98% | +3.01% |
| SNXX/USDT:USDT | below_1h_threshold | +2.60% | +2.63% |
| MUU/USDT:USDT | below_1h_threshold | +2.14% | +2.17% |
| KORU/USDT:USDT | below_1h_threshold | +2.06% | +2.09% |
| UB/USDT:USDT | below_1h_threshold | +1.73% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
