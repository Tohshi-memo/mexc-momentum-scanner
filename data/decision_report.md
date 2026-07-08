# Decision Report

- generated_at: 2026-07-08T17:24:28.614818+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8491**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=8491, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.58% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.45% | **+0.87%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.60% | **+0.39%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.14% | **+0.10%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.11% | **+0.07%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.12% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$105.15** / 初期 $100.00 (+5.15%)
- 確定トレード: 78件 (TP 29 / SL 48 / EXP 1)
- 最新: VANRY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$321.69** / 初期 $100.00 (+221.69%)
- 確定: 2682件 (Win 849 / Loss 900 / Flat 933) / skip 2370件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.50% 残高後 $321.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 642件 (Win 152 / Loss 159 / Flat 331) / skip 1260件
- 成長率目線: 平均log +0.000078 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VANRY/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $105.11

## 5. Latest Market Context

- 更新: 2026-07-08T17:24:17.925523+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=62211.0
- Funnel: target 851 → liquid 179 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +22.71% | $5,353,567.30 |
| TAG/USDT:USDT | +18.85% | $1,017,094.38 |
| TLM/USDT:USDT | +16.78% | $4,107,298.79 |
| POWER/USDT:USDT | +12.75% | $2,002,199.08 |
| BTW/USDT:USDT | +11.13% | $1,040,717.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +4.33% | +4.13% |
| BEAT/USDT:USDT | below_1h_threshold | +3.93% | +3.73% |
| YFI/USDT:USDT | below_1h_threshold | +3.45% | +3.25% |
| VVV/USDT:USDT | below_1h_threshold | +2.50% | +2.30% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.22% | +2.02% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
