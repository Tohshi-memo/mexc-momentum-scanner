# Decision Report

- generated_at: 2026-06-01T04:47:21.499535+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5273**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.55% / filled 20/20。**
- 全期間 MARKET基準: n=5273, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.81% | **+2.81%** |
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.55% | **+1.91%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.05% | **+1.33%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.64% | **+1.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.54%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.19% | **+0.33%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.05% | **+0.04%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 940件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T04:47:18.442339+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.40% price=73434.3
- Funnel: target 777 → liquid 133 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.0 >= 65=1, 4h RSI 86.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +149.35% | $29,147,774.38 |
| H/USDT:USDT | +64.75% | $22,329,285.78 |
| FHE/USDT:USDT | +30.01% | $1,191,779.06 |
| STG/USDT:USDT | +28.29% | $23,082,372.70 |
| HOME/USDT:USDT | +20.65% | $3,983,069.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.73% | +5.14% |
| BEAT/USDT:USDT | below_1h_threshold | +2.56% | +2.96% |
| CTR/USDT:USDT | below_1h_threshold | +2.48% | +2.89% |
| BILL/USDT:USDT | below_1h_threshold | +1.58% | +1.98% |
| OFC/USDT:USDT | below_1h_threshold | +0.92% | +1.32% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
