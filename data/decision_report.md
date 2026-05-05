# Decision Report

- generated_at: 2026-05-05T22:22:33.491817+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3395**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3395, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +2.83% | **+0.57%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.76% | **+0.38%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.35% | **+0.28%** |
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

- 更新: 2026-05-05T22:22:31.026090+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=81324.9
- Funnel: target 759 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +34.69% | $23,104,770.91 |
| MAVIA/USDT:USDT | +25.40% | $1,407,777.30 |
| ZEC/USDT:USDT | +21.51% | $579,025,495.86 |
| SWARMS/USDT:USDT | +20.99% | $2,324,811.05 |
| SMCISTOCK/USDT:USDT | +19.00% | $4,979,566.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +3.10% | +3.15% |
| CFX/USDT:USDT | below_1h_threshold | +3.06% | +3.10% |
| STRK/USDT:USDT | below_1h_threshold | +1.96% | +2.00% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.89% | +1.94% |
| HMSTR/USDT:USDT | below_1h_threshold | +1.62% | +1.66% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
