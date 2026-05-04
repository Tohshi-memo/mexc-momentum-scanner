# Decision Report

- generated_at: 2026-05-04T18:17:25.806748+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3247**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=3247, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.33% | **+1.28%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.22% | **+1.15%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.39% | **+1.11%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.24% | **+0.74%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.97% | **+0.69%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.43%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.48% | **+0.26%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T18:17:23.766705+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80259.0
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +22.65% | $40,671,883.73 |
| FHE/USDT:USDT | +9.47% | $2,801,412.56 |
| TST/USDT:USDT | +8.43% | $21,730,506.92 |
| RAVE/USDT:USDT | +8.05% | $13,026,886.03 |
| WLFI/USDT:USDT | +5.52% | $4,920,501.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BB/USDT:USDT | below_1h_threshold | +3.21% | +3.31% |
| RAVE/USDT:USDT | below_1h_threshold | +1.92% | +2.02% |
| ON/USDT:USDT | below_1h_threshold | +1.37% | +1.47% |
| LUNC/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |
| WLFI/USDT:USDT | below_1h_threshold | +1.21% | +1.31% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
