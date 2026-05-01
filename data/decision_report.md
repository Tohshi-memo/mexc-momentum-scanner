# Decision Report

- generated_at: 2026-05-01T20:06:52.088128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2828**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.23% / filled 20/20。**
- 全期間 MARKET基準: n=2828, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| MARKET | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.87% | **+0.79%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.32% | **+0.24%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +2.96% | **+1.27%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.14%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.16% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T20:06:50.322349+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78293.6
- Funnel: target 756 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +18.96% | $2,162,522.99 |
| TAG/USDT:USDT | +12.35% | $3,085,674.09 |
| ZEN/USDT:USDT | +10.21% | $6,392,358.05 |
| FIGHT/USDT:USDT | +9.19% | $1,221,320.94 |
| SQD/USDT:USDT | +8.37% | $2,090,322.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +2.67% | +2.70% |
| LAB/USDT:USDT | below_1h_threshold | +1.40% | +1.43% |
| SQD/USDT:USDT | below_1h_threshold | +1.33% | +1.36% |
| ZEN/USDT:USDT | below_1h_threshold | +1.27% | +1.30% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.66% | +0.69% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
