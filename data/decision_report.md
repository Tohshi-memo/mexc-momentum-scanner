# Decision Report

- generated_at: 2026-07-20T07:56:24.612792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9095**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9095, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.14% | **-1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.59% | **+0.21%** |
| LIMIT_BB3S | 2/17 | 11.8% | -1.68% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.32% | **+1.05%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.88% | **+0.73%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.44% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定トレード: 121件 (TP 43 / SL 73 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -3.98% 残高後 $108.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$399.37** / 初期 $100.00 (+299.37%)
- 確定: 3157件 (Win 986 / Loss 1001 / Flat 1170) / skip 2499件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $399.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.54** / 初期 $100.00 (+26.54%)
- 確定: 1056件 (Win 275 / Loss 218 / Flat 563) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0626 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $126.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.05** / 初期 $100.00 (+1.05%)
- 確定: 294件 (Win 98 / Loss 131 / Flat 65) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $101.05

## 6. Latest Market Context

- 更新: 2026-07-20T07:56:14.811611+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=64219.3
- Funnel: target 886 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +114.21% | $9,691,227.46 |
| BANK/USDT:USDT | +43.32% | $105,876,891.71 |
| EVAA/USDT:USDT | +32.16% | $4,268,133.56 |
| PUMPFUN/USDT:USDT | +19.80% | $22,786,147.47 |
| PROM/USDT:USDT | +15.84% | $2,595,358.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PI/USDT:USDT | below_1h_threshold | +4.51% | +4.00% |
| B/USDT:USDT | below_1h_threshold | +3.89% | +3.37% |
| BLESS/USDT:USDT | below_1h_threshold | +3.52% | +3.00% |
| PENGU/USDT:USDT | below_1h_threshold | +2.57% | +2.06% |
| TIA/USDT:USDT | below_1h_threshold | +2.33% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
