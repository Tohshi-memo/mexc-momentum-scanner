# Decision Report

- generated_at: 2026-06-19T11:40:52.347148+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7133**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7133, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_5PCT | 12/20 | 60.0% | +0.71% | **+0.43%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.50% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| ASK_LONG | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.39% | **+1.44%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.68% | **+1.43%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$102.98** / 初期 $100.00 (+2.98%)
- 確定トレード: 21件 (TP 9 / SL 12 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.98
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.90** / 初期 $100.00 (+132.90%)
- 確定: 1953件 (Win 566 / Loss 629 / Flat 758) / skip 1741件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $232.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 309件 (Win 89 / Loss 87 / Flat 133) / skip 235件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-19T11:40:47.055447+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=62594.3
- Funnel: target 795 → liquid 163 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 70.3 >= 65=1, 4h RSI 82.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +79.97% | $8,393,952.57 |
| RE/USDT:USDT | +55.43% | $28,765,371.88 |
| HEI/USDT:USDT | +40.89% | $8,582,560.37 |
| BICO/USDT:USDT | +39.92% | $1,002,269.26 |
| BTW/USDT:USDT | +37.71% | $3,579,598.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.33% | +3.19% |
| BTW/USDT:USDT | below_1h_threshold | +3.22% | +3.08% |
| AGT/USDT:USDT | below_1h_threshold | +2.99% | +2.85% |
| CLO/USDT:USDT | below_1h_threshold | +2.94% | +2.80% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.51% | +2.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
