# Decision Report

- generated_at: 2026-10-20T03:36:16.951527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17037**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=17037, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.78% | **+0.50%** |
| LIMIT_BB3S | 2/17 | 11.8% | +3.70% | **+0.43%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.75% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +5.13% | **+5.13%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.41% | **+1.19%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.44% | **+0.94%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.36% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,281.88** / 初期 $100.00 (+1181.88%)
- 確定: 6471件 (Win 1878 / Loss 2065 / Flat 2528) / skip 7127件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,281.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3797件 (Win 1044 / Loss 886 / Flat 1867) / skip 6651件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: S/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T03:36:05.280031+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=81964.5
- Funnel: target 1089 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +22.84% | $14,099,953.20 |
| LONGXIA/USDT:USDT | +12.14% | $1,323,869.38 |
| A/USDT:USDT | +11.33% | $23,127,771.85 |
| UNITREE/USDT:USDT | +9.54% | $2,567,156.93 |
| BTW/USDT:USDT | +9.32% | $29,221,811.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +4.80% | +4.56% |
| PHA/USDT:USDT | below_1h_threshold | +4.17% | +3.93% |
| AGT/USDT:USDT | below_1h_threshold | +1.16% | +0.91% |
| APE/USDT:USDT | below_1h_threshold | +1.03% | +0.78% |
| JTO/USDT:USDT | below_1h_threshold | +1.02% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
