# Decision Report

- generated_at: 2026-09-21T04:31:15.533527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15229**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.34% / filled 20/20。**
- 全期間 MARKET基準: n=15229, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 17/20 | 85.0% | +1.94% | **+1.65%** |
| MARKET | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.76% | **+1.32%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.38% | **+1.31%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.09% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.59% | **+0.72%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.78% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +1.26% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.24** / 初期 $100.00 (+1075.24%)
- 確定: 5720件 (Win 1706 / Loss 1845 / Flat 2169) / skip 6070件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZAMA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,175.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.81** / 初期 $100.00 (+146.81%)
- 確定: 3297件 (Win 911 / Loss 765 / Flat 1621) / skip 5343件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $246.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.81** / 初期 $100.00 (+21.81%)
- 確定: 3007件 (Win 889 / Loss 1186 / Flat 932) / pending 4件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000162 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $121.81

## 6. Latest Market Context

- 更新: 2026-09-21T04:31:06.973664+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=81211.0
- Funnel: target 1050 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZETA/USDT:USDT | +69.41% | $1,029,490.95 |
| NIL/USDT:USDT | +22.20% | $5,632,395.66 |
| SEI/USDT:USDT | +15.95% | $15,444,303.88 |
| KMNO/USDT:USDT | +13.77% | $1,111,208.46 |
| EGLD/USDT:USDT | +13.23% | $2,393,836.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.05% | +2.28% |
| BTW/USDT:USDT | below_1h_threshold | +1.61% | +1.84% |
| SEI/USDT:USDT | below_1h_threshold | +1.38% | +1.62% |
| W/USDT:USDT | below_1h_threshold | +1.10% | +1.33% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.86% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
