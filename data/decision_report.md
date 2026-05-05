# Decision Report

- generated_at: 2026-05-05T17:27:27.928812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3371**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.10% / filled 20/20。**
- 全期間 MARKET基準: n=3371, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.10% | **+2.10%** |
| MARKET | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.37% | **+2.01%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.96% | **+1.86%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +0.94% | **+0.19%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.38% | **-0.34%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -2.30% | **-0.35%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T17:27:25.712146+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=81381.3
- Funnel: target 765 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FHE/USDT:USDT | +11.29% | $8,773,207.63 |
| SWARMS/USDT:USDT | +10.42% | $2,040,432.17 |
| LUNC/USDT:USDT | +7.24% | $65,781,667.59 |
| LUNANEW/USDT:USDT | +6.23% | $2,155,337.47 |
| ASTEROID/USDT:USDT | +4.57% | $3,373,167.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNANEW/USDT:USDT | below_1h_threshold | +3.70% | +3.53% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.60% | +3.43% |
| FHE/USDT:USDT | below_1h_threshold | +2.99% | +2.83% |
| LUNC/USDT:USDT | below_1h_threshold | +2.89% | +2.72% |
| TAG/USDT:USDT | below_1h_threshold | +2.81% | +2.65% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
