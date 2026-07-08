# Decision Report

- generated_at: 2026-07-08T14:40:30.850510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8482**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=8482, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| ASK | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.83% | **+1.19%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | -0.60% | **-0.42%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.72% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定トレード: 75件 (TP 28 / SL 46 / EXP 1)
- 最新: AVAVSTOCK/USDT:USDT TP_HIT PnL +5.30% 残高後 $105.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.31** / 初期 $100.00 (+223.31%)
- 確定: 2681件 (Win 849 / Loss 899 / Flat 933) / skip 2362件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $323.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1252件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T14:40:25.794171+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=61884.4
- Funnel: target 851 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +32.43% | $83,191,761.32 |
| EDGE/USDT:USDT | +31.00% | $28,105,773.85 |
| UAI/USDT:USDT | +18.03% | $3,391,847.11 |
| SYN/USDT:USDT | +14.89% | $7,641,897.94 |
| PENGSTOCK/USDT:USDT | +14.65% | $1,318,278.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.90% | +2.96% |
| SPELL/USDT:USDT | below_1h_threshold | +2.61% | +2.67% |
| UAI/USDT:USDT | below_1h_threshold | +2.39% | +2.45% |
| USOIL/USDT:USDT | below_1h_threshold | +2.25% | +2.31% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.05% | +2.11% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
