# Decision Report

- generated_at: 2026-06-14T04:45:47.028966+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6636**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6636, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.14% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.18% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.72%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.30% | **+0.71%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$170.69** / 初期 $100.00 (+70.69%)
- 確定: 1509件 (Win 406 / Loss 482 / Flat 621) / skip 1688件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $170.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 46件 (Win 16 / Loss 12 / Flat 18) / skip 1件
- 成長率目線: 平均log -0.000282 / 幾何平均 -0.028% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-14T04:45:42.562126+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=64336.6
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +59.12% | $24,783,463.38 |
| TRADOOR/USDT:USDT | +54.92% | $4,952,575.94 |
| BTW/USDT:USDT | +21.28% | $2,552,324.60 |
| BRETT/USDT:USDT | +10.96% | $1,556,605.17 |
| MEGA/USDT:USDT | +8.92% | $4,067,140.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +3.41% | +3.68% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.85% | +2.13% |
| H/USDT:USDT | below_1h_threshold | +1.31% | +1.59% |
| KAS/USDT:USDT | below_1h_threshold | +0.57% | +0.85% |
| LMTSTOCK/USDT:USDT | below_1h_threshold | +0.55% | +0.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
