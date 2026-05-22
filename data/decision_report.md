# Decision Report

- generated_at: 2026-05-22T04:33:52.268484+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4664**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.37% / filled 20/20。**
- 全期間 MARKET基準: n=4664, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+2.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.37% | **+2.37%** |
| ASK | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.72% | **+1.37%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_3PCT | 11/20 | 55.0% | +2.42% | **+1.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +1.63% | **+0.65%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.01% | **+0.01%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.35% | **-0.33%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 677件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T04:33:49.681606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77757.1
- Funnel: target 766 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +82.18% | $1,269,798.85 |
| PLAY/USDT:USDT | +20.18% | $3,630,919.84 |
| NEAR/USDT:USDT | +19.21% | $59,207,826.80 |
| GRASS/USDT:USDT | +17.78% | $3,882,915.73 |
| PEAQ/USDT:USDT | +11.24% | $1,967,069.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +3.46% | +3.44% |
| GRASS/USDT:USDT | below_1h_threshold | +2.81% | +2.79% |
| PLAY/USDT:USDT | below_1h_threshold | +2.58% | +2.56% |
| RENDER/USDT:USDT | below_1h_threshold | +1.72% | +1.70% |
| NEAR/USDT:USDT | below_1h_threshold | +1.65% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
