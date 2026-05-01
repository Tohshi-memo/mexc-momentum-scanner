# Decision Report

- generated_at: 2026-05-01T14:02:21.649769+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2806**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2806, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.87% | **-1.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.11% | **+1.79%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.83% | **+1.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.02% | **+0.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.17% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T14:02:19.960226+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78663.8
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +97.12% | $20,551,968.33 |
| UB/USDT:USDT | +72.29% | $20,391,898.72 |
| NFP/USDT:USDT | +57.11% | $1,717,118.82 |
| BR/USDT:USDT | +43.88% | $25,913,184.50 |
| ORCA/USDT:USDT | +34.18% | $11,643,552.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.92% | +2.96% |
| UB/USDT:USDT | below_1h_threshold | +2.63% | +2.67% |
| NFP/USDT:USDT | below_1h_threshold | +1.46% | +1.49% |
| ST/USDT:USDT | below_1h_threshold | +1.06% | +1.09% |
| CVNASTOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.98% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
