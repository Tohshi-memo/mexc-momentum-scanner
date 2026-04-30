# Decision Report

- generated_at: 2026-04-30T19:55:58.388720+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2731**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2731, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +3.21% | **+2.73%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +6.41% | **+2.57%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T19:55:56.412378+00:00 / 保存件数 88/288
- BTC: STAGNANT 1h +0.04% price=76337.9
- Funnel: target 757 → liquid 225 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +21.43% | $9,471,332.65 |
| DRIFT/USDT:USDT | +14.18% | $1,102,908.79 |
| AIOT/USDT:USDT | +9.52% | $16,770,177.76 |
| ORCA/USDT:USDT | +9.44% | $2,840,724.59 |
| NAORIS/USDT:USDT | +8.93% | $11,002,239.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STXSTOCK/USDT:USDT | below_1h_threshold | +3.88% | +3.84% |
| BLEND/USDT:USDT | below_1h_threshold | +3.51% | +3.48% |
| ZBCN/USDT:USDT | below_1h_threshold | +3.20% | +3.17% |
| AIOT/USDT:USDT | below_1h_threshold | +2.98% | +2.95% |
| APE/USDT:USDT | below_1h_threshold | +2.59% | +2.55% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
