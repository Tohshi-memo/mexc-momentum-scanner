# Decision Report

- generated_at: 2026-05-06T05:12:21.300894+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3420**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=3420, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +3.30% | **+1.52%** |
| ASK | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.33% | **+0.93%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.80% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.87% | **+0.87%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.34% | **+0.05%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.02% | **+0.02%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T05:12:18.961713+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81237.3
- Funnel: target 765 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +39.16% | $1,517,465.34 |
| ZEC/USDT:USDT | +23.25% | $602,900,702.13 |
| MAVIA/USDT:USDT | +22.81% | $1,833,460.01 |
| B3/USDT:USDT | +20.80% | $1,394,898.10 |
| SMCISTOCK/USDT:USDT | +20.55% | $5,305,414.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POPCAT/USDT:USDT | below_1h_threshold | +2.62% | +2.70% |
| PNUT/USDT:USDT | below_1h_threshold | +2.17% | +2.24% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.45% | +1.53% |
| TURBO/USDT:USDT | below_1h_threshold | +0.77% | +0.84% |
| CTC/USDT:USDT | below_1h_threshold | +0.71% | +0.79% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
