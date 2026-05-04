# Decision Report

- generated_at: 2026-05-04T02:52:26.630042+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3132**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3132, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.50% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.73% | **+1.21%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.81% | **+1.00%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.16% | **+0.97%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.11% | **+0.67%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T02:52:21.166894+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.60% price=80224.7
- Funnel: target 757 → liquid 167 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 85.0 >= 65=1, 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +46.51% | $242,281,214.60 |
| SKYAI/USDT:USDT | +43.87% | $36,057,175.14 |
| TAG/USDT:USDT | +38.89% | $4,567,528.00 |
| BSB/USDT:USDT | +26.12% | $15,093,837.06 |
| GIGA/USDT:USDT | +24.70% | $1,103,780.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.32% | +3.72% |
| UB/USDT:USDT | below_1h_threshold | +3.63% | +3.03% |
| MONAD/USDT:USDT | below_1h_threshold | +2.59% | +1.99% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.43% | +1.83% |
| ENA/USDT:USDT | below_1h_threshold | +2.36% | +1.77% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
