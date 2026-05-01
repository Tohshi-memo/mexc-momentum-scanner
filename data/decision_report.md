# Decision Report

- generated_at: 2026-05-01T09:06:50.207303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2778**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2778, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.24% | **+2.27%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.69% | **+1.88%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.37% | **+1.69%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.22% | **+1.66%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T09:06:48.578511+00:00 / 保存件数 249/288
- BTC: STAGNANT 1h -0.05% price=77300.1
- Funnel: target 760 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +69.03% | $6,572,897.67 |
| BR/USDT:USDT | +45.85% | $22,132,892.95 |
| ZEREBRO/USDT:USDT | +44.00% | $6,247,443.05 |
| ORCA/USDT:USDT | +28.52% | $10,247,306.76 |
| UB/USDT:USDT | +25.53% | $10,518,070.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.94% | +3.99% |
| AIOT/USDT:USDT | below_1h_threshold | +3.40% | +3.45% |
| UB/USDT:USDT | below_1h_threshold | +2.43% | +2.48% |
| DRIFT/USDT:USDT | below_1h_threshold | +2.34% | +2.39% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.65% | +1.70% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
