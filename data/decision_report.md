# Decision Report

- generated_at: 2026-09-28T04:41:34.777592+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15688**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.32% / filled 20/20。**
- 全期間 MARKET基準: n=15688, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.63% | **+0.54%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.32% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.86% | **+1.63%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.62% | **+0.50%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.48% | **+0.35%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,239.61** / 初期 $100.00 (+1139.61%)
- 確定: 5981件 (Win 1766 / Loss 1923 / Flat 2292) / skip 6268件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,239.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5565件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.81** / 初期 $100.00 (+19.81%)
- 確定: 3258件 (Win 951 / Loss 1281 / Flat 1026) / pending 4件 / skip 3898件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOONNETWORK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.81

## 6. Latest Market Context

- 更新: 2026-09-28T04:41:22.396203+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=83423.2
- Funnel: target 1069 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1, 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| QNT/USDT:USDT | +46.84% | $267,585,767.13 |
| BATON/USDT:USDT | +28.32% | $1,259,102.18 |
| ONE/USDT:USDT | +21.25% | $4,584,784.25 |
| GRT/USDT:USDT | +16.82% | $9,846,556.77 |
| SEI/USDT:USDT | +13.01% | $40,055,719.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRT/USDT:USDT | below_1h_threshold | +4.53% | +4.39% |
| RARE/USDT:USDT | below_1h_threshold | +3.97% | +3.83% |
| GRAM/USDT:USDT | below_1h_threshold | +2.55% | +2.40% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.04% | +1.90% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.00% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
