# Decision Report

- generated_at: 2026-08-08T21:11:16.994726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10884**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.90% / filled 20/20。**
- 全期間 MARKET基準: n=10884, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.60% | **+0.88%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.59% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.39% | **+0.63%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.60% | **+0.30%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.38% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$646.76** / 初期 $100.00 (+546.76%)
- 確定: 3885件 (Win 1224 / Loss 1265 / Flat 1396) / skip 3560件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COOKIE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $646.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2784件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0612 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.93** / 初期 $100.00 (+17.93%)
- 確定: 1243件 (Win 389 / Loss 477 / Flat 377) / pending 5件 / skip 1112件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000127 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $117.93

## 6. Latest Market Context

- 更新: 2026-08-08T21:11:09.177859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65034.9
- Funnel: target 961 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COOKIE/USDT:USDT | +23.51% | $1,962,958.91 |
| TUT/USDT:USDT | +13.81% | $17,638,973.21 |
| LIGHT/USDT:USDT | +13.35% | $1,518,105.36 |
| CATI/USDT:USDT | +11.34% | $2,152,573.57 |
| BTW/USDT:USDT | +10.23% | $15,909,229.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAI/USDT:USDT | below_1h_threshold | +2.68% | +2.70% |
| BEAT/USDT:USDT | below_1h_threshold | +1.61% | +1.63% |
| LIGHT/USDT:USDT | below_1h_threshold | +1.57% | +1.58% |
| US/USDT:USDT | below_1h_threshold | +0.96% | +0.98% |
| ACE/USDT:USDT | below_1h_threshold | +0.86% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
