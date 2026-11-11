# Decision Report

- generated_at: 2026-11-11T08:51:32.615653+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18655**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18655, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.53% | **+0.50%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.22% | **+0.30%** |
| LIMIT_BB3S | 4/18 | 22.2% | +0.78% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 269件 (TP 97 / SL 164 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,656.10** / 初期 $100.00 (+1556.10%)
- 確定: 7211件 (Win 2073 / Loss 2306 / Flat 2832) / skip 8005件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $1,656.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4778件 (Win 1283 / Loss 1056 / Flat 2439) / skip 7288件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6813件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000573 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T08:51:16.094332+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=73730.4
- Funnel: target 1099 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +69.07% | $1,743,003.57 |
| CRWVSTOCK/USDT:USDT | +17.89% | $6,052,687.72 |
| SOXL/USDT:USDT | +16.06% | $674,946,950.53 |
| SNXX/USDT:USDT | +15.85% | $25,344,818.47 |
| MUU/USDT:USDT | +15.68% | $14,062,120.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRAM/USDT:USDT | below_1h_threshold | +1.47% | +1.93% |
| SNXX/USDT:USDT | below_1h_threshold | +1.37% | +1.82% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +0.73% | +1.19% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.72% | +1.17% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.71% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
