# Decision Report

- generated_at: 2026-07-04T22:37:50.453801+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8298**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=8298, expectancy=-0.02%
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
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.90% | **+0.45%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.20% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.37% | **+0.19%** |
| ASK_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.07% | **+0.05%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.58** / 初期 $100.00 (+1.58%)
- 確定トレード: 61件 (TP 21 / SL 39 / EXP 1)
- 最新: CAP/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.58
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$330.11** / 初期 $100.00 (+230.11%)
- 確定: 2615件 (Win 832 / Loss 879 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HMSTR/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $330.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1071件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0079 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-04T22:37:44.296640+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63203.1
- Funnel: target 834 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +26.13% | $4,651,828.20 |
| H/USDT:USDT | +17.87% | $3,409,028.59 |
| RPL/USDT:USDT | +17.03% | $2,651,219.17 |
| CAP/USDT:USDT | +14.68% | $1,682,179.53 |
| HOT/USDT:USDT | +14.41% | $1,330,842.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.75% | +4.86% |
| CAP/USDT:USDT | below_1h_threshold | +4.44% | +4.56% |
| H/USDT:USDT | below_1h_threshold | +4.01% | +4.12% |
| O/USDT:USDT | below_1h_threshold | +3.33% | +3.45% |
| HOT/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
