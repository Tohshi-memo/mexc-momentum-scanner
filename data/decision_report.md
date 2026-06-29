# Decision Report

- generated_at: 2026-06-29T19:01:00.512999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7832**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=7832, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.30% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.80% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| ASK_LONG | 20/20 | 100.0% | +0.02% | **+0.02%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定トレード: 43件 (TP 15 / SL 27 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.63
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$263.10** / 初期 $100.00 (+163.10%)
- 確定: 2336件 (Win 710 / Loss 777 / Flat 849) / skip 2057件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $263.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 786件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0336 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T19:00:55.797691+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=60233.3
- Funnel: target 811 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +12.65% | $4,682,373.68 |
| MYX/USDT:USDT | +8.82% | $2,527,082.95 |
| BILL/USDT:USDT | +8.13% | $1,517,341.02 |
| BAS/USDT:USDT | +6.68% | $2,038,330.72 |
| ACT/USDT:USDT | +6.25% | $4,438,552.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +0.68% | +0.75% |
| SYN/USDT:USDT | below_1h_threshold | +0.17% | +0.24% |
| ACT/USDT:USDT | below_1h_threshold | +0.16% | +0.23% |
| AGLD/USDT:USDT | below_1h_threshold | +0.14% | +0.21% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.13% | +0.20% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
