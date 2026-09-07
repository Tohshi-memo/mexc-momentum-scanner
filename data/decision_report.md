# Decision Report

- generated_at: 2026-09-07T18:36:16.406842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13900**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=13900, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_ATR | 4/20 | 20.0% | +1.96% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.16% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.01% | **+0.50%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.48% | **+0.29%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.29% | **+0.26%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$873.91** / 初期 $100.00 (+773.91%)
- 確定: 5173件 (Win 1546 / Loss 1683 / Flat 1944) / skip 5288件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $873.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4740件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.01** / 初期 $100.00 (+20.01%)
- 確定: 2491件 (Win 733 / Loss 938 / Flat 820) / pending 2件 / skip 2876件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $120.01

## 6. Latest Market Context

- 更新: 2026-09-07T18:36:06.454743+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=79097.9
- Funnel: target 1062 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +22.15% | $5,708,979.99 |
| BASECAT/USDT:USDT | +9.69% | $1,093,026.39 |
| UAI/USDT:USDT | +7.70% | $18,467,570.81 |
| AERO/USDT:USDT | +5.81% | $1,234,628.78 |
| IOST/USDT:USDT | +5.15% | $2,087,160.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AERO/USDT:USDT | below_1h_threshold | +2.64% | +2.71% |
| INJ/USDT:USDT | below_1h_threshold | +2.33% | +2.40% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.38% | +1.45% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.33% | +1.40% |
| EGLD/USDT:USDT | below_1h_threshold | +0.90% | +0.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
