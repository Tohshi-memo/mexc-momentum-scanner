# Decision Report

- generated_at: 2026-09-11T19:01:20.630439+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14247**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=14247, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.00% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.04% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.88% | **+3.92%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.35% | **+1.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.51% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,117.92** / 初期 $100.00 (+1017.92%)
- 確定: 5404件 (Win 1631 / Loss 1748 / Flat 2025) / skip 5404件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,117.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2819件 (Win 775 / Loss 655 / Flat 1389) / skip 4839件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.34** / 初期 $100.00 (+24.34%)
- 確定: 2739件 (Win 812 / Loss 1049 / Flat 878) / pending 5件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $124.34

## 6. Latest Market Context

- 更新: 2026-09-11T19:01:10.185157+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=77022.2
- Funnel: target 1067 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +27.06% | $6,632,219.24 |
| STORJ/USDT:USDT | +26.39% | $8,168,476.22 |
| BEAT/USDT:USDT | +15.47% | $8,545,384.40 |
| RIVER/USDT:USDT | +5.45% | $3,330,747.41 |
| HNT/USDT:USDT | +2.55% | $1,885,044.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +0.88% | +0.87% |
| USOIL/USDT:USDT | below_1h_threshold | +0.63% | +0.63% |
| NGAS/USDT:USDT | below_1h_threshold | +0.51% | +0.51% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.50% | +0.50% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.50% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
