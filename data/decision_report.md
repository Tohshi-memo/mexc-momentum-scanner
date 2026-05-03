# Decision Report

- generated_at: 2026-05-03T00:37:32.890642+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3002**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3002, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.56% | **+0.51%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.21% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.41% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T00:37:30.654325+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78623.9
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1, 4h RSI 93.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +35.19% | $1,824,815.24 |
| LUNC/USDT:USDT | +19.52% | $31,834,848.85 |
| BIANRENSHENG/USDT:USDT | +15.61% | $1,768,730.44 |
| SPACE/USDT:USDT | +14.25% | $1,738,170.15 |
| BABY/USDT:USDT | +13.97% | $1,456,625.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +4.40% | +4.44% |
| SPACE/USDT:USDT | below_1h_threshold | +3.87% | +3.91% |
| LUNC/USDT:USDT | below_1h_threshold | +2.61% | +2.64% |
| EDGE/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |
| TAC/USDT:USDT | below_1h_threshold | +1.21% | +1.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
