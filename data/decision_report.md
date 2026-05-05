# Decision Report

- generated_at: 2026-05-05T20:57:24.864617+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3385**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3385, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.17% | **+0.95%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.67% | **+0.67%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.97% | **+0.63%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | -0.07% | **-0.03%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.42% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.96% | **+1.23%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.49% | **+1.04%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.90% | **+0.77%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.88% | **+0.75%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:57:21.777853+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=81600.6
- Funnel: target 760 → liquid 190 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1, 4h RSI 85.0 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +44.15% | $17,317,540.63 |
| MAVIA/USDT:USDT | +23.28% | $1,068,767.66 |
| SWARMS/USDT:USDT | +18.47% | $2,249,695.03 |
| SMCISTOCK/USDT:USDT | +17.63% | $4,183,007.53 |
| ZEC/USDT:USDT | +13.45% | $504,492,422.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.97% | +4.92% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.66% | +4.60% |
| ZEN/USDT:USDT | below_1h_threshold | +4.63% | +4.57% |
| NOT/USDT:USDT | below_1h_threshold | +4.39% | +4.33% |
| AIN/USDT:USDT | below_1h_threshold | +3.95% | +3.89% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
