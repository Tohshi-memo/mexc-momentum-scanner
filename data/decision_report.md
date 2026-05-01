# Decision Report

- generated_at: 2026-05-01T14:32:13.399788+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2810**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2810, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.38% | **-2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.16% | **+0.15%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.25% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.12% | **+2.50%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.65% | **+2.39%** |
| MARKET_LONG | 20/20 | 100.0% | +1.38% | **+1.38%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.02% | **+1.21%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.20% | **+1.10%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T14:32:11.030944+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.64% price=78190.7
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.7 >= 65=1, 4h RSI 89.3 >= 65=1, 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +109.74% | $24,622,517.35 |
| UB/USDT:USDT | +87.70% | $21,531,607.63 |
| NFP/USDT:USDT | +57.20% | $1,910,041.51 |
| BR/USDT:USDT | +41.14% | $26,267,434.93 |
| ZEREBRO/USDT:USDT | +38.47% | $12,164,426.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +3.35% | +3.98% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +3.05% | +3.69% |
| APE/USDT:USDT | below_1h_threshold | +2.15% | +2.79% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.56% | +2.20% |
| NFP/USDT:USDT | below_1h_threshold | +1.40% | +2.04% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
