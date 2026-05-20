# Decision Report

- generated_at: 2026-05-20T16:08:50.267777+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4553**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=4553, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.23% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.73% | **+0.55%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.26% | **+0.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.09% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.72** / 初期 $100.00 (+23.72%)
- 確定: 515件 (Win 135 / Loss 175 / Flat 205) / skip 599件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $123.72

## 4. Latest Market Context

- 更新: 2026-05-20T16:08:47.945249+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77490.1
- Funnel: target 763 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +3.31% | $1,036,240.66 |
| EDEN/USDT:USDT | +3.25% | $25,579,399.62 |
| ZEST/USDT:USDT | +3.14% | $1,394,829.00 |
| BSB/USDT:USDT | +2.31% | $37,005,668.48 |
| PENGU/USDT:USDT | +1.91% | $28,424,436.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +3.61% | +3.52% |
| LYN/USDT:USDT | below_1h_threshold | +3.31% | +3.23% |
| ZEST/USDT:USDT | below_1h_threshold | +3.15% | +3.06% |
| BSB/USDT:USDT | below_1h_threshold | +2.39% | +2.31% |
| PENGU/USDT:USDT | below_1h_threshold | +1.91% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
