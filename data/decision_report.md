# Decision Report

- generated_at: 2026-05-05T21:27:25.220416+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3389**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3389, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.88% | **-1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.96% | **+1.04%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.21% | **+0.54%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.43% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.44% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.88% | **+2.01%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.91% | **+1.46%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.07% | **+1.22%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.47% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T21:27:22.525744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=81530.6
- Funnel: target 759 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1, 4h RSI 87.6 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +46.63% | $19,188,880.50 |
| MAVIA/USDT:USDT | +30.84% | $1,211,236.11 |
| SMCISTOCK/USDT:USDT | +21.95% | $4,571,747.72 |
| ZEC/USDT:USDT | +21.07% | $549,221,288.61 |
| SWARMS/USDT:USDT | +20.17% | $2,270,420.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAVIA/USDT:USDT | below_1h_threshold | +4.64% | +4.74% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.21% | +4.30% |
| FHE/USDT:USDT | below_1h_threshold | +3.57% | +3.67% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +3.25% | +3.35% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.10% | +3.20% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
