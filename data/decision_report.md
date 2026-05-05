# Decision Report

- generated_at: 2026-05-05T04:02:25.500556+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3304**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3304, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.29% | **+0.64%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_BB3S | 5/10 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.35% | **+1.28%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.03% | **+0.77%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.95% | **+0.62%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.48% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T04:02:23.527598+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80814.2
- Funnel: target 764 → liquid 204 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +71.95% | $5,457,434.99 |
| 4/USDT:USDT | +23.77% | $1,981,088.69 |
| FHE/USDT:USDT | +20.72% | $3,232,978.12 |
| TONCOIN/USDT:USDT | +20.07% | $62,344,393.38 |
| NOT/USDT:USDT | +19.25% | $2,137,402.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +2.16% | +2.19% |
| B3/USDT:USDT | below_1h_threshold | +0.68% | +0.71% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.50% | +0.53% |
| RAVE/USDT:USDT | below_1h_threshold | +0.45% | +0.47% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.42% | +0.44% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
