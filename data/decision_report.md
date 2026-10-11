# Decision Report

- generated_at: 2026-10-11T04:56:27.950200+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16534**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.70% / filled 20/20。**
- 全期間 MARKET基準: n=16534, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/12 | 33.3% | +6.75% | **+2.25%** |
| MARKET | 20/20 | 100.0% | +1.70% | **+1.70%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.45% | **+1.31%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +1.76% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.14% | **+0.13%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.10% | **+0.07%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.38% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6288件 (Win 1845 / Loss 2015 / Flat 2428) / skip 6807件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$273.08** / 初期 $100.00 (+173.08%)
- 確定: 3637件 (Win 1010 / Loss 854 / Flat 1773) / skip 6308件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $273.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4697件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-11T04:56:12.847203+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=82981.2
- Funnel: target 1087 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +34.07% | $6,056,766.21 |
| CHIP/USDT:USDT | +21.82% | $34,993,216.29 |
| TIA/USDT:USDT | +17.83% | $84,477,687.21 |
| STRK/USDT:USDT | +15.83% | $83,256,090.33 |
| SI/USDT:USDT | +15.48% | $1,905,902.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +4.58% | +4.33% |
| BTW/USDT:USDT | below_1h_threshold | +4.30% | +4.05% |
| BAT/USDT:USDT | below_1h_threshold | +4.14% | +3.90% |
| WLD/USDT:USDT | below_1h_threshold | +3.71% | +3.46% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.67% | +3.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
