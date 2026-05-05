# Decision Report

- generated_at: 2026-05-05T21:07:32.675204+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3386**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3386, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.33% | **+0.70%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.73% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.16% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.34% | **+0.13%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.42% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +1.96% | **+1.09%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.48% | **+1.04%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.97% | **+0.83%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.88% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:07:30.744365+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=81605.5
- Funnel: target 759 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +45.02% | $18,196,317.02 |
| MAVIA/USDT:USDT | +27.19% | $1,117,901.78 |
| ZEC/USDT:USDT | +18.21% | $525,738,810.80 |
| SMCISTOCK/USDT:USDT | +18.21% | $4,317,201.31 |
| SWARMS/USDT:USDT | +16.69% | $2,247,355.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +3.84% | +3.85% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.39% | +2.39% |
| FHE/USDT:USDT | below_1h_threshold | +2.17% | +2.18% |
| MAVIA/USDT:USDT | below_1h_threshold | +1.91% | +1.91% |
| 4/USDT:USDT | below_1h_threshold | +1.77% | +1.78% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
