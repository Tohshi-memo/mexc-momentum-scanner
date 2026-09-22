# Decision Report

- generated_at: 2026-09-22T01:01:18.181505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15285**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=15285, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.46% | **+1.46%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S | 10/16 | 62.5% | +1.39% | **+0.87%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.09% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.68% | **+0.27%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.22% | **+0.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.34% | **+0.13%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,177.26** / 初期 $100.00 (+1077.26%)
- 確定: 5776件 (Win 1718 / Loss 1857 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account -0.11% 残高後 $1,177.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.78** / 初期 $100.00 (+148.78%)
- 確定: 3324件 (Win 918 / Loss 768 / Flat 1638) / skip 5372件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0390 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $248.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.78** / 初期 $100.00 (+22.78%)
- 確定: 3057件 (Win 899 / Loss 1195 / Flat 963) / pending 3件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000211 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.78

## 6. Latest Market Context

- 更新: 2026-09-22T01:01:07.299747+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=85935.1
- Funnel: target 1055 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +26.19% | $8,806,467.98 |
| ALCH/USDT:USDT | +24.84% | $2,262,359.70 |
| EVAA/USDT:USDT | +20.02% | $2,156,878.08 |
| PTB/USDT:USDT | +15.95% | $1,198,222.59 |
| GRASS/USDT:USDT | +11.62% | $2,218,956.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +1.56% |
| SNXX/USDT:USDT | below_1h_threshold | +1.30% | +1.22% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.29% | +1.21% |
| SOXL/USDT:USDT | below_1h_threshold | +1.25% | +1.16% |
| ONE/USDT:USDT | below_1h_threshold | +1.20% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
