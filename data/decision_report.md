# Decision Report

- generated_at: 2026-06-13T07:01:04.974984+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6562**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.46% / filled 20/20。**
- 全期間 MARKET基準: n=6562, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.46% | **+1.46%** |
| ASK | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.43% | **+0.36%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.11% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.16% | **-0.09%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.16% | **-0.14%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1435件 (Win 389 / Loss 464 / Flat 582) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VVV/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T07:01:01.698679+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63673.3
- Funnel: target 774 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +42.46% | $1,983,784.97 |
| EDGE/USDT:USDT | +25.30% | $2,491,196.76 |
| VVV/USDT:USDT | +19.50% | $5,546,362.22 |
| SKYAI/USDT:USDT | +14.64% | $16,191,642.07 |
| NOT/USDT:USDT | +11.74% | $1,167,711.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +0.90% | +0.96% |
| EDGE/USDT:USDT | below_1h_threshold | +0.61% | +0.67% |
| RIF/USDT:USDT | below_1h_threshold | +0.49% | +0.55% |
| NOT/USDT:USDT | below_1h_threshold | +0.43% | +0.49% |
| ASTER/USDT:USDT | below_1h_threshold | +0.23% | +0.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
