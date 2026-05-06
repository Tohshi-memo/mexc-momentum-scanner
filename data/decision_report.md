# Decision Report

- generated_at: 2026-05-06T02:47:28.468510+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3410**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=3410, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/11 | 54.5% | +1.92% | **+1.05%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.16% | **+0.97%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.42% | **+0.38%** |
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +1.10% | **+0.97%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.02% | **+0.77%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.76% | **+0.61%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.55% | **+0.51%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.69% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$100.33** / 初期 $100.00 (+0.33%)
- 確定トレード: 18件 (TP 5 / SL 11 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.33
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T02:47:26.271067+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=81192.2
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B3/USDT:USDT | +35.05% | $1,319,896.20 |
| MAVIA/USDT:USDT | +27.90% | $1,723,182.33 |
| NOT/USDT:USDT | +27.02% | $5,971,056.66 |
| B/USDT:USDT | +23.33% | $11,802,556.69 |
| ZEC/USDT:USDT | +22.07% | $605,796,027.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +4.50% | +4.74% |
| NOT/USDT:USDT | below_1h_threshold | +3.66% | +3.90% |
| JTO/USDT:USDT | below_1h_threshold | +3.29% | +3.53% |
| AKT/USDT:USDT | below_1h_threshold | +2.59% | +2.84% |
| WIF/USDT:USDT | below_1h_threshold | +1.85% | +2.10% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
