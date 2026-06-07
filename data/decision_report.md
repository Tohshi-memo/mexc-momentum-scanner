# Decision Report

- generated_at: 2026-06-07T07:17:52.568719+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5930**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=5930, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +3.00% | **+1.00%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.49% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.89% | **+1.30%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.38** / 初期 $100.00 (+37.38%)
- 確定: 1049件 (Win 252 / Loss 323 / Flat 474) / skip 1442件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $137.38

## 4. Latest Market Context

- 更新: 2026-06-07T07:17:50.103547+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62088.9
- Funnel: target 771 → liquid 124 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +52.91% | $5,622,896.92 |
| LAB/USDT:USDT | +39.18% | $63,539,855.67 |
| EDEN/USDT:USDT | +29.89% | $2,050,367.39 |
| BSB/USDT:USDT | +25.73% | $5,499,924.55 |
| BLESS/USDT:USDT | +23.81% | $4,622,513.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +3.73% | +3.71% |
| H/USDT:USDT | below_1h_threshold | +2.04% | +2.02% |
| JTO/USDT:USDT | below_1h_threshold | +1.96% | +1.94% |
| VVV/USDT:USDT | below_1h_threshold | +1.91% | +1.90% |
| BTW/USDT:USDT | below_1h_threshold | +1.75% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
