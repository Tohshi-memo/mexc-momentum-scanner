# Decision Report

- generated_at: 2026-05-06T03:47:21.189370+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3413**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=3413, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +3.30% | **+1.52%** |
| ASK | 20/20 | 100.0% | +1.49% | **+1.49%** |
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.77% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +1.52% | **+1.27%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.32% | **+0.26%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.20% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T03:47:19.216507+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=81448.1
- Funnel: target 765 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +27.32% | $1,387,971.59 |
| MAVIA/USDT:USDT | +24.61% | $1,770,510.19 |
| NOT/USDT:USDT | +24.03% | $6,826,471.72 |
| ZEC/USDT:USDT | +21.97% | $607,318,336.93 |
| SMCISTOCK/USDT:USDT | +20.44% | $5,249,451.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +3.48% | +3.32% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.45% | +2.29% |
| FET/USDT:USDT | below_1h_threshold | +1.66% | +1.50% |
| TIA/USDT:USDT | below_1h_threshold | +1.54% | +1.38% |
| ETC/USDT:USDT | below_1h_threshold | +1.52% | +1.36% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
