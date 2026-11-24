# Decision Report

- generated_at: 2026-11-24T02:21:20.810385+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19548**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=19548, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 16/20 | 80.0% | +2.45% | **+1.96%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.87% | **+1.58%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.70% | **+1.10%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_3PCT | 5/20 | 25.0% | +2.92% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.61% | **+1.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.60% | **+1.43%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.41% | **+1.33%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.69% | **+0.92%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$2,020.57** / 初期 $100.00 (+1920.57%)
- 確定: 7587件 (Win 2185 / Loss 2434 / Flat 2968) / skip 8522件
- 成長率目線: 平均log +0.000396 / 幾何平均 +0.040% per trade / maxDD +9.04%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ELSA/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $2,020.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.69** / 初期 $100.00 (+367.69%)
- 確定: 5219件 (Win 1389 / Loss 1123 / Flat 2707) / skip 7740件
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

- 更新: 2026-11-24T02:21:10.880984+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.69% price=60640.4
- Funnel: target 1088 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +26.87% | $1,155,714.55 |
| NVD/USDT:USDT | +21.32% | $2,471,166.11 |
| ARIA/USDT:USDT | +18.20% | $9,855,582.24 |
| MMT/USDT:USDT | +14.49% | $2,685,758.25 |
| CYS/USDT:USDT | +13.17% | $3,714,223.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVD/USDT:USDT | below_1h_threshold | +4.46% | +5.16% |
| CYS/USDT:USDT | below_1h_threshold | +3.69% | +4.39% |
| SKDD/USDT:USDT | below_1h_threshold | +3.65% | +4.34% |
| LISTA/USDT:USDT | below_1h_threshold | +1.66% | +2.36% |
| SOXS/USDT:USDT | below_1h_threshold | +1.54% | +2.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
