# Decision Report

- generated_at: 2026-05-04T14:57:18.696832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3219**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3219, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_BB3S | 3/18 | 16.7% | +1.36% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.07% | **+2.07%** |
| MARKET_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| ASK_LONG | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.85% | **+1.29%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.82% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T14:57:14.409844+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.84% price=80194.6
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ELIZAOS/USDT:USDT | +122.94% | $1,227,427.64 |
| TST/USDT:USDT | +91.54% | $17,930,685.95 |
| SKYAI/USDT:USDT | +89.43% | $86,287,533.92 |
| GIGA/USDT:USDT | +44.95% | $2,261,501.37 |
| ASTEROID/USDT:USDT | +36.14% | $4,516,611.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_relative_strength | +6.42% | +4.58% |
| BANANAS31/USDT:USDT | below_relative_strength | +5.22% | +3.38% |
| PENDLE/USDT:USDT | below_relative_strength | +5.16% | +3.32% |
| B/USDT:USDT | below_1h_threshold | +4.90% | +3.06% |
| ORDI/USDT:USDT | below_1h_threshold | +4.16% | +2.33% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
