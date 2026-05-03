# Decision Report

- generated_at: 2026-05-03T05:37:17.396455+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3036**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=3036, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.35% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.09% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.44% | **+0.26%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.69% | **+0.21%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T05:37:12.540857+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=78179.7
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BABY/USDT:USDT | +25.75% | $2,834,384.19 |
| BR/USDT:USDT | +22.09% | $2,376,467.24 |
| AKT/USDT:USDT | +16.01% | $1,244,757.98 |
| FHE/USDT:USDT | +12.04% | $2,538,689.91 |
| FIGHT/USDT:USDT | +11.28% | $1,019,246.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +3.91% | +3.85% |
| BABY/USDT:USDT | below_1h_threshold | +3.01% | +2.95% |
| TRX/USDT:USDT | below_1h_threshold | +2.98% | +2.92% |
| BB/USDT:USDT | below_1h_threshold | +2.89% | +2.83% |
| ALCH/USDT:USDT | below_1h_threshold | +2.88% | +2.82% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
