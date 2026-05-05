# Decision Report

- generated_at: 2026-05-05T16:42:56.649494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3367**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=3367, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.31% | **+1.12%** |
| ASK | 20/20 | 100.0% | +0.97% | **+0.97%** |
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.69% | **+0.66%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.70% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.59% | **+0.39%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.36% | **+0.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T16:42:50.216572+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.53% price=81059.7
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SWARMS/USDT:USDT | +14.87% | $1,735,742.87 |
| FHE/USDT:USDT | +8.15% | $7,989,218.55 |
| BSB/USDT:USDT | +5.37% | $39,487,472.93 |
| M/USDT:USDT | +4.05% | $9,875,349.35 |
| LUNC/USDT:USDT | +3.61% | $67,065,247.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +4.06% | +4.58% |
| LUNC/USDT:USDT | below_1h_threshold | +3.51% | +4.03% |
| MERL/USDT:USDT | below_1h_threshold | +3.10% | +3.62% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.51% | +3.04% |
| ORCA/USDT:USDT | below_1h_threshold | +2.01% | +2.53% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
