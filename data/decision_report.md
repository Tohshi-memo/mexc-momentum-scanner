# Decision Report

- generated_at: 2026-06-02T08:56:43.890702+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5433**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5433, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.86% | **+0.86%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_BB3S | 9/19 | 47.4% | +1.20% | **+0.57%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.30% | **+0.15%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.14** / 初期 $100.00 (-3.86%)
- 確定トレード: 85件 (TP 24 / SL 58 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.30** / 初期 $100.00 (+34.30%)
- 確定: 945件 (Win 222 / Loss 283 / Flat 440) / skip 1049件
- 成長率目線: 平均log +0.000312 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $134.30

## 4. Latest Market Context

- 更新: 2026-06-02T08:56:41.207664+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=69734.0
- Funnel: target 772 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1, 4h RSI 79.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +46.44% | $19,041,623.52 |
| US/USDT:USDT | +40.47% | $2,075,963.03 |
| ESPORTS/USDT:USDT | +26.19% | $12,493,548.52 |
| MRVLSTOCK/USDT:USDT | +25.38% | $3,535,972.09 |
| USELESS/USDT:USDT | +20.72% | $1,685,314.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +4.46% | +4.95% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.16% | +4.65% |
| BILL/USDT:USDT | below_1h_threshold | +3.87% | +4.36% |
| USELESS/USDT:USDT | below_1h_threshold | +3.40% | +3.89% |
| H/USDT:USDT | below_1h_threshold | +2.35% | +2.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
