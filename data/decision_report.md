# Decision Report

- generated_at: 2026-06-14T18:19:47.335297+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6693**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=6693, expectancy=-0.04%
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
| LIMIT_ATR | 11/20 | 55.0% | +2.06% | **+1.13%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

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
- 確定: 1566件 (Win 417 / Loss 498 / Flat 651) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.26% 残高後 $171.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.57** / 初期 $100.00 (-1.43%)
- 確定: 72件 (Win 19 / Loss 15 / Flat 38) / skip 32件
- 成長率目線: 平均log -0.000200 / 幾何平均 -0.020% per trade / maxDD +2.07%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $98.57

## 5. Latest Market Context

- 更新: 2026-06-14T18:19:43.319516+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63678.1
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +9.23% | $4,273,775.68 |
| BANANAS31/USDT:USDT | +6.75% | $2,151,277.32 |
| CLO/USDT:USDT | +6.73% | $1,447,432.48 |
| EDGE/USDT:USDT | +4.73% | $1,104,233.47 |
| BTW/USDT:USDT | +4.57% | $3,464,998.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.99% | +2.04% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.95% | +1.99% |
| BEAT/USDT:USDT | below_1h_threshold | +1.94% | +1.99% |
| JASMY/USDT:USDT | below_1h_threshold | +1.57% | +1.61% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.25% | +1.29% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
