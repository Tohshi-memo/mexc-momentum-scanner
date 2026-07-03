# Decision Report

- generated_at: 2026-07-03T02:47:46.833315+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8126**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=8126, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +1.51% | **+1.13%** |
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| ASK | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.88% | **+0.35%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.16% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.26% | **+0.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.27% | **+0.24%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.14% | **+0.08%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.24% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$285.42** / 初期 $100.00 (+185.42%)
- 確定: 2449件 (Win 755 / Loss 817 / Flat 877) / skip 2238件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $285.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.09** / 初期 $100.00 (+5.09%)
- 確定: 580件 (Win 140 / Loss 138 / Flat 302) / skip 957件
- 成長率目線: 平均log +0.000086 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $105.09

## 5. Latest Market Context

- 更新: 2026-07-03T02:47:37.434358+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=61314.2
- Funnel: target 834 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +26.01% | $5,466,359.14 |
| THE/USDT:USDT | +24.32% | $2,062,372.91 |
| PIPPIN/USDT:USDT | +21.04% | $7,321,163.72 |
| MAGMA/USDT:USDT | +20.19% | $5,337,321.85 |
| GUA/USDT:USDT | +14.21% | $10,130,363.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +4.05% | +4.46% |
| BTW/USDT:USDT | below_1h_threshold | +3.47% | +3.88% |
| GUA/USDT:USDT | below_1h_threshold | +1.79% | +2.20% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.61% | +2.02% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +1.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
