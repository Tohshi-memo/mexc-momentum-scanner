# Decision Report

- generated_at: 2026-09-10T16:36:32.343932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14171**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.57% / filled 20/20。**
- 全期間 MARKET基準: n=14171, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.57% | **+0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/18 | 16.7% | +6.33% | **+1.06%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.85% | **+0.93%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.02% | **+0.71%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.72% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +4.46% | **+4.46%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.82% | **+0.57%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.22% | **+0.19%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 207件 (TP 78 / SL 124 / EXP 5)
- 最新: HEMI/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,060.79** / 初期 $100.00 (+960.79%)
- 確定: 5351件 (Win 1609 / Loss 1728 / Flat 2014) / skip 5381件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,060.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.55** / 初期 $100.00 (+107.55%)
- 確定: 2765件 (Win 763 / Loss 649 / Flat 1353) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1121 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $207.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.17** / 初期 $100.00 (+22.17%)
- 確定: 2676件 (Win 789 / Loss 1022 / Flat 865) / pending 6件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000379 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.17

## 6. Latest Market Context

- 更新: 2026-09-10T16:36:19.286593+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.58% price=76770.3
- Funnel: target 1067 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +6.44% | $1,487,934.93 |
| NES/USDT:USDT | +5.48% | $1,776,799.10 |
| BTW/USDT:USDT | +2.70% | $1,505,163.30 |
| PONS/USDT:USDT | +2.35% | $8,649,677.10 |
| SOXS/USDT:USDT | +1.74% | $32,737,898.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.71% | +3.29% |
| PONS/USDT:USDT | below_1h_threshold | +2.31% | +2.90% |
| USOIL/USDT:USDT | below_1h_threshold | +1.88% | +2.46% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.77% | +2.35% |
| BULLA/USDT:USDT | below_1h_threshold | +1.19% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
