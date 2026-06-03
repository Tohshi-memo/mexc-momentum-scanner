# Decision Report

- generated_at: 2026-06-03T04:11:01.655974+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5517**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=5517, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.67% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.42% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | -0.12% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1101件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-03T04:10:59.295449+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.79% price=66338.2
- Funnel: target 773 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +34.38% | $13,814,626.83 |
| CLO/USDT:USDT | +24.61% | $2,051,687.57 |
| GENIUS/USDT:USDT | +22.18% | $1,512,236.71 |
| MRVLSTOCK/USDT:USDT | +20.07% | $17,726,201.22 |
| BBSTOCK/USDT:USDT | +19.95% | $1,889,575.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_relative_strength | +5.43% | +4.63% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.76% | +1.96% |
| RENDER/USDT:USDT | below_1h_threshold | +2.67% | +1.88% |
| BILL/USDT:USDT | below_1h_threshold | +2.36% | +1.56% |
| ENA/USDT:USDT | below_1h_threshold | +2.21% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
