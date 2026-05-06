# Decision Report

- generated_at: 2026-05-06T02:12:25.143087+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3404**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=3404, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.38% | **+0.55%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.53% | **+0.48%** |
| ASK | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 18/20 | 90.0% | +1.77% | **+1.59%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T02:12:23.159575+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=81297.6
- Funnel: target 765 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +37.51% | $1,251,150.80 |
| MAVIA/USDT:USDT | +29.07% | $1,698,159.23 |
| NOT/USDT:USDT | +23.22% | $5,463,419.17 |
| ZEC/USDT:USDT | +22.76% | $598,150,862.18 |
| SWARMS/USDT:USDT | +19.76% | $2,348,727.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +3.05% | +3.17% |
| ZEC/USDT:USDT | below_1h_threshold | +2.02% | +2.13% |
| STRK/USDT:USDT | below_1h_threshold | +1.61% | +1.73% |
| AKT/USDT:USDT | below_1h_threshold | +1.45% | +1.56% |
| AERO/USDT:USDT | below_1h_threshold | +1.23% | +1.35% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
