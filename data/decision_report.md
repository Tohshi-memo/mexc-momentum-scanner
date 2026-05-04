# Decision Report

- generated_at: 2026-05-04T16:07:12.113580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3230**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3230, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.99% | **-1.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.57% | **+1.02%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.05% | **+2.43%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.75% | **+1.57%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T16:07:10.047883+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=79920.7
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1, 4h RSI 94.7 >= 65=1, 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +7.63% | $18,984,487.92 |
| ELIZAOS/USDT:USDT | +5.69% | $2,061,334.76 |
| SKYAI/USDT:USDT | +5.26% | $92,353,937.50 |
| BSB/USDT:USDT | +4.73% | $32,840,414.43 |
| 4/USDT:USDT | +2.48% | $1,850,116.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.41% | +4.48% |
| 4/USDT:USDT | below_1h_threshold | +2.48% | +2.55% |
| BABY/USDT:USDT | below_1h_threshold | +1.83% | +1.90% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.16% | +1.23% |
| FHE/USDT:USDT | below_1h_threshold | +1.16% | +1.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
