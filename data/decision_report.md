# Decision Report

- generated_at: 2026-05-13T17:08:09.479174+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4238**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4238, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.61% | **+1.53%** |
| ASK | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.24% | **+0.81%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.22% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.15% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 38件 (TP 10 / SL 25 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 457件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T17:08:06.300047+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79151.8
- Funnel: target 765 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +8.03% | $5,177,314.33 |
| SAGA/USDT:USDT | +7.43% | $44,549,657.70 |
| GUA/USDT:USDT | +6.53% | $3,778,695.41 |
| UB/USDT:USDT | +5.67% | $10,538,037.56 |
| LAB/USDT:USDT | +4.75% | $154,803,647.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +1.89% | +1.79% |
| SIREN/USDT:USDT | below_1h_threshold | +1.53% | +1.42% |
| NEAR/USDT:USDT | below_1h_threshold | +0.76% | +0.65% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.73% | +0.62% |
| BSB/USDT:USDT | below_1h_threshold | +0.71% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
