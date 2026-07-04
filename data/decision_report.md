# Decision Report

- generated_at: 2026-07-04T21:39:32.702454+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8294**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=8294, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.71% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.66% | **+0.33%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -0.56% | **-0.22%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -3.13% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$102.09** / 初期 $100.00 (+2.09%)
- 確定トレード: 60件 (TP 21 / SL 38 / EXP 1)
- 最新: O/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.09
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$333.44** / 初期 $100.00 (+233.44%)
- 確定: 2611件 (Win 831 / Loss 876 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $333.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.13** / 初期 $100.00 (+6.13%)
- 確定: 637件 (Win 152 / Loss 156 / Flat 329) / skip 1068件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0196 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.13

## 5. Latest Market Context

- 更新: 2026-07-04T21:39:27.730318+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=63346.5
- Funnel: target 834 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +19.85% | $3,442,710.37 |
| RPL/USDT:USDT | +19.58% | $2,527,676.57 |
| HOT/USDT:USDT | +13.38% | $1,213,249.12 |
| H/USDT:USDT | +12.44% | $3,065,589.06 |
| HEI/USDT:USDT | +11.81% | $2,783,923.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HMSTR/USDT:USDT | below_1h_threshold | +2.62% | +2.40% |
| O/USDT:USDT | below_1h_threshold | +2.10% | +1.89% |
| H/USDT:USDT | below_1h_threshold | +1.94% | +1.72% |
| GRASS/USDT:USDT | below_1h_threshold | +1.35% | +1.14% |
| LIT/USDT:USDT | below_1h_threshold | +1.05% | +0.83% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
