# Decision Report

- generated_at: 2026-06-27T09:30:24.159571+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7686**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7686, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |
| LIMIT_BB3S | 2/18 | 11.1% | +0.05% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.43% | **+0.97%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.20% | **+0.66%** |
| ASK_LONG | 20/20 | 100.0% | +0.63% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.86** / 初期 $100.00 (+134.86%)
- 確定: 2211件 (Win 662 / Loss 737 / Flat 812) / skip 2036件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $234.86

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.55** / 初期 $100.00 (+8.55%)
- 確定: 417件 (Win 114 / Loss 103 / Flat 200) / skip 680件
- 成長率目線: 平均log +0.000197 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0614 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $108.55

## 5. Latest Market Context

- 更新: 2026-06-27T09:30:18.376251+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=60342.3
- Funnel: target 806 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +72.84% | $78,717,340.03 |
| MYX/USDT:USDT | +40.02% | $11,102,902.64 |
| PUNDIX/USDT:USDT | +19.87% | $6,291,196.44 |
| SYRUP/USDT:USDT | +19.73% | $1,822,097.55 |
| ARX/USDT:USDT | +15.66% | $2,704,590.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.72% | +3.86% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.72% | +3.85% |
| SYN/USDT:USDT | below_1h_threshold | +2.10% | +2.24% |
| ARX/USDT:USDT | below_1h_threshold | +1.34% | +1.47% |
| PUNDIX/USDT:USDT | below_1h_threshold | +1.33% | +1.47% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
