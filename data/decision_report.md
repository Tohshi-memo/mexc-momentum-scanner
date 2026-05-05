# Decision Report

- generated_at: 2026-05-05T21:47:02.798040+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3391**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3391, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.28% | **+0.45%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +2.33% | **+1.75%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.21% | **+1.22%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.19% | **+1.12%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.62% | **+0.92%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.01% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:47:00.446740+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=81383.4
- Funnel: target 759 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1, 4h RSI 88.0 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +47.81% | $20,211,089.64 |
| MAVIA/USDT:USDT | +29.69% | $1,289,233.22 |
| SWARMS/USDT:USDT | +21.75% | $2,319,320.84 |
| ZEC/USDT:USDT | +21.71% | $575,287,648.11 |
| SMCISTOCK/USDT:USDT | +19.79% | $4,827,629.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SWARMS/USDT:USDT | below_1h_threshold | +4.22% | +4.50% |
| FHE/USDT:USDT | below_1h_threshold | +4.21% | +4.48% |
| MAVIA/USDT:USDT | below_1h_threshold | +3.86% | +4.14% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.69% | +3.96% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.97% | +3.25% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
