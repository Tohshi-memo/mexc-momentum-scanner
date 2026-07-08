# Decision Report

- generated_at: 2026-07-08T14:03:14.648697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8481**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=8481, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| ASK | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.91% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.56% | **-0.39%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.63% | **-0.41%** |

## 2. $100 Live Portfolio

- 残高: **$104.11** / 初期 $100.00 (+4.11%)
- 確定トレード: 74件 (TP 27 / SL 46 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT TP_HIT PnL +6.66% 残高後 $104.11
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.31** / 初期 $100.00 (+223.31%)
- 確定: 2681件 (Win 849 / Loss 899 / Flat 933) / skip 2361件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $323.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1251件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T14:03:09.480477+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=61894.0
- Funnel: target 851 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDGE/USDT:USDT | +57.95% | $24,575,199.09 |
| EVAA/USDT:USDT | +37.18% | $80,771,656.35 |
| PENGSTOCK/USDT:USDT | +18.38% | $1,279,033.17 |
| UAI/USDT:USDT | +16.07% | $3,085,643.03 |
| SYN/USDT:USDT | +15.37% | $7,330,546.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGSTOCK/USDT:USDT | below_1h_threshold | +1.33% | +1.37% |
| EVAA/USDT:USDT | below_1h_threshold | +1.18% | +1.22% |
| TIA/USDT:USDT | below_1h_threshold | +1.02% | +1.07% |
| VELVET/USDT:USDT | below_1h_threshold | +0.87% | +0.92% |
| UAI/USDT:USDT | below_1h_threshold | +0.80% | +0.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
