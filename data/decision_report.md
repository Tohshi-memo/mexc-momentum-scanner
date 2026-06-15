# Decision Report

- generated_at: 2026-06-15T16:30:58.052565+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6795**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=6795, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.16% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.04% | **+0.67%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.71% | **+0.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.20% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$104.05** / 初期 $100.00 (+4.05%)
- 確定トレード: 7件 (TP 5 / SL 2 / EXP 0)
- 最新: ASTEROID/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.05
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$177.27** / 初期 $100.00 (+77.27%)
- 確定: 1668件 (Win 435 / Loss 518 / Flat 715) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $177.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.82** / 初期 $100.00 (-2.18%)
- 確定: 154件 (Win 28 / Loss 29 / Flat 97) / skip 52件
- 成長率目線: 平均log -0.000143 / 幾何平均 -0.014% per trade / maxDD +2.82%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $97.82

## 5. Latest Market Context

- 更新: 2026-06-15T16:30:53.663178+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=67189.1
- Funnel: target 772 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +9.54% | $40,859,025.64 |
| UAI/USDT:USDT | +3.86% | $4,176,690.29 |
| SKYAI/USDT:USDT | +3.53% | $8,491,931.61 |
| ASTEROID/USDT:USDT | +2.31% | $6,044,528.40 |
| SPCXSTOCK/USDT:USDT | +1.68% | $125,482,969.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.89% | +3.98% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.36% | +3.45% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.31% | +2.40% |
| BSB/USDT:USDT | below_1h_threshold | +2.29% | +2.37% |
| XRP/USDT:USDT | below_1h_threshold | +1.66% | +1.75% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
