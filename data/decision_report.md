# Decision Report

- generated_at: 2026-05-03T22:22:06.740552+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3110**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3110, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.33% | **-1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.08% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.48% | **+2.43%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.47% | **+2.22%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.54% | **+1.66%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.64% | **+1.55%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T22:22:04.909212+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=79168.9
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +60.52% | $266,390,140.17 |
| SKYAI/USDT:USDT | +16.92% | $26,176,627.78 |
| TAG/USDT:USDT | +16.64% | $3,966,134.72 |
| MERL/USDT:USDT | +13.79% | $1,244,928.06 |
| BSB/USDT:USDT | +13.09% | $15,656,901.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PNUT/USDT:USDT | below_1h_threshold | +2.48% | +2.00% |
| ZEN/USDT:USDT | below_1h_threshold | +2.31% | +1.84% |
| SPX/USDT:USDT | below_1h_threshold | +2.17% | +1.70% |
| MERL/USDT:USDT | below_1h_threshold | +2.04% | +1.56% |
| AIOT/USDT:USDT | below_1h_threshold | +1.88% | +1.40% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
