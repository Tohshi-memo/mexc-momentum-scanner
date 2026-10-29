# Decision Report

- generated_at: 2026-10-29T09:16:27.706965+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17768**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.08% / filled 20/20。**
- 全期間 MARKET基準: n=17768, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +2.64% | **+1.45%** |
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.02% | **-0.01%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.48% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.31** / 初期 $100.00 (+1431.31%)
- 確定: 6802件 (Win 1975 / Loss 2179 / Flat 2648) / skip 7527件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,531.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$364.60** / 初期 $100.00 (+264.60%)
- 確定: 4289件 (Win 1161 / Loss 974 / Flat 2154) / skip 6890件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0105 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.02% 残高後 $364.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5926件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000349 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T09:16:14.869581+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=80179.9
- Funnel: target 1083 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +59.11% | $3,449,230.08 |
| BEAT/USDT:USDT | +13.30% | $8,207,688.42 |
| BULLA/USDT:USDT | +12.61% | $2,067,817.79 |
| INIT/USDT:USDT | +12.18% | $2,408,987.30 |
| ORCLSTOCK/USDT:USDT | +9.34% | $5,150,781.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +3.06% | +2.88% |
| INIT/USDT:USDT | below_1h_threshold | +1.93% | +1.74% |
| BTW/USDT:USDT | below_1h_threshold | +1.64% | +1.45% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +1.02% | +0.83% |
| UAI/USDT:USDT | below_1h_threshold | +1.01% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
