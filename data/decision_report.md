# Decision Report

- generated_at: 2026-07-17T13:26:16.013239+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8849**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8849, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.78% | **+0.71%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_BB3S | 5/13 | 38.5% | +0.23% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.93% | **+1.45%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.99% | **+1.39%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.34% | **+1.14%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.05% | **+0.68%** |
| MARKET_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$344.87** / 初期 $100.00 (+244.87%)
- 確定: 2964件 (Win 923 / Loss 947 / Flat 1094) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $344.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.49** / 初期 $100.00 (+8.49%)
- 確定: 811件 (Win 190 / Loss 171 / Flat 450) / skip 1449件
- 成長率目線: 平均log +0.000100 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0432 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $108.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.41** / 初期 $100.00 (-1.59%)
- 確定: 115件 (Win 36 / Loss 71 / Flat 8) / pending 3件 / skip 201件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.41

## 6. Latest Market Context

- 更新: 2026-07-17T13:26:11.600734+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=62832.2
- Funnel: target 885 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LRC/USDT:USDT | +35.61% | $2,711,076.57 |
| XEC/USDT:USDT | +25.76% | $1,931,358.23 |
| AKE/USDT:USDT | +25.48% | $38,733,972.57 |
| LUMIA/USDT:USDT | +20.31% | $2,993,323.62 |
| KAITO/USDT:USDT | +16.17% | $5,104,532.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LRC/USDT:USDT | below_1h_threshold | +3.58% | +3.96% |
| US/USDT:USDT | below_1h_threshold | +1.73% | +2.12% |
| SOXS/USDT:USDT | below_1h_threshold | +1.50% | +1.88% |
| ALLO/USDT:USDT | below_1h_threshold | +0.83% | +1.21% |
| CRV/USDT:USDT | below_1h_threshold | +0.62% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
