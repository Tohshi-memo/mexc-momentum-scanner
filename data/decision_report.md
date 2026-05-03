# Decision Report

- generated_at: 2026-05-03T14:27:05.834205+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3079**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3079, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/16 | 68.8% | +2.20% | **+1.51%** |
| LIMIT_ATR | 18/20 | 90.0% | +1.37% | **+1.24%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.05% | **+0.79%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.81% | **+0.69%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.09% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.81% | **+1.71%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.34% | **+1.51%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.29% | **+1.50%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.50% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T14:27:03.995849+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78625.7
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +44.03% | $4,007,870.03 |
| TAC/USDT:USDT | +35.90% | $3,611,369.79 |
| NAORIS/USDT:USDT | +29.27% | $5,114,140.76 |
| FHE/USDT:USDT | +24.09% | $4,452,768.30 |
| AKT/USDT:USDT | +20.46% | $2,472,606.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.41% | +1.42% |
| THETA/USDT:USDT | below_1h_threshold | +1.23% | +1.24% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.19% | +1.20% |
| FHE/USDT:USDT | below_1h_threshold | +0.82% | +0.83% |
| AKT/USDT:USDT | below_1h_threshold | +0.76% | +0.77% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
