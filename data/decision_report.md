# Decision Report

- generated_at: 2026-11-23T03:46:14.540946+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19414**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.15% / filled 20/20。**
- 全期間 MARKET基準: n=19414, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.15% | **+3.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.15% | **+3.15%** |
| LIMIT_1PCT | 13/20 | 65.0% | +3.06% | **+1.99%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_2PCT | 10/20 | 50.0% | +1.08% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_5PCT_LONG | 15/20 | 75.0% | +0.34% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 285件 (TP 103 / SL 174 / EXP 8)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,791.86** / 初期 $100.00 (+1691.86%)
- 確定: 7514件 (Win 2158 / Loss 2423 / Flat 2933) / skip 8461件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MMT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,791.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$461.51** / 初期 $100.00 (+361.51%)
- 確定: 5178件 (Win 1380 / Loss 1117 / Flat 2681) / skip 7647件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0573 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ELSA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $461.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7576件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-23T03:46:03.368945+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.08% price=61239.7
- Funnel: target 1086 → liquid 115 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +51.41% | $1,489,537.29 |
| ELSA/USDT:USDT | +18.49% | $1,557,391.78 |
| BULLA/USDT:USDT | +13.44% | $2,478,138.74 |
| ZHIPUSTOCK/USDT:USDT | +12.17% | $3,085,684.97 |
| IDOL/USDT:USDT | +5.83% | $2,521,525.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.44% | +3.37% |
| SI/USDT:USDT | below_1h_threshold | +4.02% | +2.95% |
| JUP/USDT:USDT | below_1h_threshold | +3.31% | +2.23% |
| ETC/USDT:USDT | below_1h_threshold | +2.68% | +1.60% |
| ARIA/USDT:USDT | below_1h_threshold | +2.46% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
