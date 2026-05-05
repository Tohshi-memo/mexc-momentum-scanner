# Decision Report

- generated_at: 2026-05-05T09:32:29.212152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3342**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3342, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 2/20 | 10.0% | +4.12% | **+0.41%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.16% | **+2.53%** |
| ASK_LONG | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.87% | **+2.13%** |
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +3.36% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T09:32:26.598075+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=80661.7
- Funnel: target 765 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1, 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +96.65% | $15,646,464.52 |
| LAB/USDT:USDT | +66.33% | $87,503,136.07 |
| HIVE/USDT:USDT | +35.87% | $4,240,998.79 |
| FHE/USDT:USDT | +30.94% | $4,529,052.89 |
| M/USDT:USDT | +27.53% | $6,783,969.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_1h_threshold | +2.68% | +2.83% |
| TURBO/USDT:USDT | below_1h_threshold | +2.58% | +2.72% |
| PNUT/USDT:USDT | below_1h_threshold | +2.12% | +2.26% |
| CHZ/USDT:USDT | below_1h_threshold | +2.03% | +2.17% |
| HIVE/USDT:USDT | below_1h_threshold | +1.27% | +1.41% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
