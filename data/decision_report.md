# Decision Report

- generated_at: 2026-11-25T22:16:32.955660+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19648**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19648, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.84% | **-1.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.02% | **+0.01%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.18% | **-0.14%** |
| LIMIT_BB3S | 2/19 | 10.5% | -2.31% | **-0.24%** |
| LIMIT_3PCT | 16/20 | 80.0% | -1.09% | **-0.87%** |
| LIMIT_ATR | 16/20 | 80.0% | -1.32% | **-1.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.65% | **+0.82%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.69% | **+0.67%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +1.63% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.31** / 初期 $100.00 (+1888.31%)
- 確定: 7612件 (Win 2191 / Loss 2450 / Flat 2971) / skip 8597件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,988.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7839件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7815件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000203 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-25T22:16:18.817910+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=60104.9
- Funnel: target 1097 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MANTRA/USDT:USDT | +33.70% | $3,447,479.17 |
| BULLA/USDT:USDT | +29.98% | $1,149,910.58 |
| SOXL/USDT:USDT | +22.83% | $1,887,143,838.61 |
| KOR/USDT:USDT | +18.82% | $1,834,706.47 |
| MVLL/USDT:USDT | +17.15% | $5,191,305.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +2.81% | +2.99% |
| NEAR/USDT:USDT | below_1h_threshold | +0.83% | +1.01% |
| USELESS/USDT:USDT | below_1h_threshold | +0.68% | +0.86% |
| MMT/USDT:USDT | below_1h_threshold | +0.62% | +0.80% |
| BEAT/USDT:USDT | below_1h_threshold | +0.57% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
