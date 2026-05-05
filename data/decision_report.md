# Decision Report

- generated_at: 2026-05-05T15:02:35.545366+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3361**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.67% / filled 20/20。**
- 全期間 MARKET基準: n=3361, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.67% | **+2.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.69% | **+2.69%** |
| MARKET | 20/20 | 100.0% | +2.67% | **+2.67%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.45% | **+2.32%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.12% | **+1.48%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.63% | **+0.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.89% | **+0.39%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -1.55% | **-0.85%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T15:02:33.599397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=81214.3
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +73.20% | $26,608,934.11 |
| LAB/USDT:USDT | +42.49% | $103,531,358.98 |
| FHE/USDT:USDT | +35.50% | $5,866,877.37 |
| HIVE/USDT:USDT | +31.21% | $8,772,971.79 |
| M/USDT:USDT | +23.88% | $8,137,624.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.11% | +1.20% |
| FHE/USDT:USDT | below_1h_threshold | +0.79% | +0.88% |
| VVV/USDT:USDT | below_1h_threshold | +0.76% | +0.84% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.63% | +0.71% |
| LUNC/USDT:USDT | below_1h_threshold | +0.40% | +0.48% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
