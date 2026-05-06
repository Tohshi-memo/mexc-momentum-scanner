# Decision Report

- generated_at: 2026-05-06T02:32:32.957744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3408**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=3408, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/11 | 54.5% | +1.92% | **+1.05%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.07% | **+0.96%** |
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.93% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.63% | **+0.50%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.39% | **+0.24%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.21% | **+0.18%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.06% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T02:32:30.826766+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=81062.4
- Funnel: target 765 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +35.53% | $1,295,779.77 |
| MAVIA/USDT:USDT | +27.90% | $1,713,045.35 |
| B/USDT:USDT | +26.33% | $11,207,494.54 |
| ZEC/USDT:USDT | +22.38% | $602,538,954.35 |
| NOT/USDT:USDT | +20.44% | $5,723,101.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKT/USDT:USDT | below_1h_threshold | +2.29% | +2.70% |
| GIGGLE/USDT:USDT | below_1h_threshold | +1.82% | +2.23% |
| ZEC/USDT:USDT | below_1h_threshold | +1.50% | +1.91% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.40% | +1.80% |
| AR/USDT:USDT | below_1h_threshold | +1.23% | +1.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
