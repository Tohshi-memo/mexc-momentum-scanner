# Decision Report

- generated_at: 2026-05-06T01:37:36.572215+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3403**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=3403, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.39% | **+0.56%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.58% | **+0.52%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.64% | **+0.45%** |
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.51% | **+1.29%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T01:37:34.303709+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=81230.0
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.8 >= 65=1, 4h RSI 73.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +40.47% | $1,194,067.68 |
| MAVIA/USDT:USDT | +28.34% | $1,679,616.90 |
| FHE/USDT:USDT | +24.64% | $28,212,034.81 |
| ZEC/USDT:USDT | +21.63% | $600,850,800.79 |
| SWARMS/USDT:USDT | +20.90% | $2,380,823.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +4.54% | +4.23% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.39% | +3.08% |
| WIF/USDT:USDT | below_1h_threshold | +3.13% | +2.82% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.93% | +2.62% |
| LYN/USDT:USDT | below_1h_threshold | +2.37% | +2.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
