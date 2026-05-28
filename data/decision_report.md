# Decision Report

- generated_at: 2026-05-28T09:39:35.013008+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4958**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=4958, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.53% | **+2.03%** |
| LIMIT_3PCT | 13/20 | 65.0% | +2.60% | **+1.69%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.38% | **+1.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.23% | **+0.63%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.53% | **+0.63%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.18% | **+0.41%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +0.46% | **+0.20%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.43% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定トレード: 69件 (TP 20 / SL 46 / EXP 3)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 693件 (Win 172 / Loss 220 / Flat 301) / skip 826件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T09:39:32.883880+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=73414.3
- Funnel: target 777 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.04% | $8,586,684.31 |
| ONDSSTOCK/USDT:USDT | +14.13% | $1,056,170.20 |
| NBISSTOCK/USDT:USDT | +13.40% | $1,861,450.93 |
| PRL/USDT:USDT | +9.58% | $1,359,469.96 |
| BILL/USDT:USDT | +8.50% | $11,384,406.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +2.32% | +2.15% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.10% | +1.94% |
| XLM/USDT:USDT | below_1h_threshold | +1.34% | +1.17% |
| ONDSSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +1.03% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.16% | +1.00% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
