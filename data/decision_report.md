# Decision Report

- generated_at: 2026-05-04T11:42:22.783791+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3198**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=3198, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.54% | **+0.38%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.56% | **+0.31%** |
| LIMIT_BB3S | 5/18 | 27.8% | +0.89% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T11:42:18.749407+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=78671.7
- Funnel: target 761 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +95.88% | $10,530,139.72 |
| SKYAI/USDT:USDT | +69.56% | $60,689,591.96 |
| GIGA/USDT:USDT | +54.57% | $1,834,853.10 |
| TAG/USDT:USDT | +41.19% | $15,488,214.57 |
| BSB/USDT:USDT | +35.88% | $28,926,731.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.58% | +4.86% |
| ENSO/USDT:USDT | below_1h_threshold | +1.68% | +1.96% |
| TST/USDT:USDT | below_1h_threshold | +1.47% | +1.75% |
| BANANAS31/USDT:USDT | below_1h_threshold | +1.35% | +1.63% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.20% | +1.48% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
