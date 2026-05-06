# Decision Report

- generated_at: 2026-05-06T08:12:28.832219+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3434**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=3434, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.15% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| ASK_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.30% | **+0.21%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.48% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T08:12:26.572346+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=81513.4
- Funnel: target 765 → liquid 198 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +64.62% | $7,634,582.00 |
| ZEC/USDT:USDT | +37.71% | $707,471,956.74 |
| B3/USDT:USDT | +30.42% | $1,446,341.32 |
| STORJ/USDT:USDT | +29.72% | $2,496,343.03 |
| FHE/USDT:USDT | +27.15% | $28,634,114.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.87% | +3.65% |
| LAB/USDT:USDT | below_1h_threshold | +3.38% | +3.16% |
| DASH/USDT:USDT | below_1h_threshold | +1.71% | +1.49% |
| S/USDT:USDT | below_1h_threshold | +1.24% | +1.02% |
| NEAR/USDT:USDT | below_1h_threshold | +1.18% | +0.96% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
