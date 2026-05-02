# Decision Report

- generated_at: 2026-05-02T14:02:16.371675+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2911**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2911, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_BB3S | 10/16 | 62.5% | -0.11% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.91% | **+1.76%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.22% | **+1.13%** |
| MARKET_LONG | 20/20 | 100.0% | +0.99% | **+0.99%** |
| ASK_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T14:02:14.559780+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78342.5
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +240.37% | $138,307,094.88 |
| TAG/USDT:USDT | +52.65% | $7,005,184.83 |
| BIO/USDT:USDT | +42.61% | $2,933,530.16 |
| SKYAI/USDT:USDT | +25.38% | $18,402,107.04 |
| SPACE/USDT:USDT | +24.92% | $1,349,467.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.95% | +2.93% |
| BIO/USDT:USDT | below_1h_threshold | +1.44% | +1.43% |
| TAG/USDT:USDT | below_1h_threshold | +1.39% | +1.38% |
| B/USDT:USDT | below_1h_threshold | +1.06% | +1.05% |
| ORDI/USDT:USDT | below_1h_threshold | +0.73% | +0.71% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
