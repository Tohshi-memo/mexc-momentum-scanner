# Decision Report

- generated_at: 2026-07-12T15:01:08.120889+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8597**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.25% / filled 20/20。**
- 全期間 MARKET基準: n=8597, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.79% | **+2.65%** |
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.01% | **+0.65%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.29% | **+0.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.28% | **+0.17%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | -0.06% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$101.51** / 初期 $100.00 (+1.51%)
- 確定トレード: 88件 (TP 30 / SL 57 / EXP 1)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.42** / 初期 $100.00 (+221.42%)
- 確定: 2783件 (Win 875 / Loss 921 / Flat 987) / skip 2375件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $321.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 644件 (Win 152 / Loss 159 / Flat 333) / skip 1364件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 27件 (Win 9 / Loss 18 / Flat 0) / pending 0件 / skip 42件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000328 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.00

## 6. Latest Market Context

- 更新: 2026-07-12T15:01:01.829348+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64147.3
- Funnel: target 863 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +29.58% | $10,752,269.99 |
| DEXE/USDT:USDT | +25.50% | $11,927,284.28 |
| SXT/USDT:USDT | +21.14% | $25,683,282.35 |
| BILL/USDT:USDT | +18.38% | $4,345,552.13 |
| FHE/USDT:USDT | +18.33% | $2,471,901.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SXT/USDT:USDT | below_1h_threshold | +0.64% | +0.69% |
| HYPE/USDT:USDT | below_1h_threshold | +0.55% | +0.59% |
| VELVET/USDT:USDT | below_1h_threshold | +0.55% | +0.59% |
| B/USDT:USDT | below_1h_threshold | +0.53% | +0.58% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.47% | +0.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
