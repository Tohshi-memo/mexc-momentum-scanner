# Decision Report

- generated_at: 2026-11-25T06:26:15.923370+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19596**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.93% / filled 20/20。**
- 全期間 MARKET基準: n=19596, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.51% | **+2.13%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.29% | **+1.60%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.54% | **+1.01%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.11% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.34% | **-0.08%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | -0.17% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.31** / 初期 $100.00 (+1888.31%)
- 確定: 7610件 (Win 2191 / Loss 2450 / Flat 2969) / skip 8547件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.06% 残高後 $1,988.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7787件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7757件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000350 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-25T06:26:04.903767+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=59122.0
- Funnel: target 1092 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIGTIME/USDT:USDT | +70.17% | $1,733,608.38 |
| OPG/USDT:USDT | +27.99% | $2,047,216.54 |
| BTW/USDT:USDT | +15.20% | $4,951,385.98 |
| GUA/USDT:USDT | +12.89% | $2,127,923.25 |
| ANSEM/USDT:USDT | +10.29% | $1,432,860.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +1.65% | +1.67% |
| SOXS/USDT:USDT | below_1h_threshold | +1.62% | +1.64% |
| AIOT/USDT:USDT | below_1h_threshold | +1.60% | +1.63% |
| XPL/USDT:USDT | below_1h_threshold | +1.01% | +1.03% |
| PEPE/USDT:USDT | below_1h_threshold | +0.89% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
