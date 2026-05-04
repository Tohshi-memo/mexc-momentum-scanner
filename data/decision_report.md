# Decision Report

- generated_at: 2026-05-04T17:12:32.545717+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3243**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3243, expectancy=-0.17%
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
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +8.00% | **+5.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.57% | **+0.86%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T17:12:30.635638+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=80303.3
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +20.11% | $34,659,645.94 |
| TST/USDT:USDT | +20.04% | $20,773,244.14 |
| FHE/USDT:USDT | +10.96% | $2,723,024.72 |
| TAG/USDT:USDT | +7.57% | $17,914,290.25 |
| GIGGLE/USDT:USDT | +5.22% | $5,060,843.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.55% | +3.14% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.66% | +2.26% |
| RAVE/USDT:USDT | below_1h_threshold | +2.45% | +2.05% |
| AGT/USDT:USDT | below_1h_threshold | +1.62% | +1.22% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.50% | +1.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
