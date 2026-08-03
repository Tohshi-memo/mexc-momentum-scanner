# Decision Report

- generated_at: 2026-08-03T07:51:18.097608+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10197**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10197, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.79% | **-1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.08% | **-0.03%** |
| LIMIT_BB3S | 8/19 | 42.1% | -0.39% | **-0.16%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.25% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.18% | **+2.39%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.57% | **+1.78%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.75% | **+1.65%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.40% | **+1.53%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.36% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3677件 (Win 1166 / Loss 1205 / Flat 1306) / skip 3081件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1282件 (Win 359 / Loss 298 / Flat 625) / skip 2326件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0356 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.67** / 初期 $100.00 (+13.67%)
- 確定: 983件 (Win 313 / Loss 383 / Flat 287) / pending 3件 / skip 681件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000288 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $113.67

## 6. Latest Market Context

- 更新: 2026-08-03T07:51:10.708841+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=62621.2
- Funnel: target 924 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +89.45% | $1,191,673.43 |
| 1000RATS/USDT:USDT | +49.62% | $38,754,386.64 |
| ICNT/USDT:USDT | +30.07% | $2,211,939.55 |
| BICO/USDT:USDT | +20.46% | $7,344,497.04 |
| GRVT/USDT:USDT | +15.44% | $2,449,490.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +3.07% | +3.03% |
| UB/USDT:USDT | below_1h_threshold | +2.34% | +2.30% |
| LIT/USDT:USDT | below_1h_threshold | +1.68% | +1.63% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.60% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.60% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
