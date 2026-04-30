# Decision Report

- generated_at: 2026-04-30T16:36:05.944911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2716**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2716, expectancy=-0.10%
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
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 6/16 | 37.5% | +1.30% | **+0.49%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.62% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.35% | **+2.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.78% | **+1.89%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T16:36:03.982133+00:00 / 保存件数 45/288
- BTC: STAGNANT 1h -0.10% price=76349.1
- Funnel: target 761 → liquid 227 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +8.65% | $5,181,051.21 |
| BR/USDT:USDT | +7.38% | $3,793,460.82 |
| ASTEROID/USDT:USDT | +4.48% | $3,403,729.83 |
| BIO/USDT:USDT | +3.37% | $3,624,789.72 |
| BSB/USDT:USDT | +3.33% | $43,503,387.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.49% | +4.59% |
| BIO/USDT:USDT | below_1h_threshold | +3.81% | +3.91% |
| BSB/USDT:USDT | below_1h_threshold | +3.27% | +3.38% |
| NGAS/USDT:USDT | below_1h_threshold | +2.82% | +2.92% |
| ZBT/USDT:USDT | below_1h_threshold | +2.19% | +2.30% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
