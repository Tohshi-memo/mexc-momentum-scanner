# Decision Report

- generated_at: 2026-06-20T00:59:49.084527+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7188**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7188, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.13% | **+0.96%** |
| LIMIT_BB3S | 3/20 | 15.0% | +5.43% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.37% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.64% | **+0.26%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.12%** |
| ASK_LONG | 20/20 | 100.0% | -0.13% | **-0.13%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.36% | **-0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1780件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 289件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T00:59:43.328779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63527.6
- Funnel: target 795 → liquid 147 → pre 50 → checked 50 → surge 6 → strict 2
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1, 4h RSI 74.5 >= 65=1, 4h RSI 70.1 >= 65=1, 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +47.97% | $15,322,496.44 |
| BLESS/USDT:USDT | +26.44% | $5,009,117.09 |
| RE/USDT:USDT | +15.12% | $75,736,882.71 |
| MET/USDT:USDT | +13.96% | $1,692,230.52 |
| EIGEN/USDT:USDT | +11.03% | $5,624,730.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +3.05% | +3.03% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.82% | +2.80% |
| AGT/USDT:USDT | below_1h_threshold | +2.26% | +2.24% |
| APE/USDT:USDT | below_1h_threshold | +1.60% | +1.58% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.01% | +0.99% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
