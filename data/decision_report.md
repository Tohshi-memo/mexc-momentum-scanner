# Decision Report

- generated_at: 2026-07-05T00:34:13.900691+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8302**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.06% / filled 20/20。**
- 全期間 MARKET基準: n=8302, expectancy=-0.02%
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
| LIMIT_2PCT | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.99% | **+0.54%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.66% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.32% | **-0.19%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.39% | **-0.20%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.41% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$101.58** / 初期 $100.00 (+1.58%)
- 確定トレード: 61件 (TP 21 / SL 39 / EXP 1)
- 最新: CAP/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1075件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T00:34:07.431776+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=62975.5
- Funnel: target 834 → liquid 145 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RPL/USDT:USDT | +39.90% | $3,644,249.27 |
| CAP/USDT:USDT | +15.80% | $2,091,612.00 |
| O/USDT:USDT | +14.83% | $6,313,137.90 |
| H/USDT:USDT | +12.66% | $4,051,527.25 |
| HOT/USDT:USDT | +10.02% | $1,705,899.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +3.37% | +3.59% |
| ARPA/USDT:USDT | below_1h_threshold | +2.47% | +2.69% |
| RE/USDT:USDT | below_1h_threshold | +1.25% | +1.47% |
| CAP/USDT:USDT | below_1h_threshold | +1.11% | +1.33% |
| DOGS/USDT:USDT | below_1h_threshold | +0.68% | +0.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
