# Decision Report

- generated_at: 2026-06-25T18:18:12.029064+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7579**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.15% / filled 20/20。**
- 全期間 MARKET基準: n=7579, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+3.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.15% | **+3.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.15% | **+3.15%** |
| ASK | 20/20 | 100.0% | +2.98% | **+2.98%** |
| LIMIT_BB3S | 6/14 | 42.9% | +3.07% | **+1.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.00% | **-0.00%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | -1.44% | **-0.93%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 2008件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定: 370件 (Win 102 / Loss 100 / Flat 168) / skip 620件
- 成長率目線: 平均log +0.000196 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IDOL/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.51

## 5. Latest Market Context

- 更新: 2026-06-25T18:18:07.277315+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=59459.9
- Funnel: target 807 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +17.85% | $1,209,345.91 |
| HEI/USDT:USDT | +12.20% | $4,290,640.34 |
| EDEN/USDT:USDT | +8.06% | $1,113,758.77 |
| BEAT/USDT:USDT | +5.89% | $32,739,454.77 |
| VVV/USDT:USDT | +5.69% | $3,085,211.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.13% | +2.46% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.12% | +2.44% |
| HEI/USDT:USDT | below_1h_threshold | +1.94% | +2.26% |
| UB/USDT:USDT | below_1h_threshold | +1.53% | +1.86% |
| AIN/USDT:USDT | below_1h_threshold | +1.50% | +1.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
