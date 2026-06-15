# Decision Report

- generated_at: 2026-06-15T15:58:05.483571+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6793**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=6793, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.20% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +0.76% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$176.39** / 初期 $100.00 (+76.39%)
- 確定: 1666件 (Win 434 / Loss 517 / Flat 715) / skip 1688件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $176.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.82** / 初期 $100.00 (-2.18%)
- 確定: 154件 (Win 28 / Loss 29 / Flat 97) / skip 50件
- 成長率目線: 平均log -0.000143 / 幾何平均 -0.014% per trade / maxDD +2.82%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $97.82

## 5. Latest Market Context

- 更新: 2026-06-15T15:58:00.739830+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.97% price=67199.0
- Funnel: target 772 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +89.28% | $39,357,622.42 |
| ASTEROID/USDT:USDT | +73.25% | $5,933,393.33 |
| JTO/USDT:USDT | +47.62% | $7,529,064.14 |
| CLO/USDT:USDT | +35.13% | $2,260,776.13 |
| GRASS/USDT:USDT | +28.59% | $3,261,511.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_relative_strength | +5.92% | +4.95% |
| GRASS/USDT:USDT | below_1h_threshold | +4.53% | +3.55% |
| JTO/USDT:USDT | below_1h_threshold | +3.73% | +2.76% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.65% | +1.68% |
| SOXL/USDT:USDT | below_1h_threshold | +2.11% | +1.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
