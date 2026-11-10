# Decision Report

- generated_at: 2026-11-10T14:56:30.262706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18607**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18607, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.57% | **+0.71%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.13% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.29% | **+1.29%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.61% | **+1.28%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.52% | **+0.99%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,699.76** / 初期 $100.00 (+1599.76%)
- 確定: 7204件 (Win 2073 / Loss 2300 / Flat 2831) / skip 7964件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: INIT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,699.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$397.18** / 初期 $100.00 (+297.18%)
- 確定: 4773件 (Win 1283 / Loss 1052 / Flat 2438) / skip 7245件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0571 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: INIT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $397.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6767件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000311 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T14:56:12.607938+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.86% price=74349.9
- Funnel: target 1099 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +97.56% | $24,997,700.00 |
| ONE/USDT:USDT | +17.21% | $9,850,934.10 |
| ARIA/USDT:USDT | +16.19% | $2,764,609.92 |
| ZHIPUSTOCK/USDT:USDT | +11.05% | $1,623,491.26 |
| BR/USDT:USDT | +10.64% | $3,806,698.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEPE/USDT:USDT | below_1h_threshold | +4.81% | +3.95% |
| LIT/USDT:USDT | below_1h_threshold | +4.70% | +3.84% |
| ARIA/USDT:USDT | below_1h_threshold | +3.17% | +2.31% |
| SQQQ/USDT:USDT | below_1h_threshold | +2.89% | +2.03% |
| NEAR/USDT:USDT | below_1h_threshold | +2.37% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
