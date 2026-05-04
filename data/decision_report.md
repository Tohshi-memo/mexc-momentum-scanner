# Decision Report

- generated_at: 2026-05-04T06:42:16.711106+00:00
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

- 更新: 2026-05-04T06:42:14.694827+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=79716.9
- Funnel: target 758 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +67.16% | $9,190,337.22 |
| SKYAI/USDT:USDT | +57.79% | $47,792,939.25 |
| BSB/USDT:USDT | +54.51% | $24,336,920.90 |
| LAB/USDT:USDT | +43.61% | $216,091,771.09 |
| TST/USDT:USDT | +36.07% | $6,655,110.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.88% | +5.21% |
| UB/USDT:USDT | below_1h_threshold | +4.46% | +4.79% |
| DASH/USDT:USDT | below_1h_threshold | +3.61% | +3.94% |
| SQD/USDT:USDT | below_1h_threshold | +3.57% | +3.90% |
| LUNC/USDT:USDT | below_1h_threshold | +3.46% | +3.79% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
