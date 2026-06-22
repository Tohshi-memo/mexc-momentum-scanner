# Decision Report

- generated_at: 2026-06-22T21:04:48.013366+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7395**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7395, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |
| MARKET | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.05% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.44% | **+0.94%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.32% | **+0.24%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.13% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.89** / 初期 $100.00 (+133.89%)
- 確定: 2051件 (Win 608 / Loss 675 / Flat 768) / skip 1905件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $233.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 494件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T21:04:43.558101+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64402.9
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +19.35% | $15,180,075.73 |
| RE/USDT:USDT | +15.57% | $26,641,804.26 |
| SYN/USDT:USDT | +15.18% | $27,937,400.25 |
| LAB/USDT:USDT | +12.16% | $40,588,623.21 |
| BLESS/USDT:USDT | +10.60% | $8,386,209.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +2.54% | +2.55% |
| ARX/USDT:USDT | below_1h_threshold | +0.77% | +0.78% |
| AERO/USDT:USDT | below_1h_threshold | +0.62% | +0.63% |
| TNSR/USDT:USDT | below_1h_threshold | +0.61% | +0.62% |
| UAI/USDT:USDT | below_1h_threshold | +0.45% | +0.46% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
