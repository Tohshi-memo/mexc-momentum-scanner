# Decision Report

- generated_at: 2026-05-05T16:27:09.251946+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3366**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.50% / filled 20/20。**
- 全期間 MARKET基準: n=3366, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.57% | **+1.57%** |
| MARKET | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.65% | **+1.32%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.32% | **+1.26%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.82% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.59% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.10% | **-0.10%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.17% | **-0.14%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T16:27:03.011577+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81401.9
- Funnel: target 765 → liquid 189 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1, 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SWARMS/USDT:USDT | +11.54% | $1,511,117.15 |
| MERL/USDT:USDT | +6.72% | $3,718,099.41 |
| BSB/USDT:USDT | +5.61% | $39,106,638.71 |
| M/USDT:USDT | +5.47% | $9,773,519.38 |
| FHE/USDT:USDT | +5.19% | $7,582,868.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.81% | +4.91% |
| LUNC/USDT:USDT | below_1h_threshold | +4.11% | +4.21% |
| LUNANEW/USDT:USDT | below_1h_threshold | +2.73% | +2.83% |
| ENA/USDT:USDT | below_1h_threshold | +1.97% | +2.07% |
| FET/USDT:USDT | below_1h_threshold | +1.93% | +2.03% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
