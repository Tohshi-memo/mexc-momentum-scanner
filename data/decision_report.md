# Decision Report

- generated_at: 2026-09-10T19:41:37.557880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14182**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=14182, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_BB3S | 3/12 | 25.0% | +2.33% | **+0.58%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.56% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.75% | **+0.41%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.52% | **+0.39%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,047.61** / 初期 $100.00 (+947.61%)
- 確定: 5362件 (Win 1611 / Loss 1734 / Flat 2017) / skip 5381件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,047.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.08** / 初期 $100.00 (+108.08%)
- 確定: 2776件 (Win 767 / Loss 650 / Flat 1359) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0912 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定: 2687件 (Win 791 / Loss 1028 / Flat 868) / pending 4件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.62

## 6. Latest Market Context

- 更新: 2026-09-10T19:41:21.145654+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77207.4
- Funnel: target 1067 → liquid 175 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +35.28% | $2,372,094.51 |
| CNPY/USDT:USDT | +17.47% | $1,796,053.15 |
| BTW/USDT:USDT | +8.63% | $2,115,743.13 |
| EIGEN/USDT:USDT | +8.57% | $2,437,832.44 |
| SAGA/USDT:USDT | +7.90% | $4,147,874.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4STOCK/USDT:USDT | below_1h_threshold | +3.06% | +3.08% |
| SAGA/USDT:USDT | below_1h_threshold | +2.91% | +2.93% |
| RAVE/USDT:USDT | below_1h_threshold | +2.34% | +2.36% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.21% | +2.23% |
| EGLD/USDT:USDT | below_1h_threshold | +1.51% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
