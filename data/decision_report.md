# Decision Report

- generated_at: 2026-09-23T02:11:20.660017+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15381**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=15381, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.54% | **+1.31%** |
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_BB3S | 7/14 | 50.0% | +2.02% | **+1.01%** |
| LIMIT_2PCT | 11/20 | 55.0% | +1.10% | **+0.61%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.96% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.68% | **+1.68%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.37% | **+0.71%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.53% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,173.21** / 初期 $100.00 (+1073.21%)
- 確定: 5859件 (Win 1731 / Loss 1880 / Flat 2248) / skip 6083件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FOLKS/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,173.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5439件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.56** / 初期 $100.00 (+22.56%)
- 確定: 3123件 (Win 919 / Loss 1225 / Flat 979) / pending 6件 / skip 3726件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000069 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNI/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.56

## 6. Latest Market Context

- 更新: 2026-09-23T02:11:09.672538+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=86276.7
- Funnel: target 1058 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHROOM/USDT:USDT | +67.67% | $1,068,405.25 |
| FOLKS/USDT:USDT | +33.13% | $5,870,904.09 |
| ALLO/USDT:USDT | +17.26% | $2,381,779.57 |
| DRIFT/USDT:USDT | +15.67% | $1,766,611.05 |
| UNI/USDT:USDT | +14.42% | $53,014,366.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SHROOM/USDT:USDT | below_1h_threshold | +3.59% | +3.65% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.83% | +2.89% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.76% | +2.81% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.65% | +1.71% |
| SAGA/USDT:USDT | below_1h_threshold | +1.43% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
