# Decision Report

- generated_at: 2026-09-29T11:46:30.568695+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15761**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=15761, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/17 | 35.3% | +2.81% | **+0.99%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.80% | **+0.42%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.33% | **+0.26%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +6.32% | **+4.22%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.83% | **+0.58%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.89% | **+0.44%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.46% | **+0.27%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.41% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5985件 (Win 1766 / Loss 1925 / Flat 2294) / skip 6337件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5638件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3924件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T11:46:18.988096+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=84240.2
- Funnel: target 1067 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +37.10% | $16,600,483.62 |
| 0G/USDT:USDT | +28.11% | $2,087,788.59 |
| GRASS/USDT:USDT | +26.79% | $8,204,791.57 |
| CRV/USDT:USDT | +19.15% | $19,006,314.95 |
| SYRUP/USDT:USDT | +18.34% | $2,877,214.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 0G/USDT:USDT | below_1h_threshold | +4.46% | +4.15% |
| XLM/USDT:USDT | below_1h_threshold | +2.94% | +2.63% |
| XPL/USDT:USDT | below_1h_threshold | +2.71% | +2.40% |
| ARB/USDT:USDT | below_1h_threshold | +2.67% | +2.37% |
| AAVE/USDT:USDT | below_1h_threshold | +2.45% | +2.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
