# Decision Report

- generated_at: 2026-07-08T09:41:23.819821+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8474**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.03% / filled 20/20。**
- 全期間 MARKET基準: n=8474, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.03% | **+3.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.03% | **+3.03%** |
| ASK | 20/20 | 100.0% | +2.43% | **+2.43%** |
| LIMIT_1PCT | 14/20 | 70.0% | +1.27% | **+0.89%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.30% | **+0.84%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.13% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.27% | **-0.09%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.31% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$104.11** / 初期 $100.00 (+4.11%)
- 確定トレード: 74件 (TP 27 / SL 46 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT TP_HIT PnL +6.66% 残高後 $104.11
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.40** / 初期 $100.00 (+223.40%)
- 確定: 2679件 (Win 849 / Loss 898 / Flat 932) / skip 2356件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDGE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $323.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1244件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T09:41:16.299060+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=62045.8
- Funnel: target 848 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +61.68% | $68,667,295.97 |
| EDGE/USDT:USDT | +40.96% | $18,282,019.54 |
| SYN/USDT:USDT | +19.01% | $5,416,062.61 |
| NES/USDT:USDT | +15.20% | $1,690,150.05 |
| KMNO/USDT:USDT | +11.69% | $1,155,325.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.65% | +4.56% |
| UAI/USDT:USDT | below_1h_threshold | +3.70% | +3.61% |
| UNI/USDT:USDT | below_1h_threshold | +2.41% | +2.32% |
| EDGE/USDT:USDT | below_1h_threshold | +1.76% | +1.67% |
| RIF/USDT:USDT | below_1h_threshold | +1.54% | +1.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
