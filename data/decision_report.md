# Decision Report

- generated_at: 2026-05-01T15:27:23.582179+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2819**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2819, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 2/16 | 12.5% | +3.33% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.90% | **+1.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T15:27:21.848981+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=78528.4
- Funnel: target 760 → liquid 193 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +122.65% | $32,392,768.84 |
| UB/USDT:USDT | +87.43% | $23,828,441.16 |
| NFP/USDT:USDT | +55.43% | $2,152,786.00 |
| ZEREBRO/USDT:USDT | +36.69% | $12,569,750.54 |
| BR/USDT:USDT | +32.72% | $26,087,162.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.42% | +3.14% |
| APE/USDT:USDT | below_1h_threshold | +3.41% | +3.13% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.74% | +2.47% |
| SIREN/USDT:USDT | below_1h_threshold | +2.38% | +2.11% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.80% | +1.52% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
