# Decision Report

- generated_at: 2026-05-04T13:57:27.742573+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3210**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3210, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.38% | **+0.41%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.01% | **+2.10%** |
| ASK_LONG | 20/20 | 100.0% | +2.03% | **+2.03%** |
| MARKET_LONG | 20/20 | 100.0% | +1.63% | **+1.63%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.20% | **+1.54%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.28% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T13:57:24.463554+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78772.4
- Funnel: target 761 → liquid 192 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1, 4h RSI 77.7 >= 65=1, 4h RSI 77.3 >= 65=1, 4h RSI 79.9 >= 65=1, 4h RSI 78.1 >= 65=1, 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +112.92% | $15,387,489.24 |
| SKYAI/USDT:USDT | +90.41% | $76,794,663.88 |
| GIGA/USDT:USDT | +46.97% | $2,176,181.68 |
| 4/USDT:USDT | +39.55% | $1,773,173.64 |
| TAG/USDT:USDT | +32.22% | $16,584,947.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +4.04% | +4.10% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.54% | +3.60% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +3.44% | +3.49% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.25% | +3.31% |
| SIREN/USDT:USDT | below_1h_threshold | +3.23% | +3.29% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
