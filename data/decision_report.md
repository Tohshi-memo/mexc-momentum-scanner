# Decision Report

- generated_at: 2026-05-13T01:53:06.295012+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4178**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=4178, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.74% | **+1.66%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.74% | **+0.96%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.23% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.73% | **+1.23%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.25% | **+0.22%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.48% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定: 314件 (Win 91 / Loss 111 / Flat 112) / skip 425件
- 成長率目線: 平均log +0.000596 / 幾何平均 +0.060% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $120.56

## 4. Latest Market Context

- 更新: 2026-05-13T01:53:03.206507+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.49% price=81065.2
- Funnel: target 763 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=2, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +18.04% | $2,314,795.71 |
| PEAQ/USDT:USDT | +16.31% | $2,195,354.58 |
| AKT/USDT:USDT | +15.23% | $2,772,483.06 |
| TIA/USDT:USDT | +10.88% | $27,246,393.70 |
| VIC/USDT:USDT | +9.65% | $7,020,321.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_relative_strength | +5.19% | +4.71% |
| PEAQ/USDT:USDT | below_relative_strength | +5.07% | +4.59% |
| NEAR/USDT:USDT | below_1h_threshold | +3.14% | +2.65% |
| TURBO/USDT:USDT | below_1h_threshold | +3.08% | +2.59% |
| TIA/USDT:USDT | below_1h_threshold | +2.90% | +2.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
