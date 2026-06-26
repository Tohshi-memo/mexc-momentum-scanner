# Decision Report

- generated_at: 2026-06-26T13:00:53.531813+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7629**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=7629, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_BB3S | 3/15 | 20.0% | +1.33% | **+0.27%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| ASK_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.85% | **-0.08%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.56** / 初期 $100.00 (+124.56%)
- 確定: 2155件 (Win 634 / Loss 715 / Flat 806) / skip 2035件
- 成長率目線: 平均log +0.000375 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $224.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 658件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T13:00:47.804819+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=59135.1
- Funnel: target 807 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +55.82% | $3,517,265.21 |
| ICNT/USDT:USDT | +50.09% | $2,596,777.98 |
| VELVET/USDT:USDT | +28.65% | $4,720,043.68 |
| HEI/USDT:USDT | +25.50% | $8,750,699.26 |
| AIN/USDT:USDT | +23.94% | $6,521,071.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +0.82% | +0.86% |
| ICNT/USDT:USDT | below_1h_threshold | +0.78% | +0.83% |
| G/USDT:USDT | below_1h_threshold | +0.62% | +0.67% |
| UB/USDT:USDT | below_1h_threshold | +0.60% | +0.65% |
| HEI/USDT:USDT | below_1h_threshold | +0.26% | +0.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
