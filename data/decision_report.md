# Decision Report

- generated_at: 2026-05-02T14:39:41.609510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2920**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2920, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-3.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.17% | **-3.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_6PCT | 10/20 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_5PCT | 11/20 | 55.0% | -0.40% | **-0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.59% | **+2.59%** |
| ASK_LONG | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.74% | **+2.05%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +5.47% | **+1.09%** |
| LIMIT_5PCT_LONG | 4/20 | 20.0% | +5.21% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T14:39:38.315524+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78349.0
- Funnel: target 755 → liquid 161 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.7 >= 65=1, 4h RSI 67.7 >= 65=1, 4h RSI 82.4 >= 65=1, 4h RSI 90.4 >= 65=1, 4h RSI 81.8 >= 65=1, 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +283.82% | $152,098,625.41 |
| TAG/USDT:USDT | +60.46% | $8,556,308.33 |
| BIO/USDT:USDT | +54.02% | $3,377,531.40 |
| SPACE/USDT:USDT | +27.50% | $1,477,012.90 |
| B/USDT:USDT | +25.04% | $73,110,879.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZBT/USDT:USDT | below_1h_threshold | +4.07% | +4.05% |
| KNC/USDT:USDT | below_1h_threshold | +3.81% | +3.79% |
| PNUT/USDT:USDT | below_1h_threshold | +2.75% | +2.72% |
| BSB/USDT:USDT | below_1h_threshold | +2.29% | +2.26% |
| BB/USDT:USDT | below_1h_threshold | +2.16% | +2.14% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
