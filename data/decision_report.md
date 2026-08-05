# Decision Report

- generated_at: 2026-08-05T23:16:19.722070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10473**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10473, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.17% | **+0.41%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.26% | **+1.07%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.04% | **+0.73%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +0.41% | **+0.23%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.26% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.31** / 初期 $100.00 (+505.31%)
- 確定: 3770件 (Win 1195 / Loss 1236 / Flat 1339) / skip 3264件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $605.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.64** / 初期 $100.00 (+40.64%)
- 確定: 1356件 (Win 379 / Loss 319 / Flat 658) / skip 2528件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $140.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1143件 (Win 365 / Loss 445 / Flat 333) / pending 1件 / skip 804件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000411 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-05T23:16:12.166017+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64630.4
- Funnel: target 948 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +49.65% | $4,805,635.55 |
| BLESS/USDT:USDT | +40.62% | $102,185,322.33 |
| HEI/USDT:USDT | +36.67% | $43,945,903.95 |
| CASHCAT/USDT:USDT | +30.42% | $1,372,791.81 |
| SITMSTOCK/USDT:USDT | +29.33% | $1,071,589.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.92% | +3.89% |
| SYN/USDT:USDT | below_1h_threshold | +3.90% | +3.86% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.53% | +3.50% |
| HFT/USDT:USDT | below_1h_threshold | +2.04% | +2.01% |
| PI/USDT:USDT | below_1h_threshold | +1.38% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
