# Decision Report

- generated_at: 2026-05-05T13:47:29.712670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3355**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=3355, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.39% | **+1.39%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.18% | **+1.12%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| ASK_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | -0.16% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T13:47:27.151723+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=81441.3
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1, 4h RSI 71.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +79.54% | $23,952,055.44 |
| LAB/USDT:USDT | +43.92% | $103,488,696.18 |
| HIVE/USDT:USDT | +37.71% | $8,087,730.85 |
| FHE/USDT:USDT | +31.13% | $5,663,126.29 |
| TONCOIN/USDT:USDT | +26.89% | $113,216,427.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUSTOCK/USDT:USDT | below_1h_threshold | +4.42% | +4.15% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +4.39% | +4.12% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.34% | +4.07% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +4.33% | +4.06% |
| CVNASTOCK/USDT:USDT | below_1h_threshold | +3.76% | +3.49% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
