# Decision Report

- generated_at: 2026-06-11T11:06:21.844838+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6343**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=6343, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.11% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.85% | **+0.77%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.04% | **+0.02%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1271件 (Win 319 / Loss 401 / Flat 551) / skip 1633件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T11:06:19.432830+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63137.4
- Funnel: target 782 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +77.55% | $15,941,262.29 |
| VELVET/USDT:USDT | +76.60% | $78,402,839.05 |
| BEAT/USDT:USDT | +48.51% | $218,044,495.14 |
| COLLECT/USDT:USDT | +45.67% | $1,967,630.90 |
| AIO/USDT:USDT | +41.93% | $7,571,057.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +2.88% | +2.85% |
| VELVET/USDT:USDT | below_1h_threshold | +1.70% | +1.67% |
| ID/USDT:USDT | below_1h_threshold | +1.10% | +1.07% |
| BEAT/USDT:USDT | below_1h_threshold | +1.05% | +1.01% |
| COLLECT/USDT:USDT | below_1h_threshold | +0.99% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
