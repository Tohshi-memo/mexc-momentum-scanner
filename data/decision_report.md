# Decision Report

- generated_at: 2026-09-21T07:06:26.456755+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15235**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=15235, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.44% | **+1.01%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.57% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,169.37** / 初期 $100.00 (+1069.37%)
- 確定: 5726件 (Win 1706 / Loss 1846 / Flat 2174) / skip 6070件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,169.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.81** / 初期 $100.00 (+146.81%)
- 確定: 3298件 (Win 911 / Loss 765 / Flat 1622) / skip 5348件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $246.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.23** / 初期 $100.00 (+22.23%)
- 確定: 3013件 (Win 890 / Loss 1186 / Flat 937) / pending 4件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $122.23

## 6. Latest Market Context

- 更新: 2026-09-21T07:06:13.504071+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=81600.0
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +63.37% | $3,468,822.76 |
| NIL/USDT:USDT | +38.73% | $6,680,962.45 |
| PTB/USDT:USDT | +27.13% | $1,047,053.43 |
| AR/USDT:USDT | +18.89% | $7,240,077.74 |
| SEI/USDT:USDT | +18.12% | $17,733,629.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +3.22% | +3.23% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.54% | +2.55% |
| SAGA/USDT:USDT | below_1h_threshold | +1.92% | +1.93% |
| KORU/USDT:USDT | below_1h_threshold | +1.69% | +1.70% |
| SOXL/USDT:USDT | below_1h_threshold | +1.19% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
