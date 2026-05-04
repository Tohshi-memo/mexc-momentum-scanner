# Decision Report

- generated_at: 2026-05-04T18:27:16.402194+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3248**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=3248, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.50% | **+1.35%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.33% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.97% | **+0.69%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.84% | **+0.54%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.76% | **+0.38%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T18:27:14.259552+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=80120.1
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +18.49% | $41,507,508.68 |
| TST/USDT:USDT | +11.00% | $21,861,418.47 |
| FHE/USDT:USDT | +9.10% | $2,820,407.72 |
| QUBIC/USDT:USDT | +8.14% | $7,216,610.97 |
| RAVE/USDT:USDT | +7.78% | $13,330,270.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QUBIC/USDT:USDT | below_1h_threshold | +2.87% | +3.14% |
| BB/USDT:USDT | below_1h_threshold | +2.68% | +2.96% |
| M/USDT:USDT | below_1h_threshold | +2.38% | +2.65% |
| RAVE/USDT:USDT | below_1h_threshold | +1.83% | +2.10% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.15% | +1.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
