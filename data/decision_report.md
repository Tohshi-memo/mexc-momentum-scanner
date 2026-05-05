# Decision Report

- generated_at: 2026-05-05T22:27:19.439552+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3396**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3396, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.16% | **+0.52%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.46% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.84% | **+0.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +2.49% | **+2.12%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.73% | **+1.37%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.83% | **+1.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.38% | **+0.97%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.49% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T22:27:16.841948+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81387.9
- Funnel: target 759 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1, 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +28.01% | $23,440,073.60 |
| MAVIA/USDT:USDT | +24.84% | $1,420,046.11 |
| ZEC/USDT:USDT | +21.07% | $580,458,067.75 |
| SWARMS/USDT:USDT | +20.93% | $2,330,266.01 |
| SMCISTOCK/USDT:USDT | +19.15% | $4,982,088.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +4.09% | +4.06% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.53% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.13% | +2.10% |
| STRK/USDT:USDT | below_1h_threshold | +2.13% | +2.10% |
| NOT/USDT:USDT | below_1h_threshold | +2.00% | +1.97% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
