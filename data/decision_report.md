# Decision Report

- generated_at: 2026-05-05T05:12:21.734250+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3309**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=3309, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.52% | **+0.68%** |
| LIMIT_BB3S | 4/12 | 33.3% | +2.00% | **+0.67%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.06% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.07% | **+0.48%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.48% | **+0.30%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.04% | **+0.02%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.02% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T05:12:19.721973+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80905.7
- Funnel: target 765 → liquid 205 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +74.60% | $7,254,063.02 |
| FHE/USDT:USDT | +27.46% | $3,619,108.96 |
| TONCOIN/USDT:USDT | +16.83% | $64,728,140.92 |
| 4/USDT:USDT | +16.58% | $2,258,723.68 |
| RAVE/USDT:USDT | +16.08% | $63,826,949.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +3.32% | +3.26% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.69% | +2.62% |
| ALGO/USDT:USDT | below_1h_threshold | +1.96% | +1.89% |
| RAVE/USDT:USDT | below_1h_threshold | +1.41% | +1.34% |
| PNUT/USDT:USDT | below_1h_threshold | +1.29% | +1.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
