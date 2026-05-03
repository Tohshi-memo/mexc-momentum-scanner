# Decision Report

- generated_at: 2026-05-03T18:01:47.178821+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3095**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3095, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_BB3S | 2/17 | 11.8% | +8.00% | **+0.94%** |
| LIMIT_ATR | 7/20 | 35.0% | +2.46% | **+0.86%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.37% | **+2.19%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.74% | **+2.05%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.64% | **+1.45%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T18:01:43.163817+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78675.5
- Funnel: target 755 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +50.09% | $300,706,151.56 |
| SKYAI/USDT:USDT | +20.75% | $23,622,114.84 |
| TST/USDT:USDT | +8.87% | $5,336,849.70 |
| ASTEROID/USDT:USDT | +6.79% | $2,004,539.10 |
| ZBT/USDT:USDT | +4.39% | $1,508,535.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.66% | +1.69% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.50% | +1.52% |
| BSB/USDT:USDT | below_1h_threshold | +0.65% | +0.67% |
| GENIUS/USDT:USDT | below_1h_threshold | +0.51% | +0.53% |
| AKT/USDT:USDT | below_1h_threshold | +0.44% | +0.47% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
