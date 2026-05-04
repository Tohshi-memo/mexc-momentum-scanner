# Decision Report

- generated_at: 2026-05-04T22:02:29.900818+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3268**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3268, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.38% | **-0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.77% | **+0.97%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.86% | **+0.97%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.67% | **+0.83%** |
| LIMIT_BB3S | 4/8 | 50.0% | +0.69% | **+0.35%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.17% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.20% | **+0.96%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.89% | **+0.95%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.69% | **+0.35%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.53% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T22:02:28.000227+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=80330.1
- Funnel: target 759 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +28.38% | $48,889,230.34 |
| PLAY/USDT:USDT | +19.95% | $1,408,599.36 |
| TST/USDT:USDT | +18.43% | $23,279,759.48 |
| FHE/USDT:USDT | +18.16% | $2,645,638.48 |
| TONCOIN/USDT:USDT | +10.01% | $30,209,725.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.57% | +1.43% |
| LUNC/USDT:USDT | below_1h_threshold | +0.70% | +0.56% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.51% | +0.37% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.48% | +0.34% |
| FHE/USDT:USDT | below_1h_threshold | +0.47% | +0.33% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
