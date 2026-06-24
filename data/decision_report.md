# Decision Report

- generated_at: 2026-06-24T20:37:08.611541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7497**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.04% / filled 20/20。**
- 全期間 MARKET基準: n=7497, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.04% | **+2.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.06% | **+2.06%** |
| MARKET | 20/20 | 100.0% | +2.04% | **+2.04%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.05% | **+1.95%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.83% | **+1.55%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.43% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| ASK_LONG | 20/20 | 100.0% | -0.21% | **-0.21%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.46% | **-0.23%** |
| MARKET_LONG | 20/20 | 100.0% | -0.24% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$102.95** / 初期 $100.00 (+2.95%)
- 確定トレード: 36件 (TP 14 / SL 22 / EXP 0)
- 最新: SNDKSTOCK/USDT:USDT SL_HIT PnL -3.46% 残高後 $102.95
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$223.69** / 初期 $100.00 (+123.69%)
- 確定: 2121件 (Win 627 / Loss 709 / Flat 785) / skip 1937件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $223.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 349件 (Win 98 / Loss 95 / Flat 156) / skip 559件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T20:36:50.952196+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.36% price=60740.5
- Funnel: target 808 → liquid 162 → pre 50 → checked 50 → surge 7 → strict 6
- Surge前reject: below_1h_threshold=41, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KORU/USDT:USDT | +17.72% | $3,268,737.32 |
| MUSTOCK/USDT:USDT | +12.56% | $84,438,483.65 |
| H/USDT:USDT | +12.56% | $16,731,929.50 |
| DRAM/USDT:USDT | +11.56% | $7,074,028.94 |
| SOXL/USDT:USDT | +10.24% | $5,613,179.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_relative_strength | +5.65% | +4.29% |
| ARMSTOCK/USDT:USDT | below_relative_strength | +5.45% | +4.09% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.51% | +2.15% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +3.46% | +2.10% |
| SPX/USDT:USDT | below_1h_threshold | +3.45% | +2.09% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
