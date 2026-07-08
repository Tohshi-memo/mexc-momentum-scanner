# Decision Report

- generated_at: 2026-07-08T13:01:28.539838+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8480**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.43% / filled 20/20。**
- 全期間 MARKET基準: n=8480, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.43% | **+2.43%** |
| ASK | 20/20 | 100.0% | +1.81% | **+1.81%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.21% | **+0.85%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.37% | **+0.82%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.08% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -1.96% | **-0.49%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | -0.81% | **-0.56%** |

## 2. $100 Live Portfolio

- 残高: **$104.11** / 初期 $100.00 (+4.11%)
- 確定トレード: 74件 (TP 27 / SL 46 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT TP_HIT PnL +6.66% 残高後 $104.11
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.31** / 初期 $100.00 (+223.31%)
- 確定: 2681件 (Win 849 / Loss 899 / Flat 933) / skip 2360件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $323.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1250件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T13:01:24.225289+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=61921.4
- Funnel: target 850 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +58.54% | $78,305,272.83 |
| EDGE/USDT:USDT | +55.80% | $22,846,598.11 |
| SYN/USDT:USDT | +18.24% | $6,981,646.76 |
| UAI/USDT:USDT | +14.13% | $2,554,499.60 |
| KAITO/USDT:USDT | +13.79% | $2,732,283.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +3.85% | +3.87% |
| VELVET/USDT:USDT | below_1h_threshold | +0.92% | +0.94% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +0.41% | +0.43% |
| KMNO/USDT:USDT | below_1h_threshold | +0.34% | +0.36% |
| RIF/USDT:USDT | below_1h_threshold | +0.33% | +0.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
