# Decision Report

- generated_at: 2026-05-03T18:42:03.483334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3101**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3101, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.79% | **-2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.68% | **+1.07%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_4PCT | 18/20 | 90.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +5.96% | **+3.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +4.03% | **+3.03%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +5.56% | **+2.78%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.90% | **+2.46%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +7.31% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T18:42:01.323396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78650.1
- Funnel: target 755 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.7 >= 65=1, 4h RSI 75.1 >= 65=1, 4h RSI 71.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +64.29% | $316,437,160.77 |
| SKYAI/USDT:USDT | +17.04% | $25,306,977.28 |
| BB/USDT:USDT | +10.37% | $1,486,395.11 |
| TST/USDT:USDT | +9.16% | $5,428,504.09 |
| UB/USDT:USDT | +8.61% | $13,760,151.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +3.68% | +3.74% |
| ZBT/USDT:USDT | below_1h_threshold | +3.49% | +3.54% |
| BIO/USDT:USDT | below_1h_threshold | +2.80% | +2.86% |
| SIREN/USDT:USDT | below_1h_threshold | +2.55% | +2.61% |
| PNUT/USDT:USDT | below_1h_threshold | +2.52% | +2.57% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
