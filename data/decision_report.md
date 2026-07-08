# Decision Report

- generated_at: 2026-07-08T16:02:56.808092+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8483**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.69% / filled 20/20。**
- 全期間 MARKET基準: n=8483, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.69% | **+1.69%** |
| ASK | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.29% | **+0.84%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.54% | **+0.54%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.65% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.34% | **-0.22%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.46% | **-0.32%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.72% | **-0.52%** |

## 2. $100 Live Portfolio

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定トレード: 75件 (TP 28 / SL 46 / EXP 1)
- 最新: AVAVSTOCK/USDT:USDT TP_HIT PnL +5.30% 残高後 $105.15
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.31** / 初期 $100.00 (+223.31%)
- 確定: 2681件 (Win 849 / Loss 899 / Flat 933) / skip 2363件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.03% 残高後 $323.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 641件 (Win 152 / Loss 158 / Flat 331) / skip 1253件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-08T16:02:49.398716+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=61733.3
- Funnel: target 851 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +8.62% | $60,745,736.95 |
| MAGMA/USDT:USDT | +3.57% | $1,361,194.49 |
| TAC/USDT:USDT | +2.17% | $3,547,377.33 |
| ESPORTS/USDT:USDT | +1.87% | $2,068,455.20 |
| SKYAI/USDT:USDT | +1.75% | $8,797,015.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDGE/USDT:USDT | below_1h_threshold | +3.22% | +3.12% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.86% | +2.77% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.81% | +1.71% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.76% | +1.66% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.71% | +1.61% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
