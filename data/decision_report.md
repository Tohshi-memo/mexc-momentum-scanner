# Decision Report

- generated_at: 2026-10-20T05:01:15.436145+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17040**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=17040, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.25% | **+1.12%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.01% | **+0.60%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.35% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.62% | **+3.62%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.65% | **+0.55%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.67% | **+0.47%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.67% | **+0.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.13% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,288.94** / 初期 $100.00 (+1188.94%)
- 確定: 6473件 (Win 1880 / Loss 2065 / Flat 2528) / skip 7128件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BAT/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.01% 残高後 $1,288.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.39** / 初期 $100.00 (+178.39%)
- 確定: 3797件 (Win 1044 / Loss 886 / Flat 1867) / skip 6654件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: S/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $278.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5199件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000303 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T05:01:06.416731+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=82050.0
- Funnel: target 1090 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +24.37% | $15,241,601.08 |
| LONGXIA/USDT:USDT | +19.41% | $1,507,616.72 |
| A/USDT:USDT | +11.72% | $23,116,736.41 |
| APR/USDT:USDT | +9.79% | $1,279,839.90 |
| SOXS/USDT:USDT | +9.51% | $3,966,575.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.41% | +1.43% |
| PHA/USDT:USDT | below_1h_threshold | +1.10% | +1.11% |
| FASTRETAILSTOCK/USDT:USDT | below_1h_threshold | +0.83% | +0.84% |
| A/USDT:USDT | below_1h_threshold | +0.69% | +0.70% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.48% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
