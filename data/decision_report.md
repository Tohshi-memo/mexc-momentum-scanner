# Decision Report

- generated_at: 2026-05-28T06:24:24.429644+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4954**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.89% / filled 20/20。**
- 全期間 MARKET基準: n=4954, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +3.86% | **+2.70%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.98% | **+2.53%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.62% | **+1.38%** |
| LIMIT_4PCT | 9/20 | 45.0% | +2.75% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +0.89% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.74% | **+1.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.53% | **+1.01%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.59% | **+0.78%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.47% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.12** / 初期 $100.00 (-1.88%)
- 確定トレード: 69件 (TP 20 / SL 46 / EXP 3)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.12
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 689件 (Win 172 / Loss 220 / Flat 297) / skip 826件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-28T06:24:22.298846+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=72882.0
- Funnel: target 777 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SNOWSTOCK/USDT:USDT | +34.98% | $7,747,320.24 |
| NBISSTOCK/USDT:USDT | +12.76% | $1,661,384.45 |
| GENIUS/USDT:USDT | +8.85% | $2,509,927.83 |
| BILL/USDT:USDT | +8.33% | $10,462,770.31 |
| NIGHT/USDT:USDT | +3.82% | $1,391,877.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +2.81% | +2.91% |
| DRAM/USDT:USDT | below_1h_threshold | +0.72% | +0.83% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.70% | +0.81% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.77% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.52% | +0.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
