# Decision Report

- generated_at: 2026-10-29T08:36:21.385053+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17765**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.68% / filled 20/20。**
- 全期間 MARKET基準: n=17765, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.68% | **+2.68%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.76% | **+1.50%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.98% | **+0.69%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.98% | **-0.44%** |
| LIMIT_FIB1618_LONG | 10/20 | 50.0% | -1.04% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,531.31** / 初期 $100.00 (+1431.31%)
- 確定: 6802件 (Win 1975 / Loss 2179 / Flat 2648) / skip 7524件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IDOL/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,531.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$365.08** / 初期 $100.00 (+265.08%)
- 確定: 4286件 (Win 1160 / Loss 972 / Flat 2154) / skip 6890件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0252 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $365.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5923件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000415 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-29T08:36:08.525479+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80015.1
- Funnel: target 1083 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +57.07% | $3,348,237.07 |
| BEAT/USDT:USDT | +13.94% | $8,285,847.89 |
| BULLA/USDT:USDT | +13.13% | $2,213,474.90 |
| ORCLSTOCK/USDT:USDT | +8.42% | $5,132,526.19 |
| UAI/USDT:USDT | +7.27% | $1,507,593.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.43% | +4.19% |
| BULLA/USDT:USDT | below_1h_threshold | +4.30% | +4.06% |
| UAI/USDT:USDT | below_1h_threshold | +2.66% | +2.42% |
| BEAT/USDT:USDT | below_1h_threshold | +2.54% | +2.31% |
| IDOL/USDT:USDT | below_1h_threshold | +1.37% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
