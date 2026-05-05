# Decision Report

- generated_at: 2026-05-05T02:07:21.138535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3290**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=3290, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.92% | **+0.87%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |
| ASK | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +2.06% | **+1.03%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.19% | **+0.89%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.94% | **+0.71%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.64% | **+0.61%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T02:07:19.233602+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=80420.5
- Funnel: target 765 → liquid 204 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +46.81% | $1,909,197.13 |
| RAVE/USDT:USDT | +23.37% | $61,626,562.19 |
| TONCOIN/USDT:USDT | +21.90% | $53,857,647.13 |
| NOT/USDT:USDT | +17.36% | $1,381,840.22 |
| FHE/USDT:USDT | +16.96% | $3,326,130.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +2.17% | +2.03% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.85% | +1.71% |
| 4/USDT:USDT | below_1h_threshold | +1.80% | +1.66% |
| SPK/USDT:USDT | below_1h_threshold | +0.83% | +0.69% |
| VELO/USDT:USDT | below_1h_threshold | +0.70% | +0.56% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
