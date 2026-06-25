# Decision Report

- generated_at: 2026-06-25T01:01:11.830400+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7512**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7512, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.21% | **+0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.21% | **-0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.14% | **-0.21%** |
| LIMIT_FIB1272 | 14/20 | 70.0% | -0.37% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.31% | **+2.15%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.65% | **+1.98%** |
| ASK_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.90% | **+1.59%** |

## 2. $100 Live Portfolio

- 残高: **$103.45** / 初期 $100.00 (+3.45%)
- 確定トレード: 38件 (TP 15 / SL 23 / EXP 0)
- 最新: ARMSTOCK/USDT:USDT TP_HIT PnL +7.19% 残高後 $103.45
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$222.57** / 初期 $100.00 (+122.57%)
- 確定: 2122件 (Win 627 / Loss 710 / Flat 785) / skip 1951件
- 成長率目線: 平均log +0.000377 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $222.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 573件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T01:01:06.261834+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=60839.2
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +19.42% | $10,836,634.72 |
| SLX/USDT:USDT | +15.17% | $10,727,543.76 |
| KORU/USDT:USDT | +14.94% | $5,584,643.42 |
| MUSTOCK/USDT:USDT | +14.67% | $96,693,761.58 |
| UB/USDT:USDT | +12.33% | $4,785,119.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +1.47% | +1.38% |
| KORU/USDT:USDT | below_1h_threshold | +1.23% | +1.15% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.64% | +0.56% |
| MVLL/USDT:USDT | below_1h_threshold | +0.63% | +0.54% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.49% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
