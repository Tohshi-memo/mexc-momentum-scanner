# Decision Report

- generated_at: 2026-05-01T23:02:20.416514+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2840**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.24% / filled 20/20。**
- 全期間 MARKET基準: n=2840, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.56% | **+1.33%** |
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.08% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.81% | **+1.00%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.68% | **+0.76%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.21%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.01% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T23:02:18.675759+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78057.8
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +42.25% | $10,788,293.14 |
| WOJAK/USDT:USDT | +12.50% | $1,049,688.46 |
| CHILLGUY/USDT:USDT | +12.34% | $1,036,257.29 |
| RLS/USDT:USDT | +12.20% | $2,527,994.79 |
| BLESS/USDT:USDT | +10.61% | $1,125,418.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.81% | +1.88% |
| WOJAK/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |
| VELVET/USDT:USDT | below_1h_threshold | +1.40% | +1.46% |
| RLS/USDT:USDT | below_1h_threshold | +0.69% | +0.76% |
| B/USDT:USDT | below_1h_threshold | +0.49% | +0.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
