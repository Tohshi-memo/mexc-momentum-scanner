# Decision Report

- generated_at: 2026-09-22T22:11:27.893814+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15368**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=15368, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.30% | **+1.11%** |
| LIMIT_BB3S | 8/14 | 57.1% | +1.61% | **+0.92%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.31% | **+0.92%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.53% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.95% | **+1.46%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.54% | **+1.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.69% | **+1.29%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,155.82** / 初期 $100.00 (+1055.82%)
- 確定: 5846件 (Win 1729 / Loss 1880 / Flat 2237) / skip 6083件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSEBOOK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,155.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5426件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.50** / 初期 $100.00 (+22.50%)
- 確定: 3117件 (Win 916 / Loss 1222 / Flat 979) / pending 3件 / skip 3724件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000145 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PYTH/USDT:USDT `MARKET` EXPIRED account +0.22% 残高後 $122.50

## 6. Latest Market Context

- 更新: 2026-09-22T22:11:14.767472+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=86030.5
- Funnel: target 1058 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MUSEBOOK/USDT:USDT | +37.50% | $1,027,863.55 |
| DRIFT/USDT:USDT | +21.86% | $1,597,742.65 |
| FOLKS/USDT:USDT | +21.74% | $2,062,488.22 |
| 4/USDT:USDT | +18.06% | $2,243,744.72 |
| USELESS/USDT:USDT | +15.99% | $10,349,989.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +1.97% | +2.10% |
| SAGA/USDT:USDT | below_1h_threshold | +1.78% | +1.91% |
| KERNEL/USDT:USDT | below_1h_threshold | +1.34% | +1.48% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.19% | +1.32% |
| TUT/USDT:USDT | below_1h_threshold | +0.82% | +0.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
