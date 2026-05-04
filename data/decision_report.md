# Decision Report

- generated_at: 2026-05-04T12:53:06.451015+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3201**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.62% / filled 20/20。**
- 全期間 MARKET基準: n=3201, expectancy=-0.16%
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
| ASK | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.14% | **+0.28%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.33% | **+0.47%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.92% | **+0.46%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.45% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T12:52:56.428589+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=78912.9
- Funnel: target 761 → liquid 187 → pre 50 → checked 50 → surge 6 → strict 4
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.4 >= 65=1, 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +92.61% | $11,857,511.93 |
| SKYAI/USDT:USDT | +81.23% | $66,827,036.89 |
| GIGA/USDT:USDT | +53.91% | $2,080,638.59 |
| TAG/USDT:USDT | +38.19% | $16,071,664.13 |
| 4/USDT:USDT | +33.33% | $1,647,403.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAPIEN/USDT:USDT | below_1h_threshold | +4.87% | +4.67% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.89% | +3.69% |
| 4/USDT:USDT | below_1h_threshold | +3.71% | +3.51% |
| LUNC/USDT:USDT | below_1h_threshold | +2.95% | +2.75% |
| DASH/USDT:USDT | below_1h_threshold | +2.71% | +2.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
