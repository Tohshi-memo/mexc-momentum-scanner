# Decision Report

- generated_at: 2026-05-05T03:02:36.584429+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3299**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=3299, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.07% | **+1.02%** |
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.36% | **+0.22%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.27% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T03:02:34.655429+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=80474.1
- Funnel: target 765 → liquid 206 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +85.31% | $3,873,671.27 |
| RAVE/USDT:USDT | +20.81% | $62,347,765.77 |
| TONCOIN/USDT:USDT | +20.54% | $59,368,472.64 |
| NOT/USDT:USDT | +17.83% | $1,618,698.41 |
| FHE/USDT:USDT | +17.61% | $3,352,967.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.16% | +4.21% |
| 4/USDT:USDT | below_1h_threshold | +3.04% | +3.09% |
| NOT/USDT:USDT | below_1h_threshold | +1.57% | +1.62% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +0.98% | +1.03% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.76% | +0.81% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
