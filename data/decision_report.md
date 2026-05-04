# Decision Report

- generated_at: 2026-05-04T06:17:16.590490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3164**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=3164, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 14/20 | 70.0% | +1.31% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.83% | **+0.54%** |
| LIMIT_BB3S | 2/11 | 18.2% | +2.74% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +0.27% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T06:17:14.694752+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=79800.0
- Funnel: target 758 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +62.77% | $23,484,366.24 |
| TAG/USDT:USDT | +59.37% | $8,279,709.64 |
| SKYAI/USDT:USDT | +54.57% | $46,996,670.58 |
| LAB/USDT:USDT | +46.57% | $214,709,971.06 |
| TST/USDT:USDT | +38.99% | $6,568,300.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.77% | +4.00% |
| SQD/USDT:USDT | below_1h_threshold | +3.60% | +3.83% |
| UB/USDT:USDT | below_1h_threshold | +2.96% | +3.19% |
| AIOT/USDT:USDT | below_1h_threshold | +2.39% | +2.62% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.68% | +1.91% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
