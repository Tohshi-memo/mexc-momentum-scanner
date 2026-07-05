# Decision Report

- generated_at: 2026-07-05T11:07:14.087230+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8319**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.59% / filled 20/20。**
- 全期間 MARKET基準: n=8319, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.59% | **+1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.59% | **+1.59%** |
| ASK | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.95% | **+0.76%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.31% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.19% | **-0.14%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.19% | **-0.15%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | -1.93% | **-0.29%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.65% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 64件 (TP 22 / SL 41 / EXP 1)
- 最新: HMSTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2261件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1092件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T11:07:07.852411+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=62684.0
- Funnel: target 835 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +27.58% | $3,143,937.53 |
| NES/USDT:USDT | +27.48% | $2,914,827.74 |
| CAP/USDT:USDT | +22.51% | $3,042,962.30 |
| HOT/USDT:USDT | +18.70% | $3,552,847.19 |
| O/USDT:USDT | +10.47% | $8,938,739.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.06% | +3.14% |
| PYTH/USDT:USDT | below_1h_threshold | +1.75% | +1.83% |
| ARX/USDT:USDT | below_1h_threshold | +1.57% | +1.66% |
| BTW/USDT:USDT | below_1h_threshold | +0.94% | +1.03% |
| HMSTR/USDT:USDT | below_1h_threshold | +0.91% | +1.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
