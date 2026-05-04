# Decision Report

- generated_at: 2026-05-04T22:27:10.311372+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3270**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=3270, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/7 | 42.9% | +2.22% | **+0.95%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.22% | **+1.05%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.61% | **+0.89%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.99% | **+0.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T22:27:08.376374+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80274.3
- Funnel: target 759 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +27.54% | $50,298,702.05 |
| TST/USDT:USDT | +17.30% | $23,505,852.38 |
| FHE/USDT:USDT | +16.58% | $2,758,611.42 |
| PLAY/USDT:USDT | +14.13% | $2,233,766.50 |
| LUNC/USDT:USDT | +9.62% | $75,363,610.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.03% | +1.96% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.91% | +1.84% |
| PENGU/USDT:USDT | below_1h_threshold | +1.85% | +1.78% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.70% | +1.63% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.57% | +1.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
