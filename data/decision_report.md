# Decision Report

- generated_at: 2026-05-29T14:14:35.733449+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5052**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=5052, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.46% | **+0.44%** |
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +3.87% | **+1.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| ASK_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.77% | **+0.58%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$99.09** / 初期 $100.00 (-0.91%)
- 確定トレード: 73件 (TP 22 / SL 48 / EXP 3)
- 最新: NIL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 873件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T14:14:33.572693+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=72990.5
- Funnel: target 777 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +150.56% | $115,858,125.96 |
| HEI/USDT:USDT | +95.39% | $2,545,399.15 |
| ID/USDT:USDT | +38.64% | $2,532,910.87 |
| DELLSTOCK/USDT:USDT | +29.70% | $10,652,478.46 |
| LAB/USDT:USDT | +27.58% | $90,596,335.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.94% | +5.11% |
| LIT/USDT:USDT | below_1h_threshold | +4.15% | +4.32% |
| GUA/USDT:USDT | below_1h_threshold | +2.46% | +2.63% |
| ID/USDT:USDT | below_1h_threshold | +1.82% | +1.99% |
| INJ/USDT:USDT | below_1h_threshold | +1.44% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
