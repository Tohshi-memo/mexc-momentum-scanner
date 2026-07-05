# Decision Report

- generated_at: 2026-07-05T07:33:56.492481+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8314**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.79% / filled 20/20。**
- 全期間 MARKET基準: n=8314, expectancy=-0.02%
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
| ASK | 20/20 | 100.0% | +2.73% | **+2.73%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.01% | **+0.66%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.51% | **+0.23%** |
| LIMIT_2PCT | 11/20 | 55.0% | +0.39% | **+0.21%** |

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
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2256件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1087件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T07:33:50.326388+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=62810.5
- Funnel: target 834 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +34.34% | $1,741,566.74 |
| HOT/USDT:USDT | +22.90% | $2,484,224.09 |
| O/USDT:USDT | +13.73% | $8,183,014.28 |
| BIRB/USDT:USDT | +13.23% | $1,275,914.47 |
| RPL/USDT:USDT | +12.65% | $5,885,668.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.46% | +3.36% |
| CAP/USDT:USDT | below_1h_threshold | +3.17% | +3.08% |
| O/USDT:USDT | below_1h_threshold | +2.91% | +2.81% |
| NES/USDT:USDT | below_1h_threshold | +2.66% | +2.56% |
| ADA/USDT:USDT | below_1h_threshold | +2.11% | +2.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
