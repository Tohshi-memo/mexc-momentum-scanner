# Decision Report

- generated_at: 2026-05-03T07:47:14.556693+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3049**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3049, expectancy=-0.15%
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
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_BB3S | 9/13 | 69.2% | +0.53% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.04% | **+0.37%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.29% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.40% | **+1.56%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.25% | **+1.46%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.72% | **+1.36%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T07:47:12.265687+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78331.0
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.6 >= 65=1, 4h RSI 97.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +58.57% | $7,876,308.13 |
| BR/USDT:USDT | +26.65% | $3,443,439.56 |
| AIGENSYN/USDT:USDT | +18.30% | $3,119,246.79 |
| FHE/USDT:USDT | +15.96% | $2,689,592.35 |
| TAC/USDT:USDT | +15.54% | $2,691,908.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.19% | +4.09% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.79% | +3.68% |
| FHE/USDT:USDT | below_1h_threshold | +3.45% | +3.34% |
| LUNC/USDT:USDT | below_1h_threshold | +1.80% | +1.70% |
| ALCH/USDT:USDT | below_1h_threshold | +1.64% | +1.53% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
