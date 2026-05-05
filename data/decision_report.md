# Decision Report

- generated_at: 2026-05-05T08:27:20.721263+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3336**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3336, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.77% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_BB3S | 2/13 | 15.4% | +1.29% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.80% | **+3.23%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.90% | **+2.94%** |
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| ASK_LONG | 20/20 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.71% | **+1.88%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T08:27:18.317179+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80834.5
- Funnel: target 765 → liquid 200 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +114.71% | $12,963,523.83 |
| LAB/USDT:USDT | +48.85% | $82,181,912.46 |
| HIVE/USDT:USDT | +37.76% | $3,862,822.32 |
| FHE/USDT:USDT | +34.75% | $4,268,866.99 |
| M/USDT:USDT | +30.69% | $6,243,378.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOT/USDT:USDT | below_1h_threshold | +4.66% | +4.64% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.76% | +2.74% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +2.41% | +2.39% |
| HIVE/USDT:USDT | below_1h_threshold | +2.28% | +2.26% |
| FLOKI/USDT:USDT | below_1h_threshold | +0.97% | +0.95% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
