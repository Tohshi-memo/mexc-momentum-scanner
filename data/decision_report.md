# Decision Report

- generated_at: 2026-05-01T00:09:06.348111+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2744**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2744, expectancy=-0.12%
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
| LIMIT_4PCT | 16/20 | 80.0% | +0.05% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.03% | **+2.73%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.84% | **+2.69%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.99% | **+2.19%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.18% | **+2.09%** |
| ASK_LONG | 20/20 | 100.0% | +1.97% | **+1.97%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T00:09:04.769141+00:00 / 保存件数 140/288
- BTC: STAGNANT 1h +0.15% price=76412.4
- Funnel: target 757 → liquid 212 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +50.16% | $5,954,552.46 |
| BR/USDT:USDT | +23.73% | $15,091,782.81 |
| AIOT/USDT:USDT | +16.63% | $18,461,848.75 |
| DRIFT/USDT:USDT | +15.10% | $1,496,179.25 |
| GENIUS/USDT:USDT | +14.41% | $1,181,016.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ORCA/USDT:USDT | below_1h_threshold | +4.87% | +4.72% |
| ENSO/USDT:USDT | below_1h_threshold | +4.62% | +4.47% |
| AIOT/USDT:USDT | below_1h_threshold | +4.00% | +3.85% |
| CVNASTOCK/USDT:USDT | below_1h_threshold | +2.66% | +2.51% |
| BR/USDT:USDT | below_1h_threshold | +1.70% | +1.55% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
