# Decision Report

- generated_at: 2026-06-14T04:02:03.832098+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6634**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6634, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.43% | **-0.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.77% | **+0.35%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.18% | **+0.18%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.63% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.85** / 初期 $100.00 (+69.85%)
- 確定: 1507件 (Win 405 / Loss 481 / Flat 621) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $169.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.64** / 初期 $100.00 (-1.36%)
- 確定: 45件 (Win 15 / Loss 12 / Flat 18) / skip 0件
- 成長率目線: 平均log -0.000304 / 幾何平均 -0.030% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $98.64

## 5. Latest Market Context

- 更新: 2026-06-14T04:01:59.169724+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64503.4
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +57.91% | $22,270,829.67 |
| TRADOOR/USDT:USDT | +43.69% | $4,164,515.76 |
| BTW/USDT:USDT | +25.04% | $2,390,522.12 |
| BRETT/USDT:USDT | +14.50% | $1,512,085.87 |
| RIF/USDT:USDT | +12.23% | $14,183,280.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +0.46% | +0.48% |
| H/USDT:USDT | below_1h_threshold | +0.39% | +0.40% |
| XPD/USDT:USDT | below_1h_threshold | +0.37% | +0.39% |
| SQD/USDT:USDT | below_1h_threshold | +0.20% | +0.21% |
| JASMY/USDT:USDT | below_1h_threshold | +0.19% | +0.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
