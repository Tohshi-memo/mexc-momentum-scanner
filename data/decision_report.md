# Decision Report

- generated_at: 2026-05-01T08:11:09.251222+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2768**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2768, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.52% | **+0.50%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.09% | **+0.07%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.08% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.96% | **+1.31%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.04% | **+1.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.13% | **+0.79%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.30% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T08:11:07.718200+00:00 / 保存件数 238/288
- BTC: STAGNANT 1h +0.03% price=77119.6
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +62.23% | $2,889,047.76 |
| ZEREBRO/USDT:USDT | +55.70% | $5,044,321.79 |
| ORCA/USDT:USDT | +29.13% | $10,165,709.99 |
| BR/USDT:USDT | +20.67% | $20,491,611.32 |
| GENIUS/USDT:USDT | +17.37% | $1,595,102.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ST/USDT:USDT | below_1h_threshold | +4.77% | +4.74% |
| B/USDT:USDT | below_1h_threshold | +2.59% | +2.56% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.30% | +2.28% |
| LINSTOCK/USDT:USDT | below_1h_threshold | +2.16% | +2.13% |
| BR/USDT:USDT | below_1h_threshold | +1.80% | +1.77% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
