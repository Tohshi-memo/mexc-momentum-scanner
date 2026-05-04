# Decision Report

- generated_at: 2026-05-04T17:37:36.288218+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3244**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3244, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.39% | **+1.43%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.08% | **+0.87%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T17:37:31.534741+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=80303.6
- Funnel: target 761 → liquid 203 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +18.25% | $36,866,094.52 |
| TST/USDT:USDT | +17.79% | $21,252,946.22 |
| FHE/USDT:USDT | +12.87% | $2,892,690.98 |
| RAVE/USDT:USDT | +6.52% | $11,566,638.69 |
| AIOZ/USDT:USDT | +4.43% | $1,377,613.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SQD/USDT:USDT | below_1h_threshold | +4.02% | +3.62% |
| OL/USDT:USDT | below_1h_threshold | +3.45% | +3.05% |
| QUBIC/USDT:USDT | below_1h_threshold | +3.40% | +3.00% |
| FHE/USDT:USDT | below_1h_threshold | +3.19% | +2.78% |
| AIOZ/USDT:USDT | below_1h_threshold | +2.40% | +2.00% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
