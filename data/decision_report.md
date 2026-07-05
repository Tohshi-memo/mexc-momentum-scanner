# Decision Report

- generated_at: 2026-07-05T08:23:02.211349+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8315**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.79% / filled 20/20。**
- 全期間 MARKET基準: n=8315, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.79% | **+2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.79% | **+2.79%** |
| ASK | 20/20 | 100.0% | +2.77% | **+2.77%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.09% | **+0.71%** |
| LIMIT_2PCT | 11/20 | 55.0% | +0.57% | **+0.31%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.45% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.75% | **-0.45%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.04% | **-0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.08** / 初期 $100.00 (+2.08%)
- 確定トレード: 63件 (TP 22 / SL 40 / EXP 1)
- 最新: BTW/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2257件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1088件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T08:22:57.225866+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62949.2
- Funnel: target 834 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +33.41% | $1,909,122.29 |
| HOT/USDT:USDT | +16.76% | $3,085,092.50 |
| CAP/USDT:USDT | +14.63% | $2,298,495.80 |
| BIRB/USDT:USDT | +14.62% | $1,311,494.75 |
| RPL/USDT:USDT | +14.31% | $6,110,615.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.99% | +3.06% |
| VANRY/USDT:USDT | below_1h_threshold | +2.09% | +2.16% |
| RPL/USDT:USDT | below_1h_threshold | +1.78% | +1.85% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.78% | +1.85% |
| XTZ/USDT:USDT | below_1h_threshold | +1.66% | +1.73% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
