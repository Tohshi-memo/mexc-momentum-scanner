# Decision Report

- generated_at: 2026-05-06T01:27:26.698421+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3402**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3402, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 15/20 | 75.0% | +1.13% | **+0.85%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.39% | **+0.56%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.84% | **+0.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.14% | **+0.46%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.62% | **+0.39%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T01:27:24.511597+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=81211.0
- Funnel: target 761 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +43.21% | $1,153,460.14 |
| MAVIA/USDT:USDT | +28.93% | $1,670,568.81 |
| FHE/USDT:USDT | +24.10% | $28,119,105.23 |
| ZEC/USDT:USDT | +21.01% | $597,851,168.37 |
| SWARMS/USDT:USDT | +20.22% | $2,378,502.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +4.32% | +4.04% |
| DOGS/USDT:USDT | below_1h_threshold | +3.19% | +2.90% |
| GIGGLE/USDT:USDT | below_1h_threshold | +3.14% | +2.85% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.64% | +2.36% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.57% | +2.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
