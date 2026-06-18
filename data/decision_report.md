# Decision Report

- generated_at: 2026-06-18T16:33:49.617635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7059**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.22% / filled 20/20。**
- 全期間 MARKET基準: n=7059, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.22% | **+2.22%** |
| ASK | 20/20 | 100.0% | +1.87% | **+1.87%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.14% | **+1.71%** |
| LIMIT_BB3S | 6/20 | 30.0% | +4.45% | **+1.33%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.90% | **+0.45%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.11% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$100.46** / 初期 $100.00 (+0.46%)
- 確定トレード: 14件 (TP 5 / SL 9 / EXP 0)
- 最新: ALLO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.46
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$215.71** / 初期 $100.00 (+115.71%)
- 確定: 1882件 (Win 530 / Loss 601 / Flat 751) / skip 1738件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $215.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 162件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-18T16:33:40.025651+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=62563.6
- Funnel: target 795 → liquid 171 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +7.28% | $1,820,222.47 |
| ESPORTS/USDT:USDT | +6.79% | $50,705,718.48 |
| VELVET/USDT:USDT | +5.81% | $17,414,674.61 |
| TAC/USDT:USDT | +4.98% | $2,251,825.32 |
| GRASS/USDT:USDT | +4.52% | $1,352,357.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_relative_strength | +5.16% | +4.81% |
| GRASS/USDT:USDT | below_1h_threshold | +4.52% | +4.17% |
| AIOT/USDT:USDT | below_1h_threshold | +4.32% | +3.97% |
| BEAT/USDT:USDT | below_1h_threshold | +4.19% | +3.83% |
| H/USDT:USDT | below_1h_threshold | +3.50% | +3.14% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
