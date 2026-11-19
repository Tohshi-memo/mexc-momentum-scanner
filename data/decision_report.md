# Decision Report

- generated_at: 2026-11-19T01:06:21.740866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19168**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=19168, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.88% | **+1.69%** |
| LIMIT_BB3S | 7/17 | 41.2% | +2.66% | **+1.10%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.00% | **+0.70%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.55% | **+1.04%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.03% | **+0.61%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,728.05** / 初期 $100.00 (+1628.05%)
- 確定: 7359件 (Win 2113 / Loss 2360 / Flat 2886) / skip 8370件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,728.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5019件 (Win 1335 / Loss 1087 / Flat 2597) / skip 7560件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0469 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7330件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T01:06:10.598055+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63229.9
- Funnel: target 1079 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +25.66% | $3,794,356.01 |
| IRYS/USDT:USDT | +20.86% | $4,983,645.94 |
| PHAROS/USDT:USDT | +19.25% | $1,810,572.53 |
| HUMA/USDT:USDT | +17.99% | $2,393,069.91 |
| LUNC/USDT:USDT | +13.53% | $1,565,289.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CSOPSKHYNIX2L/USDT:USDT | below_1h_threshold | +4.39% | +4.28% |
| KORU/USDT:USDT | below_1h_threshold | +3.99% | +3.88% |
| HUMA/USDT:USDT | below_1h_threshold | +3.30% | +3.19% |
| PHAROS/USDT:USDT | below_1h_threshold | +2.94% | +2.83% |
| SOXL/USDT:USDT | below_1h_threshold | +2.63% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
