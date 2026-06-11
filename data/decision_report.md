# Decision Report

- generated_at: 2026-06-11T02:07:14.158137+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6292**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=6292, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +2.10% | **+2.10%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.01% | **+1.51%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.43% | **+1.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.93% | **+0.29%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.19% | **+0.16%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | -0.89% | **-0.18%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | -0.21% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1583件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T02:07:11.651699+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=62155.3
- Funnel: target 785 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +94.05% | $46,832,204.78 |
| AIO/USDT:USDT | +71.75% | $1,614,975.20 |
| BEAT/USDT:USDT | +29.25% | $189,241,578.07 |
| FIGHT/USDT:USDT | +18.76% | $1,091,860.72 |
| FOLKS/USDT:USDT | +15.85% | $13,264,726.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +1.92% | +1.96% |
| BSB/USDT:USDT | below_1h_threshold | +1.84% | +1.87% |
| RIVER/USDT:USDT | below_1h_threshold | +1.33% | +1.37% |
| HOME/USDT:USDT | below_1h_threshold | +1.03% | +1.06% |
| BEAT/USDT:USDT | below_1h_threshold | +0.86% | +0.90% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
