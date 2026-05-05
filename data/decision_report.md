# Decision Report

- generated_at: 2026-05-05T21:57:27.631505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3393**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3393, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.39% | **+0.85%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.50% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.42% | **+1.94%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.23% | **+1.22%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.40% | **+1.08%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.94% | **+1.03%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.52% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:57:24.963439+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=81418.6
- Funnel: target 759 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1, 4h RSI 68.3 >= 65=1, 4h RSI 73.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +30.87% | $21,937,938.20 |
| MAVIA/USDT:USDT | +30.84% | $1,309,812.45 |
| SWARMS/USDT:USDT | +20.94% | $2,333,171.80 |
| ZEC/USDT:USDT | +19.33% | $585,080,199.23 |
| SMCISTOCK/USDT:USDT | +18.17% | $4,891,063.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_1h_threshold | +4.92% | +5.16% |
| SWARMS/USDT:USDT | below_1h_threshold | +3.50% | +3.73% |
| DOGS/USDT:USDT | below_1h_threshold | +3.44% | +3.68% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.13% | +3.37% |
| ONDO/USDT:USDT | below_1h_threshold | +2.91% | +3.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
