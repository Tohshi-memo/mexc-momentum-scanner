# Decision Report

- generated_at: 2026-11-10T04:16:19.857858+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18576**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18576, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.72% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.09% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.56% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.67% | **+0.37%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.74% | **+0.18%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.16% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,669.67** / 初期 $100.00 (+1569.67%)
- 確定: 7174件 (Win 2063 / Loss 2288 / Flat 2823) / skip 7963件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INIT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,669.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$387.85** / 初期 $100.00 (+287.85%)
- 確定: 4758件 (Win 1277 / Loss 1048 / Flat 2433) / skip 7229件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1498 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $387.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6736件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T04:16:08.702376+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=74545.7
- Funnel: target 1094 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIUBI/USDT:USDT | +47.98% | $1,973,499.77 |
| INIT/USDT:USDT | +44.29% | $5,434,635.11 |
| CLAUDIA/USDT:USDT | +10.09% | $1,063,702.65 |
| ZHIPUSTOCK/USDT:USDT | +10.07% | $1,368,457.09 |
| ON/USDT:USDT | +7.75% | $5,403,508.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +3.48% | +3.47% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +3.38% | +3.37% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.84% | +0.83% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.75% | +0.74% |
| JUP/USDT:USDT | below_1h_threshold | +0.72% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
