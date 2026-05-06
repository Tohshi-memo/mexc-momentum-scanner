# Decision Report

- generated_at: 2026-05-06T02:22:33.003393+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3407**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=3407, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/10 | 50.0% | +2.27% | **+1.14%** |
| ASK | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.09% | **+0.98%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.93% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.88% | **+0.74%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T02:22:30.880590+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=81220.9
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +35.87% | $1,275,747.94 |
| MAVIA/USDT:USDT | +28.63% | $1,704,613.74 |
| ZEC/USDT:USDT | +22.57% | $600,935,744.48 |
| B/USDT:USDT | +22.04% | $10,668,677.78 |
| NOT/USDT:USDT | +19.73% | $5,629,681.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +3.22% | +3.43% |
| AKT/USDT:USDT | below_1h_threshold | +2.42% | +2.63% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.06% | +2.27% |
| ZEC/USDT:USDT | below_1h_threshold | +1.67% | +1.88% |
| STRK/USDT:USDT | below_1h_threshold | +1.27% | +1.48% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
