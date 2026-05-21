# Decision Report

- generated_at: 2026-05-21T17:44:00.611906+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4652**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=4652, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| ASK | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.36% | **+0.31%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.20% | **-0.17%** |
| MARKET_LONG | 20/20 | 100.0% | -0.24% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 547件 (Win 138 / Loss 185 / Flat 224) / skip 666件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPOTSTOCK/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T17:43:58.517191+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.88% price=77841.1
- Funnel: target 763 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GRASS/USDT:USDT | +7.85% | $1,264,556.79 |
| BABY/USDT:USDT | +5.20% | $1,240,868.97 |
| INJ/USDT:USDT | +4.75% | $24,820,376.15 |
| VVV/USDT:USDT | +4.51% | $10,459,773.13 |
| RIVER/USDT:USDT | +3.77% | $4,095,227.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_relative_strength | +5.27% | +4.40% |
| SPX/USDT:USDT | below_1h_threshold | +4.33% | +3.46% |
| INJ/USDT:USDT | below_1h_threshold | +4.18% | +3.30% |
| GRASS/USDT:USDT | below_1h_threshold | +3.70% | +2.82% |
| JTO/USDT:USDT | below_1h_threshold | +3.58% | +2.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
