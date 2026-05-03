# Decision Report

- generated_at: 2026-05-03T21:47:05.667883+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3109**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3109, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.93% | **-1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.08% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.14% | **+2.82%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.05% | **+2.63%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.11% | **+2.01%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.16% | **+1.58%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T21:47:03.796686+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=78641.8
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +67.47% | $289,640,579.47 |
| SKYAI/USDT:USDT | +20.08% | $27,095,209.78 |
| TAG/USDT:USDT | +13.33% | $4,092,642.00 |
| BSB/USDT:USDT | +12.21% | $15,811,797.75 |
| MERL/USDT:USDT | +10.26% | $1,233,290.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.62% | +4.93% |
| LUNC/USDT:USDT | below_1h_threshold | +3.13% | +3.44% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.97% | +3.29% |
| BSB/USDT:USDT | below_1h_threshold | +2.14% | +2.46% |
| PARTI/USDT:USDT | below_1h_threshold | +1.66% | +1.98% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
