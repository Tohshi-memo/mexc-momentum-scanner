# Decision Report

- generated_at: 2026-05-05T08:57:20.514757+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3340**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3340, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.17% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_BB3S | 2/12 | 16.7% | +1.29% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.91% | **+2.47%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.37% | **+2.02%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +3.36% | **+1.68%** |
| ASK_LONG | 20/20 | 100.0% | +1.53% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T08:57:18.438610+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80773.0
- Funnel: target 764 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +98.80% | $14,306,338.70 |
| LAB/USDT:USDT | +54.10% | $86,427,839.51 |
| HIVE/USDT:USDT | +36.69% | $4,008,759.00 |
| FHE/USDT:USDT | +34.75% | $4,403,108.18 |
| M/USDT:USDT | +28.83% | $6,735,991.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +1.82% | +1.88% |
| BCH/USDT:USDT | below_1h_threshold | +1.75% | +1.80% |
| PENGU/USDT:USDT | below_1h_threshold | +1.57% | +1.63% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.35% | +1.41% |
| HIVE/USDT:USDT | below_1h_threshold | +1.35% | +1.41% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
