# Decision Report

- generated_at: 2026-05-05T06:57:27.263698+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3322**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3322, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| ASK | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_BB3S | 4/14 | 28.6% | +2.15% | **+0.61%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.95% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.12% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| ASK_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T06:57:24.541744+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=80873.6
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.7 >= 65=1, 4h RSI 96.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +77.69% | $8,741,180.09 |
| HIVE/USDT:USDT | +36.17% | $3,175,610.87 |
| FHE/USDT:USDT | +28.25% | $3,922,804.94 |
| M/USDT:USDT | +24.43% | $3,748,950.15 |
| TONCOIN/USDT:USDT | +22.74% | $66,649,163.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QUBIC/USDT:USDT | below_1h_threshold | +4.05% | +4.11% |
| 4/USDT:USDT | below_1h_threshold | +3.18% | +3.25% |
| NOT/USDT:USDT | below_1h_threshold | +2.73% | +2.80% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.29% | +2.36% |
| TURBO/USDT:USDT | below_1h_threshold | +1.29% | +1.36% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
