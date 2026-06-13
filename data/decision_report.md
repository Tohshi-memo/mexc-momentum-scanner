# Decision Report

- generated_at: 2026-06-13T08:49:08.967611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6568**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6568, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +1.16% | **+0.17%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.42% | **+0.12%** |
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.07% | **+0.04%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.22% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.38% | **+0.55%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.77% | **+0.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.33% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$97.07** / 初期 $100.00 (-2.93%)
- 確定トレード: 25件 (TP 6 / SL 18 / EXP 1)
- 最新: SPCXSTOCK/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.48** / 初期 $100.00 (+64.48%)
- 確定: 1441件 (Win 389 / Loss 464 / Flat 588) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $164.48

## 4. Latest Market Context

- 更新: 2026-06-13T08:49:05.007612+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63826.9
- Funnel: target 774 → liquid 160 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1, 4h RSI 69.6 >= 65=1, 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +52.42% | $3,368,130.56 |
| EDGE/USDT:USDT | +24.10% | $2,879,222.43 |
| RIF/USDT:USDT | +22.79% | $1,904,461.42 |
| SQD/USDT:USDT | +14.90% | $1,393,114.25 |
| VVV/USDT:USDT | +14.32% | $6,296,472.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQD/USDT:USDT | below_1h_threshold | +2.73% | +2.72% |
| OP/USDT:USDT | below_1h_threshold | +2.55% | +2.54% |
| ORDI/USDT:USDT | below_1h_threshold | +1.18% | +1.17% |
| HOME/USDT:USDT | below_1h_threshold | +0.98% | +0.97% |
| TAO/USDT:USDT | below_1h_threshold | +0.81% | +0.80% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
