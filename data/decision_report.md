# Decision Report

- generated_at: 2026-05-22T16:52:49.526236+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4719**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4719, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +1.41% | **+0.85%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.07% | **+0.62%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.61% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.23%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.25% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.82** / 初期 $100.00 (+21.82%)
- 確定: 566件 (Win 145 / Loss 187 / Flat 234) / skip 714件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $121.82

## 4. Latest Market Context

- 更新: 2026-05-22T16:52:47.773026+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=76950.8
- Funnel: target 768 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +15.74% | $27,263,027.89 |
| ICP/USDT:USDT | +3.08% | $14,842,657.01 |
| PEAQ/USDT:USDT | +3.08% | $1,310,884.28 |
| GUA/USDT:USDT | +2.92% | $1,041,406.98 |
| GENIUS/USDT:USDT | +2.60% | $5,232,000.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICP/USDT:USDT | below_1h_threshold | +3.09% | +2.84% |
| PEAQ/USDT:USDT | below_1h_threshold | +3.08% | +2.83% |
| GUA/USDT:USDT | below_1h_threshold | +2.92% | +2.67% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.60% | +2.35% |
| USELESS/USDT:USDT | below_1h_threshold | +2.44% | +2.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
