# Decision Report

- generated_at: 2026-05-06T02:37:23.658504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3409**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=3409, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_BB3S | 6/12 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.31% | **+0.92%** |
| ASK | 20/20 | 100.0% | +0.91% | **+0.91%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +0.47% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.22% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T02:37:21.223198+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=81071.2
- Funnel: target 765 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.5 >= 65=1, 4h RSI 76.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +35.45% | $1,303,385.06 |
| MAVIA/USDT:USDT | +27.28% | $1,718,219.17 |
| B/USDT:USDT | +26.13% | $11,342,951.76 |
| ZEC/USDT:USDT | +22.09% | $603,555,159.21 |
| NOT/USDT:USDT | +21.89% | $5,746,648.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +3.14% | +3.53% |
| AKT/USDT:USDT | below_1h_threshold | +2.56% | +2.95% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.18% | +2.57% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.74% | +2.13% |
| TST/USDT:USDT | below_1h_threshold | +1.34% | +1.74% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
