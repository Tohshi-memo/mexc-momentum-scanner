# Decision Report

- generated_at: 2026-07-05T06:46:37.070775+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8311**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=8311, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.08% | **+2.08%** |
| MARKET | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.19% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.69% | **-0.34%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.63% | **-0.38%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -1.00% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$101.07** / 初期 $100.00 (+1.07%)
- 確定トレード: 62件 (TP 21 / SL 40 / EXP 1)
- 最新: TLM/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2253件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1084件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T06:46:26.536482+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=62726.1
- Funnel: target 834 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +30.03% | $1,387,656.06 |
| RPL/USDT:USDT | +19.58% | $5,683,520.96 |
| HOT/USDT:USDT | +16.20% | $2,183,154.26 |
| BIRB/USDT:USDT | +13.89% | $1,136,140.05 |
| BTW/USDT:USDT | +10.39% | $1,231,380.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARX/USDT:USDT | below_1h_threshold | +4.63% | +4.62% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.87% | +3.86% |
| CAP/USDT:USDT | below_1h_threshold | +2.05% | +2.03% |
| H/USDT:USDT | below_1h_threshold | +1.38% | +1.37% |
| JUP/USDT:USDT | below_1h_threshold | +1.06% | +1.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
