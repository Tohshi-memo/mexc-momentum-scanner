# Decision Report

- generated_at: 2026-07-26T08:36:31.354625+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9564**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9564, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.85% | **+0.85%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.36% | **+0.54%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.88% | **+0.51%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.26% | **+0.45%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.43% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.79% | **+1.43%** |
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.60% | **+1.26%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.92% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$466.38** / 初期 $100.00 (+366.38%)
- 確定: 3392件 (Win 1078 / Loss 1100 / Flat 1214) / skip 2733件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $466.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.66** / 初期 $100.00 (+39.66%)
- 確定: 1217件 (Win 338 / Loss 270 / Flat 609) / skip 1758件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1430 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $139.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.43** / 初期 $100.00 (+9.43%)
- 確定: 607件 (Win 206 / Loss 231 / Flat 170) / pending 5件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000511 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.43

## 6. Latest Market Context

- 更新: 2026-07-26T08:36:18.061207+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=64374.8
- Funnel: target 898 → liquid 119 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +67.01% | $38,706,040.58 |
| PIEVERSE/USDT:USDT | +49.69% | $3,698,663.02 |
| DIA/USDT:USDT | +41.99% | $2,233,096.43 |
| BANK/USDT:USDT | +21.92% | $94,112,322.86 |
| SHIB/USDT:USDT | +18.63% | $74,522,744.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.39% | +3.34% |
| DIA/USDT:USDT | below_1h_threshold | +3.37% | +3.32% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.39% | +2.34% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.86% | +1.81% |
| VVV/USDT:USDT | below_1h_threshold | +1.80% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
