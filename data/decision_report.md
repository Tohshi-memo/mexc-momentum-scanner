# Decision Report

- generated_at: 2026-05-05T14:12:24.716705+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3358**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.97% / filled 20/20。**
- 全期間 MARKET基準: n=3358, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.99% | **+1.99%** |
| MARKET | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.76% | **+1.67%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.70% | **+1.02%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| ASK_LONG | 20/20 | 100.0% | -0.27% | **-0.27%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.48% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T14:12:22.720315+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81221.7
- Funnel: target 765 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +70.69% | $25,134,837.04 |
| LAB/USDT:USDT | +41.46% | $101,807,445.21 |
| HIVE/USDT:USDT | +34.57% | $8,316,589.94 |
| FHE/USDT:USDT | +33.13% | $5,726,092.75 |
| M/USDT:USDT | +24.63% | $8,056,351.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +1.75% | +1.81% |
| JUP/USDT:USDT | below_1h_threshold | +1.74% | +1.80% |
| MORPHO/USDT:USDT | below_1h_threshold | +1.59% | +1.65% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.17% | +1.24% |
| ICP/USDT:USDT | below_1h_threshold | +1.01% | +1.08% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
