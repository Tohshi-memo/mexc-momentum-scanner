# Decision Report

- generated_at: 2026-07-05T01:04:08.412487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8303**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.66% / filled 20/20。**
- 全期間 MARKET基準: n=8303, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.66% | **+2.66%** |
| ASK | 20/20 | 100.0% | +2.63% | **+2.63%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.19% | **+0.71%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.30% | **+0.65%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.09% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.32% | **-0.19%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.46% | **-0.25%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -1.69% | **-0.42%** |

## 2. $100 Live Portfolio

- 残高: **$101.58** / 初期 $100.00 (+1.58%)
- 確定トレード: 61件 (TP 21 / SL 39 / EXP 1)
- 最新: CAP/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2245件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1076件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T01:04:02.365886+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=62974.8
- Funnel: target 834 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RPL/USDT:USDT | +33.79% | $3,935,087.47 |
| H/USDT:USDT | +15.68% | $4,135,692.67 |
| O/USDT:USDT | +13.25% | $6,543,823.27 |
| HEI/USDT:USDT | +11.03% | $2,955,711.63 |
| HOT/USDT:USDT | +8.77% | $1,717,363.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALGO/USDT:USDT | below_1h_threshold | +1.88% | +1.86% |
| BCH/USDT:USDT | below_1h_threshold | +1.16% | +1.13% |
| ADA/USDT:USDT | below_1h_threshold | +0.99% | +0.96% |
| ANSEM/USDT:USDT | below_1h_threshold | +0.86% | +0.84% |
| VELVET/USDT:USDT | below_1h_threshold | +0.85% | +0.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
