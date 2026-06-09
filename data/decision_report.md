# Decision Report

- generated_at: 2026-06-09T04:06:05.090194+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6113**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.40% / filled 20/20。**
- 全期間 MARKET基準: n=6113, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.40% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 10件 (TP 1 / SL 8 / EXP 1)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.24** / 初期 $100.00 (+54.24%)
- 確定: 1153件 (Win 286 / Loss 353 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000376 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $154.24

## 4. Latest Market Context

- 更新: 2026-06-09T04:06:02.525296+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=62748.8
- Funnel: target 777 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +45.30% | $23,706,079.14 |
| CTR/USDT:USDT | +13.66% | $1,077,691.98 |
| SLX/USDT:USDT | +12.82% | $1,210,042.02 |
| MOVE/USDT:USDT | +8.12% | $5,456,012.44 |
| FOLKS/USDT:USDT | +7.04% | $1,482,127.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +2.32% | +2.47% |
| BANK/USDT:USDT | below_1h_threshold | +1.39% | +1.53% |
| SLX/USDT:USDT | below_1h_threshold | +1.17% | +1.32% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.01% | +1.16% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.79% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
