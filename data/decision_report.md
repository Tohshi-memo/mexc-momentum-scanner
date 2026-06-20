# Decision Report

- generated_at: 2026-06-20T13:28:43.055046+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7243**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.47% / filled 20/20。**
- 全期間 MARKET基準: n=7243, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | +2.26% | **+2.14%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.43% | **+1.43%** |
| ASK | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.55% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.47% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.53% | **+0.19%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.06% | **+0.03%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.14% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.83** / 初期 $100.00 (+124.83%)
- 確定: 1974件 (Win 573 / Loss 643 / Flat 758) / skip 1830件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $224.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 344件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T13:28:38.437538+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.60% price=63247.7
- Funnel: target 796 → liquid 143 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +90.54% | $39,501,602.70 |
| BEL/USDT:USDT | +52.57% | $2,032,109.54 |
| BICO/USDT:USDT | +50.84% | $30,791,485.18 |
| SLX/USDT:USDT | +36.61% | $1,268,227.01 |
| RE/USDT:USDT | +29.42% | $85,051,700.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAND/USDT:USDT | below_1h_threshold | +2.81% | +3.40% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.10% | +2.70% |
| EDGE/USDT:USDT | below_1h_threshold | +2.05% | +2.65% |
| USOIL/USDT:USDT | below_1h_threshold | +1.96% | +2.56% |
| BEL/USDT:USDT | below_1h_threshold | +1.62% | +2.22% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
