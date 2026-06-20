# Decision Report

- generated_at: 2026-06-20T13:42:46.658113+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7245**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=7245, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +2.78% | **+2.64%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.93% | **+1.93%** |
| ASK | 20/20 | 100.0% | +1.17% | **+1.17%** |
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.07% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.24% | **+0.10%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.16% | **-0.08%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.25% | **-0.11%** |
| MARKET_LONG | 20/20 | 100.0% | -0.21% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.96** / 初期 $100.00 (+125.96%)
- 確定: 1975件 (Win 574 / Loss 643 / Flat 758) / skip 1831件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $225.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 346件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T13:42:40.145526+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=63433.5
- Funnel: target 796 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +94.00% | $40,300,236.00 |
| BEL/USDT:USDT | +56.17% | $2,099,311.42 |
| BICO/USDT:USDT | +47.24% | $31,146,378.07 |
| SLX/USDT:USDT | +35.67% | $1,302,457.82 |
| RE/USDT:USDT | +25.62% | $86,086,272.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEL/USDT:USDT | below_1h_threshold | +4.04% | +4.35% |
| SAND/USDT:USDT | below_1h_threshold | +3.79% | +4.09% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.94% | +2.25% |
| USOIL/USDT:USDT | below_1h_threshold | +1.73% | +2.04% |
| AXS/USDT:USDT | below_1h_threshold | +1.23% | +1.54% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
