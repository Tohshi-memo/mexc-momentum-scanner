# Decision Report

- generated_at: 2026-05-02T13:26:58.349471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2906**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2906, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -0.22% | **-0.07%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.36% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.83% | **+1.72%** |
| MARKET_LONG | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.63% | **+1.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T13:26:56.541362+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=78277.3
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +220.56% | $131,832,082.81 |
| TAG/USDT:USDT | +41.88% | $6,470,448.21 |
| BIO/USDT:USDT | +30.11% | $2,426,825.42 |
| SKYAI/USDT:USDT | +29.60% | $20,821,750.84 |
| SPACE/USDT:USDT | +26.58% | $1,292,064.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.82% | +3.68% |
| TAG/USDT:USDT | below_1h_threshold | +3.51% | +3.37% |
| BB/USDT:USDT | below_1h_threshold | +2.26% | +2.12% |
| SPACE/USDT:USDT | below_1h_threshold | +2.09% | +1.95% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.07% | +1.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
