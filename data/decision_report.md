# Decision Report

- generated_at: 2026-10-13T07:41:29.555798+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16633**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=16633, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 4/14 | 28.6% | +2.53% | **+0.72%** |
| LIMIT_10PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.14% | **-0.07%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.75% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.35% | **+1.17%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.91% | **+0.86%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.90% | **+0.72%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,285.29** / 初期 $100.00 (+1185.29%)
- 確定: 6294件 (Win 1845 / Loss 2017 / Flat 2432) / skip 6900件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,285.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$273.41** / 初期 $100.00 (+173.41%)
- 確定: 3649件 (Win 1014 / Loss 860 / Flat 1775) / skip 6395件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: OGN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $273.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4794件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000179 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-13T07:41:17.576834+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=83984.2
- Funnel: target 1089 → liquid 195 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAT/USDT:USDT | +21.31% | $10,633,397.83 |
| CT/USDT:USDT | +13.94% | $4,717,085.52 |
| OGN/USDT:USDT | +12.32% | $5,830,233.38 |
| SYN/USDT:USDT | +9.21% | $1,646,998.21 |
| LONGXIA/USDT:USDT | +9.16% | $1,505,037.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ATOM/USDT:USDT | below_1h_threshold | +2.69% | +2.39% |
| LSK/USDT:USDT | below_1h_threshold | +1.74% | +1.44% |
| STX/USDT:USDT | below_1h_threshold | +1.18% | +0.87% |
| CT/USDT:USDT | below_1h_threshold | +1.03% | +0.73% |
| SOXS/USDT:USDT | below_1h_threshold | +0.90% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
