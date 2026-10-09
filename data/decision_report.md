# Decision Report

- generated_at: 2026-10-09T08:56:29.193853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16417**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=16417, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +5.00% | **+4.00%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | -0.36% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,309.24** / 初期 $100.00 (+1209.24%)
- 確定: 6283件 (Win 1845 / Loss 2013 / Flat 2425) / skip 6695件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KAIA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,309.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3634件 (Win 1010 / Loss 853 / Flat 1771) / skip 6194件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0309 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4579件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000404 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-09T08:56:17.456293+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=82665.0
- Funnel: target 1084 → liquid 186 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.2 >= 65=1, 4h RSI 79.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +72.42% | $1,931,313.40 |
| JCT/USDT:USDT | +71.63% | $4,618,723.20 |
| BATON/USDT:USDT | +63.70% | $6,384,275.61 |
| RLC/USDT:USDT | +42.51% | $37,922,685.87 |
| KAIA/USDT:USDT | +33.88% | $1,516,600.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| W/USDT:USDT | below_1h_threshold | +4.40% | +4.35% |
| S/USDT:USDT | below_1h_threshold | +3.01% | +2.95% |
| SYRUP/USDT:USDT | below_1h_threshold | +2.54% | +2.48% |
| KAS/USDT:USDT | below_1h_threshold | +2.07% | +2.02% |
| LAB/USDT:USDT | below_1h_threshold | +1.80% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
