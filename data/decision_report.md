# Decision Report

- generated_at: 2026-07-05T10:20:35.176751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8318**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.19% / filled 20/20。**
- 全期間 MARKET基準: n=8318, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.19% | **+2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.19% | **+2.19%** |
| ASK | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.28% | **+0.96%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.53% | **+0.24%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.36% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | -0.43% | **-0.34%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.41% | **-0.35%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.86% | **-0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 64件 (TP 22 / SL 41 / EXP 1)
- 最新: HMSTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2260件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1091件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T10:20:30.202980+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=62678.7
- Funnel: target 834 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +26.31% | $2,680,892.37 |
| CAP/USDT:USDT | +16.92% | $2,942,091.20 |
| HOT/USDT:USDT | +16.89% | $3,417,171.01 |
| BTW/USDT:USDT | +14.10% | $2,223,977.49 |
| AIGENSYN/USDT:USDT | +12.73% | $1,260,546.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.13% | +4.01% |
| H/USDT:USDT | below_1h_threshold | +3.23% | +3.11% |
| CAP/USDT:USDT | below_1h_threshold | +2.67% | +2.55% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.66% | +2.53% |
| XTZ/USDT:USDT | below_1h_threshold | +2.27% | +2.15% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
