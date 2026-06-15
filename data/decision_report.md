# Decision Report

- generated_at: 2026-06-15T16:37:21.000719+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6796**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=6796, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| ASK | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.16% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.04% | **+0.67%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +0.13% | **+0.03%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | -0.19% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$176.38** / 初期 $100.00 (+76.38%)
- 確定: 1669件 (Win 435 / Loss 519 / Flat 715) / skip 1688件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $176.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.82** / 初期 $100.00 (-2.18%)
- 確定: 154件 (Win 28 / Loss 29 / Flat 97) / skip 53件
- 成長率目線: 平均log -0.000143 / 幾何平均 -0.014% per trade / maxDD +2.82%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $97.82

## 5. Latest Market Context

- 更新: 2026-06-15T16:37:15.642780+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=67198.8
- Funnel: target 772 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +9.89% | $41,133,649.89 |
| RAVE/USDT:USDT | +4.68% | $1,519,448.21 |
| UAI/USDT:USDT | +4.19% | $4,185,188.68 |
| SKYAI/USDT:USDT | +4.07% | $8,517,410.53 |
| WLFI/USDT:USDT | +1.95% | $2,631,779.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.68% | +4.75% |
| UAI/USDT:USDT | below_1h_threshold | +4.19% | +4.27% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.02% | +4.09% |
| WLFI/USDT:USDT | below_1h_threshold | +2.01% | +2.08% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.93% | +2.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
