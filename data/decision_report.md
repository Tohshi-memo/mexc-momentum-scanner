# Decision Report

- generated_at: 2026-05-05T07:27:18.725804+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3327**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3327, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +1.86% | **+0.57%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.07% | **+0.32%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.93% | **+0.29%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.11% | **-0.05%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.18% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.72% | **+2.31%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +6.14% | **+1.76%** |
| MARKET_LONG | 20/20 | 100.0% | +1.72% | **+1.72%** |
| ASK_LONG | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T07:27:16.311140+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=81029.3
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +90.31% | $9,731,058.39 |
| HIVE/USDT:USDT | +37.46% | $3,419,121.76 |
| FHE/USDT:USDT | +29.18% | $3,964,914.95 |
| M/USDT:USDT | +28.00% | $5,009,608.02 |
| LAB/USDT:USDT | +26.30% | $78,321,771.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TURBO/USDT:USDT | below_1h_threshold | +2.39% | +2.27% |
| PRL/USDT:USDT | below_1h_threshold | +2.06% | +1.94% |
| SPX/USDT:USDT | below_1h_threshold | +2.00% | +1.89% |
| RAVE/USDT:USDT | below_1h_threshold | +1.87% | +1.76% |
| LUNC/USDT:USDT | below_1h_threshold | +1.85% | +1.73% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
