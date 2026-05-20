# Decision Report

- generated_at: 2026-05-20T11:03:56.844277+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4540**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=4540, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +0.72% | **+0.54%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.90% | **+0.50%** |
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.48% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.38% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.39** / 初期 $100.00 (+24.39%)
- 確定: 502件 (Win 131 / Loss 173 / Flat 198) / skip 599件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $124.39

## 4. Latest Market Context

- 更新: 2026-05-20T11:03:54.822149+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77455.0
- Funnel: target 763 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +85.68% | $1,882,201.38 |
| FIDA/USDT:USDT | +32.81% | $2,947,281.18 |
| PROMPT/USDT:USDT | +30.00% | $12,667,927.72 |
| BANANAS31/USDT:USDT | +25.43% | $1,711,475.77 |
| EDEN/USDT:USDT | +24.57% | $22,157,892.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.64% | +1.66% |
| UP/USDT:USDT | below_1h_threshold | +0.96% | +0.98% |
| CHIP/USDT:USDT | below_1h_threshold | +0.93% | +0.95% |
| FIDA/USDT:USDT | below_1h_threshold | +0.76% | +0.79% |
| DASH/USDT:USDT | below_1h_threshold | +0.72% | +0.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
