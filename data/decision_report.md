# Decision Report

- generated_at: 2026-05-26T16:39:36.668046+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4905**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=4905, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| ASK | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.92% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.00% | **+3.00%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.75% | **+0.56%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +1.36% | **+0.41%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.17% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$129.22** / 初期 $100.00 (+29.22%)
- 確定: 677件 (Win 171 / Loss 215 / Flat 291) / skip 789件
- 成長率目線: 平均log +0.000379 / 幾何平均 +0.038% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUSTOCK/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $129.22

## 4. Latest Market Context

- 更新: 2026-05-26T16:39:31.313254+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=76644.9
- Funnel: target 769 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +11.58% | $6,420,223.12 |
| BILL/USDT:USDT | +7.03% | $14,607,933.07 |
| PHA/USDT:USDT | +4.16% | $5,874,960.01 |
| GRASS/USDT:USDT | +3.82% | $9,677,887.42 |
| FIDA/USDT:USDT | +2.92% | $1,060,285.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.84% | +3.62% |
| PHA/USDT:USDT | below_1h_threshold | +3.82% | +3.61% |
| FIDA/USDT:USDT | below_1h_threshold | +2.92% | +2.71% |
| UB/USDT:USDT | below_1h_threshold | +2.05% | +1.83% |
| ONDO/USDT:USDT | below_1h_threshold | +1.82% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
