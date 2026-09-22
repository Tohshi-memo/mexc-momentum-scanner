# Decision Report

- generated_at: 2026-09-22T17:06:31.360055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15343**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=15343, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.50% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.19% | **+0.83%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.69% | **+0.48%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.63% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.50% | **+2.63%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.51% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.04% | **+0.04%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -3.05% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,167.58** / 初期 $100.00 (+1067.58%)
- 確定: 5829件 (Win 1727 / Loss 1875 / Flat 2227) / skip 6075件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CHR/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,167.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$249.51** / 初期 $100.00 (+149.51%)
- 確定: 3353件 (Win 926 / Loss 781 / Flat 1646) / skip 5401件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KERNEL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $249.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.76** / 初期 $100.00 (+22.76%)
- 確定: 3107件 (Win 912 / Loss 1217 / Flat 978) / pending 5件 / skip 3713件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000109 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $122.76

## 6. Latest Market Context

- 更新: 2026-09-22T17:06:18.924869+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=86481.8
- Funnel: target 1058 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CHR/USDT:USDT | +25.68% | $2,382,410.10 |
| MUBARAK/USDT:USDT | +20.43% | $10,295,703.04 |
| BR/USDT:USDT | +12.94% | $5,307,843.14 |
| ZRO/USDT:USDT | +10.59% | $3,873,719.57 |
| 4/USDT:USDT | +5.84% | $1,192,568.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHR/USDT:USDT | below_1h_threshold | +3.81% | +3.69% |
| 4/USDT:USDT | below_1h_threshold | +3.19% | +3.07% |
| USELESS/USDT:USDT | below_1h_threshold | +2.40% | +2.28% |
| DASH/USDT:USDT | below_1h_threshold | +1.83% | +1.71% |
| SNXX/USDT:USDT | below_1h_threshold | +1.64% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
