# Decision Report

- generated_at: 2026-05-17T23:13:32.826130+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4427**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=4427, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| ASK | 20/20 | 100.0% | +0.39% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.26% | **+0.89%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.05% | **+0.74%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.98% | **+0.68%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.66% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定: 424件 (Win 110 / Loss 143 / Flat 171) / skip 564件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $121.36

## 4. Latest Market Context

- 更新: 2026-05-17T23:13:30.814986+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=77828.9
- Funnel: target 761 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +38.91% | $3,987,849.99 |
| UB/USDT:USDT | +15.50% | $14,095,574.35 |
| BUILDONBOB/USDT:USDT | +11.24% | $1,307,032.24 |
| BILL/USDT:USDT | +7.67% | $34,168,369.69 |
| ZEC/USDT:USDT | +5.25% | $480,268,260.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +0.75% | +0.92% |
| BUILDONBOB/USDT:USDT | below_1h_threshold | +0.53% | +0.70% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.44% | +0.61% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.28% | +0.45% |
| RIVER/USDT:USDT | below_1h_threshold | +0.27% | +0.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
