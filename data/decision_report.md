# Decision Report

- generated_at: 2026-07-17T19:46:23.475868+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8882**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8882, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.60% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.39% | **+0.15%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.07% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.32% | **+0.40%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$361.13** / 初期 $100.00 (+261.13%)
- 確定: 2997件 (Win 932 / Loss 952 / Flat 1113) / skip 2446件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KORU/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $361.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.59** / 初期 $100.00 (+10.59%)
- 確定: 844件 (Win 199 / Loss 172 / Flat 473) / skip 1449件
- 成長率目線: 平均log +0.000119 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1033 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KORU/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $110.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.17** / 初期 $100.00 (-0.83%)
- 確定: 142件 (Win 45 / Loss 78 / Flat 19) / pending 3件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000345 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KORU/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.17

## 6. Latest Market Context

- 更新: 2026-07-17T19:46:17.716491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=64171.6
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.1 >= 65=1, 4h RSI 83.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +20.65% | $10,131,225.48 |
| AKE/USDT:USDT | +16.91% | $36,628,762.43 |
| XEC/USDT:USDT | +12.55% | $2,762,934.12 |
| CASHCAT/USDT:USDT | +10.24% | $1,222,553.72 |
| VVV/USDT:USDT | +7.02% | $2,356,467.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +1.87% | +1.95% |
| LIT/USDT:USDT | below_1h_threshold | +1.53% | +1.61% |
| SOXS/USDT:USDT | below_1h_threshold | +1.16% | +1.24% |
| H/USDT:USDT | below_1h_threshold | +0.96% | +1.04% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
