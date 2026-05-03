# Decision Report

- generated_at: 2026-05-03T18:37:12.700766+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3099**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3099, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +2.59% | **+1.17%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 6/20 | 30.0% | +1.68% | **+0.51%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +5.30% | **+3.71%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.97% | **+2.98%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.65% | **+2.92%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.69% | **+1.64%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.83% | **+1.56%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T18:37:08.085240+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=78653.7
- Funnel: target 755 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +62.09% | $314,921,283.32 |
| SKYAI/USDT:USDT | +16.92% | $25,214,879.82 |
| TST/USDT:USDT | +10.44% | $5,415,571.70 |
| BB/USDT:USDT | +9.11% | $1,449,793.11 |
| H/USDT:USDT | +8.82% | $8,600,962.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BB/USDT:USDT | below_1h_threshold | +4.77% | +4.82% |
| ZBT/USDT:USDT | below_1h_threshold | +3.22% | +3.27% |
| TAG/USDT:USDT | below_1h_threshold | +2.71% | +2.76% |
| UB/USDT:USDT | below_1h_threshold | +2.67% | +2.73% |
| BIO/USDT:USDT | below_1h_threshold | +2.57% | +2.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
