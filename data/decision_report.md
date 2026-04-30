# Decision Report

- generated_at: 2026-04-30T21:25:51.243866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2735**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2735, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.46% | **+1.97%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.03% | **+1.81%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.76% | **+1.67%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T21:25:49.726571+00:00 / 保存件数 106/288
- BTC: STAGNANT 1h -0.12% price=76359.9
- Funnel: target 756 → liquid 223 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +19.55% | $12,495,852.29 |
| GENIUS/USDT:USDT | +12.97% | $1,074,723.82 |
| AIOT/USDT:USDT | +11.70% | $16,743,707.70 |
| NAORIS/USDT:USDT | +11.39% | $12,063,646.47 |
| DRIFT/USDT:USDT | +11.17% | $1,241,860.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +4.77% | +4.89% |
| ORCA/USDT:USDT | below_1h_threshold | +1.99% | +2.11% |
| BLEND/USDT:USDT | below_1h_threshold | +1.93% | +2.05% |
| AIOT/USDT:USDT | below_1h_threshold | +1.80% | +1.92% |
| ENSO/USDT:USDT | below_1h_threshold | +1.70% | +1.82% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
