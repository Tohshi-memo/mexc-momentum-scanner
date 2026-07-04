# Decision Report

- generated_at: 2026-07-04T23:36:32.391135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8300**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.27% / filled 20/20。**
- 全期間 MARKET基準: n=8300, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.31% | **+1.31%** |
| MARKET | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.24% | **+0.56%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.40% | **+0.26%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.38% | **-0.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| MARKET_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | -0.50% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$101.58** / 初期 $100.00 (+1.58%)
- 確定トレード: 61件 (TP 21 / SL 39 / EXP 1)
- 最新: CAP/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$326.82** / 初期 $100.00 (+226.82%)
- 確定: 2617件 (Win 832 / Loss 881 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: O/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $326.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1073件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-04T23:36:27.362784+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63122.2
- Funnel: target 834 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RPL/USDT:USDT | +22.86% | $2,795,972.17 |
| H/USDT:USDT | +18.95% | $3,711,287.37 |
| O/USDT:USDT | +18.37% | $5,755,490.49 |
| CAP/USDT:USDT | +13.71% | $1,900,556.52 |
| HOT/USDT:USDT | +10.02% | $1,434,885.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.04% | +2.12% |
| CAP/USDT:USDT | below_1h_threshold | +1.77% | +1.85% |
| GUA/USDT:USDT | below_1h_threshold | +1.76% | +1.83% |
| BSB/USDT:USDT | below_1h_threshold | +1.32% | +1.39% |
| RE/USDT:USDT | below_1h_threshold | +0.87% | +0.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
