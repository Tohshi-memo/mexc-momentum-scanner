# Decision Report

- generated_at: 2026-05-05T02:22:15.462434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3293**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=3293, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.91% | **+0.49%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.58% | **+0.44%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.40% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T02:22:13.541936+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80341.4
- Funnel: target 765 → liquid 204 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +50.15% | $2,278,455.62 |
| RAVE/USDT:USDT | +22.36% | $61,879,946.96 |
| TONCOIN/USDT:USDT | +22.20% | $55,090,601.13 |
| FHE/USDT:USDT | +16.82% | $3,619,140.55 |
| NAORIS/USDT:USDT | +15.72% | $6,279,734.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.85% | +1.81% |
| PENGU/USDT:USDT | below_1h_threshold | +1.77% | +1.73% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.68% | +1.64% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.23% | +1.19% |
| 4/USDT:USDT | below_1h_threshold | +0.93% | +0.90% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
