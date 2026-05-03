# Decision Report

- generated_at: 2026-05-03T07:32:20.448071+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3046**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3046, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_BB3S | 8/12 | 66.7% | +0.66% | **+0.44%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.68% | **+0.30%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +3.66% | **+2.02%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.39% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T07:32:18.237691+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=78398.0
- Funnel: target 755 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.5 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +57.80% | $6,954,639.10 |
| BR/USDT:USDT | +35.08% | $3,218,645.83 |
| AIGENSYN/USDT:USDT | +24.03% | $2,839,570.69 |
| FHE/USDT:USDT | +15.46% | $2,669,128.03 |
| TAC/USDT:USDT | +12.91% | $2,667,305.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +4.93% | +4.74% |
| BR/USDT:USDT | below_1h_threshold | +3.87% | +3.68% |
| FHE/USDT:USDT | below_1h_threshold | +3.00% | +2.81% |
| LUNC/USDT:USDT | below_1h_threshold | +2.86% | +2.67% |
| TAC/USDT:USDT | below_1h_threshold | +2.16% | +1.97% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
