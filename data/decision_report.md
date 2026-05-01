# Decision Report

- generated_at: 2026-05-01T03:15:57.427752+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2750**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2750, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.26% | **-0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.88% | **+0.35%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 3/20 | 15.0% | -0.70% | **-0.10%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.16% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.87% | **+1.29%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.57% | **+1.02%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| MARKET_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.99% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T03:15:56.073098+00:00 / 保存件数 178/288
- BTC: STAGNANT 1h +0.17% price=76685.9
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +26.90% | $9,112,585.39 |
| BR/USDT:USDT | +23.91% | $16,747,049.11 |
| GENIUS/USDT:USDT | +18.48% | $1,430,571.11 |
| ASTEROID/USDT:USDT | +15.95% | $4,019,044.32 |
| RDDTSTOCK/USDT:USDT | +14.10% | $3,917,073.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRB/USDT:USDT | below_1h_threshold | +3.44% | +3.27% |
| UB/USDT:USDT | below_1h_threshold | +3.25% | +3.08% |
| AXS/USDT:USDT | below_1h_threshold | +2.24% | +2.06% |
| ZBT/USDT:USDT | below_1h_threshold | +1.72% | +1.55% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.55% | +1.38% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
