# Decision Report

- generated_at: 2026-05-03T07:12:04.483521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3046**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3046, expectancy=-0.15%
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
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_BB3S | 8/12 | 66.7% | +0.66% | **+0.44%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.68% | **+0.30%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.66% | **+2.02%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.39% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T07:12:02.651266+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=78357.0
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +52.60% | $6,059,672.12 |
| BR/USDT:USDT | +31.02% | $2,840,652.85 |
| AIGENSYN/USDT:USDT | +24.65% | $2,552,407.38 |
| BSB/USDT:USDT | +15.32% | $14,982,470.80 |
| FHE/USDT:USDT | +14.45% | $2,615,769.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.91% | +4.77% |
| BABY/USDT:USDT | below_1h_threshold | +3.56% | +3.42% |
| TAC/USDT:USDT | below_1h_threshold | +2.75% | +2.61% |
| FHE/USDT:USDT | below_1h_threshold | +2.55% | +2.41% |
| LUNC/USDT:USDT | below_1h_threshold | +0.99% | +0.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
