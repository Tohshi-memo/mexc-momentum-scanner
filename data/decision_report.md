# Decision Report

- generated_at: 2026-07-05T01:52:34.675666+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8304**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.66% / filled 20/20。**
- 全期間 MARKET基準: n=8304, expectancy=-0.02%
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
| ASK | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.53% | **+0.76%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.19% | **+0.71%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.03% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.24% | **+0.15%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
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
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2246件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1077件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T01:52:28.183305+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=62850.1
- Funnel: target 834 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RPL/USDT:USDT | +27.96% | $4,340,059.75 |
| H/USDT:USDT | +14.92% | $4,477,861.12 |
| O/USDT:USDT | +11.60% | $6,771,014.63 |
| HOT/USDT:USDT | +10.05% | $1,740,533.05 |
| VELVET/USDT:USDT | +9.81% | $32,209,045.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000BONK/USDT:USDT | below_1h_threshold | +1.92% | +2.09% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.08% | +1.26% |
| HOT/USDT:USDT | below_1h_threshold | +1.06% | +1.24% |
| EPIC/USDT:USDT | below_1h_threshold | +0.67% | +0.85% |
| RIVER/USDT:USDT | below_1h_threshold | +0.67% | +0.84% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
