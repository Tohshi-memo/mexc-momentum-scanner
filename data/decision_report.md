# Decision Report

- generated_at: 2026-09-14T10:36:13.441361+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14511**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.12% / filled 20/20。**
- 全期間 MARKET基準: n=14511, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.12% | **+3.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.12% | **+3.12%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.26% | **+1.81%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.02% | **+1.41%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.51% | **+0.91%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.72% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.42%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.99% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | -0.15% | **-0.12%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | -0.36% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,057.73** / 初期 $100.00 (+957.73%)
- 確定: 5444件 (Win 1637 / Loss 1769 / Flat 2038) / skip 5628件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,057.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.62** / 初期 $100.00 (+127.62%)
- 確定: 2991件 (Win 830 / Loss 716 / Flat 1445) / skip 4931件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $227.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.76** / 初期 $100.00 (+25.76%)
- 確定: 2889件 (Win 859 / Loss 1119 / Flat 911) / pending 1件 / skip 3091件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.76

## 6. Latest Market Context

- 更新: 2026-09-14T10:36:04.515171+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=77902.0
- Funnel: target 1068 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +49.53% | $13,439,746.77 |
| AIN/USDT:USDT | +48.25% | $2,887,429.14 |
| CATE/USDT:USDT | +45.82% | $1,950,992.63 |
| MTL/USDT:USDT | +19.38% | $1,302,910.25 |
| MAGMA/USDT:USDT | +12.49% | $1,836,689.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.43% | +3.69% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.94% | +3.21% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.84% | +2.11% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.72% | +1.99% |
| CAKE/USDT:USDT | below_1h_threshold | +1.62% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
