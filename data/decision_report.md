# Decision Report

- generated_at: 2026-05-05T21:02:36.334700+00:00
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

- 更新: 2026-05-05T21:02:34.322356+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81583.8
- Funnel: target 759 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +40.14% | $17,767,409.66 |
| MAVIA/USDT:USDT | +25.66% | $1,079,680.86 |
| SMCISTOCK/USDT:USDT | +18.10% | $4,299,765.70 |
| SWARMS/USDT:USDT | +16.58% | $2,240,431.32 |
| ZEC/USDT:USDT | +15.43% | $500,396,385.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VET/USDT:USDT | below_1h_threshold | +1.70% | +1.73% |
| ZEC/USDT:USDT | below_1h_threshold | +1.57% | +1.60% |
| DASH/USDT:USDT | below_1h_threshold | +1.20% | +1.23% |
| AIN/USDT:USDT | below_1h_threshold | +1.05% | +1.08% |
| ZEN/USDT:USDT | below_1h_threshold | +1.05% | +1.08% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
