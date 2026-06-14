# Decision Report

- generated_at: 2026-06-14T20:48:21.575586+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6697**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6697, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.51% | **+0.98%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.71% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.54% | **+0.69%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.84% | **+0.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$171.93** / 初期 $100.00 (+71.93%)
- 確定: 1570件 (Win 418 / Loss 498 / Flat 654) / skip 1688件
- 成長率目線: 平均log +0.000345 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.20% 残高後 $171.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 73件 (Win 20 / Loss 15 / Flat 38) / skip 35件
- 成長率目線: 平均log -0.000179 / 幾何平均 -0.018% per trade / maxDD +2.07%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: OPG/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.13% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T20:48:17.750138+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=64006.2
- Funnel: target 770 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +32.14% | $9,131,997.63 |
| BP/USDT:USDT | +9.31% | $1,049,114.35 |
| BABY/USDT:USDT | +7.26% | $1,525,020.20 |
| BTW/USDT:USDT | +6.77% | $3,647,079.58 |
| CLO/USDT:USDT | +5.90% | $1,525,015.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.73% | +3.37% |
| BTW/USDT:USDT | below_1h_threshold | +3.34% | +2.98% |
| XPL/USDT:USDT | below_1h_threshold | +2.68% | +2.32% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.25% | +1.89% |
| OPG/USDT:USDT | below_1h_threshold | +2.15% | +1.79% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
