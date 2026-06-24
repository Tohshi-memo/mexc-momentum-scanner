# Decision Report

- generated_at: 2026-06-24T18:26:14.156968+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7489**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=7489, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.61% | **+2.61%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.18% | **+1.01%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.87% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.57% | **+0.32%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -3.56% | **-0.53%** |
| ASK_LONG | 20/20 | 100.0% | -0.55% | **-0.55%** |

## 2. $100 Live Portfolio

- 残高: **$102.44** / 初期 $100.00 (+2.44%)
- 確定トレード: 34件 (TP 13 / SL 21 / EXP 0)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.44
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.81** / 初期 $100.00 (+124.81%)
- 確定: 2120件 (Win 627 / Loss 708 / Flat 785) / skip 1930件
- 成長率目線: 平均log +0.000382 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $224.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 346件 (Win 98 / Loss 95 / Flat 153) / skip 554件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0201 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-24T18:26:09.643223+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.64% price=59744.2
- Funnel: target 808 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +23.12% | $14,622,012.99 |
| BSB/USDT:USDT | +4.86% | $6,270,316.61 |
| O/USDT:USDT | +3.56% | $7,814,522.03 |
| XPL/USDT:USDT | +3.08% | $7,148,522.77 |
| ARX/USDT:USDT | +2.99% | $3,359,429.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAVE/USDT:USDT | below_1h_threshold | +4.88% | +4.24% |
| ZEC/USDT:USDT | below_1h_threshold | +3.88% | +3.24% |
| MAVIA/USDT:USDT | below_1h_threshold | +3.63% | +2.99% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +3.58% | +2.94% |
| ID/USDT:USDT | below_1h_threshold | +3.25% | +2.61% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
