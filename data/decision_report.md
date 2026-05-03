# Decision Report

- generated_at: 2026-05-03T08:17:11.103208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3052**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3052, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_BB3S | 10/13 | 76.9% | +0.26% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.78% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.07% | **+1.84%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.19% | **+1.42%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.43% | **+1.09%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T08:17:09.119979+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=78437.1
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +64.10% | $9,925,581.05 |
| BR/USDT:USDT | +21.03% | $3,692,998.05 |
| FHE/USDT:USDT | +19.47% | $2,784,187.47 |
| TAC/USDT:USDT | +19.04% | $2,709,218.79 |
| AIGENSYN/USDT:USDT | +16.52% | $3,264,671.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_relative_strength | +5.13% | +4.97% |
| BABY/USDT:USDT | below_1h_threshold | +4.91% | +4.75% |
| FHE/USDT:USDT | below_1h_threshold | +3.16% | +3.01% |
| ALCH/USDT:USDT | below_1h_threshold | +2.60% | +2.45% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.22% | +2.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
