# Decision Report

- generated_at: 2026-06-22T19:21:53.095119+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7392**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=7392, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| ASK | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.64% | **+0.39%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.76% | **+0.31%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.47% | **+0.38%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.63% | **+0.16%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.02% | **+0.01%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.88** / 初期 $100.00 (+132.88%)
- 確定: 2048件 (Win 607 / Loss 674 / Flat 767) / skip 1905件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $232.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 491件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T19:21:47.645008+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=64385.1
- Funnel: target 808 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +18.18% | $27,209,506.79 |
| RE/USDT:USDT | +14.36% | $26,011,159.68 |
| BLESS/USDT:USDT | +13.93% | $6,086,996.82 |
| VELVET/USDT:USDT | +13.87% | $10,678,223.27 |
| LAB/USDT:USDT | +12.75% | $38,256,773.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.93% | +4.82% |
| LAB/USDT:USDT | below_1h_threshold | +3.53% | +3.42% |
| SYN/USDT:USDT | below_1h_threshold | +3.38% | +3.27% |
| MYX/USDT:USDT | below_1h_threshold | +2.62% | +2.51% |
| BLESS/USDT:USDT | below_1h_threshold | +1.67% | +1.56% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
