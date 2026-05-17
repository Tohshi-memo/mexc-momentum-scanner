# Decision Report

- generated_at: 2026-05-17T02:43:25.514401+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4375**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.44% / filled 20/20。**
- 全期間 MARKET基準: n=4375, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.44% | **+1.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.44% | **+1.44%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_1PCT | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.80% | **+0.44%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.87% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.70% | **+0.42%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.73% | **+0.37%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.17** / 初期 $100.00 (-1.83%)
- 確定トレード: 48件 (TP 13 / SL 32 / EXP 3)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 543件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T02:43:22.242374+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77872.8
- Funnel: target 760 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +29.13% | $2,119,985.18 |
| LYN/USDT:USDT | +13.17% | $4,048,815.06 |
| BSB/USDT:USDT | +10.93% | $3,893,926.07 |
| CGPT/USDT:USDT | +7.46% | $1,358,143.51 |
| ASTEROID/USDT:USDT | +6.55% | $4,472,191.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_relative_strength | +5.17% | +4.93% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.89% | +2.65% |
| CGPT/USDT:USDT | below_1h_threshold | +2.15% | +1.91% |
| CFX/USDT:USDT | below_1h_threshold | +2.11% | +1.88% |
| H/USDT:USDT | below_1h_threshold | +2.00% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
