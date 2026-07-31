# Decision Report

- generated_at: 2026-07-31T10:01:20.811974+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9985**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=9985, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/12 | 41.7% | +2.53% | **+1.05%** |
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.07% | **+0.32%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.56% | **+1.83%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.39% | **+1.18%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.88% | **+0.39%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.23% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$547.70** / 初期 $100.00 (+447.70%)
- 確定: 3573件 (Win 1141 / Loss 1168 / Flat 1264) / skip 2973件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $547.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.30** / 初期 $100.00 (+41.30%)
- 確定: 1276件 (Win 359 / Loss 296 / Flat 621) / skip 2120件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0804 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $141.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.22** / 初期 $100.00 (+11.22%)
- 確定: 818件 (Win 267 / Loss 325 / Flat 226) / pending 4件 / skip 634件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $111.22

## 6. Latest Market Context

- 更新: 2026-07-31T10:01:12.329372+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63658.5
- Funnel: target 921 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +61.76% | $11,970,928.99 |
| MMT/USDT:USDT | +44.89% | $13,666,167.25 |
| GIGGLE/USDT:USDT | +33.80% | $8,017,881.61 |
| AXTISTOCK/USDT:USDT | +32.32% | $4,963,839.95 |
| AMZU/USDT:USDT | +22.23% | $1,634,327.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +1.19% | +1.24% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.00% | +1.05% |
| RLC/USDT:USDT | below_1h_threshold | +0.84% | +0.89% |
| AMZU/USDT:USDT | below_1h_threshold | +0.79% | +0.84% |
| DEXE/USDT:USDT | below_1h_threshold | +0.72% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
