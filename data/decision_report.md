# Decision Report

- generated_at: 2026-05-04T20:42:17.477218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3258**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3258, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.60% | **+0.88%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.92% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.13% | **+0.83%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.54% | **+0.51%** |
| LIMIT_BB3S | 2/12 | 16.7% | +2.06% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.48% | **+0.75%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.43%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.62% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T20:42:15.559794+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=79892.4
- Funnel: target 760 → liquid 201 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +43.15% | $38,891,629.80 |
| TST/USDT:USDT | +12.20% | $22,635,476.47 |
| SKYAI/USDT:USDT | +11.79% | $102,368,238.60 |
| FHE/USDT:USDT | +9.47% | $2,634,234.65 |
| LUNC/USDT:USDT | +7.37% | $71,630,832.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.74% | +3.90% |
| AIOZ/USDT:USDT | below_1h_threshold | +2.89% | +3.04% |
| RAVE/USDT:USDT | below_1h_threshold | +2.76% | +2.91% |
| MUBARAK/USDT:USDT | below_1h_threshold | +2.74% | +2.90% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.30% | +2.46% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
