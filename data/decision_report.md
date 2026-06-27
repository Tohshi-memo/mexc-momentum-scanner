# Decision Report

- generated_at: 2026-06-27T08:37:51.871025+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7682**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7682, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.87% | **+0.09%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.70% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.99% | **+0.79%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.07% | **+0.54%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.34% | **+0.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$236.04** / 初期 $100.00 (+136.04%)
- 確定: 2207件 (Win 662 / Loss 736 / Flat 809) / skip 2036件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $236.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.38** / 初期 $100.00 (+8.38%)
- 確定: 413件 (Win 113 / Loss 103 / Flat 197) / skip 680件
- 成長率目線: 平均log +0.000195 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0569 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $108.38

## 5. Latest Market Context

- 更新: 2026-06-27T08:37:45.330526+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=60371.0
- Funnel: target 806 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +45.48% | $65,691,675.52 |
| MYX/USDT:USDT | +38.61% | $10,333,456.18 |
| PUNDIX/USDT:USDT | +20.73% | $6,216,941.46 |
| SYRUP/USDT:USDT | +18.15% | $1,732,483.59 |
| SLX/USDT:USDT | +15.43% | $10,745,861.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.70% | +3.95% |
| PUNDIX/USDT:USDT | below_1h_threshold | +2.27% | +2.52% |
| MYX/USDT:USDT | below_1h_threshold | +2.09% | +2.34% |
| ARX/USDT:USDT | below_1h_threshold | +1.38% | +1.63% |
| USELESS/USDT:USDT | below_1h_threshold | +1.29% | +1.54% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
