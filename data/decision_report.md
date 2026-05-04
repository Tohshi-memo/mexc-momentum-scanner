# Decision Report

- generated_at: 2026-05-04T11:37:26.321991+00:00
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

- 更新: 2026-05-04T11:37:21.509832+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=78779.5
- Funnel: target 761 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +92.47% | $10,411,469.38 |
| SKYAI/USDT:USDT | +67.14% | $60,367,785.38 |
| GIGA/USDT:USDT | +56.82% | $1,821,599.51 |
| TAG/USDT:USDT | +39.91% | $15,391,621.56 |
| 4/USDT:USDT | +36.53% | $1,519,396.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +2.99% | +3.14% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.41% | +1.56% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +1.08% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.93% | +1.07% |
| BANANAS31/USDT:USDT | below_1h_threshold | +0.86% | +1.00% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
