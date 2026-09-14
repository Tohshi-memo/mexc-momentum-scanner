# Decision Report

- generated_at: 2026-09-14T08:06:21.509085+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14503**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.02% / filled 20/20。**
- 全期間 MARKET基準: n=14503, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.99% | **+0.84%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.66% | **+0.75%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.59% | **+0.53%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.60% | **+1.62%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +2.11% | **+1.58%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.57% | **+1.25%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.50% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,077.97** / 初期 $100.00 (+977.97%)
- 確定: 5436件 (Win 1636 / Loss 1763 / Flat 2037) / skip 5628件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CVC/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,077.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4923件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.20** / 初期 $100.00 (+26.20%)
- 確定: 2884件 (Win 859 / Loss 1117 / Flat 908) / pending 4件 / skip 3087件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CVC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.20

## 6. Latest Market Context

- 更新: 2026-09-14T08:06:11.082197+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77728.2
- Funnel: target 1068 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +47.67% | $1,838,579.85 |
| AIN/USDT:USDT | +45.75% | $1,758,223.27 |
| BR/USDT:USDT | +36.03% | $5,874,658.77 |
| MTL/USDT:USDT | +31.85% | $1,393,652.66 |
| ARK/USDT:USDT | +26.20% | $4,316,533.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +1.85% | +2.01% |
| ARK/USDT:USDT | below_1h_threshold | +1.83% | +1.99% |
| PUNDIX/USDT:USDT | below_1h_threshold | +0.56% | +0.72% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.30% | +0.46% |
| 4/USDT:USDT | below_1h_threshold | +0.24% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
