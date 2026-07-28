# Decision Report

- generated_at: 2026-07-28T22:21:16.837098+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9734**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9734, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.66% | **-0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_BB3S | 10/18 | 55.6% | +0.86% | **+0.48%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.84% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.55% | **+1.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.85% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.09% | **+0.63%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.07% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$510.93** / 初期 $100.00 (+410.93%)
- 確定: 3504件 (Win 1110 / Loss 1136 / Flat 1258) / skip 2791件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $510.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1919件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1547 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.75** / 初期 $100.00 (+10.75%)
- 確定: 751件 (Win 244 / Loss 285 / Flat 222) / pending 5件 / skip 451件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000524 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.04% 残高後 $110.75

## 6. Latest Market Context

- 更新: 2026-07-28T22:21:08.633341+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63945.0
- Funnel: target 904 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +26.35% | $43,044,473.01 |
| ZIL/USDT:USDT | +23.10% | $5,330,853.36 |
| BTW/USDT:USDT | +22.11% | $5,979,807.87 |
| RIF/USDT:USDT | +17.07% | $3,510,414.68 |
| JIMOTHY/USDT:USDT | +16.72% | $1,391,338.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.86% | +2.87% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.82% | +1.83% |
| USOIL/USDT:USDT | below_1h_threshold | +1.69% | +1.70% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.57% | +1.59% |
| EUL/USDT:USDT | below_1h_threshold | +1.53% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
