# Decision Report

- generated_at: 2026-07-28T15:41:30.411199+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9705**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9705, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.65% | **+0.33%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.16% | **+0.29%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_BB3S | 3/19 | 15.8% | +1.10% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.57% | **+1.93%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.71% | **+0.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$106.38** / 初期 $100.00 (+6.38%)
- 確定トレード: 149件 (TP 51 / SL 93 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.38
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$474.91** / 初期 $100.00 (+374.91%)
- 確定: 3475件 (Win 1096 / Loss 1127 / Flat 1252) / skip 2791件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $474.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1890件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1006 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.20** / 初期 $100.00 (+9.20%)
- 確定: 723件 (Win 235 / Loss 276 / Flat 212) / pending 5件 / skip 449件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $109.20

## 6. Latest Market Context

- 更新: 2026-07-28T15:41:21.969536+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.68% price=63814.6
- Funnel: target 904 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +53.48% | $23,663,363.28 |
| ON/USDT:USDT | +44.46% | $22,380,674.88 |
| SOONNETWORK/USDT:USDT | +36.18% | $3,039,847.91 |
| BULLA/USDT:USDT | +27.70% | $2,222,357.61 |
| VANRY/USDT:USDT | +24.82% | $1,558,100.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_relative_strength | +5.47% | +4.79% |
| VVV/USDT:USDT | below_1h_threshold | +4.59% | +3.91% |
| VANRY/USDT:USDT | below_1h_threshold | +3.57% | +2.89% |
| XPL/USDT:USDT | below_1h_threshold | +3.15% | +2.47% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.06% | +2.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
