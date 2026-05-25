# Decision Report

- generated_at: 2026-05-25T02:49:07.234488+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4840**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=4840, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.63% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.34% | **+0.13%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.06% | **+0.04%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.40** / 初期 $100.00 (+22.40%)
- 確定: 646件 (Win 159 / Loss 206 / Flat 281) / skip 755件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $122.40

## 4. Latest Market Context

- 更新: 2026-05-25T02:49:04.899501+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=77127.5
- Funnel: target 764 → liquid 115 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +20.62% | $1,291,324.38 |
| SPORTFUN/USDT:USDT | +13.22% | $1,166,084.78 |
| H/USDT:USDT | +5.50% | $1,021,656.10 |
| MYX/USDT:USDT | +4.96% | $2,557,377.59 |
| SUPER/USDT:USDT | +4.91% | $3,427,955.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +4.19% | +3.90% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.45% | +1.16% |
| INJ/USDT:USDT | below_1h_threshold | +1.38% | +1.09% |
| CHIP/USDT:USDT | below_1h_threshold | +1.25% | +0.96% |
| SAGA/USDT:USDT | below_1h_threshold | +1.07% | +0.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
