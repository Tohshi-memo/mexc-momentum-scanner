# Decision Report

- generated_at: 2026-05-01T13:52:22.772203+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2804**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2804, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.87% | **-1.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.05% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.46% | **+2.34%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.70% | **+2.30%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.17% | **+1.30%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T13:52:14.625566+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.68% price=78376.9
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 7 → strict 2
- Surge前reject: below_1h_threshold=42, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 68.3 >= 65=1, 4h RSI 72.7 >= 65=1, 4h RSI 70.5 >= 65=1, 4h RSI 66.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +85.64% | $19,145,167.19 |
| UB/USDT:USDT | +65.00% | $21,038,758.61 |
| NFP/USDT:USDT | +52.05% | $1,649,958.71 |
| BR/USDT:USDT | +43.76% | $26,107,933.92 |
| ORCA/USDT:USDT | +34.12% | $11,729,097.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUSTOCK/USDT:USDT | below_relative_strength | +5.10% | +4.42% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.55% | +3.87% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.39% | +3.71% |
| BR/USDT:USDT | below_1h_threshold | +3.56% | +2.88% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.61% | +1.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
