# Decision Report

- generated_at: 2026-05-06T08:07:22.171657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3433**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3433, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.29% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.46% | **+1.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.79% | **+0.79%** |
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.53% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T08:07:20.172422+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=81531.8
- Funnel: target 765 → liquid 197 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +66.92% | $7,370,262.81 |
| ZEC/USDT:USDT | +40.43% | $699,978,544.76 |
| B3/USDT:USDT | +30.53% | $1,444,698.21 |
| STORJ/USDT:USDT | +28.82% | $2,489,126.35 |
| FHE/USDT:USDT | +23.29% | $28,579,731.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_1h_threshold | +3.12% | +2.88% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.30% | +2.05% |
| LAB/USDT:USDT | below_1h_threshold | +2.13% | +1.89% |
| FHE/USDT:USDT | below_1h_threshold | +1.92% | +1.67% |
| ZEC/USDT:USDT | below_1h_threshold | +1.53% | +1.29% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
