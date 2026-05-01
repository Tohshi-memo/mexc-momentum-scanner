# Decision Report

- generated_at: 2026-05-01T04:35:59.827285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2752**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2752, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.99% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.22% | **+0.18%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.12% | **+0.09%** |
| LIMIT_2PCT | 17/20 | 85.0% | -0.10% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.66% | **+1.20%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.06% | **+0.90%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.13% | **+0.73%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T04:35:57.762040+00:00 / 保存件数 195/288
- BTC: STAGNANT 1h -0.05% price=77042.8
- Funnel: target 760 → liquid 204 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORCA/USDT:USDT | +27.30% | $9,591,095.89 |
| BR/USDT:USDT | +25.66% | $17,193,930.99 |
| ZEREBRO/USDT:USDT | +23.59% | $1,871,569.73 |
| ASTEROID/USDT:USDT | +16.90% | $4,206,712.45 |
| GENIUS/USDT:USDT | +16.37% | $1,454,240.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +3.00% | +3.05% |
| AIOT/USDT:USDT | below_1h_threshold | +2.80% | +2.85% |
| BIO/USDT:USDT | below_1h_threshold | +2.43% | +2.48% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.34% | +2.39% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.56% | +1.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
