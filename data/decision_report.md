# Decision Report

- generated_at: 2026-05-05T20:22:29.230298+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3380**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3380, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.84% | **-0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.53% | **+0.76%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.73% | **+0.36%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.10% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.46% | **+2.76%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.10% | **+0.93%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.14% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T20:22:26.351692+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=81526.1
- Funnel: target 760 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.5 >= 65=1, 4h RSI 84.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +38.73% | $15,056,735.30 |
| SWARMS/USDT:USDT | +17.33% | $2,186,762.23 |
| STX/USDT:USDT | +16.25% | $13,462,077.42 |
| SMCISTOCK/USDT:USDT | +12.77% | $1,969,583.63 |
| ZEC/USDT:USDT | +8.38% | $444,535,372.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICP/USDT:USDT | below_1h_threshold | +4.93% | +4.97% |
| ZEC/USDT:USDT | below_1h_threshold | +3.67% | +3.71% |
| 4/USDT:USDT | below_1h_threshold | +3.22% | +3.25% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +2.50% | +2.54% |
| SWARMS/USDT:USDT | below_1h_threshold | +2.48% | +2.52% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
