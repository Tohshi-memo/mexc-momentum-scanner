# Decision Report

- generated_at: 2026-10-04T06:16:25.813971+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16094**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=16094, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.02% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_BB3S | 6/19 | 31.6% | +2.05% | **+0.65%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.40% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.64% | **+0.61%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |
| MARKET_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,286.81** / 初期 $100.00 (+1186.81%)
- 確定: 6156件 (Win 1813 / Loss 1973 / Flat 2370) / skip 6499件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_BB3S` SL_HIT account -0.50% 残高後 $1,286.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3608件 (Win 1005 / Loss 845 / Flat 1758) / skip 5897件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4257件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T06:16:14.695503+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=84877.8
- Funnel: target 1086 → liquid 136 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +50.99% | $5,367,070.35 |
| BATON/USDT:USDT | +24.93% | $1,222,786.86 |
| SPORTFUN/USDT:USDT | +20.68% | $1,730,209.90 |
| AXS/USDT:USDT | +17.19% | $4,271,862.90 |
| PHA/USDT:USDT | +11.63% | $1,179,180.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXS/USDT:USDT | below_1h_threshold | +2.95% | +2.94% |
| TIA/USDT:USDT | below_1h_threshold | +1.82% | +1.81% |
| GALA/USDT:USDT | below_1h_threshold | +1.01% | +1.00% |
| PONS/USDT:USDT | below_1h_threshold | +0.99% | +0.99% |
| MANA/USDT:USDT | below_1h_threshold | +0.71% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
