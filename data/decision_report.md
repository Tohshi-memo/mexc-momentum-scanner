# Decision Report

- generated_at: 2026-06-13T07:20:42.191445+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6563**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=6563, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.43% | **+0.36%** |
| ASK | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.11% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.22% | **+0.11%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.24% | **+0.11%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.06% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1436件 (Win 389 / Loss 464 / Flat 583) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T07:20:38.716474+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=63699.9
- Funnel: target 774 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +55.58% | $2,290,658.77 |
| EDGE/USDT:USDT | +21.60% | $2,569,504.88 |
| VVV/USDT:USDT | +16.08% | $5,900,725.47 |
| RIF/USDT:USDT | +11.37% | $1,593,516.39 |
| SQD/USDT:USDT | +11.09% | $1,299,153.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.50% | +3.51% |
| TAO/USDT:USDT | below_1h_threshold | +2.38% | +2.39% |
| OP/USDT:USDT | below_1h_threshold | +1.06% | +1.07% |
| APT/USDT:USDT | below_1h_threshold | +0.86% | +0.87% |
| JTO/USDT:USDT | below_1h_threshold | +0.85% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
