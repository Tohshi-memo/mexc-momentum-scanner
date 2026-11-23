# Decision Report

- generated_at: 2026-11-23T00:01:16.432565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19407**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.45% / filled 20/20。**
- 全期間 MARKET基準: n=19407, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.45% | **+1.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.45% | **+1.45%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.22% | **+1.22%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.99%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.29% | **+0.82%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.13% | **+0.56%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,791.86** / 初期 $100.00 (+1691.86%)
- 確定: 7514件 (Win 2158 / Loss 2423 / Flat 2933) / skip 8454件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,791.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$461.51** / 初期 $100.00 (+361.51%)
- 確定: 5171件 (Win 1380 / Loss 1117 / Flat 2674) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0618 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $461.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7565件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T00:01:06.621334+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=61289.1
- Funnel: target 1086 → liquid 108 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +59.82% | $1,217,562.08 |
| BULLA/USDT:USDT | +28.00% | $1,968,825.16 |
| ARIA/USDT:USDT | +4.48% | $1,265,207.11 |
| SNXX/USDT:USDT | +4.13% | $1,221,835.28 |
| VVV/USDT:USDT | +3.88% | $6,566,519.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.18% | +2.10% |
| SOXL/USDT:USDT | below_1h_threshold | +1.79% | +1.71% |
| SNXX/USDT:USDT | below_1h_threshold | +1.61% | +1.52% |
| MUU/USDT:USDT | below_1h_threshold | +1.54% | +1.45% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.48% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
