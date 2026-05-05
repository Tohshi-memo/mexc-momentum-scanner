# Decision Report

- generated_at: 2026-05-05T15:52:40.026526+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3363**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3363, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.09% | **+2.09%** |
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.87% | **+1.77%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.84% | **+1.38%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.33% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.89% | **+0.39%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.89% | **-0.40%** |
| MARKET_LONG | 20/20 | 100.0% | -0.49% | **-0.49%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T15:52:37.537971+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=81548.2
- Funnel: target 765 → liquid 195 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1, 4h RSI 73.8 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +70.86% | $27,883,078.89 |
| LAB/USDT:USDT | +51.53% | $107,793,607.61 |
| FHE/USDT:USDT | +46.23% | $6,815,208.74 |
| TONCOIN/USDT:USDT | +26.22% | $144,332,542.11 |
| M/USDT:USDT | +25.04% | $9,131,347.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VIRTUAL/USDT:USDT | below_1h_threshold | +4.30% | +3.98% |
| PENDLE/USDT:USDT | below_1h_threshold | +3.58% | +3.26% |
| LUNC/USDT:USDT | below_1h_threshold | +3.46% | +3.13% |
| UB/USDT:USDT | below_1h_threshold | +3.20% | +2.88% |
| LUNANEW/USDT:USDT | below_1h_threshold | +2.13% | +1.80% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
