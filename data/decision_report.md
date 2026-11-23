# Decision Report

- generated_at: 2026-11-23T02:41:37.728077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19411**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.13% / filled 20/20。**
- 全期間 MARKET基準: n=19411, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.13% | **+3.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.13% | **+3.13%** |
| LIMIT_1PCT | 14/20 | 70.0% | +2.60% | **+1.82%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_2PCT | 11/20 | 55.0% | +1.49% | **+0.82%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.73% | **+0.95%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.76% | **+0.46%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.47% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,791.86** / 初期 $100.00 (+1691.86%)
- 確定: 7514件 (Win 2158 / Loss 2423 / Flat 2933) / skip 8458件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,791.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$461.51** / 初期 $100.00 (+361.51%)
- 確定: 5175件 (Win 1380 / Loss 1117 / Flat 2678) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0617 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZHIPUSTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $461.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7573件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T02:41:16.038526+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=60659.4
- Funnel: target 1086 → liquid 114 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +46.61% | $1,459,177.03 |
| BULLA/USDT:USDT | +13.33% | $2,420,216.55 |
| ELSA/USDT:USDT | +7.39% | $1,449,169.88 |
| ZHIPUSTOCK/USDT:USDT | +4.79% | $2,327,120.91 |
| ENSO/USDT:USDT | +3.68% | $1,168,961.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UVXY/USDT:USDT | below_1h_threshold | +1.02% | +1.32% |
| ELSA/USDT:USDT | below_1h_threshold | +0.85% | +1.15% |
| ENSO/USDT:USDT | below_1h_threshold | +0.73% | +1.03% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.92% |
| SOXS/USDT:USDT | below_1h_threshold | +0.61% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
