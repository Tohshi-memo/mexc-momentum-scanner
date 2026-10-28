# Decision Report

- generated_at: 2026-10-28T15:56:20.819099+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17725**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.80% / filled 20/20。**
- 全期間 MARKET基準: n=17725, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.38% | **+2.26%** |
| MARKET | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.29% | **+0.91%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.67% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.68%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,538.28** / 初期 $100.00 (+1438.28%)
- 確定: 6769件 (Win 1969 / Loss 2170 / Flat 2630) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HAEDAL/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,538.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$357.45** / 初期 $100.00 (+257.45%)
- 確定: 4246件 (Win 1152 / Loss 969 / Flat 2125) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0564 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HAEDAL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $357.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5886件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T15:56:07.549358+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=80497.9
- Funnel: target 1083 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +110.21% | $19,803,274.77 |
| SI/USDT:USDT | +47.28% | $2,081,410.26 |
| XAN/USDT:USDT | +39.33% | $1,887,028.98 |
| BLESS/USDT:USDT | +29.98% | $20,404,406.81 |
| ON/USDT:USDT | +19.75% | $1,064,874.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +3.34% | +3.43% |
| XPL/USDT:USDT | below_1h_threshold | +2.67% | +2.76% |
| PONS/USDT:USDT | below_1h_threshold | +2.56% | +2.65% |
| SI/USDT:USDT | below_1h_threshold | +1.77% | +1.86% |
| LAB/USDT:USDT | below_1h_threshold | +1.74% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
