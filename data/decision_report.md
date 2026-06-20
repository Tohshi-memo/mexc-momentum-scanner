# Decision Report

- generated_at: 2026-06-20T00:45:36.551753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7185**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7185, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/19 | 21.1% | +3.08% | **+0.65%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.43% | **+0.36%** |
| ASK | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.30% | **+0.46%** |
| ASK_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.19% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1777件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 286件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T00:45:30.872167+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63564.1
- Funnel: target 795 → liquid 147 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1, 4h RSI 93.2 >= 65=1, 4h RSI 76.0 >= 65=1, 4h RSI 77.6 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +47.27% | $14,597,310.00 |
| BTW/USDT:USDT | +46.22% | $11,285,129.31 |
| BLESS/USDT:USDT | +27.54% | $4,961,586.99 |
| MET/USDT:USDT | +21.05% | $1,562,466.27 |
| EIGEN/USDT:USDT | +16.05% | $5,501,775.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_1h_threshold | +3.78% | +3.70% |
| GUA/USDT:USDT | below_1h_threshold | +1.92% | +1.84% |
| AGT/USDT:USDT | below_1h_threshold | +1.88% | +1.80% |
| POL/USDT:USDT | below_1h_threshold | +1.73% | +1.65% |
| APE/USDT:USDT | below_1h_threshold | +1.68% | +1.60% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
