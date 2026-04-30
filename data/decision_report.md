# Decision Report

- generated_at: 2026-04-30T16:16:05.822635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2714**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2714, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_BB3S | 6/17 | 35.3% | +1.30% | **+0.46%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.13% | **+0.45%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.30% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +7.03% | **+4.69%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.32% | **+1.49%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.12% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T16:16:01.961503+00:00 / 保存件数 41/288
- BTC: STAGNANT 1h -0.04% price=76399.8
- Funnel: target 761 → liquid 224 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +4.72% | $3,223,939.78 |
| BIO/USDT:USDT | +4.06% | $3,557,484.55 |
| APE/USDT:USDT | +3.81% | $6,412,877.86 |
| BLEND/USDT:USDT | +1.70% | $12,083,216.61 |
| AIN/USDT:USDT | +1.67% | $1,843,872.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.49% | +4.53% |
| APE/USDT:USDT | below_1h_threshold | +3.75% | +3.78% |
| BLEND/USDT:USDT | below_1h_threshold | +1.70% | +1.74% |
| AIN/USDT:USDT | below_1h_threshold | +1.65% | +1.69% |
| TAC/USDT:USDT | below_1h_threshold | +1.64% | +1.67% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
