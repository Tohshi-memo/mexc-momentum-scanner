# Decision Report

- generated_at: 2026-07-28T16:36:26.378912+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9708**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9708, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.68% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.20% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.70% | **+2.02%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.52% | **+1.37%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.79% | **+1.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| MARKET_LONG | 20/20 | 100.0% | +0.51% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$484.45** / 初期 $100.00 (+384.45%)
- 確定: 3478件 (Win 1098 / Loss 1127 / Flat 1253) / skip 2791件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $484.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1893件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1037 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.38** / 初期 $100.00 (+9.38%)
- 確定: 726件 (Win 236 / Loss 277 / Flat 213) / pending 6件 / skip 449件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000392 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $109.38

## 6. Latest Market Context

- 更新: 2026-07-28T16:36:19.251512+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=63783.4
- Funnel: target 904 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +9.56% | $6,170,953.25 |
| AEON1/USDT:USDT | +4.75% | $2,719,736.99 |
| BULLA/USDT:USDT | +3.02% | $2,364,757.34 |
| LIT/USDT:USDT | +2.57% | $3,342,657.10 |
| ZIL/USDT:USDT | +2.33% | $1,171,957.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.76% | +4.94% |
| BULLA/USDT:USDT | below_1h_threshold | +2.99% | +3.17% |
| GGLL/USDT:USDT | below_1h_threshold | +2.93% | +3.12% |
| LIT/USDT:USDT | below_1h_threshold | +2.57% | +2.75% |
| BASTOCK/USDT:USDT | below_1h_threshold | +2.45% | +2.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
