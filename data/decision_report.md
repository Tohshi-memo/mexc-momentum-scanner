# Decision Report

- generated_at: 2026-04-30T16:41:14.418379+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2717**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2717, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +4.98% | **+2.49%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.06% | **+1.68%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.00% | **+1.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.51% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T16:41:09.374894+00:00 / 保存件数 46/288
- BTC: STAGNANT 1h -0.16% price=76302.3
- Funnel: target 761 → liquid 227 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1, 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +12.91% | $5,576,143.81 |
| BR/USDT:USDT | +7.60% | $3,883,895.99 |
| ASTEROID/USDT:USDT | +5.82% | $3,444,865.55 |
| BIO/USDT:USDT | +3.50% | $3,629,476.45 |
| NGAS/USDT:USDT | +3.37% | $1,294,174.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +3.50% | +3.67% |
| NGAS/USDT:USDT | below_1h_threshold | +3.30% | +3.46% |
| BSB/USDT:USDT | below_1h_threshold | +3.29% | +3.45% |
| RIVER/USDT:USDT | below_1h_threshold | +2.72% | +2.88% |
| ZBT/USDT:USDT | below_1h_threshold | +2.60% | +2.76% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
