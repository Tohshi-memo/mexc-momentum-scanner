# Decision Report

- generated_at: 2026-05-05T20:02:51.369289+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3377**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3377, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.59% | **+0.72%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.75% | **+0.37%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.10% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +2.48% | **+1.98%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.51% | **+0.43%** |
| ASK_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.94% | **+0.19%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.24% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:02:49.441625+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=81610.0
- Funnel: target 760 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +31.61% | $13,782,585.01 |
| STX/USDT:USDT | +19.56% | $3,397,613.93 |
| SWARMS/USDT:USDT | +15.04% | $2,169,636.30 |
| TONCOIN/USDT:USDT | +6.64% | $169,752,706.50 |
| H/USDT:USDT | +4.38% | $10,433,278.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STX/USDT:USDT | below_1h_threshold | +4.73% | +4.66% |
| LAB/USDT:USDT | below_1h_threshold | +1.35% | +1.29% |
| VET/USDT:USDT | below_1h_threshold | +1.35% | +1.28% |
| GALA/USDT:USDT | below_1h_threshold | +0.80% | +0.73% |
| PYPLSTOCK/USDT:USDT | below_1h_threshold | +0.77% | +0.71% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
