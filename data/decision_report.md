# Decision Report

- generated_at: 2026-11-24T01:46:27.310593+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19547**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=19547, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +2.77% | **+2.36%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.29% | **+1.98%** |
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_3PCT | 6/20 | 30.0% | +3.76% | **+1.13%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.70% | **+1.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.96% | **+1.48%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.41% | **+1.32%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.38% | **+1.31%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.11% | **+1.16%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.34% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,020.57** / 初期 $100.00 (+1920.57%)
- 確定: 7587件 (Win 2185 / Loss 2434 / Flat 2968) / skip 8521件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $2,020.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7739件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $467.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7706件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T01:46:15.613427+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=61491.8
- Funnel: target 1088 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +47.37% | $1,111,745.05 |
| NVD/USDT:USDT | +18.91% | $2,464,718.70 |
| ARIA/USDT:USDT | +18.59% | $9,837,102.78 |
| LISTA/USDT:USDT | +13.66% | $1,042,194.16 |
| MMT/USDT:USDT | +13.08% | $2,645,349.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SUMIELECSTOCK/USDT:USDT | below_1h_threshold | +3.06% | +2.75% |
| ATOM/USDT:USDT | below_1h_threshold | +2.43% | +2.13% |
| MMT/USDT:USDT | below_1h_threshold | +1.79% | +1.48% |
| YAGEOSTOCK/USDT:USDT | below_1h_threshold | +1.70% | +1.40% |
| TQQQ/USDT:USDT | below_1h_threshold | +1.31% | +1.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
