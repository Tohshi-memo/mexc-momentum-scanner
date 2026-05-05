# Decision Report

- generated_at: 2026-05-05T07:06:30.750726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3324**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=3324, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/14 | 28.6% | +1.86% | **+0.53%** |
| ASK | 20/20 | 100.0% | +0.31% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.95% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.65% | **+1.41%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T07:06:28.759040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80872.0
- Funnel: target 765 → liquid 205 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +82.77% | $9,002,846.16 |
| HIVE/USDT:USDT | +38.36% | $3,280,184.80 |
| M/USDT:USDT | +35.85% | $4,120,237.72 |
| FHE/USDT:USDT | +27.92% | $3,927,820.98 |
| TONCOIN/USDT:USDT | +21.52% | $66,954,700.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +4.33% | +4.41% |
| PLAY/USDT:USDT | below_1h_threshold | +3.76% | +3.83% |
| DOGS/USDT:USDT | below_1h_threshold | +3.74% | +3.82% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.00% | +3.08% |
| LAB/USDT:USDT | below_1h_threshold | +1.29% | +1.37% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
