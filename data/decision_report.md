# Decision Report

- generated_at: 2026-06-14T19:36:33.651952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6694**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6694, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.20% | **+0.90%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.87% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.57% | **-0.09%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.53% | **-0.27%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.58** / 初期 $100.00 (+71.58%)
- 確定: 1567件 (Win 417 / Loss 498 / Flat 652) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $171.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.57** / 初期 $100.00 (-1.43%)
- 確定: 72件 (Win 19 / Loss 15 / Flat 38) / skip 33件
- 成長率目線: 平均log -0.000200 / 幾何平均 -0.020% per trade / maxDD +2.07%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $98.57

## 5. Latest Market Context

- 更新: 2026-06-14T19:36:29.614708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=63786.3
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +20.59% | $6,889,269.35 |
| BABY/USDT:USDT | +9.20% | $1,275,221.01 |
| BANANAS31/USDT:USDT | +7.08% | $2,339,764.05 |
| BTW/USDT:USDT | +6.41% | $3,590,152.63 |
| CLO/USDT:USDT | +5.73% | $1,494,955.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BABY/USDT:USDT | below_1h_threshold | +3.95% | +3.95% |
| BTW/USDT:USDT | below_1h_threshold | +3.60% | +3.60% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.31% | +3.31% |
| H/USDT:USDT | below_1h_threshold | +3.16% | +3.15% |
| EVAA/USDT:USDT | below_1h_threshold | +2.94% | +2.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
