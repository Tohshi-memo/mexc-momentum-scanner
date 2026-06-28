# Decision Report

- generated_at: 2026-06-28T01:12:18.764679+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7723**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7723, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | +5.46% | **+1.09%** |
| LIMIT_BB3S | 3/13 | 23.1% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_6PCT | 5/20 | 25.0% | -1.63% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +0.35% | **+0.10%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.13% | **+0.09%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.08% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$239.53** / 初期 $100.00 (+139.53%)
- 確定: 2231件 (Win 671 / Loss 745 / Flat 815) / skip 2053件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $239.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.83** / 初期 $100.00 (+6.83%)
- 確定: 454件 (Win 120 / Loss 118 / Flat 216) / skip 680件
- 成長率目線: 平均log +0.000145 / 幾何平均 +0.015% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.83

## 5. Latest Market Context

- 更新: 2026-06-28T01:12:14.137385+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=60007.0
- Funnel: target 806 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +19.06% | $2,549,718.78 |
| LAB/USDT:USDT | +15.60% | $41,871,770.48 |
| SLX/USDT:USDT | +12.04% | $18,619,113.94 |
| S/USDT:USDT | +8.22% | $4,582,593.92 |
| VELVET/USDT:USDT | +7.76% | $255,783,177.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +2.09% | +2.29% |
| SLX/USDT:USDT | below_1h_threshold | +1.62% | +1.82% |
| BAS/USDT:USDT | below_1h_threshold | +1.13% | +1.32% |
| LAB/USDT:USDT | below_1h_threshold | +0.81% | +1.01% |
| BICO/USDT:USDT | below_1h_threshold | +0.63% | +0.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
