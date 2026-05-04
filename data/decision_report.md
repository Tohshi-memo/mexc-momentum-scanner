# Decision Report

- generated_at: 2026-05-04T13:37:41.302276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3206**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3206, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.38% | **+0.41%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.84% | **+2.27%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.07% | **+1.65%** |
| ASK_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.99% | **+1.35%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.86% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$102.88** / 初期 $100.00 (+2.88%)
- 確定トレード: 13件 (TP 5 / SL 6 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.88
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T13:37:36.046271+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=79000.0
- Funnel: target 761 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +117.61% | $13,298,718.72 |
| SKYAI/USDT:USDT | +88.29% | $73,497,185.13 |
| GIGA/USDT:USDT | +54.45% | $2,126,347.74 |
| 4/USDT:USDT | +38.13% | $1,721,360.74 |
| GIGGLE/USDT:USDT | +28.51% | $4,020,462.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.33% | +3.10% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.01% | +2.78% |
| 4/USDT:USDT | below_1h_threshold | +2.72% | +2.49% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.65% | +2.42% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.34% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
