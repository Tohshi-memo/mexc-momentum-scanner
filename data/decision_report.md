# Decision Report

- generated_at: 2026-06-30T23:43:50.317906+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7933**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=7933, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.40% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.99% | **+0.55%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.19% | **+0.22%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.01% | **-0.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | -0.11% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2139件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.52** / 初期 $100.00 (+6.52%)
- 確定: 475件 (Win 125 / Loss 121 / Flat 229) / skip 869件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0348 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BILL/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.52

## 5. Latest Market Context

- 更新: 2026-06-30T23:43:45.550699+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=58571.2
- Funnel: target 818 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +15.71% | $1,205,262.81 |
| OPG/USDT:USDT | +12.96% | $1,071,548.42 |
| BESTOCK/USDT:USDT | +12.92% | $1,148,657.44 |
| AIGENSYN/USDT:USDT | +12.89% | $15,060,138.66 |
| BASED/USDT:USDT | +9.21% | $2,482,907.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +3.04% | +3.05% |
| TAIKO/USDT:USDT | below_1h_threshold | +2.92% | +2.93% |
| M/USDT:USDT | below_1h_threshold | +2.63% | +2.63% |
| BASED/USDT:USDT | below_1h_threshold | +1.91% | +1.92% |
| XLM/USDT:USDT | below_1h_threshold | +1.87% | +1.88% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
