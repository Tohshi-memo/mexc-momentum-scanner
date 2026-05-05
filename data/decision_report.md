# Decision Report

- generated_at: 2026-05-05T08:07:21.870151+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3333**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3333, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.79% | **-2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/13 | 23.1% | +3.53% | **+0.81%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.47% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.42% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.96% | **+3.36%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +5.00% | **+3.25%** |
| MARKET_LONG | 20/20 | 100.0% | +2.79% | **+2.79%** |
| ASK_LONG | 20/20 | 100.0% | +2.14% | **+2.14%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +4.71% | **+1.88%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T08:07:19.748655+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80837.8
- Funnel: target 765 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +109.82% | $11,972,219.35 |
| LAB/USDT:USDT | +41.58% | $78,808,950.92 |
| M/USDT:USDT | +39.25% | $5,907,832.03 |
| FHE/USDT:USDT | +35.50% | $4,153,089.27 |
| HIVE/USDT:USDT | +35.07% | $3,738,217.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.38% | +4.36% |
| NOT/USDT:USDT | below_1h_threshold | +2.19% | +2.17% |
| M/USDT:USDT | below_1h_threshold | +1.49% | +1.47% |
| 4/USDT:USDT | below_1h_threshold | +1.19% | +1.16% |
| FLOKI/USDT:USDT | below_1h_threshold | +0.88% | +0.86% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
