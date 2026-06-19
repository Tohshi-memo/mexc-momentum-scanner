# Decision Report

- generated_at: 2026-06-19T04:43:06.590658+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7101, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.18% | **+0.05%** |
| LIMIT_BB3S | 2/16 | 12.5% | -1.50% | **-0.19%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.97% | **+0.60%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.69% | **+0.45%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.47% | **+0.40%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.38% | **+0.35%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.84% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$102.99** / 初期 $100.00 (+2.99%)
- 確定トレード: 18件 (TP 8 / SL 10 / EXP 0)
- 最新: MYX/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$221.64** / 初期 $100.00 (+121.64%)
- 確定: 1921件 (Win 549 / Loss 619 / Flat 753) / skip 1741件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASED/USDT:USDT `LIMIT_9PCT_LONG` SL_HIT account -0.50% 残高後 $221.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 308件 (Win 89 / Loss 86 / Flat 133) / skip 204件
- 成長率目線: 平均log +0.000202 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MITO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-19T04:43:00.073523+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=62580.1
- Funnel: target 795 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +69.85% | $6,712,600.67 |
| BASED/USDT:USDT | +19.34% | $5,567,234.26 |
| ZEREBRO/USDT:USDT | +18.50% | $3,616,752.89 |
| HEI/USDT:USDT | +15.09% | $1,344,287.66 |
| BTW/USDT:USDT | +14.58% | $3,358,502.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.76% | +4.03% |
| HEI/USDT:USDT | below_1h_threshold | +3.74% | +4.00% |
| BEAT/USDT:USDT | below_1h_threshold | +3.53% | +3.80% |
| BR/USDT:USDT | below_1h_threshold | +1.94% | +2.21% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +1.53% | +1.79% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
