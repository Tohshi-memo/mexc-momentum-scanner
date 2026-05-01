# Decision Report

- generated_at: 2026-05-01T06:01:06.743975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2754**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2754, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.23% | **+0.78%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.12% | **+0.09%** |
| ASK | 20/20 | 100.0% | -0.04% | **-0.04%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.10% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.56% | **+1.15%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.06% | **+0.69%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.76% | **+0.61%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T06:01:05.112647+00:00 / 保存件数 212/288
- BTC: STAGNANT 1h -0.02% price=77122.7
- Funnel: target 760 → liquid 202 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +32.90% | $9,805,556.89 |
| BR/USDT:USDT | +31.15% | $18,320,011.40 |
| ZEREBRO/USDT:USDT | +25.54% | $2,079,213.74 |
| GENIUS/USDT:USDT | +17.55% | $1,475,462.73 |
| AIOT/USDT:USDT | +16.06% | $17,962,298.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +0.82% | +0.83% |
| ZBT/USDT:USDT | below_1h_threshold | +0.43% | +0.44% |
| CYS/USDT:USDT | below_1h_threshold | +0.36% | +0.37% |
| NOM/USDT:USDT | below_1h_threshold | +0.30% | +0.32% |
| PLAY/USDT:USDT | below_1h_threshold | +0.28% | +0.30% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
