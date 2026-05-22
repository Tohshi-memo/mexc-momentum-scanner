# Decision Report

- generated_at: 2026-05-22T02:43:49.552185+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4659**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.85% / filled 20/20。**
- 全期間 MARKET基準: n=4659, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.85% | **+1.85%** |
| ASK | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.79% | **+1.26%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.03% | **+1.22%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.14% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.02% | **+0.02%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| ASK_LONG | 20/20 | 100.0% | -0.26% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 672件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T02:43:47.496879+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77609.3
- Funnel: target 766 → liquid 138 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEAR/USDT:USDT | +16.66% | $50,759,232.78 |
| GRASS/USDT:USDT | +15.72% | $3,570,257.07 |
| PEAQ/USDT:USDT | +13.37% | $1,928,451.13 |
| PLUME/USDT:USDT | +11.86% | $1,691,232.54 |
| BILL/USDT:USDT | +9.68% | $15,329,068.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEAR/USDT:USDT | below_1h_threshold | +4.46% | +4.42% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.35% | +4.32% |
| ICP/USDT:USDT | below_1h_threshold | +3.37% | +3.33% |
| NIL/USDT:USDT | below_1h_threshold | +3.25% | +3.22% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.85% | +2.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
