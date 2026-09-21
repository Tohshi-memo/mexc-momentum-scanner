# Decision Report

- generated_at: 2026-09-21T02:11:18.069000+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15225**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.43% / filled 20/20。**
- 全期間 MARKET基準: n=15225, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.16% | **+1.05%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.35% | **+0.81%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.91% | **+0.73%** |
| MARKET | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.20% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.78% | **+0.62%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.07% | **+0.53%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.43% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.24** / 初期 $100.00 (+1075.24%)
- 確定: 5718件 (Win 1706 / Loss 1845 / Flat 2167) / skip 6068件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.14% 残高後 $1,175.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.81** / 初期 $100.00 (+146.81%)
- 確定: 3297件 (Win 911 / Loss 765 / Flat 1621) / skip 5339件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0025 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $246.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.02** / 初期 $100.00 (+22.02%)
- 確定: 3004件 (Win 889 / Loss 1185 / Flat 930) / pending 4件 / skip 3689件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.04% 残高後 $122.02

## 6. Latest Market Context

- 更新: 2026-09-21T02:11:09.595298+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=81267.9
- Funnel: target 1050 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIL/USDT:USDT | +26.01% | $5,245,334.22 |
| SEI/USDT:USDT | +13.49% | $15,447,662.82 |
| LUNANEW/USDT:USDT | +13.14% | $2,454,855.10 |
| JUP/USDT:USDT | +11.59% | $4,482,256.87 |
| B2/USDT:USDT | +11.45% | $1,700,449.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.44% | +2.07% |
| XMR/USDT:USDT | below_1h_threshold | +1.43% | +1.05% |
| BTW/USDT:USDT | below_1h_threshold | +1.09% | +0.72% |
| VVV/USDT:USDT | below_1h_threshold | +1.06% | +0.68% |
| STRK/USDT:USDT | below_1h_threshold | +0.91% | +0.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
