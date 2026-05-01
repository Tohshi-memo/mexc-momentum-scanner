# Decision Report

- generated_at: 2026-05-01T00:01:16.793153+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2743**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2743, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.21% | **-2.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.97% | **+2.78%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.03% | **+2.73%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.17% | **+2.29%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.26% | **+2.13%** |
| ASK_LONG | 20/20 | 100.0% | +1.96% | **+1.96%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T00:01:15.180333+00:00 / 保存件数 138/288
- BTC: STAGNANT 1h +0.04% price=76331.4
- Funnel: target 757 → liquid 210 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +41.40% | $5,503,305.23 |
| BR/USDT:USDT | +21.56% | $14,985,526.51 |
| DRIFT/USDT:USDT | +16.31% | $1,481,700.80 |
| GENIUS/USDT:USDT | +14.70% | $1,176,314.03 |
| RDDTSTOCK/USDT:USDT | +13.32% | $3,992,444.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CVNASTOCK/USDT:USDT | below_1h_threshold | +3.65% | +3.61% |
| ENSO/USDT:USDT | below_1h_threshold | +2.44% | +2.40% |
| AIOT/USDT:USDT | below_1h_threshold | +0.66% | +0.62% |
| MEGA/USDT:USDT | below_1h_threshold | +0.66% | +0.62% |
| SOMI/USDT:USDT | below_1h_threshold | +0.43% | +0.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
