# Decision Report

- generated_at: 2026-06-20T05:12:57.956513+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7205**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=7205, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.97% | **+1.97%** |
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.59% | **+1.43%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.62% | **+1.05%** |
| LIMIT_BB3S | 2/17 | 11.8% | +6.74% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.35% | **+0.21%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.35% | **+0.17%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.32% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.84** / 初期 $100.00 (+124.84%)
- 確定: 1970件 (Win 571 / Loss 641 / Flat 758) / skip 1796件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $224.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 306件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T05:12:52.418056+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=63722.0
- Funnel: target 795 → liquid 145 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +42.43% | $17,524,436.80 |
| BICO/USDT:USDT | +36.02% | $19,921,493.85 |
| BLESS/USDT:USDT | +26.54% | $5,906,356.14 |
| AXS/USDT:USDT | +23.49% | $3,483,123.27 |
| EIGEN/USDT:USDT | +21.29% | $6,639,009.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOL/USDT:USDT | below_1h_threshold | +1.69% | +1.43% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.53% | +1.27% |
| CLO/USDT:USDT | below_1h_threshold | +1.20% | +0.94% |
| PENGU/USDT:USDT | below_1h_threshold | +1.18% | +0.92% |
| AAVE/USDT:USDT | below_1h_threshold | +1.16% | +0.90% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
