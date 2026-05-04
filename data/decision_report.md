# Decision Report

- generated_at: 2026-05-04T22:07:13.974656+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3269**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=3269, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/7 | 42.9% | +2.22% | **+0.95%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.84% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.97% | **+0.49%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.47% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T22:07:12.043889+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80241.1
- Funnel: target 759 → liquid 198 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +28.02% | $49,190,925.77 |
| PLAY/USDT:USDT | +19.14% | $1,572,156.01 |
| FHE/USDT:USDT | +18.91% | $2,686,746.62 |
| TST/USDT:USDT | +18.87% | $23,314,205.95 |
| TONCOIN/USDT:USDT | +10.54% | $30,667,595.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +1.71% | +1.68% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.40% | +1.38% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.34% | +1.31% |
| ZEC/USDT:USDT | below_1h_threshold | +0.98% | +0.96% |
| LUNC/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
