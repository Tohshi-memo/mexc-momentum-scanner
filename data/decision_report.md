# Decision Report

- generated_at: 2026-10-20T06:21:21.590720+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17044**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=17044, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.02% | **+1.82%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.43% | **+0.78%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.35% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.14% | **+3.14%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | -0.19% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,288.94** / 初期 $100.00 (+1188.94%)
- 確定: 6473件 (Win 1880 / Loss 2065 / Flat 2528) / skip 7132件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BAT/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.01% 残高後 $1,288.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3799件 (Win 1044 / Loss 886 / Flat 1869) / skip 6656件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5203件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000314 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T06:21:09.465486+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=81724.0
- Funnel: target 1090 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +28.36% | $16,352,494.32 |
| A/USDT:USDT | +12.45% | $23,149,140.85 |
| BR/USDT:USDT | +12.15% | $40,067,875.10 |
| SOXS/USDT:USDT | +9.79% | $4,082,660.92 |
| LONGXIA/USDT:USDT | +9.04% | $1,712,365.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +2.34% | +2.29% |
| TIA/USDT:USDT | below_1h_threshold | +2.30% | +2.25% |
| PHA/USDT:USDT | below_1h_threshold | +2.01% | +1.96% |
| SOXS/USDT:USDT | below_1h_threshold | +1.12% | +1.07% |
| BAT/USDT:USDT | below_1h_threshold | +0.78% | +0.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
